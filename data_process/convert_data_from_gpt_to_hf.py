import os
import json
os.makedirs("./train_data", exist_ok=True)

def split_src_tgt(split):
    print(split)
    with open("./"+split+".json") as f:
        data = [s.strip() for s in f]
        print(len(data))
    with open("./train_data/"+split+".source", 'w') as f1, open("./train_data/"+split+".target", 'w') as f2:
        for item in data:
            item_dict = json.loads(item)
            src, tgt = item_dict['context'], item_dict['completion']
            f1.write(src.rstrip('\n')+ '\n')
            f2.write(tgt.strip("<|endoftext}>")+ '\n')
    
split_src_tgt("test")
#16237
split_src_tgt("val")
#16447
split_src_tgt("train")
#488861
