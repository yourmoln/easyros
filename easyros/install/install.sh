#!/bin/bash
wget http://fishros.com/install -O fishros
chmod 777 ./fishros
./fishros << EOF
1
1
2
1
1
EOF
wget http://fishros.com/install -O fishros
chmod 777 ./fishros
./fishros << EOF
3
EOF
rosdepc update