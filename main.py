# -*- coding:utf-8 -*-
import time
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from homepage import choicepage
from fastpage import formwighte
from management import manage
from setting import setpage
from journalpage import journalpage
from web import Webpage
from md5 import md5contrast
from progress import qpgb
from finalpage import baogaopage
from detailed_md5 import confirmation
from slowpage import slow_confirm
from localpage import local_confirm


class QTitleLabel(QLabel):
    """
    新建标题栏标签类
    """

    def __init__(self, *args):
        super(QTitleLabel, self).__init__(*args)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFixedHeight(40)


class QTitleButton(QPushButton):
    """
    新建标题栏按钮类
    """

    def __init__(self, *args):
        super(QTitleButton, self).__init__(*args)
        self.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self.setFixedWidth(40)


class QUnFrameWindow(QMainWindow):

    def __init__(self):

        super(QUnFrameWindow, self).__init__(None, Qt.FramelessWindowHint)  # 无边框
        self.ri_widget()
        self.init_widget()
        self.menu1()
        self._padding = 5  # 设置边界宽度为5
        self.initTitleLabel()  # 安放标题栏标签
        self.setWindowTitle = self._setTitleText(self.setWindowTitle)  # 用装饰器将设置WindowTitle名字函数共享到标题栏标签上
        self.setWindowTitle("深度学习数据污染检测系统")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.initLayout()  # 设置框架布局
        self.setMinimumWidth(720)
        self.setMinimumHeight(480)
        self.resize(1440, 810)
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self.initDrag()  # 设置鼠标跟踪判断默认值
        self.bottem()
        self.status()
        _h_rect = 720
        _w_rect = 1440

    def init_left2(self):
        '''
        初始化左侧布局
        '''
        self.left_widget = QWidget(self)  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')  # 左侧部件对象命名
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.left_widget.setLayout(self.left_layout)  # 将左侧部件设置为网格布局
        self.left_widget.setGeometry(QtCore.QRect(220, 59, 1440 - 220, 1980))
        # self.stackedWidget_param.setFixedWidth(220)
        self.left_widget.setStyleSheet("QWidget{background-color:#bababa;border:none}")

        # 接下来添加按钮控件等...，细节略

    def status(self):
        status = self.statusBar()  # 创建状态栏
        status.showMessage("就绪!")  # 显示消息
        status.resize(1440, 30)
        status.setStyleSheet("QWidget{background-color:#ffffff;}")

    def menu1(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('文件')
        editMenu = mainMenu.addMenu('编辑')
        viewMenu = mainMenu.addMenu('视图')
        searchMenu = mainMenu.addMenu('搜索')
        toolsMenu = mainMenu.addMenu('工具')
        helpMenu = mainMenu.addMenu('帮助')
        mainMenu.setStyleSheet("QMenuBar{background-color:#E7F0F2")
        # mainMenu.setContentsMargins(0, 0, 0, 0)
        # mainMenu.setGeometry(QtCore.QRect(30, 30, 1280, 50))
        # impMenu = QMenu("Import", self)  # 创建菜单项
        # impAct = QAction("Import Email", self)  # Import菜单下有子菜单 Import Email
        # impMenu.addAction(impAct)

    #
    def screensize(self):
        #     # 获取显示器分辨率大小
        width = self.size().width()
        height = self.size().height()
        return width, height

    def init_widget(self):
        self.stackedWidget_param = QtWidgets.QStackedWidget(self)  # QStackedWidget表示多分页的窗口
        self.stackedWidget_param.setObjectName("stackedWidget_param")
        self.stackedWidget_param.setGeometry(QtCore.QRect(0, 58, 200, 810 - 78))
        self.stackedWidget_param.setStyleSheet("QWidget{background-color:#ffffff;border:none}")

    def bottem(self):
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        ll, tt, x, y = 0, 60, 200, 40
        self.btn1 = QPushButton("主      页", self)
        self.btn1.setFont(font)
        self.btn1.setGeometry(QtCore.QRect(ll, tt, x, y))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn1.setIcon(icon1)
        self.btn1.clicked.connect(self.btn1see)
        self.btn1.setObjectName("button")

        self.btn2 = QPushButton("数据管理", self)
        self.btn2.setFont(font)
        self.btn2.setGeometry(QtCore.QRect(ll, 110, x, y))
        icon1.addPixmap(QtGui.QPixmap("./icon/guanli.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn2.setIcon(icon1)
        self.btn2.clicked.connect(self.btn2see)
        self.btn2.setObjectName("button")

        self.btn3 = QPushButton("网      页", self)
        self.btn3.setFont(font)
        self.btn3.setGeometry(QtCore.QRect(ll, 160, x, y))
        icon1.addPixmap(QtGui.QPixmap("./icon/sousuo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn3.setIcon(icon1)
        self.btn3.clicked.connect(self.btn3see)
        self.btn3.setObjectName("button")

        self.btn4 = QPushButton("日志记录", self)
        self.btn4.setFont(font)
        self.btn4.setGeometry(QtCore.QRect(ll, 210, x, y))
        icon1.addPixmap(QtGui.QPixmap("./icon/rizhi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn4.setIcon(icon1)
        self.btn4.clicked.connect(self.btn4see)
        self.btn4.setObjectName("button")

        self.btn5 = QPushButton("收      起", self)
        self.btn5.setFont(font)
        self.btn5.setGeometry(QtCore.QRect(ll, 260, x, y))
        icon1.addPixmap(QtGui.QPixmap("./icon/shouqi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn5.setIcon(icon1)
        self.btn5.clicked.connect(self.change)
        self.btn5.setObjectName("button")

        self.btn6 = QPushButton("设      置", self)
        self.btn6.setFont(font)
        self.btn6.setGeometry(QtCore.QRect(ll, 310, x, y))
        self.btn6.setObjectName("button")
        icon1.addPixmap(QtGui.QPixmap("./icon/shezhi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn6.setIcon(icon1)
        self.btn6.clicked.connect(self.btn5see)
        self.btn6.setObjectName("button")

    def btn1see(self):
        self.stackedWidget.setCurrentIndex(0)

    def btn2see(self):
        self.stackedWidget.setCurrentIndex(3)

    def btn3see(self):
        self.stackedWidget.setCurrentIndex(1)

    def btn4see(self):
        self.stackedWidget.setCurrentIndex(5)

    def btn5see(self):
        self.stackedWidget.setCurrentIndex(4)

    def change(self):
        h, w = self.screensize()
        if (self.stackedWidget_param.width() == 200):
            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("./icon/zhankai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn5.setIcon(icon1)
            for i in range(200, 49, -10):
                self.stackedWidget_param.setGeometry(QtCore.QRect(0, 59, i, h))
                self.btn1.setGeometry(QtCore.QRect(0, 60, i, 40))
                self.btn2.setGeometry(QtCore.QRect(0, 110, i, 40))
                self.btn3.setGeometry(QtCore.QRect(0, 160, i, 40))
                self.btn4.setGeometry(QtCore.QRect(0, 210, i, 40))
                self.btn5.setGeometry(QtCore.QRect(0, 260, i, 40))
                self.btn6.setGeometry(QtCore.QRect(0, 310, i, 40))
                self.stackedWidget.setGeometry(QtCore.QRect(i, 58, self._TitleLabel.size().width() - i, w))
                QApplication.processEvents()
                time.sleep(0.005)

        else:
            self.btn1.setText("主      页")
            self.btn2.setText("数据管理")
            self.btn3.setText("网      页")
            self.btn4.setText("日志记录")
            self.btn5.setText("收      起")
            self.btn6.setText("设      置")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("./icon/shouqi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn5.setIcon(icon1)

            for i in range(50, 201, 10):
                self.stackedWidget_param.setGeometry(QtCore.QRect(0, 59, i, h))
                self.btn1.setGeometry(QtCore.QRect(0, 60, i, 40))
                self.btn2.setGeometry(QtCore.QRect(0, 110, i, 40))
                self.btn3.setGeometry(QtCore.QRect(0, 160, i, 40))
                self.btn4.setGeometry(QtCore.QRect(0, 210, i, 40))
                self.btn5.setGeometry(QtCore.QRect(0, 260, i, 40))
                self.btn6.setGeometry(QtCore.QRect(0, 310, i, 40))
                self.stackedWidget.setGeometry(QtCore.QRect(i, 58, self._TitleLabel.size().width() - i, w))
                QApplication.processEvents()
                time.sleep(0.005)
        self.page0.a1.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a2.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9 * 3.5),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a3.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9 * 6),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a11.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a22.setGeometry(
            QtCore.QRect(
                int((self.size().width() - self.stackedWidget_param.width()) / 9 * 3.5), int(self.size().height() / 4),
                int((self.size().height() / 2 / 8 * 5)), int(self.size().height() / 2)))
        self.page0.a33.setGeometry(
            QtCore.QRect(
                int((self.size().width() - self.stackedWidget_param.width()) / 9 * 6), int(self.size().height() / 4),
                int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))

    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def initTitleLabel(self):
        # 安放标题栏标签
        self._TitleLabel = QTitleLabel(self)
        self._TitleLabel.setMouseTracking(False)  # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        self._TitleLabel.setIndent(10)  # 设置标题栏文本缩进
        self._TitleLabel.move(0, 0)  # 标题栏安放到左上角

    def ri_widget(self):
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.page0 = choicepage()  # 主页
        self.page1 = Webpage()  # 网页
        self.page2 = formwighte()  # 快速页面
        self.page3 = manage()  # 数据管理界面
        self.page4 = setpage()  # 设置界面
        self.page5 = journalpage()  # 日志界面
        self.page6 = qpgb()  # 加载页面
        self.page7 = md5contrast()  # md5生成
        self.page8 = baogaopage()  # 报告界面
        self.page9 = confirmation()  # 检测所有文件md5
        self.page10 = slow_confirm()  # 慢速页面
        self.page11 = local_confirm()  # 本地页面
        self.stackedWidget.addWidget(self.page0)
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page3)
        self.stackedWidget.addWidget(self.page4)
        self.stackedWidget.addWidget(self.page5)
        self.stackedWidget.addWidget(self.page6)
        self.stackedWidget.addWidget(self.page8)
        self.stackedWidget.addWidget(self.page10)
        self.stackedWidget.addWidget(self.page11)
        self.page0.a11.clicked.connect(self.pd1)
        self.page0.a22.clicked.connect(self.pd2)
        self.page0.a33.clicked.connect(self.pd3)
        self.page2.cancel_btn.clicked.connect(self.homepage)
        self.page2.submit_btn.clicked.connect(self.homepage3)
        self.page10.cancel_btn.clicked.connect(self.homepage)
        self.page10.submit_btn.clicked.connect(self.homepage3)
        self.page11.cancel_btn.clicked.connect(self.homepage)
        self.page11.submit_btn.clicked.connect(self.homepage3)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 58, 1440 - 200, 810 - 78))

    def homepage(self):
        self.stackedWidget.setCurrentIndex(0)

    def pd1(self):
        self.tt = '快速检测'
        self.stackedWidget.setCurrentIndex(2)

    def pd2(self):
        self.tt = '慢速检测'
        self.stackedWidget.setCurrentIndex(8)

    def pd3(self):
        self.tt = '本地检测'
        self.stackedWidget.setCurrentIndex(9)

    def homepage3(self):
        if self.page2.edt.text() == '' and self.page10.edt.text() == '' and self.page11.local_edt.text() == '':
            QMessageBox.information(self, "提示", "未选择数据集")
        elif self.page2.local_edt.text() == '' and self.page10.local_edt.text() == '' and self.page11.local_edt.text() == '':
            QMessageBox.information(self, "提示", "未选择数据集")
        else:
            self.stackedWidget.setCurrentIndex(6)
            for i in range(40):
                self.page6.pbar.setValue(i)
                time.sleep(0.01)
                QApplication.processEvents()  # 实时显示

            if self.tt == '快速检测':
                self.result = self.page7.getting(self.page2.local_edt.text(), self.page2.edt.text())
                self.page8.edt3.setText('无')
                self.page8.edt1.setText(self.page2.local_edt.text())
                self.page8.edt2.setText(self.page2.edt.text())
            elif self.tt == '慢速检测':
                self.result = self.page9.inspect(self.page10.local_edt.text(), self.page10.edt.text())
                self.page8.edt3.setText('被污染数据集：' + str(self.page9.wrrong))
                self.page8.edt1.setText(self.page10.local_edt.text())
                self.page8.edt2.setText(self.page10.edt.text())
            else:
                self.result = self.page11.operation()
                self.page8.edt3.setText('无')
                self.page8.edt1.setText(self.page11.local_edt.text())
                self.page8.edt2.setText('无')
            if self.result == True:
                txt1 = '数据没有被污染'
            elif self.result == False or (type(self.result) != float and type(self.result) != int):
                txt1 = '数据被污染'
            else:
                txt1 = '被污染概率：' + str(self.result)
            for i in range(41, 101):
                self.page6.pbar.setValue(i)
                time.sleep(0.01)
                QApplication.processEvents()  # 实时显示
            self.stackedWidget.setCurrentIndex(7)
            self.page8.edt4.setText(self.tt)
            self.page8.edt5.setText(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            self.page8.edt6.setText(txt1)
            self.page8.buttn2.clicked.connect(self.homepage)

    def mangement(self):
        self.stackedWidget.setCurrentIndex(3)

    def webpage(self):
        self.stackedWidget.setCurrentIndex(2)

    def rizhi(self):
        self.stackedWidget.setCurrentIndex(5)

    def setting(self):
        self.stackedWidget.setCurrentIndex(3)

    def initLayout(self):
        # 设置框架布局
        self._MainLayout = QVBoxLayout()
        self._MainLayout.setSpacing(0)
        self._MainLayout.addWidget(QLabel(), Qt.AlignLeft)  # 顶一个QLabel在竖放框架第一行，以免正常内容挤占到标题范围里
        self._MainLayout.addStretch()
        self.setLayout(self._MainLayout)

    def addLayout(self, QLayout):
        # 给widget定义一个addLayout函数，以实现往竖放框架的正确内容区内嵌套Layout框架
        self._MainLayout.addLayout(QLayout)

    def _setTitleText(self, func):
        # 设置标题栏标签的装饰器函数
        def wrapper(*args):
            self._TitleLabel.setText(*args)
            return func(*args)

        return wrapper

    def setTitleAlignment(self, alignment):
        # 给widget定义一个setTitleAlignment函数，以实现标题栏标签的对齐方式设定
        self._TitleLabel.setAlignment(alignment | Qt.AlignVCenter)

    def setCloseButton(self, bool):
        # 给widget定义一个setCloseButton函数，为True时设置一个关闭按钮
        if bool == True:
            self._CloseButton = QTitleButton(b'\xef\x81\xb2'.decode("utf-8"), self)
            self._CloseButton.setObjectName("CloseButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
            self._CloseButton.setToolTip("关闭窗口")
            self._CloseButton.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
            self._CloseButton.setFixedHeight(self._TitleLabel.height())  # 设置按钮高度为标题栏高度
            self._CloseButton.clicked.connect(self.close)  # 按钮信号连接到关闭窗口的槽函数

    def setMinMaxButtons(self, bool):
        # 给widget定义一个setMinMaxButtons函数，为True时设置一组最小化最大化按钮
        if bool == True:
            self._MinimumButton = QTitleButton(b'\xef\x80\xb0'.decode("utf-8"), self)
            self._MinimumButton.setObjectName("MinMaxButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
            self._MinimumButton.setToolTip("最小化")
            self._MinimumButton.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
            self._MinimumButton.setFixedHeight(self._TitleLabel.height())  # 设置按钮高度为标题栏高度
            self._MinimumButton.clicked.connect(self.showMinimized)  # 按钮信号连接到最小化窗口的槽函数
            self._MaximumButton = QTitleButton(b'\xef\x80\xb1'.decode("utf-8"), self)
            self._MaximumButton.setObjectName("MinMaxButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
            self._MaximumButton.setToolTip("最大化")
            self._MaximumButton.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
            self._MaximumButton.setFixedHeight(self._TitleLabel.height())  # 设置按钮高度为标题栏高度
            self._MaximumButton.clicked.connect(self._changeNormalButton)  # 按钮信号连接切换到恢复窗口大小按钮函数

    def _changeNormalButton(self):
        # 切换到恢复窗口大小按钮
        try:
            self.showMaximized()  # 先实现窗口最大化
            self._MaximumButton.setText(b'\xef\x80\xb2'.decode("utf-8"))  # 更改按钮文本
            self._MaximumButton.setToolTip("恢复")  # 更改按钮提示
            self._MaximumButton.disconnect()  # 断开原本的信号槽连接
            self._MaximumButton.clicked.connect(self._changeMaxButton)  # 重新连接信号和槽
        except:
            pass

    def _changeMaxButton(self):
        # 切换到最大化按钮
        try:
            self.showNormal()
            self._MaximumButton.setText(b'\xef\x80\xb1'.decode("utf-8"))
            self._MaximumButton.setToolTip("最大化")
            self._MaximumButton.disconnect()
            self._MaximumButton.clicked.connect(self._changeNormalButton)
        except:
            pass

    def resizeEvent(self, QResizeEvent):
        # 自定义窗口调整大小事件
        self._TitleLabel.setFixedWidth(self.width())  # 将标题标签始终设为窗口宽度
        self.stackedWidget.setGeometry(QtCore.QRect(self.stackedWidget_param.size().width(), 58,
                                                    self.width() - self.stackedWidget_param.size().width(),
                                                    self.height() - 78))
        self.stackedWidget_param.setGeometry(
            QtCore.QRect(0, 58, self.stackedWidget_param.size().width(), self.height() - 78))
        self.page0.a1.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a2.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9 * 3.5),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a3.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9 * 6),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a11.setGeometry(
            QtCore.QRect(int((self.size().width() - self.stackedWidget_param.width()) / 9),
                         int(self.size().height() / 4),
                         int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        self.page0.a22.setGeometry(
            QtCore.QRect(
                int((self.size().width() - self.stackedWidget_param.width()) / 9 * 3.5), int(self.size().height() / 4),
                int((self.size().height() / 2 / 8 * 5)), int(self.size().height() / 2)))
        self.page0.a33.setGeometry(
            QtCore.QRect(
                int((self.size().width() - self.stackedWidget_param.width()) / 9 * 6), int(self.size().height() / 4),
                int(self.size().height() / 2 / 8 * 5), int(self.size().height() / 2)))
        # self.page1.a1.text()
        # 分别移动三个按钮到正确的位置
        try:
            self._CloseButton.move(self.width() - self._CloseButton.width(), 0)
        except:
            pass
        try:
            self._MinimumButton.move(self.width() - (self._CloseButton.width() + 1) * 3 + 1, 0)
        except:
            pass
        try:
            self._MaximumButton.move(self.width() - (self._CloseButton.width() + 1) * 2 + 1, 0)
        except:
            pass
        # 重新调整边界范围以备实现鼠标拖放缩放窗口大小，采用三个列表生成式生成三个列表
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(1, self.height() - self._padding)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                             for y in range(self.height() - self._padding, self.height() + 1)]

    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < self._TitleLabel.height()):
            # 鼠标左键点击标题栏区域
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    window = QUnFrameWindow()
    window.setCloseButton(True)
    window.setMinMaxButtons(True)
    window.show()
    sys.exit(app.exec_())
