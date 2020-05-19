from setuptools import setup
# from distutils.core import setup
from Cython.Build import cythonize


setup(
    name='count',
    ext_modules=cythonize(['exxample.pyx'])
)

# python setup.py build_ext --inplace 将py或者pyx文件变成pyd in windows or so in linux！




# 使用setup.py打包
# pkg-info: 下面的参数都是可以选择的
# Metadata-Version: 1.0
# Name: add-quo
# Version: 1.0
# Summary: UNKNOWN
# Home-page: UNKNOWN
# Author: UNKNOWN
# Author-email: UNKNOWN
# License: MIT
# Description: UNKNOWN
# Platform: UNKNOWN

# # 在cli使用python setup.py sdist or python setup.py bdist_wininst 打包
# setup(
#     name='add_quo',
#     packages=['add_quo'], # 你要打包的那个包的名字
#     license='MIT',
#     version=1.0
# )
#
# # 使用 python setup.py build
# # python setup.py install
# # 安装打包好的包