import subprocess
import time

run_type = 'xray'


class ColorStr:
    RED = '\033[31m'  # 红色
    GREEN = '\033[32m'  # 绿色
    YELLOW = '\033[33m'  # 黄色
    BLUE = '\033[34m'  # 蓝色
    FUCHSIA = '\033[35m'  # 紫红色
    CYAN = '\033[36m'  # 青蓝色
    WHITE = '\033[37m'  # 白色
    #: no color
    RESET = '\033[0m'  # 终端默认颜色

    @classmethod
    def red(cls, s):
        return cls.RED + s + cls.RESET

    @classmethod
    def green(cls, s):
        return cls.GREEN + s + cls.RESET

    @classmethod
    def yellow(cls, s):
        return cls.YELLOW + s + cls.RESET

    @classmethod
    def blue(cls, s):
        return cls.BLUE + s + cls.RESET

    @classmethod
    def cyan(cls, s):
        return cls.CYAN + s + cls.RESET

    @classmethod
    def fuchsia(cls, s):
        return cls.FUCHSIA + s + cls.RESET

    @classmethod
    def white(cls, s):
        return cls.WHITE + s + cls.RESET


def xray_run(command, keyword):
    try:
        subprocess.check_output('systemctl daemon-reload', shell=True)
        subprocess.check_output(command, shell=True)
        print("{}ing {}...".format(keyword, run_type))
        time.sleep(2)
        if subprocess.check_output("systemctl is-active {}|grep active".format(run_type),
                                   shell=True) or keyword == "stop":
            print(ColorStr.green("{} {} success !".format(run_type, keyword)))
        else:
            raise subprocess.CalledProcessError
    except Exception as error:
        print(ColorStr.red("{} {} fail ! Exception: {}".format(run_type, keyword, error)))


def xray_restart():
    xray_run("systemctl restart {}".format(run_type), "restart")


def xray_start():
    xray_run("systemctl start {}".format(run_type), "start")


def xray_stop():
    xray_run("systemctl stop {}".format(run_type), "stop")


if __name__ == '__main__':
    pass
