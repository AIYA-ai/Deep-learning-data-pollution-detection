import json
import shutil
import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, \
    QHBoxLayout, QWidget, QLabel, QMessageBox, \
    QRadioButton, QListView, QListWidgetItem, QListWidget, QFileDialog, QInputDialog


class journalpage(QWidget):
    def __init__(self):
        super(journalpage, self).__init__()
        self.initUI()
        self.resize(1240, 732)

    def initUI(self):
        self.Hbox = QHBoxLayout()
        self.qlab = QLabel("操作类型筛选：")
        self.qlab.setObjectName("QLab")
        self.allset = QRadioButton("全部")
        self.allset.setChecked(True)
        self.sett = QRadioButton("设置操作")
        self.adddel = QRadioButton("数据修改")
        self.allset.toggled.connect(self.allradio)
        self.sett.toggled.connect(self.setradio)
        self.adddel.toggled.connect(self.changeradio)
        self.allset.setObjectName("radiobutton")
        self.sett.setObjectName("radiobutton")
        self.adddel.setObjectName("radiobutton")
        # radio = QRadioButton("其他操作")
        self.btn1 = QPushButton()
        self.btn1.setText("导出日志文件")
        self.btn2 = QPushButton()
        self.btn1.clicked.connect(self.msg)
        self.btn2.setText("重置日志")
        self.btn1.setObjectName("choice")
        self.btn1.setFixedSize(150, 50)
        self.btn2.setObjectName("choice")
        self.btn2.setFixedSize(150, 50)
        self.btn2.clicked.connect(self.deleterizhi)
        listview = QListView()
        self.Hbox.addWidget(self.qlab)
        self.Hbox.addWidget(self.allset)
        self.Hbox.addWidget(self.sett)
        self.Hbox.addWidget(self.adddel)
        self.Hbox.addStretch()
        self.Hbox.addWidget(self.btn1)
        self.Hbox.addWidget(self.btn2)
        # 实例化列表模型，添加数据
        layout = QVBoxLayout(self)
        self.listwidget_1 = QListWidget(self)
        with open("logs.json", encoding="utf-8") as f:
            d = json.load(f)
            aex = '时间'.center(25) + '内容'.center(125) + '类型'.rjust(10)
            self.item = QListWidgetItem(aex)
            self.listwidget_1.addItem(self.item)
            for i in range(len(d)):
                aex = f"{d[len(d) - i - 1]['time']}".ljust(25) + f"{d[len(d) - i - 1]['content']}".ljust(
                    90) + f"{d[len(d) - i - 1]['type']}"
                self.item = QListWidgetItem(aex)
                self.listwidget_1.addItem(self.item)

        layout.addLayout(self.Hbox)
        layout.addWidget(self.listwidget_1)

    def allradio(self):
        self.listwidget_1.clear()
        with open("logs.json", encoding="utf-8") as f:
            d = json.load(f)
        for i in range(len(d)):
            aex = f"{d[len(d) - i - 1]['time']}".ljust(25) + f"{d[len(d) - i - 1]['content']}".ljust(
                90) + f"{d[len(d) - i - 1]['type']}"
            self.item = QListWidgetItem(aex)
            self.listwidget_1.addItem(self.item)

    def setradio(self):
        self.listwidget_1.clear()
        with open("logs.json", encoding="utf-8") as f:
            d = json.load(f)
        for i in range(len(d)):
            if d[len(d) - i - 1]['type'] == '设置操作':
                aex = f"{d[len(d) - i - 1]['time']}".ljust(25) + f"{d[len(d) - i - 1]['content']}".ljust(
                    90) + f"{d[len(d) - i - 1]['type']}"
                self.item = QListWidgetItem(aex)
                self.listwidget_1.addItem(self.item)

    def changeradio(self):
        self.listwidget_1.clear()
        with open("logs.json", encoding="utf-8") as f:
            d = json.load(f)
        for i in range(len(d)):
            if d[len(d) - i - 1]['type'] == '数据修改':
                aex = f"{d[len(d) - i - 1]['time']}".ljust(25) + f"{d[len(d) - i - 1]['content']}".ljust(
                    90) + f"{d[len(d) - i - 1]['type']}"
                self.item = QListWidgetItem(aex)
                self.listwidget_1.addItem(self.item)

    def msg(self):
        try:
            directory1 = QFileDialog.getExistingDirectory(self,
                                                          "选取文件夹",
                                                          "./")  # 起始路径
            saveaddress = directory1
            shutil.copyfile("logs.json", f'{saveaddress}/logs备份.json')
        except:
            pass

    def saveother(self):
        pass

    def deleterizhi(self):
        a = QInputDialog.getText(self, "输入密码框", "输入密码")
        b = "123"
        if a[0] == b:
            time1 = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
            shutil.copyfile("logs.json", f'logs{time1}.json')
            os.remove("logs.json")
            f = open("logs.json", 'w')
            self.listwidget_1.clear()
            f.close()
            QMessageBox.information(self, "提示", "已删除，可从设置中恢复")
        elif a[1] == True:
            QMessageBox.information(self, "提示", "密码错误！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    demo = journalpage()
    demo.show()
    sys.exit(app.exec_())
