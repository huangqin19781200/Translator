from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os

from main import *


RESIZE_STATE = False


class UiFunctions(MainWindow):
    def __init__(self) -> None:
        MainWindow.__init__(self)

    # 设置界面中握把的启用
    def enable_grips(self, isture: bool) -> None:
        if isture:
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
            self.ui.frameSizeGrip.show()
        else:
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
            self.ui.frameSizeGrip.hide()

    # 当检测窗口大小改变事件时, 调整握把大小
    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # 放大化/还原各组件
    def set_widgets(self, isRestore: bool) -> None:
        if isRestore:
            # 还原窗口大小
            self.resize(self.width(), self.height())
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)

            # 还原圆角 
            self.ui.frameTopBackground.setStyleSheet(u"#frameTopBackground {	\n"
                "	background-color: rgb(33, 37, 43);\n"
                "	border-top-left-radius: 10px;\n"
                "	border-top-right-radius: 10px;\n"
                "}\n"
                "#frameTopBackground .QPushButton {\n"
                "	background-color: rgba(255, 255, 255, 0);\n"
                "	border: none;\n"
                "}\n"
                "#frameTopBackground .QPushButton:hover {\n"
                "	background-color: rgb(44, 49, 57);\n"
                "	border-style: solid;\n"
                "}\n"
                "#frameTopBackground .QPushButton:pressed {\n"
                "	background-color: rgb(23, 26, 30);\n"
                "	border-style: solid;\n"
                "}")
            self.ui.frameBottomBackground.setStyleSheet(u"border-top-left-radius: 0px;\n"
                "border-top-right-radius: 0px;")

            self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/maximize.png"))    # 切换为最大化图标
            UiFunctions.enable_grips(self, True)                                        # 显示握把

        else:
            # 取消圆角
            self.ui.frameTopBackground.setStyleSheet(u"border-top-left-radius: 0px;\n"
                "border-top-right-radius: 0px;")
            self.ui.frameBottomBackground.setStyleSheet(u"border-bottom-left-radius: 0px;\n"
	            "border-bottom-right-radius: 0px;")

            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)                       # 取消窗口边距
            self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/restore.png")) # 切换为还原图标
            UiFunctions.enable_grips(self, False)                                   # 隐藏握把

    # 最大化/还原窗口
    def maximize_restore(self) -> None:
        global RESIZE_STATE
        if RESIZE_STATE:
            self.showNormal()   # 还原窗口
            RESIZE_STATE = False
            UiFunctions.set_widgets(self, True)
        else:
            self.showMaximized()    # 最大化窗口
            RESIZE_STATE = True
            UiFunctions.set_widgets(self, False)  # 取消圆角

    def ui_definitions(self) -> None:
        # 设置窗口拖动
        def moveWindow(event) -> None:
            # 当前窗口状态为最大化时，还原窗口
            if RESIZE_STATE:
                UiFunctions.maximize_restore(self)

            # 开始移动窗口
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        # 将顶部无组件区域的鼠标点击事件与函数连接
        self.ui.frameTopLogo.mouseMoveEvent = moveWindow  
        self.ui.widgetTop.mouseMoveEvent = moveWindow

        def closeEvent(event) -> None:
            # 启用系统托盘
            def openTray() -> None:
                event.ignore()
                QMainWindow.hide(self)
                self.trayicon.show()    # 显示托盘

            # 创建提问框
            self.question_box = QMessageBox()
            self.question_box.setWindowTitle("退出")
            self.question_box.setText("是否要关闭程序？")
            self.question_box.setIcon(QMessageBox.Question)

            icon = QIcon()
            icon.addFile(u":/images/icon/winlogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.question_box.setWindowIcon(icon)

            # 添加按钮
            btnYes = QPushButton("是")
            self.question_box.addButton(btnYes, QMessageBox.ActionRole)
            btnYes.clicked.connect(lambda: event.accept())

            btnNo = QPushButton("否")
            self.question_box.addButton(btnNo, QMessageBox.ActionRole)
            btnNo.clicked.connect(lambda: event.ignore())

            btnTray = QPushButton("后台运行")
            self.question_box.addButton(btnTray, QMessageBox.ActionRole)
            btnTray.clicked.connect(lambda: openTray())

            self.question_box.setFont(QFont("\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular", 12)) # 设置字体样式

            self.question_box.exec()  # 等待操作
        self.closeEvent = closeEvent

        # 设置窗口阴影
        self.shadow = QGraphicsDropShadowEffect()		
        self.shadow.setBlurRadius(8)    		                    # 半径为 8
        self.shadow.setOffset(0, 0)                                 # 偏移为 0,0
        self.shadow.setColor(QColor(2, 10, 25))                     # 颜色为 2, 10, 25
        self.ui.frameAppBackground.setGraphicsEffect(self.shadow)	# 为程序背景启用阴影效果

        self.ui.btnMinimize.clicked.connect(lambda: self.showMinimized())                       # 最小化窗口
        self.ui.btnMaximizeRestore.clicked.connect(lambda: UiFunctions.maximize_restore(self))  # 最大化/还原窗口
        self.ui.btnClose.clicked.connect(lambda: self.close())                                  # 关闭窗口

        self.setWindowFlags(Qt.FramelessWindowHint)     # 设置窗口没有原始边框和标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口的背景为半透明的

        os.environ["QT_FONT_DPI"] = "96"    # 修复高分辨率的问题



    def grip_definitions(self) -> None:
        # 设置窗口右下角的握把
        self.sizegrip = QSizeGrip(self.ui.frameSizeGrip)
        self.sizegrip.setStyleSheet(u"width: 20px; height: 20px;\n"
            "margin 0px; padding: 0px;")

        # 定义窗口握把
        self.left_grip = CustomGrip(self, Qt.LeftEdge)
        self.right_grip = CustomGrip(self, Qt.RightEdge)
        self.top_grip = CustomGrip(self, Qt.TopEdge)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge)



    def tray_definitions(self) -> None:
        # 为系统托盘菜单添加功能的函数
        def addTrayMenuAction(text, method):
            function = QAction(text, self)      # 功能的文字
            function.triggered.connect(method)  # 连接的方法/函数
            self.traymenu.addAction(function)
            self.trayaction.append(function)

        # 左键系统托盘图标的打开程序界面
        def leftClickTrayIcon(reason):
            if reason == QSystemTrayIcon.ActivationReason.Trigger:
                if self.isHidden():
                    openApp()

        # 打开程序界面
        def openApp():
            self.trayicon.hide()
            QMainWindow.show(self)

        # 配置系统托盘
        self.trayicon = QSystemTrayIcon(self)
        self.trayicon.setIcon(QIcon(u":/images/icon/winlogo.png"))

        # 创建系统托盘的右键菜单
        self.traymenu = QMenu()
        self.trayaction = []
        self.traymenu.setFont(QFont("\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular", 12))   # 设置字体
        self.trayicon.setContextMenu(self.traymenu)                                                     # 为托盘设定右键菜单

        # 为系统托盘添加功能
        addTrayMenuAction('显示界面', lambda: openApp())
        addTrayMenuAction('退出程序', lambda: sys.exit(QApplication.exit()))

        self.trayicon.activated.connect(leftClickTrayIcon)  # 为托盘图标添加左键点击事件
