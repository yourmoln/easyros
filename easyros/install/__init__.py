import os
script_path = os.path.split(os.path.realpath(__file__))[0]
def rosInstall():
    os.system(f"chmod 777 {script_path}/install.sh")
    os.system(f"{script_path}/install.sh")

if __name__ == '__main__':
    rosInstall()