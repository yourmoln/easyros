import os,sys
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
from install import rosInstall
from github import mGithub
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
    mode = input("[1]auto install ros\n[2]mirror github\n")
    if mode in ['1']:
        if input('Do you want to auto install ros?  (y/n)') == 'y':
            rosInstall()
            print("over")
    elif mode in ['2']:
        link = input("Please input github link: ")
        print(mGithub(link))
if __name__ == "__main__":
    run()