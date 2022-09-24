import json
import os
import sys
from datetime import datetime
import pymysql
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QTabWidget, QApplication, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QListWidgetItem, QListWidget, QMessageBox


class WebEngineView(QWebEngineView):

    def __init__(self, mainwindow, parent=None):
        super(WebEngineView, self).__init__(parent)
        self.mainwindow = mainwindow
        ##############
        self.page().windowCloseRequested.connect(self.on_windowCloseRequested)  # 页面关闭请求
        self.page().profile().downloadRequested.connect(self.on_downloadRequested)  # 页面下载请求

    #  支持页面关闭请求
    def on_windowCloseRequested(self):
        the_index = self.mainwindow.tabWidget.currentIndex()
        self.mainwindow.tabWidget.removeTab(the_index)

    #  支持页面下载按钮
    def on_downloadRequested(self, downloadItem):
        if downloadItem.isFinished() == False and downloadItem.state() == 0:
            ###生成文件存储地址
            the_filename = downloadItem.url().fileName()
            QMessageBox.information(self, "提示", "文件开始下载")
            if len(the_filename) == 0 or "." not in the_filename:
                cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                the_filename = "下载文件" + cur_time + ".xls"
            f = open('config1.json', 'r', encoding='utf-8')
            self.jl = json.load(f)
            savepath = self.jl['下载路径']
            the_sourceFile = os.path.join(savepath, the_filename)
            downloadItem.setPath(the_sourceFile)
            downloadItem.accept()
            downloadItem.finished.connect(self.on_downloadfinished)

    #  下载结束触发函数
    def on_downloadfinished(self):
        QMessageBox.information(self, "提示", "文件下载完成")
        # 重写createwindow()

    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)
        self.mainwindow.create_tab(new_webview)
        return new_webview


