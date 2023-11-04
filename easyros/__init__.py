import os,sys
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
from install import rosInstall
def run():
    rosInstall()
    print("自动安装已结束")
if __name__ == "__main__":
    run()