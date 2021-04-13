def create_pairs(split):
    print(split)
    with open("new_train/"+split+".source") as f1, open("new_train/"+split+".target") as f2:
        data = [s.strip() for s in f1]
        data2 = [t.strip() for t in f2]
    print(len(data))
    assert len(data) == len(data2)
    with open("new_train/"+split+"_pairs.txt", 'w') as f:
        for s,t in zip(data, data2):
            f.write(s + " <||> " + t+ '\n')
    print(len(data))

create_pairs("test")
create_pairs("val")
create_pairs("train")
