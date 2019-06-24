from airtest.cli.runner import AirtestCase, run_script
from argparse import Namespace
import airtest.report.report as report
import jinja2
import shutil
import os
import io
import time
 
 
class CustomAirtestCase(AirtestCase):
    
    def setUp(self):
        print("custom setup")
        super(CustomAirtestCase, self).setUp()
 
    def tearDown(self):
        print("custom tearDown")
        super(CustomAirtestCase, self).tearDown()
 
    def run_air(self, root_dir=None, device=[]):
        ''' 
        start to run all xxx.air files which in the root_dir.
        root_dir: the root path of project
        device: the device parameter, we can find this parameter in the AirtestIDE, such as for the windows programs: 'windows:///123456'
        
        '''
        # 测试用例结果集
        results = []
        # 创建日志根目录
        root_log = root_dir + '\\' + 'logs'
        if os.path.isdir(root_log):
            shutil.rmtree(root_log)
        else:
            os.makedirs(root_log)
            print(str(root_log) + 'is created')
           
        print(os.path.join(root_dir, "testcases"))
        # 遍历当前testcasts目录下的所有.air测试用例
        for f in os.listdir(os.path.join(root_dir, "testcases")):
            if f.endswith(".air"):
                print(f)
                # 当前测试用例名称, xxx.air
                airName = f
                # 当前测试用例的绝对路径
                script = os.path.join(os.path.join(root_dir, "testcases"), f)
                print(script)  # D:\Eclipse\AirtestDemo\src\testcases\kugou.air
                # 当前用例log日志保存根目录
                log = os.path.join(root_dir, 'logs' + '\\' + airName.replace('.air', ''))
                print(log)  # D:\Eclipse\AirtestDemo\src\log
                if os.path.isdir(log):
                    shutil.rmtree(log)
                else:
                    os.makedirs(log) 
                    print(str(log) + ' is created')
                # 当前测试用例log文件命名
                output_file = log + '\\' + 'log.html'
                print(output_file)  # D:\Eclipse\AirtestDemo\src\log\kugou\log.html
                
                args = Namespace(device=device, log=log, recording=None, script=script)
                print("args is: ")
                print(args)
                try:
                    run_script(args, AirtestCase)
                except:
                    pass
                finally:
                    rpt = report.LogToHtml(script, log)
                    rpt.report("log_template.html", output_file=output_file)
                    result = {}
                    result["name"] = airName.replace('.air', '')
                    result["result"] = rpt.test_result
                    results.append(result)
                    
        # 生成聚合报告
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(root_dir), extensions=(), autoescape=True)
        template = env.get_template("reports_template.html", root_dir) # os.path.join(root_dir, "templates")
        html = template.render({"results": results})
        # 当前日期时间
        nowtime = time.strftime("%Y-%m-%d %H_%M_%S")
        # 聚合报告名称
        reportname = "summary_report_" + nowtime + '.html'
        # 聚合报告保存路径
        reportpath = os.path.join(root_dir, "reports")
        # 写入聚合报告
        output_file = os.path.join(reportpath, reportname)
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)
        print(output_file)
 
 
if __name__ == '__main__':
    test = CustomAirtestCase()
    device = ['windows:///330802']
    test.run_air('D:\\Eclipse\\AirtestDemo\\src', device)
