import zipfile
import os

# with zipfile.ZipFile('another.zip', 'w') as f:
#     f.write('./20200217-20200315计算机网络系统作业成绩分布-第一章作业.xls')

# with zipfile.ZipFile('another.zip','r') as f:
#     f.extractall('unpack_another')


# import shutil
#
# # shutil.make_archive(base_name='another', format='zip', base_dir='20200217-20200315计算机网络系统作业成绩分布-第一章作业.xls')
# shutil.unpack_archive('another.zip', 'jack', 'zip')

# print(os.getcwd())
# print(os.path.abspath(os.path.realpath(__file__)))

for dirname, file, dir in os.walk(os.path.abspath('pep')):
    print('dirpath:{}'.format(dirname))
    print('dirsname:{}'.format(file))
    print('filename:{}'.format(dir))