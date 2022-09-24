import shutil
import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, \
    QHBoxLayout, QCheckBox, QWidget, QLabel, QLineEdit, QMessageBox, \
    QFileDialog
import json


class setpage(QWidget):
    def __init__(self):
        super(setpage, self).__init__()
        self.initUI()
        self.resize(1240, 732)

    def initUI(self):
        f = open('config1.json', 'r', encoding='utf-8')
        self.jl = json.load(f)
        self.jl = dict(self.jl)
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.hbox1 = QHBoxLayout(self)
        self.hbox2 = QHBoxLayout(self)
        self.hbox3 = QHBoxLayout(self)
        self.hbox4 = QHBoxLayout(self)
        self.hbox5 = QHBoxLayout(self)
        self.titel = QLabel('设置', self)
        self.titel1 = QLabel('启动：', self)
        self.titel2 = QLabel('模式：', self)
        self.titel3 = QLabel('数据集存储位置：')
        self.titel4 = QLabel('关于本软件：', self)
        self.titel5 = QLabel('当前版本：1.1v', self)
        self.titel7 = QLabel('配置文件存储位置：')
        self.titel6 = QLabel('版权所有：©菏泽学院-遇到困难不摆烂队', self)
        self.titel8 = QLabel('使用说明：', self)
        self.titel9 = QLabel('恢复：', self)
        self.titel10 = QLabel('日志恢复', self)
        self.titel.setStyleSheet("QLabel{font:30px 'Microsoft YaHei';}")
        self.titel5.setStyleSheet("QLabel{font:15px 'Microsoft YaHei';}")
        self.titel6.setStyleSheet("QLabel{font:15px 'Microsoft YaHei';}")
        self.titel8.setStyleSheet("QLabel{font:15px 'Microsoft YaHei';}")
        self.titel10.setStyleSheet("QLabel{font:15px 'Microsoft YaHei';}")
        self.titel1.setObjectName("QLab")
        self.titel2.setObjectName("QLab")
        self.titel3.setObjectName("QLab")
        self.titel4.setObjectName("QLab")
        self.titel7.setObjectName("QLab")
        self.titel9.setObjectName("QLab")

        self.cheakbox = QCheckBox()
        self.cheakbox.setText("开机自启")
        if self.jl["开机自启"] == 'True':
            self.cheakbox.setChecked(True)
        self.cheakbox1 = QCheckBox()
        self.cheakbox1.setText("安全模式")
        if self.jl["安全模式"] == 'True':
            self.cheakbox1.setChecked(True)
        self.cheakbox.setObjectName("Cbox")
        self.cheakbox1.setObjectName("Cbox")
        self.edt = QLineEdit()
        self.edt.setFixedSize(500, 30)
        self.edt.setObjectName("editline")
        self.edt.setText(self.jl['下载路径'])
        self.edt1 = QLineEdit()
        self.edt1.setFixedSize(500, 30)
        self.edt1.setObjectName("editline")
        self.edt1.setText(self.jl['配置文件'])
        self.submit_btn = QPushButton("选择")
        self.submit_btn.clicked.connect(self.mfd1)
        self.submit_btn1 = QPushButton("选择")
        self.submit_btn1.clicked.connect(self.mfd2)
        self.submit_btn3 = QPushButton("选择")

        self.submit_btn2 = QPushButton("打开")
        self.cheak_btn = QPushButton("检查更新")
        self.back_btn = QPushButton("意见反馈")

        self.hbox1.addWidget(self.edt)
        self.hbox1.addWidget(self.submit_btn)
        self.hbox1.addStretch()
        self.hbox2.addWidget(self.titel5)
        self.hbox2.addWidget(self.cheak_btn)
        self.hbox2.addWidget(self.back_btn)
        self.hbox2.addStretch()
        self.hbox3.addWidget(self.edt1)
        self.hbox3.addWidget(self.submit_btn1)
        self.hbox3.addStretch()
        self.hbox4.addWidget(self.titel8)
        self.hbox4.addWidget(self.submit_btn2)
        self.hbox4.addStretch()

        self.hbox5.addWidget(self.titel10)
        self.hbox5.addWidget(self.submit_btn3)
        self.hbox5.addStretch()
        self.btn1 = QPushButton("保存", self)
        self.btn1.clicked.connect(self.saveconfig)
        self.btn2 = QPushButton("重置", self)
        self.btn2.clicked.connect(self.restoreconfig)
        self.submit_btn.setObjectName("choice")
        self.submit_btn1.setObjectName("choice")
        self.submit_btn2.setObjectName("choice")
        self.submit_btn3.setObjectName("choice")
        self.btn1.setObjectName("choice")
        self.btn2.setObjectName("choice")
        self.back_btn.setObjectName("choice")
        self.cheak_btn.setObjectName("choice")

        self.submit_btn.setFixedSize(100, 30)
        self.submit_btn1.setFixedSize(100, 30)
        self.submit_btn2.setFixedSize(100, 30)
        self.submit_btn3.setFixedSize(100, 30)
        self.cheak_btn.setFixedSize(100, 30)
        self.back_btn.setFixedSize(100, 30)
        self.btn1.setFixedSize(150, 40)
        self.btn2.setFixedSize(150, 40)

        self.cheak_btn.clicked.connect(self.cheaknew)
        self.submit_btn2.clicked.connect(self.openfile)
        self.submit_btn3.clicked.connect(self.recovery)

        self.hbox.addStretch()
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.hbox.addStretch()
        self.vbox.setSpacing(15)
        self.vbox.addWidget(self.titel)
        self.vbox.addWidget(self.titel1)
        self.vbox.addWidget(self.cheakbox)
        self.vbox.addWidget(self.titel2)
        self.vbox.addWidget(self.cheakbox1)
        self.vbox.addWidget(self.titel9)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.titel3)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addWidget(self.titel7)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addWidget(self.titel4)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.titel6)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addSpacing(20)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch()

    def mfd1(self):
        self.directory1 = QFileDialog.getExistingDirectory(self,
                                                           "选取文件夹",
                                                           "./")  # 起始路径
        self.edt.setText(self.directory1)

    def mfd2(self):
        self.directory2 = QFileDialog.getExistingDirectory(self,
                                                           "选取文件夹",
                                                           "./")  # 起始路径
        self.edt1.setText(self.directory2)

    def cheaknew(self):
        QMessageBox.information(self, "更新检查", "当前版本已为最新版本")  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

    def openfile(self):
        path = r"abc.txt"
        QDesktopServices.openUrl(QUrl.fromLocalFile(path))

    def recovery(self):
        try:
            fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                              "选取文件",
                                                              "./",
                                                              "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
            address = fileName1
            shutil.copyfile(address, "rizhi.txt")
            QMessageBox.information(self, "提示", "日志已恢复")
        except:
            pass

    def saveconfig(self):
        self.j2 = self.jl
        if self.cheakbox.isChecked() == True:
            self.j2['开机自启'] = "True"
        else:
            self.j2['开机自启'] = "False"
        if self.cheakbox1.isChecked() == True:
            self.j2["安全模式"] = "True"
        else:
            self.j2['安全模式'] = "False"
        self.j2["下载路径"] = self.edt.text()
        self.j2["配置文件"] = self.edt1.text()
        f = open("config1.json", 'w', encoding='utf-8')
        json_str = json.dumps(self.j2, indent=1, ensure_ascii=False)
        f.write(f"{json_str}")
        QMessageBox.information(self, "提示", "保存成功")

    def restoreconfig(self):
        os.remove("config1.json")
        self.cheakbox.setChecked(True)
        self.cheakbox1.setChecked(True)
        self.edt.setText(self.jl["下载路径"])
        self.edt1.setText(self.jl["配置文件"])
        shutil.copyfile('config.json', "config1.json")
        QMessageBox.information(self, "提示", "重置成功")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    demo = setpage()
    demo.show()
    sys.exit(app.exec_())
