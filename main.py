import sys
import os

from ui import *
from config import *
from models import *


class MainWindow(QMainWindow, LoggingSettings):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        LoggingSettings.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UiFunctions.ui_definitions(self)
        UiFunctions.grip_definitions(self)
        UiFunctions.tray_definitions(self)

        # 设置按钮连接
        self.ui.btnSet.clicked.connect(self.buttonClick)
        self.ui.btnAppend.clicked.connect(self.buttonClick)
        self.ui.btnClearInput.clicked.connect(self.buttonClick)
        self.ui.btnClearOutput.clicked.connect(self.buttonClick)

        self.show() # 显示窗口

    def buttonClick(self) -> None:
        btn_name = self.sender().objectName()   # 获取按钮名字

        # 覆盖到输出窗口
        if btn_name == 'btnSet':
            select = self.ui.comboxSelect.currentText()
            source_text = self.ui.plainTextEditInput.toPlainText()
            target_text =  AppFunctions.translate(self, source_text, select)
            self.ui.plainTextEditOutput.setPlainText(target_text)

        # 追加到输出窗口
        if btn_name == 'btnAppend':
            select = self.ui.comboxSelect.currentText()
            source_text = self.ui.plainTextEditInput.toPlainText()
            target_text = AppFunctions.translate(self, source_text, select)
            self.ui.plainTextEditOutput.appendPlainText(target_text)

        # 清空输入内容
        if btn_name == 'btnClearInput':
            self.ui.plainTextEditInput.clear()

        # 清空输出内容
        if btn_name == 'btnClearOutput':
            self.ui.plainTextEditOutput.clear()

    # 检测鼠标按下事件, 获取鼠标指针的坐标
    def mousePressEvent(self, event) -> None:
        self.dragPos = event.globalPosition().toPoint()

    def resizeEvent(self, event) -> None:
        UiFunctions.resize_grips(self)


def lock_message():
        # 创建提示框
        information_box = QMessageBox()
        information_box.setWindowTitle("提示")
        information_box.setText("程序已经启动！")
        information_box.setIcon(QMessageBox.Information)

        icon = QIcon()
        icon.addFile(u":/images/icon/winlogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        information_box.setWindowIcon(icon)

        # 添加按钮
        btnYes = QPushButton("是")
        information_box.addButton(btnYes, QMessageBox.ActionRole)

        information_box.setFont(QFont("\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular", 12)) # 设置字体样式

        information_box.exec()  # 等待操作

# 运行程序
def runWindow() -> None:
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))    # 设置程序图标

    # 创建文件锁，防止多开
    temp_path = os.environ.get('TEMP')
    lockFile = QLockFile(os.path.join(temp_path, "Translator.lock")) if temp_path else QLockFile("Translator.lock")

    if lockFile.tryLock(250):
        window = MainWindow()
        sys.exit(app.exec())
    else:
        lock_message()
        sys.exit(-1)

if __name__ == "__main__":
    runWindow()