class Webpage(QWidget):
    def __init__(self, *args):
        super(Webpage, self).__init__(*args)
        self.resize(1240, 732)
        self.windows = []
        self.initUI()

    def initUI(self):
        self.windows = []
        icon1 = QtGui.QIcon()
        self.btn1 = QPushButton()
        icon1.addPixmap(QtGui.QPixmap("./icon/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn1.setObjectName("button")
        self.btn1.setIcon(icon1)
        self.btn2 = QPushButton()
        icon1.addPixmap(QtGui.QPixmap("./icon/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn2.setObjectName("button")
        self.btn2.setIcon(icon1)
        self.btn3 = QPushButton()
        icon1.addPixmap(QtGui.QPixmap("./icon/reflash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn3.setObjectName("button")
        self.btn3.setIcon(icon1)
        self.btn3.clicked.connect(self.reflash)

        self.btn4 = QPushButton()
        icon1.addPixmap(QtGui.QPixmap("./icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn4.setObjectName("button")
        self.btn4.setIcon(icon1)
        self.btn4.clicked.connect(self.homepage)

        self.btn5 = QPushButton()
        icon1.addPixmap(QtGui.QPixmap("./icon/collection2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn5.setIcon(icon1)
        self.btn5.setObjectName("button")
        self.btn5.clicked.connect(self.collection1)

        self.btn6 = QPushButton()
        icon1.addPixmap(QtGui.QPixmap("./icon/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn6.setIcon(icon1)
        self.btn6.setObjectName("button")
        self.btn6.clicked.connect(self.displaytt)
        self.edt1 = QLineEdit()
        self.edt1.setFixedHeight(30)
        self.edt1.returnPressed.connect(self.init)
        self.edt1.setObjectName("editline")
        self.tabWidget = QTabWidget()
        self.Hbox = QHBoxLayout()
        self.Hbox.addWidget(self.btn1)
        self.Hbox.addWidget(self.btn2)
        self.Hbox.addWidget(self.btn3)
        self.Hbox.addWidget(self.btn4)
        self.Hbox.addWidget(self.edt1)
        self.Hbox.addWidget(self.btn5)
        self.Hbox.addWidget(self.btn6)
        self.Vbox = QVBoxLayout(self)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.currentChanged.connect(self.changepage)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)

        self.Vbox.addLayout(self.Hbox)
        self.Vbox.addWidget(self.tabWidget)
        ###第一个tab
        self.webview = WebEngineView(self)  # self必须要有，是将主窗口作为参数，传给浏览器
        self.webview.load(QUrl("http://www.baidu.com"))
        self.edt1.setText('https://www.baidu.com')
        self.create_tab(self.webview)
        self.tt1 = QWidget(self)
        self.tt = QWidget(self)

        self.tt.setGeometry(1040, 45, 0, 0)
        self.tt1.setGeometry(1040, 45, 0, 0)
        self.tt1.setStyleSheet("QWidget{background-color:#bababa;border-radius:5px;}")
        self.btn7 = QPushButton()
        self.btn7.setText("收藏")
        self.btn7.setObjectName("choice")
        self.btn7.raise_()
        self.btn7.clicked.connect(self.sss)
        self.btn7.setFixedHeight(40)
        self.btn8 = QPushButton("设置")
        self.btn8.setObjectName("choice")
        self.btn8.setFixedHeight(40)

        self.Vbox1 = QVBoxLayout()

        self.Vbox1.addWidget(self.btn7)
        self.Vbox1.addWidget(self.btn8)
        self.Vbox1.addStretch()
        self.tt.setLayout(self.Vbox1)
        self.tt.setWindowOpacity(0.1)
        self.newwindow = NewWindow()
        self.result = []
        con = self.mysql_db()
        cur = con.cursor()
        sql = f"select webname from blacklist_table"
        cur.execute(sql)
        while 1:
            d = cur.fetchone()
            if d != None:
                self.result.append(d[0])
            else:
                break

    def mysql_db(self):
        # 连接数据库肯定需要一些参数
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            database="data_verification",
            charset="utf8",
            user="root",
            passwd="lyz517",
            autocommit=True
        )
        return conn

    def sss(self):
        self.newwindow.show()

    def hidett(self):
        self.tt.setFixedSize(0, 0)
        self.tt1.setFixedSize(0, 0)
        self.btn6.disconnect()
        self.btn6.clicked.connect(self.displaytt)

    def displaytt(self):
        self.tt.setFixedSize(200, 100)
        self.tt1.setFixedSize(200, 100)
        self.btn6.disconnect()
        self.btn6.clicked.connect(self.hidett)

    def collection1(self):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/collection1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn5.setIcon(icon1)
        self.btn5.disconnect()
        self.btn5.clicked.connect(self.collection2)
        f = open("coll.txt", 'r', encoding='utf-8')
        d = []
        for row in f.readlines():
            d.append(row)
        if self.windows[self.tabWidget.currentIndex()] not in d:
            if self.windows[self.tabWidget.currentIndex()] != '':
                f = open("coll.txt", 'a+', encoding='utf-8')
                f.write(self.windows[self.tabWidget.currentIndex()] + '\n')

    def collection2(self):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/collection2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn5.setIcon(icon1)
        self.btn5.disconnect()
        self.btn5.clicked.connect(self.collection1)
        f = open("coll.txt", 'r', encoding='utf-8')
        d = []
        for row in f.readlines():
            d.append(row)
        if self.windows[self.tabWidget.currentIndex()] + '\n' in d:
            f = open("coll.txt", 'w', encoding='utf-8')
            d.remove(self.windows[self.tabWidget.currentIndex()] + '\n')
            for i in d:
                if i != '':
                    f.write(i)

    def reflash(self):
        self.webview = WebEngineView(self)
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        try:
            self.webview.load(QUrl(self.windows[self.tabWidget.currentIndex() + 1]))
            self.create_tab1(self.webview)
        except:
            pass

    def cheakcoll(self):
        f = open("coll.txt", 'r', encoding='utf-8')
        d = []
        for row in f.readlines():
            d.append(row)
        try:
            if self.windows[self.tabWidget.currentIndex()] + '\n' in d:
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("./icon/collection1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btn5.setIcon(icon1)
                self.btn5.disconnect()
                self.btn5.clicked.connect(self.collection2)
            else:
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("./icon/collection2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btn5.setIcon(icon1)
                self.btn5.disconnect()
                self.btn5.clicked.connect(self.collection1)
        except:
            pass

    def changepage(self):
        try:
            if self.edt1.text() in self.windows:
                self.edt1.setText(self.windows[self.tabWidget.currentIndex()])
                self.edt1.setCursorPosition(0)
        except:
            pass
        self.cheakcoll()

    def create_tab(self, webview):

        self.tab = QWidget()
        webview.urlChanged.connect(self.renewUrl)
        webview.titleChanged.connect(self.update_title)
        self.tabWidget.addTab(self.tab, "新建页面")
        self.tabWidget.setCurrentWidget(self.tab)
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)
        self.cheakcoll()

    def create_tab1(self, webview):

        self.tab = QWidget()
        webview.urlChanged.connect(self.renewUrl)
        webview.titleChanged.connect(self.update_title)
        if len(self.windows) > self.tabWidget.currentIndex() + 1:
            self.tabWidget.insertTab(self.tabWidget.currentIndex() + 1, self.tab, "新建页面")
        else:
            self.tabWidget.addTab(self.tab, "新建页面")
        self.tabWidget.setCurrentWidget(self.tab)
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)
        self.cheakcoll()

    def close_Tab(self, index):
        if self.tabWidget.count() > 1:
            self.tabWidget.removeTab(index)
        else:
            self.close()  # 当只有1个tab时，关闭主窗口

    def init(self):
        if 'http' in self.edt1.text():
            self.webview = WebEngineView(self)
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            self.webview.load(QUrl(self.edt1.text()))
            self.create_tab1(self.webview)
        elif self.edt1.text() == '':
            self.homepage()
        else:
            self.webview = WebEngineView(self)
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            self.webview.load(QUrl(r'http://' + self.edt1.text()))
            self.create_tab1(self.webview)
        self.edt1.setText(self.webview.url().toString())

    def homepage(self):
        self.webview = WebEngineView(self)
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        self.webview.load(QUrl('https://www.baidu.com'))
        self.edt1.setText('https://www.baidu.com')
        self.create_tab1(self.webview)

    def update_title(self, title):
        if 'http' in title:
            if title in self.result:
                QMessageBox.warning(self, "警告", f"该网页在数据库黑名单中！")
        self.tabWidget.setTabText(self.tabWidget.currentIndex(), title)

    def renewUrl(self, url):
        # 将当前网页的链接更新到地址栏

        if len(self.windows) >= self.tabWidget.currentIndex() + 1:
            self.windows[self.tabWidget.currentIndex()] = url.toString()
        else:
            self.windows.append(url.toString())
        self.edt1.setText(url.toString())
        self.edt1.setCursorPosition(0)
        self.cheakcoll()

    def get_resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('收藏')
        self.resize(280, 230)
        self.initUI()

    def initUI(self):
        self.listitem = QListWidget(self)
        f = open("coll.txt", 'r', encoding='utf-8')
        d = []
        for row in f.readlines():
            self.item = QListWidgetItem(row)
            self.listitem.addItem(self.item)
        self.vob2 = QVBoxLayout(self)
        self.vob2.addWidget(self.listitem)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    demo = Webpage()
    demo.show()
    sys.exit(app.exec_())
