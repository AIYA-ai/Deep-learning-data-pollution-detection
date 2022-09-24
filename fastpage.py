import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QHBoxLayout, \
    QInputDialog, QFormLayout, QLineEdit, QRadioButton, QFileDialog, QButtonGroup
from PyQt5 import QtGui, QtWidgets
import sys


class formwighte(QWidget):
    def __init__(self):
        super(formwighte, self).__init__()
        self.resize(1240, 732)
        self.iniUI()
        palette = QPalette()
        pix = QPixmap("background.jpg")
        pix = pix.scaled(1920, 1080)
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def iniUI(self):
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        formlagout = QFormLayout()
        self.edt = QLineEdit()
        self.edt.setFixedSize(500, 40)
        self.edt.setObjectName("editline")
        self.edt.setText("")
        self.local_edt = QLineEdit()
        self.local_edt.setFixedSize(500, 40)
        self.local_edt.setObjectName("editline")
        hbotton = QHBoxLayout()
        self.submit_btn = QPushButton("确定")
        self.submit_btn.setObjectName("mitcancel")
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.setObjectName("mitcancel")
        self.submit_btn.setFixedSize(200, 50)
        self.cancel_btn.setFixedSize(200, 50)
        hbotton.addWidget(self.submit_btn)
        hbotton.addWidget(self.cancel_btn)
        hbotton.setAlignment(Qt.AlignCenter)
        # 添加到表单布局里

        v_box1 = QHBoxLayout()
        self.group1 = QButtonGroup()
        self.folder = QRadioButton("文件夹")
        self.folder.toggled.connect(self.changeradio1)
        self.folder.setChecked(True)
        self.filemessage = QRadioButton("文件")
        self.filemessage.toggled.connect(self.changeradio1)
        self.group1.addButton(self.folder)
        self.group1.addButton(self.filemessage)
        self.folder.setObjectName('radiobutton')
        self.filemessage.setObjectName('radiobutton')
        # # text.clicked.connect(self.radio)
        allname = QLabel("上传文件类型:")
        allname.setObjectName("textsize")
        v_box1.addStretch()
        # # v_box.addStretch(3)
        v_box1.addWidget(allname)
        v_box1.addWidget(self.folder)
        v_box1.addWidget(self.filemessage)
        # v_box.addStretch(8)
        v_box1.addStretch()

        v_box = QHBoxLayout()
        self.allset = QRadioButton("全部")
        self.allset.toggled.connect(self.changeradio)
        self.allset.setChecked(True)
        self.image = QRadioButton("图像数据集")
        # image.toggled.connect(self.buttonState)
        self.image.toggled.connect(self.changeradio)
        self.text = QRadioButton("文本数据集")
        self.text.toggled.connect(self.changeradio)
        # text.clicked.connect(self.radio)
        self.radio = QRadioButton("语音数据集")
        self.radio.toggled.connect(self.changeradio)
        self.model = QRadioButton("预训练模型")
        self.model.toggled.connect(self.changeradio)
        self.allset.setObjectName('radiobutton')
        self.image.setObjectName('radiobutton')
        self.text.setObjectName('radiobutton')
        self.radio.setObjectName('radiobutton')
        self.model.setObjectName('radiobutton')
        # text.clicked.connect(self.radio)
        d = QLabel("数据类型:")
        d.setObjectName("textsize")
        v_box.addStretch()
        v_box.addWidget(d)
        v_box.addWidget(self.allset)
        v_box.addWidget(self.image)
        v_box.addWidget(self.text)
        v_box.addWidget(self.radio)
        v_box.addWidget(self.model)
        v_box.addStretch()
        ab = QVBoxLayout(self)

        self.choice1 = QPushButton(self)
        self.choice1.setText('选择')
        self.choice1.clicked.connect(self.getItem)
        self.choice1.setFixedSize(100, 40)
        self.choice1.setObjectName("choice")

        formlagout.addRow(self.edt, self.choice1)
        formlagout.setLabelAlignment(Qt.AlignCenter)
        self.choice2 = QPushButton("选择")
        self.choice2.setFixedSize(100, 40)
        self.choice2.clicked.connect(self.mfd)
        self.choice2.setObjectName("choice")
        formlagout1 = QFormLayout()
        formlagout2 = QFormLayout()

        aaa = QHBoxLayout()
        edt_lable = QLabel("  对比数据集:")
        edt_lable.setObjectName("textsize")
        formlagout2.addRow(edt_lable, self.edt)
        aaa.addStretch(1)
        aaa.addLayout(formlagout2)
        aaa.addWidget(self.choice1)
        aaa.setAlignment(Qt.AlignCenter)
        aaa.addStretch(1)

        bbb = QHBoxLayout()
        local_lable = QLabel("  本地数据集:")
        local_lable.setObjectName("textsize")
        formlagout1.addRow(local_lable, self.local_edt)
        bbb.addStretch(1)
        bbb.addLayout(formlagout1)
        bbb.addWidget(self.choice2)
        bbb.setAlignment(Qt.AlignCenter)
        bbb.addStretch(1)
        ab.addLayout(v_box1)
        ab.addLayout(v_box)

        ab.addLayout(bbb)
        ab.addLayout(aaa)
        ab.addLayout(hbotton)
        ab.setAlignment(Qt.AlignCenter)

    def changeradio(self):
        if self.allset.isChecked() == True:
            dataname = 'all_table'
        elif self.image.isChecked() == True:
            dataname = 'image_table'
        elif self.model.isChecked() == True:
            dataname = 'pretraining_table'
        elif self.text.isChecked() == True:
            dataname = 'image_table'
        elif self.radio.isChecked() == True:
            dataname = 'voice_table'

        self.result = []
        con = self.mysql_db()
        cur = con.cursor()
        sql = f"select data_name from {dataname}"
        cur.execute(sql)
        while 1:
            d = cur.fetchone()
            if d != None:
                if d[0] not in self.result:
                    self.result.append(d[0])
            else:
                break

    def changeradio1(self):
        try:
            if self.folder.isChecked() == True:
                self.choice2.disconnect()
                self.choice2.clicked.connect(self.mfd)
            elif self.filemessage.isChecked() == True:
                self.choice2.disconnect()
                self.choice2.clicked.connect(self.msg)
        except:
            pass

    def mysql_db(self):
        # 连接数据库肯定需要一些参数
        conn = pymysql.connect(
            host="106.12.144.39",
            port=3306,
            database="data_verification",
            charset="utf8",
            user="tourist",
            passwd="~!@#cxsys987",
            autocommit=True
        )
        return conn

    def mfd(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        self.local_edt.setText(directory1)

    def msg(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.local_edt.setText(fileName1)

    def getItem(self):

        items = self.result
        dialog = QInputDialog()
        item, ok = dialog.getItem(self, '请选择对比数据', '数据列表', items)
        if ok and item:  # 点击ok且不为空
            self.edt.setText(item)
        temp_list = QtWidgets.QCompleter(items)
        self.edt.setCompleter(temp_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    windous = formwighte()
    windous.show()
    sys.exit(app.exec_())
