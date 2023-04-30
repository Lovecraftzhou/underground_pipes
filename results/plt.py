import os

import matplotlib.pyplot as plt
import pandas as pd



#获取文件夹下的csv文件
def get_filename(path):
  return os.listdir(path)

#绘制图形
def paint(file_name):
    plt.figure()

    cur_path = os.getcwd()
    data_path = os.path.join(cur_path, file_name)
    file = get_filename(data_path)
    # print(file)

    ct = 0
    colors = ["red", "blue", "green", "orange", "purple"]
    for i in file:
        file_path = os.path.join(data_path, i)
        len_mean = pd.read_csv(file_path)
        # 设置折线颜色，折线标签
        name = i.split(".")[0]
        plt.plot(len_mean['Step'], len_mean['Value'], color=colors[ct], label=name)
        ct += 1

    plt.legend(loc='upper right')
    plt.xlabel("epoch")
    plt.ylabel("Value")
    plt.title(file_name)
    # plt.show()
    # 保存图片，也可以是其他格式，如pdf
    plt.savefig(fname=file_name +'.png', format='png')

def paint_mAP(file_name,title,loc):
    plt.figure()

    cur_path = os.getcwd()
    data_path = os.path.join(cur_path, file_name)
    file = get_filename(data_path)
    # print(file)

    ct = 0
    colors = ["red", "blue", "green", "orange", "purple"]
    for i in file:
        file_path = os.path.join(data_path, i)
        len_mean = pd.read_csv(file_path)
        # 设置折线颜色，折线标签
        name = i.split(".")[0]
        plt.plot(len_mean['Step'], len_mean['Value'], color=colors[ct], label=name)
        ct += 1

    plt.legend(loc=loc)
    plt.xlabel("epoch")
    plt.ylabel("Value")
    plt.title(title)
    # plt.show()
    # 保存图片，也可以是其他格式，如pdf
    plt.savefig(fname=file_name +'.png', format='png')

if __name__ == '__main__':
    # paint("loss/box_loss")
    # paint("loss/class_loss")
    # paint("loss/obj_loss")
    paint_mAP("mAP@0.5","mAP@0.5","lower right")
    paint_mAP("mAP@0.95","mAP@0.5:0.95","lower right")


