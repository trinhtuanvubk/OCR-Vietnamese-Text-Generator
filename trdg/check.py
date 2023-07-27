import os 

root = "./out/dataset"



img_list = [filename for filename in os.listdir(root) if filename.endswith("jpg")]
img_list_name = [i.split(".")[0] for i in img_list]
label_list = [filename for filename in os.listdir(root) if filename.endswith("txt")]
label_list_name = [j.split(".")[0] for j in label_list]

i=0
for j in img_list_name:
    if j not in label_list_name:
        print(j)
        i+=1
print("----------------------")
for k in label_list_name:
    if k not in img_list_name:
        print(k)
        i+=1
print("-----------------")
print(i)
