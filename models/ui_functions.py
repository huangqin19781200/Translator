from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from main import *


STATE = False


class UiFunctions(MainWindow):
    def __init__(self) -> None:
        # 初始化设置
        MainWindow.__init__(self)

    # 最大化/还原
    def maximize_restore(self) -> None:
        global STATE
        if STATE == False:
            self.showMaximized()
            STATE = True

            # 取消窗口边距
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            
            self.ui.btnMaximizeRestore.setToolTip("Restore")
            self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/restore.png"))

            # 隐藏握把
            self.ui.frameSizeGrip.hide()

        else:
            self.showNormal()
            STATE = False

            # 还原窗口大小
            self.resize(self.width(), self.height())
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)

            self.ui.btnMaximizeRestore.setToolTip("Maximize")
            self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/maximize.png"))

            # 显示握把
            self.ui.frameSizeGrip.show()

    # 定义窗口边界的握把
    def uiDefinitions(self) -> None:
        # 双击最大化/还原窗口
        def dobleClickMaximizeRestore(event: QGraphicsSceneMouseEvent):
            if event.type() == QEvent.MouseButtonDblClick:
                UiFunctions.maximize_restore(self)

        # 将顶部栏背景与方法绑定
        self.ui.frameTopBackground.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # 设置窗口拖动
        def moveWindow(event: QGraphicsSceneMouseEvent) -> None:
            global STATE
            # 当窗口最大化时先进行的操作
            if STATE:
                STATE = False

                self.ui.btnMaximizeRestore.setToolTip("Maximize")
                self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/maximize.png"))

                # 显示握把
                self.ui.frameSizeGrip.show()

            # 开始移动窗口
            if event.buttons() == Qt.LeftButton:
                self.windowHandle().startSystemMove()

        # 将程序背景与方法绑定
        self.ui.frameAppBackgroud.mouseMoveEvent = moveWindow
        
        # 设置窗口右下角的握把
        self.sizegrip = QSizeGrip(self.ui.frameSizeGrip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
