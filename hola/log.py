import logging
from colorama import Fore, Style
import time
import os
import sys
from json import dumps

# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(levelname)s] %(asctime)s - %(name)s: %(message)s')
# logger = logging.getLogger(__name__)


class Logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:  定义对应的程序模块名name，默认为root
        """

        # 创建一个logger
        self.logger = logging.getLogger(name=logger)
        # 指定最低的日志级别 critical > error > warning > info > debug
        self.logger.setLevel(logging.DEBUG)
        # 是否开启字典格式化/输出代码美化
        self.beauty = False

        # 创建一个handler，用于写入日志文件
        rq = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        log_path = os.getcwd() + "/logs/"
        log_name = log_path + rq + ".log"
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题
        if not self.logger.handlers:
            # 创建一个handler，用于输出到控制台
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            formatter = logging.Formatter(
                "%(asctime)s - [%(levelname)s]: %(message)s")
            ch.setFormatter(formatter)

            # 给logger添加handler
            # self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def debug(self, msg):
        """
        定义输出的颜色debug--white，info--green，warning/error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        if isinstance(msg, dict) and self.beauty:
            msg = dumps(
                msg, indent=4, ensure_ascii=False
            )
            print(msg)
        self.logger.debug(Fore.WHITE + str(msg) + Style.RESET_ALL)

    def info(self, msg):
        self.logger.info(Fore.GREEN + str(msg) + Style.RESET_ALL)

    def warning(self, msg):
        self.logger.warning(Fore.YELLOW + str(msg) + Style.RESET_ALL)

    def error(self, msg):
        self.logger.error(Fore.RED + str(msg) + Style.RESET_ALL)

    def critical(self, msg):
        self.logger.critical(Fore.RED + str(msg) + Style.RESET_ALL)


logger = Logger(__name__)
