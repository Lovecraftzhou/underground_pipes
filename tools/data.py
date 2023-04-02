from dataenhancement import *
import cv2

dataAug = DataAugmentForObjectDetection()
img = cv2.imread("./data_uniform/images/CJ/CJ0000000000.jpg")

values = toolhelper.parse_xml("./data_uniform/labels_xml/CJ/CJ0000000000.xml")  # 解析得到box信息，格式为[[x_min,y_min,x_max,y_max,name]]
coords = [v[:4] for v in values]  # 得到框
labels = [v[-1] for v in values]  # 对象的标签
auged_img1, auged_bboxes1 = dataAug.is_rotate_img_bbox(img, coords)
show_pic(auged_img1,auged_bboxes1)
auged_img2, auged_bboxes2 = dataAug._shift_pic_bboxes(img, coords)
show_pic(auged_img2,auged_bboxes2)
auged_img3, auged_bboxes3 = dataAug._filp_pic_bboxes(img, coords)
show_pic(auged_img3,auged_bboxes3)
auged_img4 = dataAug._addNoise(img)
show_pic(auged_img4)

