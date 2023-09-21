# coding=utf-8

from setuptools import setup, find_packages, PackageFinder

# python setup.py sdist 打包成tar.gz的形式
# python setup.py bdist_wheel  打包成wheel格式

setup(
    py_modules=["cal_similarity"],  # 需要打包的文件夹下的py文件名词cal_similarity.py
    # packages=find_packages(),  # 需要打包的目录列表
    packages=PackageFinder.find(),
    name="cal_similarity",  # 包名称，也就是文件夹名称
    version="1.0.0",  # 包的版本
    description="cal_similar between two word",  # 对当前package的较短总结
    long_description="***",  # 对当前package的详细说明
    author="yin",  # 作者姓名
    author_email="72666*@qq.com",  # 作者邮箱
    install_requires=[],  # 第三方依赖,这些依赖包会在程序安装的时候也会安装
    zip_safe=False,  # 此项需要，否则卸载报windows error错误
    license="MIT Licence",  # 支持的开源协议
    python_requires=">=3.6.0",  # 指定python的安装要求
    include_package_data=True
)
