from setuptools import setup, find_packages

setup(
    name='greet',
    version='1.0.0',
    packages=find_packages(include=['greet_pkg', 'greet_pkg.*']),
    url='',
    license='uestc',
    author='jack',
    author_email='2444093230@qq.com',
    description='test package',
    py_modules=['greet2'],
    install_requires=['pyjokes']
)
