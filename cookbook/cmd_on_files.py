import glob
import subprocess

files = glob.glob('*.py')

for f in files:
    x = subprocess.run("echo {}".format(f))
    print(x.returncode)
