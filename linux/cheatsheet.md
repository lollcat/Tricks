# Linux Cheatsheet

## Basic
remove a folder (recursivley delete contents) : rm -r filename	

## Session 
Run multiple programs, prevent disconnect stopping program
   - screen -S session_name
   - screen -r session_name
   - ctrl + A, :sessionname mySessionName
   
## Python
Run python file
   python filename.py
Run 2 python files in **sequence** (requires first script to run successfully)
   python file1.py && python file2.py
Run 2 python files in **sequence** (first script need not run successfully)
   python file1.py || python file2.py
Run 2 python files in **parallel**
   python file1.py & python file2.py
   
