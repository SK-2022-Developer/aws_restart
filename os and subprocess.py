# Python 3.10.4
# Coding: utf-8

# This is practice file for utilizing os and subprocess libraries
"""
# using os module
import os

os.system("ls")
os.system("pwd")
"""

# using subprocess module
import subprocess

#subprocess.run(["ls"])
#subprocess.run(["pwd"])
#subprocess.run(["ls","-l"])
#subprocess.run(["ls","-l","index.html"])
"""
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
"""
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])