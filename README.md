# srblib

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.ocm/srbcheema1/srblib/issues)
[![a srbcheema1 production](https://img.shields.io/badge/-a%20srbcheema1%20production-blue.svg)](https://github.com/srbcheema1)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/srbcheema1/srblib)
[![HitCount](http://hits.dwyl.io/srbcheema1/srblib.svg)](http://hits.dwyl.io/srbcheema1/srblib)

**srblib** is an umberalla python library to hold my useful python scripts which can be used in other projects.


### Installation

#### Install using pip (Recommended)

- Use pip to install, user `--user` flag
```
python3 -m pip install --user srblib
```

#### Build from Source

- Clone the repository and checkout to stable commit
```
git clone https://github.com/srbcheema1/srblib
cd srblib
git checkout <latest_version say: v0.0.x>
```

- install requirements
```
python3 -m pip install --user -r requirements.txt
```
- Install srblib
```
python3 setup.py install --user
```
- Building Source Distribution
```
python3 setup.py sdist
```


### Classes Offered


- Colour - A class with color names and a static print function which prints coloured output to stderr
- SrbBank - A class to store things for later use of a program. can act as a database
- SrbJson - A class to use json file more easily
- Tabular - A class to user tabular data and read write json,xlsx,csv files

### Functions Offered

- abs_path - returns absolute path of a path given. works on windows as well as linux.
- get_os_name - returns OS name. values are windows, linux or mac
- is_installed - checks if the following application is installed on machine or not
- file_extension - returns back the extention of a file from filepath, may return '' if no ext
- file_name - returns filename from a filepath
- remove - removes a path recursively. it deletes all files and folders under that path
- verify_file - verify that a file exists. if not it will create one. also creates parents if needed
- verify_folder - verify that a folder exists. creates one if not there. also creates parents if needed


### Variables Offered

- debug - a boolean whose value can be changed in ~/.config/srblib/debug.json


### Contact / Social Media

[![Github](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/github.png)](https://github.com/srbcheema1/)
[![LinkedIn](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/linkedin-48x48.png)](https://www.linkedin.com/in/srbcheema1/)
[![Facebook](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/fb.png)](https://www.facebook.com/srbcheema/)


### Development by

Developer / Author: [Srb Cheema](https://github.com/srbcheema1/)
