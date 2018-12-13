import os

srbpc = False
if(os.environ['USER'] == 'srb'):
    srbpc = True

travis = False
if(os.environ['USER'] == 'travis'):
    travis = True

debug = False

