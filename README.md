# Python 檔案啟動器

##介紹
只要設定`setting.ini`就可以設置啟動器了.

```
[DEFAULT]
# To decide which mode you want, support two mode, in detail see below.
FolderMode = False

[PATH]
# FolderPath Use raw str e.g. D:\PythonProject\Project1
# Path Use "," to split Path e.g. D:\PythonProject\Project2\main.py , D:\PythonProject\Project3\main.py
FolderPath = D:\PythonProject\Project1
Path = D:\PythonProject\Project2\main.py,
        D:\PythonProject\Project3\main.py
```

主要支援同一時間的開啟多個檔案.

## 開發目的
主要是配合windows內建的工作排程器,
一般來講你要設定開機自啟檔案的話,
就必須到工作排程建立新的工作.

那要啟動5個檔案你就需要設定5次, 太麻煩了,
所以我做了一個小程式可以更簡單的配置開啟程式,
配置完後再將此python檔加入工作排程就可以了.

## 更多內容
後來發現其實只要使用.bat檔案執行python, 就可以達到相同的目的了:)