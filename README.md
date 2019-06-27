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

虽然AirtestIDE提供了一站式功能：脚本开发（录制、编辑）、设备管理、运行、回放、结果查看，但是只能进行执行1条测试用例，而且不能更多的第三方的框架，所以需要在本地安装Airtest框架环境，来实现批量执行测试用例与整合聚合测试报告。

### 目录说明
src (项目根目录)
 |
 |--logs (保存着测试用例执行过程的素材：xxx.jpg、log.html、log.txt，每个测试用例生成独立的文件夹，如：kugou)
 |	 |
 |	 |--kugou (kugou测试用例素材目录)
 |	 |	  |
 |	 |	  |--xxx.jpg (测试过程相关截图)
 |	 |	  |--log.html (kugou测试用例报告)
 |	 |	  |--log.txt (测试日志内容)
 |	 | 
 |	 |--kugou2 (kugou2测试用例素材目录)
 |	 	  |--xxx.jpg (测试过程相关截图)
 |	 	  |--log.html (kugou2测试用例报告)
 |	 	  |--log.txt (测试日志内容)
 |
 |--reports (聚合测试报告目录)
 |	  |
 |	  |--summary_report_xxx.html (聚合测试报告，统计所有测试用例的执行情况)
 |
 |--testcases (测试用例脚本目录，使用AirtestIDE录制编写好的.air脚本放置到该目录下执行)
 |		|
 |		|--kugou.air (kugou测试用例目录)
 |		|	   |
 |		|	   |--kugou.py (kugou测试用例脚本代码)
 |		|	   |--xxx.png (测试脚本用到的截图)
 |		|
 |		|--kugou2.air (kugou2测试用例目录)
 |			   |
 |			   |--kugou2.py (kugou2测试用例脚本代码)
 |			   |--xxx.png (测试脚本用到的截图)
 |
 |--custom_launcher.py (启动程序，python custom_launcher.py直接运行即可)
 |
 |--reports_template.html (聚合报告模板，按需自定义)
 |
 |--README.md




















