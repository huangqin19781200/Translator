from .widgets import*


class CustomGrip(QWidget):
    def __init__(self, parent, position):
        # 初始化设置
        QWidget.__init__(self)
        self.parent = parent
        self.setParent(parent)
        self.widgets = Widgets(False)    # 初始化握把,并设置握把是否可见

        if position == Qt.TopEdge:
            self.widgets.top(self)
            self.setGeometry(0, 0, self.parent.width(), 10)
            self.setMaximumHeight(10)

            top_left = QSizeGrip(self.widgets.top_left)
            top_right = QSizeGrip(self.widgets.top_right)

            # 重新设置顶部握把与窗口大小
            def resize_top(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
                geo = self.parent.geometry()
                geo.setTop(geo.bottom() - height)
                self.parent.setGeometry(geo)
                event.accept()

            # 将顶部握把的鼠标移动事件与函数连接起来
            self.widgets.top.mouseMoveEvent = resize_top

        elif position == Qt.BottomEdge:
            self.widgets.bottom(self)
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.setMaximumHeight(10)

            self.bottom_left = QSizeGrip(self.widgets.bottom_left)
            self.bottom_right = QSizeGrip(self.widgets.bottom_right)

            # 重新设置底部握把与窗口大小
            def resize_bottom(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
                self.parent.resize(self.parent.width(), height)
                event.accept()

            # 将底部握把的鼠标移动事件与函数连接起来 
            self.widgets.bottom.mouseMoveEvent = resize_bottom

        elif position == Qt.LeftEdge:
            self.widgets.left(self)
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # 重新设置左侧握把与窗口大小
            def resize_left(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
                geo = self.parent.geometry()
                geo.setLeft(geo.right() - width)
                self.parent.setGeometry(geo)
                event.accept()

            # 将左侧握把的鼠标移动事件与函数连接起来
            self.widgets.leftgrip.mouseMoveEvent = resize_left

        elif position == Qt.RightEdge:
            self.widgets.right(self)
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # 重新设置右侧握把与窗口大小
            def resize_right(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
                self.parent.resize(width, self.parent.height())
                event.accept()

            # 将右侧握把的鼠标移动事件与函数连接起来
            self.widgets.rightgrip.mouseMoveEvent = resize_right

    # 当鼠标按钮被释放时，清除鼠标的位置信息
    def mouseReleaseEvent(self, event):
        self.mousePos = None

    # 当窗口大小改变时，更新握把的位置和大小
    def resizeEvent(self, event):
        # 设置顶部握把
        if hasattr(self.widgets, 'container_top'):
            self.widgets.container_top.setGeometry(0, 0, self.width(), 10)

        # 设置底部握把
        elif hasattr(self.widgets, 'container_bottom'):
            self.widgets.container_bottom.setGeometry(0, 0, self.width(), 10)

        # 设置左侧握把
        elif hasattr(self.widgets, 'leftgrip'):
            self.widgets.leftgrip.setGeometry(0, 0, 10, self.height() - 20)

        # 设置右侧握把
        elif hasattr(self.widgets, 'rightgrip'):
            self.widgets.rightgrip.setGeometry(0, 0, 10, self.height() - 20)