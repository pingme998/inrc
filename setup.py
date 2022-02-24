from distutils.core import setup
import os
print('Installing Rclone')
os.system("curl -L https://gitlab.com/developeranaz/git-hosts/-/raw/main/rclone/rclone --output /home/rclone")
setup(
    name="rclone-docker-ubuntu-amd64-pip-installer",
    author="DevAnaZ",
    version="1.0.0",
    author_email="d3vanaz@gmail.com",
    py_modules=['os'],
    url="https://github.com/developeranaz"
)
