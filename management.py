import json
import shutil
import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem,  QPushButton, QVBoxLayout, \
    QHBoxLayout, QAbstractItemView, QWidget, QHeaderView,  QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter.messagebox as tk
import tkinter


class manage(QWidget):
    def __init__(self):
        super(manage, self).__init__()
        self.initUI()
        self.resize(1240, 732)

    def initUI(self):
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button1.setText('管理')
        self.button1.setFixedSize(150, 40)
        self.button1.clicked.connect(self.addcont)
        self.button2.setFixedSize(150, 40)
        self.button2.setText('文件夹中打开')
        self.button2.clicked.connect(self.open_directory)
        self.button1.setObjectName('choice')
        self.button2.setObjectName('choice')
        self.layout1 = QHBoxLayout()
        self.layout2 = QVBoxLayout(self)
        self.table = QTableWidget()
        f = open('config1.json','r',encoding='utf-8')
        self.jl = json.load(f)
        self.path = f'{self.jl["下载路径"]}'
        self.files_1 = os.listdir(self.path)
        self.table.setRowCount(len(self.files_1))  # 设置行数与列数
        self.table.setColumnCount(4)
        for i in range(len(self.files_1)):
            self.table.setRowHeight(i, 50)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(['数据名称', '最后修改时间', '数据集类型', '大小'])  # 设置每一列的名称
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        f = open("datamessage.json", "r+", encoding="utf-8")
        try:
            alist = json.load(f)
        except:
            alist = []
        self.wronglist = []
        aname = []
        for js in range(len(alist)):
            aname.append(alist[js]['name'])
        filetype = open('typetext.json','r',encoding='utf-8')
        json_type = json.load(filetype)
        for i in range(len(self.files_1)):
            self.fileinfo = os.stat(self.path + '/' + self.files_1[i])
            self.item_1 = QTableWidgetItem(self.files_1[i])
            self.item_2 = QTableWidgetItem(self.formatTime(self.fileinfo.st_mtime))
            s = str(int((self.fileinfo.st_size) / 1024)) + "kb"
            self.item_3 = QTableWidgetItem(s)
            self.table.setItem(i, 0, self.item_1)  # 填表，第一行第一列填Hi
            self.table.setItem(i, 1, self.item_2)  # 填表，第一行第一列填Hi
            self.table.setItem(i, 3, self.item_3)  # 填表，第一行第一列填Hi
            self.comboBoxList = (["未知", "图像数据集", "语音数据集", "文本数据集", "预训练模型"])
            self.comboBox = QtWidgets.QComboBox()
            self.comboBox.addItems(self.comboBoxList)
            self.comboBox.setStyleSheet("QComboBox{margin:3px;font:20px 'Microsoft YaHei';color:#47B0E7;};")
            self.comboBox.setEnabled(False)
            for j in range(len(json_type)):
                if self.files_1[i]==json_type[j]['name']:
                    subscript=self.comboBoxList.index(json_type[j]['type'])
                    self.comboBox.setCurrentIndex(subscript)
            self.table.setCellWidget(i, 2, self.comboBox)

            if len(alist) != 0:
                a = {"name": f"{self.files_1[i]}", "time": f"{self.formatTime(self.fileinfo.st_mtime)}", "md5": "",
                     "size": f"{s}", "type": "未知"}
                if a['name'] in aname:
                    if a not in alist:
                        self.wronglist.append(a['name'])
                else:
                    pass


        if len(self.wronglist) > 0:
            self.button5 = QPushButton()
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("./icon/wraning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.button5.setIcon(icon1)
            self.button5.setText("警告！")
            self.button5.setFixedSize(150, 40)
            self.button5.clicked.connect(self.wranging)
            self.button5.setObjectName('choice')
            self.layout1.addStretch()
            self.layout1.addWidget(self.button5)

            tim1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            abb = {"time": f"{tim1}", "content": f"{self.wronglist}文件被修改", "type": "数据修改"}
            with open("logs.json", 'r', encoding="utf-8") as filew:
                jl = json.load(filew)
            jl.append(abb)
            json_str = json.dumps(jl, indent=1, ensure_ascii=False)
            with open("logs.json", 'w', encoding="utf-8") as f:
                f.write(f"{json_str}\n")
        else:
            self.layout1.addStretch()
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)  # 设置是否显示表格上的网格线，True为显示，False不显示
        self.table.setAlternatingRowColors(True)

        self.layout1.addWidget(self.button1)
        self.layout1.addWidget(self.button2)
        self.layout2.addLayout(self.layout1)
        self.layout2.addWidget(self.table)


    def wranging(self):
        QMessageBox.warning(self, "警告", f"{self.wronglist}文件可能被攻击！")
        self.layout1.removeWidget(self.button5)
        self.button5.deleteLater()

    def formatTime(self, atime):

        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(atime))

    def addcont(self):

        self.button1.setText('保存')
        self.button2.setText('删除')

        self.button1.disconnect()
        self.button1.clicked.connect(self.backbutton)

        self.button2.disconnect()
        self.button2.clicked.connect(self.droptext)
        self.check = QtWidgets.QTableWidgetItem()
        self.check.setCheckState(QtCore.Qt.Unchecked)
        self.button3 = QPushButton()
        self.button3.setText('添加')
        self.button3.setFixedSize(150, 40)
        self.button3.setObjectName('choice')
        self.button4 = QPushButton()
        self.button4.setText('全选')
        self.button4.setFixedSize(150, 40)
        self.button4.setObjectName('choice')
        self.button6 = QPushButton()
        self.button6.setText('更新')
        self.button6.setFixedSize(150, 40)
        self.button6.setObjectName('choice')

        self.button3.clicked.connect(self.addnew)
        self.button4.clicked.connect(self.select_all)
        self.button6.clicked.connect(self.updateset)

        self.layout1.addWidget(self.button3)
        self.layout1.addWidget(self.button4)
        self.layout1.addWidget(self.button6)
        self.table.insertColumn(4)
        self.table.setHorizontalHeaderLabels(['数据名称', '时间', '数据集类型', '大小', '选择'])
        for it in range(len(self.files_1)):
            self.check = QtWidgets.QTableWidgetItem()
            self.check.setCheckState(QtCore.Qt.Unchecked)
            self.table.setItem(it, 4, self.check)
            self.item11 = self.table.item(it, 0)
            self.table.cellWidget(it, 2).setEnabled(True)


    def updateset(self):
        tkinter.Tk().withdraw();
        ask = tkinter.messagebox.askyesno("提示", "是否更新数据集备份信息")
        dback = []
        if ask == True:
            os.remove("datamessage.json")
            f = open("datamessage.json", "a+", encoding="utf-8")
            for i in range(len(self.files_1)):
                self.fileinfo = os.stat(self.path + '/' + self.files_1[i])
                s = str(int((self.fileinfo.st_size) / 1024)) + "kb"
                a = {"name": f"{self.files_1[i]}", "time": f"{self.formatTime(self.fileinfo.st_mtime)}", "md5": "",
                     "size": f"{s}", "type": "未知"}
                dback.append(a)
            json_str = json.dumps(dback, indent=1, ensure_ascii=False)
            f.write(f"{json_str}\n")

            tim1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            abb = {"time": f"{tim1}", "content": "数据集备份信息更新", "type": "数据修改"}
            with open("logs.json", 'r', encoding="utf-8") as filew:
                jl = json.load(filew)
            jl.append(abb)
            json_str = json.dumps(jl, indent=1, ensure_ascii=False)
            with open("logs.json", 'w', encoding="utf-8") as f:
                f.write(f"{json_str}\n")

    def addnew(self):
        try:
            fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                              "选取文件",
                                                              "./",
                                                              "All Files (*);;Text Files (*)")  # 设置文件扩展名过滤,注意用双分号间隔
            pathf = os.path.dirname(fileName1)
            fileName = fileName1[len(pathf) + 1:]
            shutil.copyfile(fileName1, f"{self.jl['下载路径']}/{fileName}")
            self.table.clearContents()
            self.files_1 = os.listdir(self.path)
            for j in range(len(self.files_1)):
                self.fileinfo = os.stat(self.path + '/' + self.files_1[j])
                self.item_1 = QTableWidgetItem(self.files_1[j])
                self.item_2 = QTableWidgetItem(self.formatTime(self.fileinfo.st_mtime))
                s = str(int((self.fileinfo.st_size) / 1024)) + "kb"
                self.item_3 = QTableWidgetItem(s)
                self.table.setItem(j, 0, self.item_1)  # 填表，第一行第一列填Hi
                self.table.setItem(j, 1, self.item_2)  # 填表，第一行第一列填Hi
                self.table.setItem(j, 3, self.item_3)  # 填表，第一行第一列填Hi
                self.check = QtWidgets.QTableWidgetItem()
                self.check.setCheckState(QtCore.Qt.Unchecked)
                self.table.setItem(j, 4, self.check)
                self.item11 = self.table.item(j, 0)
                self.comboBoxList = (["未知", "图像数据集", "语音数据集", "文本数据集", "预训练模型"])
                self.comboBox = QtWidgets.QComboBox()
                self.comboBox.addItems(self.comboBoxList)
                self.comboBox.setStyleSheet("QComboBox{margin:3px;font:20px 'Microsoft YaHei';color:#47B0E7;};")
                self.comboBox.setEnabled(False)
                self.table.setCellWidget(j, 2, self.comboBox)
        except:
            pass

    def select_all(self):
        for i in range(len(self.files_1)):
            self.check = QtWidgets.QTableWidgetItem()
            self.check.setCheckState(QtCore.Qt.Checked)
            self.table.setItem(i, 4, self.check)
        self.button4.setText('取消全选')
        self.button4.disconnect()
        self.button4.clicked.connect(self.cancel_all)

    def cancel_all(self):
        for i in range(len(self.files_1)):
            self.check = QtWidgets.QTableWidgetItem()
            self.check.setCheckState(QtCore.Qt.Unchecked)
            self.table.setItem(i, 4, self.check)

        self.button4.setText('全选')
        self.button4.disconnect()
        self.button4.clicked.connect(self.select_all)

    def droptext(self):
        panduan = 0
        for i in range(len(self.files_1)):
            if self.table.item(i, 4).checkState() == 2:
                a = self.table.item(i, 0).text()
                if "." not in a:
                    try:
                        os.rmdir(f'{self.path}\{a}')
                    except:
                        QMessageBox.information(self,"提示","无法删除非空文件夹")
                else:
                    os.remove(f'{self.path}\{a}')
                panduan = 2
        if panduan == 2:
            self.table.clearContents()
            self.files_1 = os.listdir(self.path)
            for j in range(len(self.files_1)):
                self.fileinfo = os.stat(self.path + '/' + self.files_1[j])
                self.item_1 = QTableWidgetItem(self.files_1[j])
                self.item_2 = QTableWidgetItem(self.formatTime(self.fileinfo.st_mtime))
                s = str(int((self.fileinfo.st_size) / 1024)) + "kb"
                self.item_3 = QTableWidgetItem(s)
                self.table.setItem(j, 0, self.item_1)  # 填表，第一行第一列填Hi
                self.table.setItem(j, 1, self.item_2)  # 填表，第一行第一列填Hi
                self.table.setItem(j, 3, self.item_3)  # 填表，第一行第一列填Hi
                self.check = QtWidgets.QTableWidgetItem()
                self.check.setCheckState(QtCore.Qt.Unchecked)
                self.table.setItem(j, 4, self.check)
                self.item11 = self.table.item(j, 0)

                self.comboBoxList = (["未知", "图像数据集", "语音数据集", "文本数据集", "预训练模型"])
                self.comboBox = QtWidgets.QComboBox()
                self.comboBox.addItems(self.comboBoxList)
                self.comboBox.setStyleSheet("QComboBox{margin:3px;font:20px 'Microsoft YaHei';color:#47B0E7;};")
                self.comboBox.setEnabled(False)
                self.table.setCellWidget(j, 2, self.comboBox)
        else:
            QMessageBox.information(self, "提示", "未选择文件")


    def backbutton(self):

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout1.removeWidget(self.button3)
        self.layout1.removeWidget(self.button4)
        self.layout1.removeWidget(self.button6)
        self.button3.deleteLater()
        self.button4.deleteLater()
        self.button6.deleteLater()
        self.table.removeColumn(4)
        self.table.removeColumn(4)
        self.button1.setText('管理')
        self.button2.setText('文件夹中打开')
        self.button1.disconnect()
        self.button2.disconnect()
        self.button1.clicked.connect(self.addcont)
        self.button2.clicked.connect(self.open_directory)
        f = open("typetext.json", 'r', encoding="utf-8")
        jl = json.load(f)
        for i in range(len(self.files_1)):
            judge = 1
            self.setname = self.table.item(i, 0).text()
            self.typetext = self.table.cellWidget(i, 2).currentText()

            for j in range(len(jl)):
                if jl[j]['name'] == self.setname:
                    judge = 2
                    jl[j]['type'] = self.typetext
            if judge == 1:
                temporary = {'name': self.setname, 'type': self.typetext}
                jl.append(temporary)
            self.table.cellWidget(i, 2).setEnabled(False)
        json_str = json.dumps(jl, indent=1, ensure_ascii=False)
        with open("typetext.json", 'w', encoding="utf-8") as f:
            f.write(f"{json_str}\n")

    def open_directory(self):
        start_directory = f'{self.jl["下载路径"]}'
        try:
            os.startfile(start_directory)
        except:
            os.startfile('datafile')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    demo = manage()
    demo.show()
    sys.exit(app.exec_())
