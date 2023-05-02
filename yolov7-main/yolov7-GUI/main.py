from PyQt5.QtWidgets import QApplication


from window import *
if __name__ == '__main__':
    app = QApplication([])
    yolo = MyWindow()
    globf._init()
    globf.set_value('yolo', yolo)
    Glo_yolo = globf.get_value('yolo')
    Glo_yolo.show()
    app.exec()
