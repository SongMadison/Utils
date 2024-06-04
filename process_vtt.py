import os
import glob
import json
import re

def clean_trancript(transcript):
    def process_turn(text):
        s, t = re.sub("<v (.*?)>.*", "\\1", text),  re.sub("<v (.*?)>(.*)</v>", "\\2", text)
        return s + ": " + t
    try:
        text_list = transcript.split("\n")
        text_list = [process_turn(x) for x in text_list if x.startswith("<v ")]
    except Exception as e:
        print("ERROR:", e)
        print("transcript: ", transcript)
    return "\n".join(text_list)


files = glob.glob("./internal_team_meetings/*.vtt")
output_dir = "./internal_team_meetings/00_processed"
os.makedirs(output_dir, exist_ok=True)
for input_file in files:
    with open(input_file) as f_in:
        transcript=f_in.read()
    cleaned_transcript = clean_trancript(transcript)
    if cleaned_transcript == "":
        print("incorrect format!!")
        print(f"skip {input_file}")
        continue
    meeting_id = input_file.split("/")[-1]
    with open(f"{output_dir}/{meeting_id}".replace(".vtt", ".json"), "w") as f_out:
        json_example = {'id':input_file.split("/")[-1],
            'title':"",
            'content_type':"internal meeting",
            'content':cleaned_transcript,
            }
        json.dump(json_example, f_out, indent=4)

# create a single file with all the meetings   
with open(f"{output_dir}/00_all_real_meetings.jsonl", "w") as f_out:
    for input_file in files:
        with open(input_file) as f_in:
            transcript=f_in.read()
        cleaned_transcript = clean_trancript(transcript)
        if cleaned_transcript == "":
            print("incorrect format!!")
            print(f"skip {input_file}")
            continue
        json_example = {'id':input_file.split("/")[-1],
            'title':"",
            'content_type':"internal meetings",
            'content':cleaned_transcript,
            }
        f_out.write(json.dumps(json_example) +'\n')
