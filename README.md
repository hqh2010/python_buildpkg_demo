# 说明

这是一个python打包的例子。

# 运行

```bash
打包
python setup bdist_wheel
安装
python -m pip install cal_similarity-1.0.0-py3-none-any.whl
卸载
python -m pip uninstall cal_similarity-1.0.0-py3-none-any.whl
```

python setup bdist_wheel构建成功后，会生成如下三个目录：

![](.\image\1.png)

安装之后，可以在系统的python环境目录找到安装成功的cal_similarity包，如下图：

 ![](.\image\2.png)

# 说明

对于cal_similarity中utils目录下的自定义模块（包），一定要加上“__init__.py”文件，文件内容可以为空，否则打包时无法将自定义模块打包到dist下的.whl包中，安装后运行目标python程序会因找不到模块而报错。

# 参考文档

* [Python .whl安装包简介和制作](https://blog.csdn.net/zyq880625/article/details/131415452)

