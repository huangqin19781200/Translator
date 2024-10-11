from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QSizeGrip, QFrame, QHBoxLayout


class Widgets(object):
    def __init__(self, enable_view) -> None:
        # 接收是否显示的参数
        self.enable_view = enable_view

    # 顶部拖拽握把
    def top(self, Form) -> None:
        if not Form.objectName():
            Form.setObjectName(u"Form")

        # 创建顶部拖拽握把容器
        self.container_top = QFrame(Form)
        self.container_top.setObjectName(u"container_top")
        self.container_top.setGeometry(QRect(0, 0, 500, 10))
        self.container_top.setMinimumSize(QSize(0, 10))
        self.container_top.setMaximumSize(QSize(16777215, 10))
        self.container_top.setFrameShape(QFrame.NoFrame)
        self.container_top.setFrameShadow(QFrame.Raised)

        # 创建顶部布局
        self.top_layout = QHBoxLayout(self.container_top)
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, 0, 0, 0)

        # 创建顶部左斜角握把
        self.top_left = QFrame(self.container_top)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(10, 10))
        self.top_left.setMaximumSize(QSize(10, 10))
        self.top_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.top_left.setStyleSheet("background: transparent")
        self.top_left.setFrameShape(QFrame.NoFrame)
        self.top_left.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_left)

        # 创建顶部中间握把
        self.top = QFrame(self.container_top)
        self.top.setObjectName(u"top")
        self.top.setCursor(QCursor(Qt.SizeVerCursor))
        self.top.setStyleSheet("background: transparent")
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top)

        # 创建顶部右斜角握把
        self.top_right = QFrame(self.container_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(10, 10))
        self.top_right.setMaximumSize(QSize(10, 10))
        self.top_right.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.top_right.setStyleSheet("background: transparent")
        self.top_right.setFrameShape(QFrame.NoFrame)
        self.top_right.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_right)

        # 是否显示顶部拖拽握把
        if self.enable_view:
            self.top_left.setStyleSheet(u"background-color: rgb(40, 140, 43);")
            self.top.setStyleSheet(u"background-color: rgb(85, 255, 255);")
            self.top_right.setStyleSheet(u"background-color: rgb(40, 140, 43);")

    # 底部拖拽握把
    def bottom(self, Form) -> None:
        if not Form.objectName():
            Form.setObjectName(u"Form")

        # 创建底部拖拽握把容器
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, 10))
        self.container_bottom.setMinimumSize(QSize(0, 10))
        self.container_bottom.setMaximumSize(QSize(16777215, 10))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)

        # 创建底部布局
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)

        # 创建底部左斜角握把
        self.bottom_left = QFrame(self.container_bottom)
        self.bottom_left.setObjectName(u"bottom_left")
        self.bottom_left.setMinimumSize(QSize(10, 10))
        self.bottom_left.setMaximumSize(QSize(10, 10))
        self.bottom_left.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.bottom_left.setStyleSheet("background: transparent")
        self.bottom_left.setFrameShape(QFrame.NoFrame)
        self.bottom_left.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_left)


        # 创建底部中间握把
        self.bottom = QFrame(self.container_bottom)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom.setStyleSheet("background: transparent")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom)

        # 创建底部右斜角握把
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(10, 10))
        self.bottom_right.setMaximumSize(QSize(10, 10))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet("background: transparent")
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

        # 是否显示底部拖拽握把
        if self.enable_view:
            self.bottom_left.setStyleSheet(u"background-color: rgb(85, 255, 200);")
            self.bottom.setStyleSheet(u"background-color: rgb(85, 170, 0);")
            self.bottom_right.setStyleSheet(u"background-color: rgb(85, 255, 200);")
            
    # 左侧拖拽握把
    def left(self, Form) -> None:
        if not Form.objectName():
            Form.setObjectName(u"Form")

        # 创建左侧拖拽握把
        self.leftgrip = QFrame(Form)
        self.leftgrip.setObjectName(u"left")
        self.leftgrip.setGeometry(QRect(0, 10, 10, 480))
        self.leftgrip.setMinimumSize(QSize(10, 0))
        self.leftgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.leftgrip.setStyleSheet("background: transparent")
        self.leftgrip.setFrameShape(QFrame.NoFrame)
        self.leftgrip.setFrameShadow(QFrame.Raised)

        # 是否显示左侧拖拽握把
        if self.enable_view:
            self.leftgrip.setStyleSheet(u"background-color: rgb(255, 121, 198);")
            
    # 右侧拖拽握把
    def right(self, Form) -> None:
        if not Form.objectName():
            Form.setObjectName(u"Form")

        # 创建右侧拖拽握把
        self.rightgrip = QFrame(Form)
        self.rightgrip.setObjectName(u"right")
        self.rightgrip.setGeometry(QRect(0, 0, 10, 500))
        self.rightgrip.setMinimumSize(QSize(10, 0))
        self.rightgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.rightgrip.setStyleSheet("background: transparent")
        self.rightgrip.setFrameShape(QFrame.NoFrame)
        self.rightgrip.setFrameShadow(QFrame.Raised)

        # 是否显示右侧拖拽握把
        if self.enable_view:
            self.rightgrip.setStyleSheet(u"background-color: rgb(255, 0, 127);")