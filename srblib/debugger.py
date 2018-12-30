import os

from .srb_json import SrbJson
on_srbpc = False
if(os.environ['USER'] == 'srb'):
    on_srbpc = True

_debug_template = {'srblib':{'debug':False,'on_travis':False}}
_debug_json = SrbJson('~/.config/srblib/debug.json',_debug_template)

on_travis = False
if(os.environ['USER'] == 'travis'):
    on_travis = True
if(not on_travis):
    on_travis = _debug_json['on_travis']

debug = _debug_json['debug']
