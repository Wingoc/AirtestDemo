# -*- encoding=utf8 -*-
__author__ = "xianbr"

from airtest.core.api import *

auto_setup(__file__)


double_click(Template(r"tpl1561347238109.png", record_pos=(0.427, -0.216), resolution=(1255, 877)))

# text(" ")
keyevent("王力宏")

touch(Template(r"tpl1560999111708.png", record_pos=(0.627, -0.198), resolution=(1255, 834)))
touch(Template(r"tpl1560999129683.png", record_pos=(1.002, -0.076), resolution=(1255, 834)))
sleep(2)

double_click(Template(r"tpl1561348471901.png", record_pos=(0.473, 0.127), resolution=(1255, 989)))


