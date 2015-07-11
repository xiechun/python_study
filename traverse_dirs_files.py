#!coding=utf-8
#!/usr/bin/python

import os
import os.path

loop_dir = "/home/ptrade/front1";

for root_dir, cur_dir, files in os.walk(loop_dir):
    for d in cur_dir:
        print "current_dir is: ", d;
    for f in files:
        print "files:", f;
