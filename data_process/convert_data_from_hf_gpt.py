import os
import json
import fire


def convert_data_hf_to_gpt3(input_prefix, output_prefix):
    print(input_prefix)
    with open(input_prefix+".source") as f1, open(input_prefix+".target") as f2:
        with open(output_prefix+".json", 'w') as f_out:
            for s, t in zip(f1, f2):
                data = {"context":s+"\n\n", 'completion':t+"<|enoftext|>"}
                f_out.write(json.dumps(data)+'\n')

if __name__=='__main__':
    output_folder="./train_data_gpt3"
    os.makedirs(output_folder, exist_ok=True)
    #convert_data_hf_to_gpt3("train_data_new/test", output_folder+"/test")
    convert_data_hf_to_gpt3("train_data_new/val", output_folder+"/val")
    convert_data_hf_to_gpt3("train_data_new/train", output_folder+"/train")

