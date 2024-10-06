import sys
import os

from config import *
from models import *
from ui_window import *

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class MainWindow(QMainWindow, LoggingSettings):
    def __init__(self) -> None:
        # 初始化设置
        QMainWindow.__init__(self)
        LoggingSettings.__init__(self)
        logging.info(f"Program starts.")

        # 初始化窗口
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 修复高分辨率的问题
        os.environ["QT_FONT_DPI"] = "96"  

        # 设置按钮连接
        self.ui.btnSet.clicked.connect(self.buttonClick)
        self.ui.btnAppend.clicked.connect(self.buttonClick)
        self.ui.btnClearInput.clicked.connect(self.buttonClick)
        self.ui.btnClearOutput.clicked.connect(self.buttonClick)

        self.ui.btnMinimize.clicked.connect(self.buttonClick)
        self.ui.btnMaximizeRestore.clicked.connect(self.buttonClick)
        self.ui.btnClose.clicked.connect(self.buttonClick)

        self.setWindowFlags(Qt.FramelessWindowHint)         # 设置无边框
        self.setAttribute(Qt.WA_TranslucentBackground)      # 将界面属性设置为半透明

        # 设定阴影
        self.shadow = QGraphicsDropShadowEffect()		
        self.shadow.setBlurRadius(4)    		                    # 半径为 4
        self.shadow.setColor(QColor(2, 10, 25))                     # 颜色为 2, 10, 25
        self.shadow.setOffset(0, 0)                                 # 偏移为 0,0
        self.ui.frameAppBackgroud.setGraphicsEffect(self.shadow)	# 为frameAppBackgroud设定阴影效果

        # 使控制窗口的各功能生效
        UiFunctions.uiDefinitions(self)

        # 显示窗口
        self.show()
    
    # 程序的按钮功能
    def buttonClick(self) -> None:
        # 获取按钮名字
        btn_name = self.sender().objectName()

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

        # 最小化隐藏窗口
        if btn_name == 'btnMinimize':
            self.showMinimized()
            UiFunctions.maximize_restore(self)

        # 最大化/还原窗口
        if btn_name == 'btnMaximizeRestore':
            UiFunctions.maximize_restore(self)

        # 关闭窗口
        if btn_name == 'btnClose':
            logging.info(f"Program closes.\n")
            self.close()

# 程序退出执行的命令
def app_exit() -> None:
    app.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))
    window = MainWindow()
    sys.exit(app_exit())