import time
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtGui import QPalette, QPixmap, QBrush
import sys
from PyQt5.QtCore import Qt


class qpgb(QWidget):
    def __init__(self):
        super(qpgb, self).__init__()
        self.initUI()
        self.resize(1240, 732)
        self.initUI()
        palette = QPalette()
        pix = QPixmap("background.jpg")
        pix = pix.scaled(1920, 1080)
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def initUI(self):
        # 构建一个进度条
        l1 = QtWidgets.QLabel(self)
        l1.setText("检测进度")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        l1.setFont(font)
        l1.setStyleSheet("QWidget{font:40pt}")
        # l1.move(120,120)
        l1.resize(1240, 200)
        l1.setAlignment(Qt.AlignCenter)
        self.pbar = QProgressBar(self)
        # 从左上角30-50的界面，显示一个200*25的界面
        self.pbar.setFixedSize(1000, 50)  # 设置进度条的位置
        self.pbar.setAlignment(Qt.AlignCenter)
        self.pbar.move(120, 500)
        # 设置开始按钮
        self.pv = 0
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(100)
        self.pbar.setValue(self.pv)


if __name__ == '__main__':
    # 创建一个Qt应用对象
    app = QApplication(sys.argv)
    myqt = qpgb()
    myqt.show()
    for i in range(101):
        myqt.pbar.setValue(i)
        time.sleep(0.01)
        QApplication.processEvents()  # 实时显示
        if (i == 100):
            sys.exit(app.exec_())
