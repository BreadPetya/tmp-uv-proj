# 

Добавить много файлов в libtmp.
В разных директориях.
Не только python-файлы. Чтобы в build попали ещё *.sh файлы.

В poetry это можно сделать так:
```
[tool.poetry]
packages = [{ include = "nam_lib" }]
include = ["*.sh", "*.json"]
```
