'''
博客模板生成器
2022.05.04 
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

from encodings import utf_8
import time

title_time = time.strftime("%Y-%m-%d",time.localtime())
title_txt = input("博客标题:")
title_str = title_time + "-"+title_txt.replace(" ","-")+".md"

md_doc = open(title_str,'a',encoding='utf-8')
md_doc.write("---\n")
md_doc.write("layout: post\n")
md_doc.write("title: "+title_txt+"\n")
md_doc.write("author: DaCaiGouX\n")
date = time.strftime("%Y-%m-%d %H:%M",time.localtime())
md_doc.write("date: "+date+"+0800\n")

md_doc.write("tags: \n")
n = int(input("Tags数目:"))
for i in range(n):
    s = input("Tags: \n")
    md_doc.write("- "+s+"\n")
md_doc.write("toc: true\n")      #显示目录
md_doc.write("excerpt_separator: <!--more-->\n")    #用来生成摘要
md_doc.write("---\n")

md_doc.write("*在这里书写摘要*\n")
md_doc.write("<!--more-->\n")