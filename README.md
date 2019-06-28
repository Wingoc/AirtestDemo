# AirtestDemo

    AirtestDemo是基于Python + Airtest + Unittest技术实现的Windows系统客户端的UI自动化测试例程，以供参考。

## Airtest
    Airtest框架基于基于图像识别，适用于所有Android和Windows系统，通过截图生成测试脚本来实现UI自动化测试。

## AirtestIDE
    AirtestIDE是一个跨平台、多端（Windows、web、android、ios、游戏）的UI自动化测试编辑器，可以实现自动化脚本录制、一键回放、报告查看等功能。
### 安装：
  1.下载地址：[链接](http://airtest.netease.com/changelog.html)
    
  2.解压下载的压缩包，双击AirtestIDE.exe程序即可使用；
    
  
### 使用：
  官方快速入门教程，有演示视频、动图，简单明了：[链接](http://airtest.netease.com/tutorial/Tutorial.html)

## AirtestDemo 介绍

  虽然AirtestIDE提供了一站式功能：脚本开发（录制、编辑）、设备管理、运行、回放、结果查看，但是只能进行执行1条测试用例，而且不能使用更多的第三方的框架，所以需要在本地安装Airtest框架环境，来实现批量执行测试用例与整合聚合测试报告。

### 目录说明
  ![Image text](https://github.com/Wingoc/AirtestDemo/blob/master/tree.png)

### 本地Python环境安装
    安装Python环境，使用 pip安装Airtest模块：pip install airtest

### 用例脚本录制编写
  测试用例脚本使用AietestIDE工具录制编写，[详细教程](http://airtest.netease.com/docs/docs_AirtestIDE-zh_CN/3_record_script/0_script_faq.html)，将录制编写的用例脚本保存放置在"./testcases/"目录下即可。

### 修改custome_launcher.py启动程序
  根据本地运行环境修改custome_launcher.py启动程序，直接执行"python custom_launcher.py"命令即可启动自动化测试，测试结束后可在"./reports/"目录下查看测试结果；
  custome_launcher.py脚本需要修改的地方如下：
  1. root_dir: 项目的根目录，如："D:\\Eclipse\\AirtestDemo\\src"
  2. device: 设备参数，如："['windows:///1508866']", 即："windows": windows窗口; "1508866": 窗口句柄, 该参数是根据AirtestIDE执行脚本是获取
  3. Ps: 我在本地执行"rpt = report.LogToHtml(script, log)"生成报告时报错目录异常，如有遇到该问题，可以尝试将"./airtest/report/report.py"脚本中的"script_path = os.path.join(self.script_root, self.script_name)",修改为"script_path = self.script_root"
  
















