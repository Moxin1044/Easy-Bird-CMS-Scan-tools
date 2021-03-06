"""
Copyright (c) 2020-2021 Moxin
   [Software Name] is licensed under Mulan PSL v2.
   You can use this software according to the terms and conditions of the Mulan PSL v2.
   You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2
   THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
   See the Mulan PSL v2 for more details.
By：M0x1n Time：2020.12.23Updated
Ver:1.2(Third edition) 1.2第三版
https://bbs.moxinwangluo.cn/
此脚本可以通过一些网站特征来进行CMS识别，当然，这个脚本也是开源的。
This script can be used for CMS recognition based on some website features, and of course, this script is also open source.
"""
from auxiliary import http_status
import os
import auxiliary
import re
import sys
import urllib
from urllib import request
import chardet
import requests
import cms
import robotsscan


def dedever(url):
    if http_status(url + "/data/admin/ver.txt") == 200:
        page = request.urlopen(url + "/data/admin/ver.txt")
        content = page.read()
        fp = open("date\\files.txt", "w+b")  # 打开一个文本文件
        fp.write(content)  # 写入数据
        fp.close()  # 关闭文件
        print("这个站点可能是织梦Dedecms，版本号：", content) # 直接输出文本内容