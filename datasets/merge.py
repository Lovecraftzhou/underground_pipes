import os,re

cur_path = os.getcwd()
label_original_path = "pipe/labels/"
file_path = "pipe/images/"

path = os.path.join(cur_path,label_original_path)
total_txt = os.listdir(label_original_path)
file_txt = os.listdir(file_path)

dataset_image = "pipe_enhance/images"
dataset_label = "pipe_enhance/labels"


def replace(path,num,aim):
    file_data = ""
    with open(path,"r", encoding="utf-8") as f1:
        for line in f1:
            target = line[0]
            origin = line[1:]
            # print(target)
            # print(origin)
            if num in target:
                target = target.replace(num, aim)
            file_data += target + origin
            print(line + "---->" + file_data)
    with open(path,"w", encoding="utf-8") as f1:
        f1.write(file_data)

def delete(path,num):
    file_data = ""
    with open(path,"r", encoding="utf-8") as f1:
        for line in f1:
            # print(line)
            target = line[0]
            # print(target)
            if num in target:
                file_data = ""
            else:
                file_data += line
            print(file_data)
    with open(path,"w", encoding="utf-8") as f1:
        f1.write(file_data)

if __name__ == '__main__':
    dataset_label_path = os.path.join(cur_path,dataset_label)
    # print(dataset_label_path)
    label_list = os.listdir(dataset_label_path)
    for i in label_list:
        tar_path = os.path.join(dataset_label_path,i)
        replace(tar_path,"3","2")






