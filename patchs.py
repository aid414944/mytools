#!/usr/bin/env python

#For example:
#patchs.py "-p1 -E" /path/to/patchsdir

import os
import sys

def patchs(patchsDir):
    for patch in os.listdir(patchsDir):
        path = os.path.join(patchsDir, patch)
        if os.path.isdir(path):
            patchs(path)
        elif os.path.isfile(path):
            os.system("patch " + sys.argv[1] + " < " + path)
 
patchs(sys.argv[2])