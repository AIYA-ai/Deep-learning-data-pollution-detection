from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class choicepage(QWidget):
    def __init__(self, *args):
        super(choicepage, self).__init__(*args)
        self.resize(1240, 732)
        self.initUI()
        palette = QPalette()
        pix = QPixmap("background.jpg")
        pix = pix.scaled(1920, 1080)
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def initUI(self):
        self.text = "选择检测模式"
        self.box = QHBoxLayout(self)
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        l1 = QtWidgets.QLabel(self)
        l1.setText("选择检测模式")
        l1.setFont(font)
        l1.setStyleSheet("QWidget{font:40pt}")
        l1.resize(1240, 200)
        l1.setAlignment(Qt.AlignCenter)

        global a1
        global a2
        global a3
        a1 = MyBtn(self)

        a1.setText("快速检测\n\n\n\n\n\n")
        a1.setObjectName("button1")
        a1.setGeometry(
            QtCore.QRect(int(self.size().width() / 7.5), int(self.size().height() / 4), int(self.size().height() / 2 / 8 * 5),
                         int(self.size().height() / 2)))
        a1.setFont(font)
        self.a1 = a1

        self.a11 = MyBtn(self)
        self.a11.setText("        适合大批量的图像\n数据，对文本，可快速\n对数据健康进行检测，\n有一定可靠性。          ")
        self.a11.setObjectName("button11")
        self.a11.setGeometry(
            QtCore.QRect(int(self.size().width() / 7.5), int(self.size().height() / 4), int(self.size().height() / 2 / 8 * 5),
                         int(self.size().height() / 2)))
        self.a11.setFont(font)

        a2 = MyBtn(self)
        a2.setText("慢速检测\n\n\n\n\n\n")
        a2.setObjectName("button1")
        a2.setGeometry(
            QtCore.QRect(int(self.size().width() / 7.5 * 3), int(self.size().height() / 4), int(self.size().height() / 2 / 8 * 5),
                         int(self.size().height() / 2)))
        a2.setFont(font)
        self.a2 = a2
        self.a22 = MyBtn(self)
        self.a22.setText("        适合中批量的图像\n数据，对文本，可较快\n对数据健康进行检测，\n有足够的可靠性。        ")
        self.a22.setObjectName("button22")
        self.a22.setGeometry(
            QtCore.QRect(int(self.size().width() / 7.5 * 3), int(self.size().height() / 4), int(self.size().height() / 2 / 8 * 5),
                         int(self.size().height() / 2)))
        self.a22.setFont(font)

        a3 = MyBtn(self)
        a3.setText("本地检测\n\n\n\n\n\n")
        a3.setObjectName("button1")
        a3.setGeometry(
            QtCore.QRect(int(self.size().width() / 7.5 * 5),int(self.size().height() / 4), int(self.size().height() / 2 / 8 * 5),
                         int(self.size().height() / 2)))
        a3.setFont(font)
        self.a3 = a3
        self.a33 = MyBtn(self)
        self.a33.setText("        当数据库没有要对比的数据时，\n或小批量图像数据检测\n是具有极高的可靠性。                  \n")
        self.a33.setObjectName("button33")
        self.a33.setGeometry(
            QtCore.QRect(int(self.size().width() / 7.5 * 5), int(self.size().height() / 4), int(self.size().height() / 2 / 8 * 5),
                         int(self.size().height() / 2)))
        self.a33.setFont(font)


class MyBtn(QPushButton):

    def __init__(self, text):
        super().__init__(text)
        self.ww = 100
        self.hh = 100

    def enterEvent(self, a0):
        self.ww = self.size().width()
        self.hh = self.size().height()
        new_width = self.size().width() + 80
        new_height = self.size().height() + 80

        if self.objectName() == "button11":
            a1.resize(new_width, new_height)
            a1.move(self.pos().x() - 40, self.pos().y() - 40)
            self.resize(new_width, new_height)
            self.move(self.pos().x() - 40, self.pos().y() - 40)
            a1.setStyleSheet("QWidget{font:35pt}")
        elif self.objectName() == "button22":
            a2.resize(new_width, new_height)
            a2.move(self.pos().x() - 40, self.pos().y() - 40)
            self.resize(new_width, new_height)
            self.move(self.pos().x() - 40, self.pos().y() - 40)
            a2.setStyleSheet("QWidget{font:35pt}")
        elif self.objectName() == "button33":
            a3.resize(new_width, new_height)
            a3.move(self.pos().x() - 40, self.pos().y() - 40)
            self.resize(new_width, new_height)
            self.move(self.pos().x() - 40, self.pos().y() - 40)
            a3.setStyleSheet("QWidget{font:35pt}")
        return super().enterEvent(a0)

    def leaveEvent(self, a0):
        old_width = self.size().width() - 80
        old_height = self.size().height() - 80
        if self.objectName() == "button11":
            a1.resize(old_width, old_height)
            a1.move(self.pos().x() + 40, self.pos().y() + 40)
            self.move(self.pos().x() + 40, self.pos().y() + 40)
            self.resize(old_width, old_height)
            a1.setStyleSheet("QWidget{font:30pt}")
        elif self.objectName() == "button22":
            a2.resize(old_width, old_height)
            a2.move(self.pos().x() + 40, self.pos().y() + 40)
            self.move(self.pos().x() + 40, self.pos().y() + 40)
            self.resize(old_width, old_height)
            a2.setStyleSheet("QWidget{font:30pt}")
        elif self.objectName() == "button33":
            a3.resize(old_width, old_height)
            a3.move(self.pos().x() + 40, self.pos().y() + 40)
            self.move(self.pos().x() + 40, self.pos().y() + 40)
            self.resize(old_width, old_height)
            a3.setStyleSheet("QWidget{font:30pt}")
        return super().leaveEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./buttun.qss").read())
    # 创建主窗口
    browser = choicepage()
    browser.show()
    # 运行应用，并监听事件
    sys.exit(app.exec_())
