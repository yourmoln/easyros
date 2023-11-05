import os,sys
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
from install import *
from github import *
from rostool import *
run_path = getpath()
def run():
    print("""
  ______                _____   ____   _____ 
 |  ____|              |  __ \ / __ \ / ____|
 | |__   __ _ ___ _   _| |__) | |  | | (___  
 |  __| / _` / __| | | |  _  /| |  | |\___ \ 
 | |___| (_| \__ \ |_| | | \ \| |__| |____) |
 |______\__,_|___/\__, |_|  \_\\____/|_____/ 
                   __/ |                     
                  |___/                      
==============================================""")
    mode = input("[1]自动安装ros\n[2]github镜像\n[3]一键创造ros工作空间\n")
    if mode in ['1']:
        if input('你确定想要自动安装ros吗  (y/n)') == 'y':
            rosInstall()
            print("安装完成")
    elif mode in ['2']:
        link = input("请输入github链接: ")
        print(mGithub(link))
    elif mode in ['3']:
        name = input("请输入工作空间的名称: ")
        creat(name,run_path)
        print("创造完成")
if __name__ == "__main__":
    run()