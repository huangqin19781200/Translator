from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os

from main import *


class UiFunctions(MainWindow):
    def __init__(self) -> None:
        # 初始化设置
        MainWindow.__init__(self)

    # 最大化/还原窗口
    def maximize_restore(self) -> None:
        if self.is_maximize:
            self.showNormal()   # 还原窗口
            self.is_maximize = False

            # 还原窗口大小
            self.resize(self.width(), self.height())
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
        
            # 还原圆角
            self.ui.frameTopBackground.setStyleSheet(
                "border-top-left-radius: 10px;\
                border-top-right-radius: 10px;\
                border-bottom-left-radius: 0px;\
                border-bottom-right-radius: 0px;"
                )

            self.ui.frameAppBackground.setStyleSheet(
                "border-top-left-radius: 10px;\
                border-top-right-radius: 10px;\
                border-bottom-left-radius: 10px;\
                border-bottom-right-radius: 10px;"
                )
            
            self.ui.frameBottomBackground.setStyleSheet(
                "border-top-left-radius: 0px;\
                border-top-right-radius: 0px;\
                border-bottom-left-radius: 10px;\
                border-bottom-right-radius: 10px;"
                )
            
            # 切换为最大化图标
            self.ui.btnMaximizeRestore.setToolTip("Maximize")
            self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/maximize.png"))

            # 显示握把
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
            self.ui.frameSizeGrip.show()

        else:
            self.showMaximized()    # 最大化窗口
            self.is_maximize = True

            # 取消窗口边距
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)

            # 取消圆角
            self.ui.frameTopBackground.setStyleSheet(
                "border-top-left-radius: 0px;\
                border-top-right-radius: 0px;\
                border-bottom-left-radius: 0px;\
                border-bottom-right-radius: 0px;"
                )

            self.ui.frameAppBackground.setStyleSheet(
                "border-top-left-radius: 0px;\
                border-top-right-radius: 0px;\
                border-bottom-left-radius: 0px;\
                border-bottom-right-radius: 0px;"
                )
            
            self.ui.frameBottomBackground.setStyleSheet(
                "border-top-left-radius: 0px;\
                border-top-right-radius: 0px;\
                border-bottom-left-radius: 0px;\
                border-bottom-right-radius: 0px;"
                )
            
            # 切换为还原图标
            self.ui.btnMaximizeRestore.setToolTip("Restore")
            self.ui.btnMaximizeRestore.setIcon(QIcon(u":/images/icon/restore.png"))

            # 隐藏握把
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
            self.ui.frameSizeGrip.hide()
            
    # 窗口设置
    def ui_definitions(self) -> None:
        # 设置窗口阴影
        self.shadow = QGraphicsDropShadowEffect()		
        self.shadow.setBlurRadius(8)    		                    # 半径为 8
        self.shadow.setOffset(0, 0)                                 # 偏移为 0,0
        self.shadow.setColor(QColor(2, 10, 25))                     # 颜色为 2, 10, 25
        self.ui.frameAppBackground.setGraphicsEffect(self.shadow)	# 为程序背景启用阴影效果

        # 设置窗口右下角的握把
        self.sizegrip = QSizeGrip(self.ui.frameSizeGrip)
        self.sizegrip.setStyleSheet(
            "width: 20px;\
            height: 20px;\
            margin 0px;\
            padding: 0px;"
            )

        self.ui.btnMinimize.clicked.connect(lambda: self.showMinimized())                       # 最小化隐藏窗口
        self.ui.btnMaximizeRestore.clicked.connect(lambda: UiFunctions.maximize_restore(self))  # 最大化/还原窗口
        self.ui.btnClose.clicked.connect(lambda: self.close())                                  # 关闭窗口

        self.setWindowFlags(Qt.FramelessWindowHint)     # 设置窗口没有原始边框和标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口的背景为半透明的

        # 修复高分辨率的问题
        os.environ["QT_FONT_DPI"] = "96"  

        # 定义窗口拖拽握把
        self.left_grip = CustomGrip(self, Qt.LeftEdge)
        self.right_grip = CustomGrip(self, Qt.RightEdge)
        self.top_grip = CustomGrip(self, Qt.TopEdge)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge)