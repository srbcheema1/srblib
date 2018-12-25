import os

on_srbpc = False
if(os.environ['USER'] == 'srb'):
    on_srbpc = True

on_travis = False
if(os.environ['USER'] == 'travis'):
    on_travis = True

debug = False

