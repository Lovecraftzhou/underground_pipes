import os
from shutil import copy

import pandas as pd

Labels = ["PL","CJ","CK","ZW","CR"]
path1 = "D:\CDUT\CDUT-OBS\Semester 6\Proj\dataset\my_data\dataset_uniform"
path2 = "D:\CDUT\CDUT-OBS\Semester 6\Proj\dataset\my_data\dataset_uniform_training"

for fl in Labels:
    file_path1 = os.path.join(path1,fl)
    file1 = os.listdir(file_path1)
    file_path2 = os.path.join(path2,fl)
    file2 = os.listdir(file_path2)
    file = file1 + file2
    # print(file)
    cont = 0
    for fn in file1:
        new_name = fl + str(cont).rjust(10,"0") + ".jpg"
        old_root1 = os.path.join(file_path1,fn)
        new_root1 = os.path.join("D:\CDUT\CDUT-OBS\Semester 6\Proj\dataset\my_data\dataset\images\\train",new_name)
        print(old_root1 + "----->" + new_root1)
        copy(old_root1,new_root1)
        cont += 1

    for fn2 in file2:
        new_name2 = fl + str(cont).rjust(10,"0")+ ".jpg"
        old_root2 = os.path.join(file_path2, fn2)
        new_root2 = os.path.join("D:\CDUT\CDUT-OBS\Semester 6\Proj\dataset\my_data\dataset\images\\train", new_name2)
        print(old_root2 + "----->" + new_root2)
        copy(old_root2, new_root2)
        cont += 1
    # print(cont)

