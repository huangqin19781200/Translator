import sys

from config import *
from models import *
from ui_window import *
from widgets import *


class MainWindow(QMainWindow, LoggingSettings):
    def __init__(self) -> None:
        # 初始化设置和窗口
        QMainWindow.__init__(self)
        LoggingSettings.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UiFunctions.ui_definitions(self)    # 初始化窗口设置

        self.is_maximize = False    # 默认未最大化窗口

        # 设置按钮连接
        self.ui.btnSet.clicked.connect(self.buttonClick)
        self.ui.btnAppend.clicked.connect(self.buttonClick)
        self.ui.btnClearInput.clicked.connect(self.buttonClick)
        self.ui.btnClearOutput.clicked.connect(self.buttonClick)

        self.ui.frameAppBackground.mouseMoveEvent = self.moveWindow                         # 将窗口背景与窗口移动方法绑定
        self.ui.frameTopBackground.mouseDoubleClickEvent = self.dobleClickMaximizeRestore   # 将顶部栏与双击最大化/还原方法绑定

        self.show() # 显示窗口
    
    # 程序的按钮功能
    def buttonClick(self) -> None:
        # 获取按钮名字
        btn_name = self.sender().objectName()

        # 输出翻译
        if btn_name == 'btnSet' or btn_name == 'btnAppend':
            selecte = self.ui.comboxSelect.currentText()
            source, target = AppFunctions.select_language(self, selecte)

            target_text = AppFunctions.translate(self, source, target)

            # 覆盖到输出窗口
            if btn_name == 'btnSet':
                self.ui.plainTextEditOutput.setPlainText(target_text)

            # 追加到输出窗口
            if btn_name == 'btnAppend':
                self.ui.plainTextEditOutput.appendPlainText(target_text)

        # 清空输入内容
        if btn_name == 'btnClearInput':
            self.ui.plainTextEditInput.clear()

        # 清空输出内容
        if btn_name == 'btnClearOutput':
            self.ui.plainTextEditOutput.clear()

    # 检测鼠标事件, 并根据鼠标事件调整窗口大小及拖拽握把
    def resizeEvent(self, event) -> None:
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # 检测鼠标按下事件, 获取鼠标指针在屏幕上的全局坐标，并赋值给变量
    def mousePressEvent(self, event) -> None:
        self.dragPos = event.globalPos()

    # 双击最大化/还原窗口
    def dobleClickMaximizeRestore(self, event) -> None:
        # 当双击顶部栏时
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: UiFunctions.maximize_restore(self))

    # 设置窗口拖动
    def moveWindow(self, event) -> None:
        # 当前窗口状态为最大化时，还原窗口
        if self.is_maximize:
            UiFunctions.maximize_restore(self)

        # 开始移动窗口
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))
    window = MainWindow()
    sys.exit(app.exec())
