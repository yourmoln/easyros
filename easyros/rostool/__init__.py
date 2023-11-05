from .evar import *
import os
script_path = os.path.split(os.path.realpath(__file__))[0]
def creat(name,path):
    os.system(f"chmod 777 {script_path}/creat.sh")
    os.system(f"{script_path}/creat.sh {name} {path}")
