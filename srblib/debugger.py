import os

from .srb_json import srbjson
on_srbpc = False
if(os.environ['USER'] == 'srb'):
    on_srbpc = True

on_travis = False
if(os.environ['USER'] == 'travis'):
    on_travis = True

_debug_template = {'srblib':{'debug':False}}
_debug_json = srbjson('~/.config/srblib/debug.json',_debug_template)
debug = _debug_json['debug']
