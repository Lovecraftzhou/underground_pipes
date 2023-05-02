# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/win.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(1057, 757)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget#Form{\n"
"background-image: url(:/img/img/background.png);\n"
"    border: 0px solid #42adff;\n"
"    border-radius:5px;\n"
"}")
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QHBoxLayout()
        self.logo.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.logo.setContentsMargins(10, 0, -1, 3)
        self.logo.setSpacing(0)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/swimming.png"))
        self.label.setObjectName("label")
        self.logo.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logo.addItem(spacerItem)
        self.name = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet("QLabel#name{\n"
"    font: 20pt \"Arial\";\n"
"    rgb(255, 0, 0);\n"
"}")
        self.name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.logo.addWidget(self.name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logo.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, -1, 0, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MinButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinButton.sizePolicy().hasHeightForWidth())
        self.MinButton.setSizePolicy(sizePolicy)
        self.MinButton.setMinimumSize(QtCore.QSize(25, 25))
        self.MinButton.setStyleSheet("QPushButton#MinButton{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.MinButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icons/minus-square-outlined-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MinButton.setIcon(icon)
        self.MinButton.setIconSize(QtCore.QSize(25, 25))
        self.MinButton.setObjectName("MinButton")
        self.horizontalLayout.addWidget(self.MinButton)
        self.MaxButton = QtWidgets.QPushButton(Form)
        self.MaxButton.setMinimumSize(QtCore.QSize(25, 25))
        self.MaxButton.setStyleSheet("QPushButton#MaxButton{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.MaxButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icons/square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MaxButton.setIcon(icon1)
        self.MaxButton.setIconSize(QtCore.QSize(25, 25))
        self.MaxButton.setObjectName("MaxButton")
        self.horizontalLayout.addWidget(self.MaxButton)
        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setMinimumSize(QtCore.QSize(25, 25))
        self.CloseButton.setStyleSheet("QPushButton#CloseButton{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.CloseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon2)
        self.CloseButton.setIconSize(QtCore.QSize(25, 25))
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_4.setStretch(0, 10)
        self.logo.addLayout(self.verticalLayout_4)
        self.logo.setStretch(0, 1)
        self.logo.setStretch(1, 2)
        self.logo.setStretch(2, 5)
        self.logo.setStretch(3, 50)
        self.logo.setStretch(4, 5)
        self.verticalLayout.addLayout(self.logo)
        self.main = QtWidgets.QVBoxLayout()
        self.main.setContentsMargins(-1, 0, -1, 0)
        self.main.setSpacing(0)
        self.main.setObjectName("main")
        self.main_top = QtWidgets.QFrame(Form)
        self.main_top.setStyleSheet("QFrame#main_top{\n"
"    border-top:1px solid #7e7e7e;\n"
"    border-bottom:1px solid #7e7e7e;\n"
"}")
        self.main_top.setObjectName("main_top")
        self.maintop = QtWidgets.QHBoxLayout(self.main_top)
        self.maintop.setContentsMargins(0, 0, 0, 0)
        self.maintop.setSpacing(0)
        self.maintop.setObjectName("maintop")
        self.left = QtWidgets.QHBoxLayout()
        self.left.setContentsMargins(0, 0, 0, 0)
        self.left.setSpacing(0)
        self.left.setObjectName("left")
        self.toolbar = QtWidgets.QLabel(self.main_top)
        self.toolbar.setMinimumSize(QtCore.QSize(220, 0))
        self.toolbar.setMaximumSize(QtCore.QSize(220, 16777215))
        self.toolbar.setStyleSheet("QLabel#toolbar{\n"
"    font: 500 18pt \"Arial\";\n"
"    border-right: 1px solid #7e7e7e;\n"
"    border-top: 0px solid rgba(200, 200, 200,100);\n"
"    border-left: 0px solid rgba(200, 200, 200,100);\n"
"}")
        self.toolbar.setObjectName("toolbar")
        self.left.addWidget(self.toolbar)
        self.maintop.addLayout(self.left)
        self.right = QtWidgets.QHBoxLayout()
        self.right.setContentsMargins(0, 0, 0, 0)
        self.right.setSpacing(0)
        self.right.setObjectName("right")
        self.viewbar = QtWidgets.QLabel(self.main_top)
        self.viewbar.setStyleSheet("QLabel#viewbar{\n"
"    font: 500 18pt \"Arial\";\n"
"    border:none;\n"
"}")
        self.viewbar.setObjectName("viewbar")
        self.right.addWidget(self.viewbar)
        self.maintop.addLayout(self.right)
        self.maintop.setStretch(0, 25)
        self.maintop.setStretch(1, 100)
        self.main.addWidget(self.main_top)
        self.main_bottom = QtWidgets.QHBoxLayout()
        self.main_bottom.setSpacing(0)
        self.main_bottom.setObjectName("main_bottom")
        self.menu_box = QtWidgets.QFrame(Form)
        self.menu_box.setMinimumSize(QtCore.QSize(220, 0))
        self.menu_box.setMaximumSize(QtCore.QSize(220, 16777215))
        self.menu_box.setStyleSheet("QFrame#menu_box{\n"
"    border-right:1px solid  #7e7e7e;\n"
"     border-left:0px solid  black;\n"
"     border-top:0px solid  black;\n"
"}")
        self.menu_box.setObjectName("menu_box")
        self.menubox = QtWidgets.QVBoxLayout(self.menu_box)
        self.menubox.setContentsMargins(0, 1, 0, 0)
        self.menubox.setSpacing(0)
        self.menubox.setObjectName("menubox")
        self.menu = QtWidgets.QFrame(self.menu_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QtCore.QSize(0, 0))
        self.menu.setStyleSheet("QGroup#menu{\n"
"    border:none;\n"
"}")
        self.menu.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.menu.setObjectName("menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tools = QtWidgets.QHBoxLayout()
        self.tools.setContentsMargins(0, 6, 1, 2)
        self.tools.setSpacing(2)
        self.tools.setObjectName("tools")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.folder = QtWidgets.QPushButton(self.menu)
        self.folder.setMinimumSize(QtCore.QSize(40, 40))
        self.folder.setStyleSheet("QPushButton#folder{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.folder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folder.setIcon(icon3)
        self.folder.setIconSize(QtCore.QSize(40, 40))
        self.folder.setObjectName("folder")
        self.verticalLayout_6.addWidget(self.folder)
        self.folder_txt = QtWidgets.QLabel(self.menu)
        self.folder_txt.setStyleSheet("QLabel#folder_txt{\n"
"    font-size:10pt;\n"
"}")
        self.folder_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.folder_txt.setObjectName("folder_txt")
        self.verticalLayout_6.addWidget(self.folder_txt)
        self.tools.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.importbtn = QtWidgets.QPushButton(self.menu)
        self.importbtn.setMinimumSize(QtCore.QSize(40, 40))
        self.importbtn.setStyleSheet("QPushButton#importbtn{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.importbtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importbtn.setIcon(icon4)
        self.importbtn.setIconSize(QtCore.QSize(40, 40))
        self.importbtn.setObjectName("importbtn")
        self.verticalLayout_8.addWidget(self.importbtn)
        self.import_txt = QtWidgets.QLabel(self.menu)
        self.import_txt.setStyleSheet("QLabel#import_txt{\n"
"    font-size:10pt;\n"
"}")
        self.import_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.import_txt.setObjectName("import_txt")
        self.verticalLayout_8.addWidget(self.import_txt)
        self.tools.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.exporter = QtWidgets.QPushButton(self.menu)
        self.exporter.setMinimumSize(QtCore.QSize(40, 40))
        self.exporter.setStyleSheet("QPushButton#exporter{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.exporter.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exporter.setIcon(icon5)
        self.exporter.setIconSize(QtCore.QSize(40, 40))
        self.exporter.setObjectName("exporter")
        self.verticalLayout_9.addWidget(self.exporter)
        self.recog_txt_2 = QtWidgets.QLabel(self.menu)
        self.recog_txt_2.setStyleSheet("QLabel#export_txt{\n"
"    font-size:10pt;\n"
"}")
        self.recog_txt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.recog_txt_2.setObjectName("recog_txt_2")
        self.verticalLayout_9.addWidget(self.recog_txt_2)
        self.tools.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.tools)
        self.args = QtWidgets.QFrame(self.menu)
        self.args.setStyleSheet("QFrame#args{\n"
"    border-top:1px solid black;\n"
"}")
        self.args.setObjectName("args")
        self.argsbar = QtWidgets.QVBoxLayout(self.args)
        self.argsbar.setContentsMargins(2, 4, 2, 1)
        self.argsbar.setSpacing(4)
        self.argsbar.setObjectName("argsbar")
        self.confidence = QtWidgets.QLabel(self.args)
        self.confidence.setStyleSheet("QLabel#confidence{\n"
"    font-size:12pt;\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.confidence.setObjectName("confidence")
        self.argsbar.addWidget(self.confidence)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, -1, 0, -1)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.con_num = QtWidgets.QDoubleSpinBox(self.args)
        self.con_num.setMinimumSize(QtCore.QSize(62, 25))
        self.con_num.setMaximumSize(QtCore.QSize(62, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(-1)
        self.con_num.setFont(font)
        self.con_num.setStyleSheet("QDoubleSpinBox{\n"
"background:white;\n"
"color:black;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;\n"
"margin: 0px 0;\n"
"     left: 5px;\n"
"    right: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/img/icons/down-arrow.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/img/icons/down-arrow.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/img/icons/up-arrow.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/img/icons/up-arrow.png);}\n"
"")
        self.con_num.setMaximum(1.0)
        self.con_num.setSingleStep(0.01)
        self.con_num.setProperty("value", 0.25)
        self.con_num.setObjectName("con_num")
        self.horizontalLayout_8.addWidget(self.con_num)
        self.con_slider = QtWidgets.QSlider(self.args)
        self.con_slider.setStyleSheet("QSlider{\n"
"    border-color: #bcbcbc;\n"
"    color:#57a4ff;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"       margin: 0px 0;\n"
"     left: 5px;\n"
"    right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/img/icons/full-moon.png);\n"
"     width:17px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #f9f9f9, stop:0.25 #f9f9f9, stop:0.5 #f9f9f9, stop:1 #f9f9f9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #57a4ff, stop:0.25 #57a4ff, stop:0.5 #57a4ff, stop:1 #57a4ff);\n"
"}")
        self.con_slider.setMaximum(100)
        self.con_slider.setProperty("value", 20)
        self.con_slider.setOrientation(QtCore.Qt.Horizontal)
        self.con_slider.setObjectName("con_slider")
        self.horizontalLayout_8.addWidget(self.con_slider)
        self.argsbar.addLayout(self.horizontalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.argsbar.addItem(spacerItem2)
        self.iou = QtWidgets.QLabel(self.args)
        self.iou.setStyleSheet("QLabel#iou{\n"
"    font-size:12pt;\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.iou.setObjectName("iou")
        self.argsbar.addWidget(self.iou)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.iou_num = QtWidgets.QDoubleSpinBox(self.args)
        self.iou_num.setMinimumSize(QtCore.QSize(62, 25))
        self.iou_num.setMaximumSize(QtCore.QSize(62, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(-1)
        self.iou_num.setFont(font)
        self.iou_num.setStyleSheet("QDoubleSpinBox{\n"
"background:white;\n"
"color:black;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;\n"
"margin: 0px 0;\n"
"     left: 5px;\n"
"    right: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/img/icons/down-arrow.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/img/icons/down-arrow.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/img/icons/up-arrow.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/img/icons/up-arrow.png);}\n"
"")
        self.iou_num.setMaximum(1.0)
        self.iou_num.setSingleStep(0.01)
        self.iou_num.setProperty("value", 0.4)
        self.iou_num.setObjectName("iou_num")
        self.horizontalLayout_9.addWidget(self.iou_num)
        self.iou_slider = QtWidgets.QSlider(self.args)
        self.iou_slider.setStyleSheet("QSlider{\n"
"    border-color: #bcbcbc;\n"
"    color:#57a4ff;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"       margin: 0px 0;\n"
"     left: 5px;\n"
"    right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/img/icons/full-moon.png);\n"
"     width:17px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #f9f9f9, stop:0.25 #f9f9f9, stop:0.5 #f9f9f9, stop:1 #f9f9f9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #57a4ff, stop:0.25 #57a4ff, stop:0.5 #57a4ff, stop:1 #57a4ff);\n"
"}")
        self.iou_slider.setMaximum(100)
        self.iou_slider.setProperty("value", 40)
        self.iou_slider.setOrientation(QtCore.Qt.Horizontal)
        self.iou_slider.setObjectName("iou_slider")
        self.horizontalLayout_9.addWidget(self.iou_slider)
        self.argsbar.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.argsbar.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ptmodel = QtWidgets.QLabel(self.args)
        self.ptmodel.setStyleSheet("QLabel#ptmodel{\n"
"    font-size:12pt;\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.ptmodel.setObjectName("ptmodel")
        self.horizontalLayout_2.addWidget(self.ptmodel)
        self.comboBox = QtWidgets.QComboBox(self.args)
        self.comboBox.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"background:white;\n"
"selection-background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: black;\n"
"border-width:1px;\n"
"border-color:grey;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,0);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:1;\n"
"margin-right:2;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image:url(:/img/icon/list.png);\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_2.setStretch(0, 12)
        self.horizontalLayout_2.setStretch(1, 30)
        self.argsbar.addLayout(self.horizontalLayout_2)
        self.argsbar.setStretch(1, 10)
        self.argsbar.setStretch(2, 2)
        self.argsbar.setStretch(4, 10)
        self.argsbar.setStretch(5, 2)
        self.argsbar.setStretch(6, 8)
        self.verticalLayout_2.addWidget(self.args)
        self.resultbox = QtWidgets.QVBoxLayout()
        self.resultbox.setContentsMargins(-1, 6, -1, -1)
        self.resultbox.setSpacing(0)
        self.resultbox.setObjectName("resultbox")
        self.result_2 = QtWidgets.QFrame(self.menu)
        self.result_2.setStyleSheet("QFrame#result_2{\n"
"    border-top:1px solid #7e7e7e;\n"
"    border-bottom:1px solid #7e7e7e;\n"
"}")
        self.result_2.setObjectName("result_2")
        self.mess = QtWidgets.QHBoxLayout(self.result_2)
        self.mess.setContentsMargins(0, 0, 0, 0)
        self.mess.setSpacing(0)
        self.mess.setObjectName("mess")
        self.resultbar = QtWidgets.QLabel(self.result_2)
        self.resultbar.setStyleSheet("QLabel#resultbar{\n"
"    font: 500 18pt \"Arial\";\n"
"}")
        self.resultbar.setObjectName("resultbar")
        self.mess.addWidget(self.resultbar)
        self.resultbox.addWidget(self.result_2)
        self.resultlist = QtWidgets.QListWidget(self.menu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.resultlist.setFont(font)
        self.resultlist.setStyleSheet("QListWidget#resultlist{\n"
"    border:none;\n"
"    font: 500 18pt \"Arial\";\n"
"}")
        self.resultlist.setObjectName("resultlist")
        self.resultbox.addWidget(self.resultlist)
        self.resultbox.setStretch(0, 1)
        self.resultbox.setStretch(1, 15)
        self.verticalLayout_2.addLayout(self.resultbox)
        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(2, 50)
        self.menubox.addWidget(self.menu)
        self.main_bottom.addWidget(self.menu_box)
        self.result = QtWidgets.QVBoxLayout()
        self.result.setContentsMargins(0, 0, 0, 0)
        self.result.setSpacing(0)
        self.result.setObjectName("result")
        self.view_top = QtWidgets.QFrame(Form)
        self.view_top.setMinimumSize(QtCore.QSize(0, 30))
        self.view_top.setMaximumSize(QtCore.QSize(16777215, 30))
        self.view_top.setStyleSheet("QFrame#view_top{\n"
"    border-top:0px solid black;\n"
"    border-bottom:1px solid #7e7e7e;\n"
"}")
        self.view_top.setObjectName("view_top")
        self.top = QtWidgets.QHBoxLayout(self.view_top)
        self.top.setContentsMargins(0, 0, 0, 0)
        self.top.setSpacing(0)
        self.top.setObjectName("top")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top.addItem(spacerItem4)
        self.before = QtWidgets.QLabel(self.view_top)
        self.before.setStyleSheet("QLabel#before{\n"
"    font-size : 20px;\n"
"    font: 18pt \"Arial\";\n"
"}")
        self.before.setObjectName("before")
        self.top.addWidget(self.before)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top.addItem(spacerItem5)
        self.after = QtWidgets.QLabel(self.view_top)
        self.after.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.after.setStyleSheet("QLabel#after{\n"
"    font: 18pt \"Arial\";\n"
"    font-size : 20px;\n"
"}")
        self.after.setObjectName("after")
        self.top.addWidget(self.after)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top.addItem(spacerItem6)
        self.top.setStretch(0, 25)
        self.top.setStretch(1, 10)
        self.top.setStretch(2, 50)
        self.top.setStretch(3, 10)
        self.top.setStretch(4, 25)
        self.result.addWidget(self.view_top)
        self.bottom = QtWidgets.QHBoxLayout()
        self.bottom.setContentsMargins(1, 1, 1, 3)
        self.bottom.setSpacing(0)
        self.bottom.setObjectName("bottom")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setStyleSheet("#splitter::handle{\n"
"    background: 1px solid  rgba(200, 200, 200,100);\n"
"}\n"
"QSplitter#splitter{\n"
"    border-bottom:1px solid #7e7e7e;\n"
"    border-top: 0px solid  black;\n"
"    border-right:0px solid  black;\n"
"    border-left: 0px solid  black;\n"
"}")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName("splitter")
        self.input = Label_click_Mouse(self.splitter)
        self.input.setMinimumSize(QtCore.QSize(200, 0))
        self.input.setAutoFillBackground(False)
        self.input.setStyleSheet("QLabel#input{\n"
"    border:none;\n"
"}")
        self.input.setText("")
        self.input.setObjectName("input")
        self.output = Label_click_Mouse(self.splitter)
        self.output.setMinimumSize(QtCore.QSize(200, 0))
        self.output.setStyleSheet("QLabel#output{\n"
"    border:none;\n"
"}")
        self.output.setText("")
        self.output.setObjectName("output")
        self.bottom.addWidget(self.splitter)
        self.result.addLayout(self.bottom)
        self.player = QtWidgets.QFrame(Form)
        self.player.setMinimumSize(QtCore.QSize(0, 35))
        self.player.setMaximumSize(QtCore.QSize(16777215, 35))
        self.player.setObjectName("player")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.player)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.playbtn = QtWidgets.QPushButton(self.player)
        self.playbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.playbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.playbtn.setStyleSheet("QPushButton#playbtn{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 15px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.playbtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/icons/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playbtn.setIcon(icon6)
        self.playbtn.setIconSize(QtCore.QSize(28, 28))
        self.playbtn.setCheckable(False)
        self.playbtn.setObjectName("playbtn")
        self.horizontalLayout_3.addWidget(self.playbtn)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.progressBar = QtWidgets.QProgressBar(self.player)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    color: rgb(255, 255, 255);\n"
"    font:12pt;\n"
"    text-align:center;\n"
"    border:none;\n"
"    background-color: rgba(215, 215, 215,100);\n"
"    border-radius:4px;\n"
"}\n"
"QProgressBar:chunk{\n"
"    border-radius:4px;\n"
"     background: rgba(55, 55, 55, 200);\n"
"}")
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.stopbtn = QtWidgets.QPushButton(self.player)
        self.stopbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.stopbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.stopbtn.setStyleSheet("QPushButton#stopbtn{\n"
"    border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 15px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.stopbtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/icons/stop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopbtn.setIcon(icon7)
        self.stopbtn.setIconSize(QtCore.QSize(28, 28))
        self.stopbtn.setObjectName("stopbtn")
        self.horizontalLayout_3.addWidget(self.stopbtn)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 100)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 5)
        self.horizontalLayout_3.setStretch(6, 1)
        self.result.addWidget(self.player)
        self.result.setStretch(0, 5)
        self.result.setStretch(1, 100)
        self.main_bottom.addLayout(self.result)
        self.main_bottom.setStretch(0, 25)
        self.main_bottom.setStretch(1, 100)
        self.main.addLayout(self.main_bottom)
        self.main.setStretch(1, 100)
        self.verticalLayout.addLayout(self.main)
        self.foot = QtWidgets.QFrame(Form)
        self.foot.setStyleSheet("#foot{\n"
"    border-top:1px solid  #7e7e7e;\n"
"    border-left:0px solid black;\n"
"    border-left:0px solid black;\n"
"}")
        self.foot.setObjectName("foot")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.foot)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.outputbox = QtWidgets.QLabel(self.foot)
        self.outputbox.setMinimumSize(QtCore.QSize(0, 20))
        self.outputbox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.outputbox.setStyleSheet("")
        self.outputbox.setText("")
        self.outputbox.setObjectName("outputbox")
        self.horizontalLayout_6.addWidget(self.outputbox)
        self.verticalLayout.addWidget(self.foot)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 100)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.MaxButton, self.CloseButton)
        Form.setTabOrder(self.CloseButton, self.MinButton)
        Form.setTabOrder(self.MinButton, self.importbtn)
        Form.setTabOrder(self.importbtn, self.folder)
        Form.setTabOrder(self.folder, self.exporter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YOLOv7-pipe Detect"))
        self.name.setText(_translate("Form", "YOLO Detect"))
        self.toolbar.setText(_translate("Form", "Tool"))
        self.viewbar.setText(_translate("Form", "Prediction box"))
        self.folder_txt.setText(_translate("Form", "File"))
        self.import_txt.setText(_translate("Form", "Model"))
        self.recog_txt_2.setText(_translate("Form", "Image/Video"))
        self.confidence.setText(_translate("Form", "Confidence:"))
        self.iou.setText(_translate("Form", "IoU:"))
        self.ptmodel.setText(_translate("Form", "Model:"))
        self.resultbar.setText(_translate("Form", "Results"))
        self.before.setText(_translate("Form", "Before"))
        self.after.setText(_translate("Form", "  After"))

from MouseLabel import Label_click_Mouse
import apprcc_rc
