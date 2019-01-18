import os

from .srb_json import SrbJson
on_srbpc = False
if(os.environ.get('USER') == 'srb'):
    on_srbpc = True

_debug_template = {'srblib':{'debug':False,'on_travis':False,'on_appveyor':False,'on_ci':False}}
_debug_json = SrbJson('~/.config/srblib/debug.json',_debug_template)

on_travis = False
if(os.environ.get('TRAVIS','False').lower() == 'true'):
    on_travis = True
if(not on_travis):
    on_travis = _debug_json['on_travis']

on_appveyor = False
if(os.environ.get('APPVEYOR','False').lower() == 'true'):
    on_appveyor = True
if(not on_appveyor):
    on_appveyor = _debug_json['on_appveyor']

on_ci = False
if(os.environ.get('CI','False').lower() == 'true'):
    on_ci = True
if(not on_ci):
    on_ci = _debug_json['on_ci']

if on_ci:
    on_travis = True
    on_appveyor = True

debug = _debug_json['debug']

