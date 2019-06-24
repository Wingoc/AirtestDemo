# -*- encoding=utf8 -*-
__author__ = "xianbr"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1561342003299.png", record_pos=(0.451, -0.215), resolution=(1255, 877)))
text("GEM")
touch(Template(r"tpl1561087604651.png", record_pos=(0.645, -0.189), resolution=(1255, 811)))
touch(Template(r"tpl1560998743112.png", record_pos=(1.002, -0.071), resolution=(1255, 834)))
sleep(2)

double_click(Template(r"tpl1561087863623.png", record_pos=(0.482, 0.025), resolution=(1255, 912)))
