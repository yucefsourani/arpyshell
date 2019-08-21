#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  arpyshell.py
#  
#  Copyright 2019 youcef sourani <youssef.m.sourani@gmail.com>
#
#
import subprocess
from functools import partial

class SHELL(object):
    def __run(self,command,argv="",shell="bash -c ",output=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,utf8=True):
        if argv:
            if output:
                p = subprocess.Popen(
                "{} '{}'".format(shell,command+" "+argv),
                stdout=stdout,
                stderr=stderr
                ,shell=True)
                out,err = p.communicate()
                if utf8:
                    out = out.decode("utf-8")
                    err = err.decode("utf-8")
                return out,err
            else:
                return subprocess.call("{} '{}'".format(shell,command+" "+argv),shell=True)
        else:
            if output:
                p = subprocess.Popen(
                "{} '{}'".format(shell,command),
                stdout=stdout,
                stderr=stderr
                ,shell=True)
                out,err = p.communicate()
                if utf8:
                    out = out.decode("utf-8")
                    err = err.decode("utf-8")
                return out,err
            else:
                return subprocess.call("{} '{}'".format(shell,command),shell=True)
    
    def __getattr__(self,attr):
        return partial(self.__run, attr)
