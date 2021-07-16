# Linux Cheatsheet

# SSH 
Double ssh (port 6000 now takes you to target_server_ip):
```ssh -L 6000:<target_server_ip>:22 <proxy_server_user>@<proxy_server_ip>```
<br>
Can now connect to target_server_ip with below line (can also now use below line to connect Pycharm to server):
```ssh -p 6000 <target_server_user>@localhost```

## Basic
remove a folder (recursivley delete contents) : 
```rm -r filename	```

## Session 
Run multiple programs, prevent disconnect stopping program
```
screen -S session_name # start screen
screen -r session_name # connect
ctrl + A, :sessionname mySessionName   # rename screen
screen -r -d session_name # retach to a screen that says "attached" when screen -ls, but isn't actually attached
  ```
  
## Jupyter Server
```
# https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/
jupyter notebook --no-browser --port=XXXX # activate
ssh -N -f -L localhost:YYYY:localhost:XXXX remoteuser@remotehost # port forward
localhost:YYYY # paste into browser to connect
```

## Python
Run python file
   - python filename.py
   
Run 2 python files in **sequence** (requires first script to run successfully)
   - python file1.py && python file2.py
   
Run 2 python files in **sequence** (first script need not run successfully)
   - python file1.py || python file2.py
   
Run 2 python files in **parallel**
   - python file1.py & python file2.py
   
## Running things from pycharm in terminal
```
# to prevent import errors
import os
import sys
if not os.getcwd() in sys.path:
    sys.path.append(os.getcwd())
now we can go call from the parent dir: python subdir/subsubdir.python_file.py
```
## Double port forward for jupyter no browser
```
ssh -t -l usr3 -L:7119:localhost:7119 -L:6042:localhost:6042 gate.eng.cam.ac.uk ssh -L:7119:localhost:7119 -L:6042:localhost:6006 computer1
 jupyter notebook --no-browser --port=7119
 ```
 
