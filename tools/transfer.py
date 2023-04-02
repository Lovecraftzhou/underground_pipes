import os
import shutil

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CURRENT_DIR, "data_enhance")
# print(path)

images_path = os.path.join(path,"images")
labels_path = os.path.join(path,"labels")

images = os.path.join(CURRENT_DIR,"dataset_enhance/images")
labels = os.path.join(CURRENT_DIR,"dataset_enhance/labels")

name = ["CJ","CR","PL"]
for n in name:
    path1 = os.path.join(images_path,n)
    # print(path1)
    list1 = os.listdir(path1)
    for i in list1:
        file_name = os.path.join(path1,i)
        # print(file_name)
        shutil.copy(file_name,images)

    path2 = os.path.join(labels_path,n)
    list2 = os.listdir(path2)
    for x in list2:
        file_name2 = os.path.join(path2,x)
        shutil.copy(file_name2,labels)