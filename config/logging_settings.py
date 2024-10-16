import logging

class LoggingSettings():
    def __init__(self) -> None:
        # 日志设置
        logging.basicConfig(
            datefmt="%Y/%m/%d-%H:%M:%S",
            format="|%(asctime)s| %(levelname)s %(message)s",
            level=logging.INFO,
            handlers=[
                logging.FileHandler('logs.log')
            ]
        )