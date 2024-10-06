# 项目名称
翻译器

# 项目简介
一款开源的简易翻译工具。主要使用 PySide6 实现图形化界面，使用 tencentcloud-sdk-python 实现翻译功能，使用 logging 模块实现日志记录功能。  

# 功能说明
1. 按钮功能

- 覆盖翻译：点击该按钮会将翻译后的文本覆盖到输出窗口。

- 追加翻译：点击该按钮会将翻译后的文本追加到输出窗口。

- 清空输入：点击该按钮会清空输入窗口的内容。

- 清空输出：点击该按钮会清空输出窗口的内容。

- 语言选择：通过下拉框选择源语言和目标语言。

2. 支持的语言

- 英语 -> 中文
- 日语 -> 中文
- 俄语 -> 中文
- 中文 -> 英语
- 中文 -> 日语
- 中文 -> 俄语

# 环境配置
Python 版本：3.11.9  
依赖库列表：
- sys
- os
- pyside6
- tencentcloud-sdk-python
- json
- logging

# 运行方法
确保已经安装了 Python 环境和依赖库。  
然后运行 python main.py 启动程序。

# 注意事项
确保 logo.ico 文件存在于项目目录下。  
翻译功能依赖于 AppFunctions.select_language 和 AppFunctions.translate 函数，请确保这两个函数已经实现并且正确导入。
翻译功能使用了腾讯云的翻译服务，需要在腾讯云控制台创建一个翻译服务的应用，并获取到对应的 API 密钥和 SecretKey，再将其配置到settings.Setting中。

# 贡献者
- 作者：[HGG](https://github.com/huangqin19781200)

# 贡献指南
如果你想为这个项目做出贡献，请遵循以下指南：

1. Fork 本仓库，创建一个新的分支进行你的修改，提交你的修改并创建一个 Pull Request。

2. 许可证 本项目采用 MIT 许可证。

# Project Name
Translator

# Project Introduction
An open source simple translation tool. It mainly uses PySide6 to implement the graphical interface, tencentcloud-sdk-python to implement the translation function, and the logging module to implement the log recording function.

# Function Description
1. Button function

- Overwrite translation: Click this button to overwrite the translated text to the output window.

- Append translation: Click this button to append the translated text to the output window.

- Clear input: Click this button to clear the content of the input window.

- Clear output: Click this button to clear the content of the output window.

- Language selection: Select the source language and target language through the drop-down box.

2. Supported languages

- English -> Chinese
- Japanese -> Chinese
- Russian -> Chinese
- Chinese -> English
- Chinese -> Japanese
- Chinese -> Russian

# Environment Configuration
Python version: 3.11.9
Dependency library list:
- sys
- os
- pyside6
- tencentcloud-sdk-python
- json
- logging

# Running Method
Ensure that the Python environment and dependency libraries are installed.
Then run `python main.py` to start the program.

# Notes
Ensure that the `logo.ico` file exists in the project directory.
The translation function relies on the `AppFunctions.select_language` and `AppFunctions.translate` functions. Please ensure that these two functions have been implemented and correctly imported.
The translation function uses Tencent Cloud's translation service. You need to create a translation service application in the Tencent Cloud console and obtain the corresponding API key and SecretKey, and then configure them in `settings.Settings`.

# Contributors
- Author: [HGG](https://github.com/huangqin19781200)

# Contribution Guidelines
If you want to contribute to this project, please follow these guidelines:

1. Fork this repository and create a new branch for your changes. Submit your changes and create a Pull Request.

2. License
This project is licensed under the MIT License.
