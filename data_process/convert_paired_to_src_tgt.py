import os
os.makedirs("new_train/train_data", exist_ok=True)

def split_src_tgt(split):
    print(split)
    with open("new_train/"+split+"_pairs_shuf.txt") as f:
        data = [s.strip() for s in f]
        print(len(data))
    with open("new_train/train_data/"+split+".source", 'w') as f1, open("new_train/train_data/"+split+".target", 'w') as f2:
        for item in data:
            src, tgt = item.split(" <||> ")
            f1.write(src+ '\n')
            f2.write(tgt+ '\n')
    
split_src_tgt("test")
#16237
split_src_tgt("val")
#16447
split_src_tgt("train")
#488861
