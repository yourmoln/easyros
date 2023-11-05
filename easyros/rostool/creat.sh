#!/bin/bash
mkdir -p $2/$1/src
cd $2/$1/src/ && catkin_init_workspace
cd $2/$1 && catkin_make
echo "source $2/$1/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
