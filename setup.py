from distutils.core import setup
import os
print('hello py')
os.system("curl -L https://gitlab.com/developeranaz/git-hosts/-/raw/main/rclone/rclone --output /storage/emulated/0/Download/celeron-dude-indexer-main/pio/hellopy/rclone")
setup(
    name="rclone-docker-ubuntu-amd64",
    author="xxx",
    version="1.0.0",
    author_email="xxx@gmail.com",
    py_modules=['hellopy.hello'],
    url="http://www.xxx.com"
)
