# srblib

[![a srbcheema1 production](https://img.shields.io/badge/-a%20srbcheema1%20production-blue.svg)](https://github.com/srbcheema1)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.ocm/srbcheema1/srblib/issues)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/srbcheema1/srblib)
[![Build Status](https://travis-ci.org/srbcheema1/srblib.svg?branch=master)](https://travis-ci.org/srbcheema1/srblib)
[![Build status](https://ci.appveyor.com/api/projects/status/e4pjlfby5xp2jy0d/branch/master?svg=true)](https://ci.appveyor.com/project/srbcheema1/srblib/branch/master)
[![HitCount](http://hits.dwyl.io/srbcheema1/srblib.svg)](http://hits.dwyl.io/srbcheema1/srblib)

**srblib** is an umberalla python library to hold my useful python scripts which can be used in other projects.

Its just not a *library*. Its a **perspective**.


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
```
    Colour.print(message,Colour.RED) # for foreground as red
    Colour.print(message,Colour.FULLGREEN) # for background as green
    Colour.print(message,Colour.FULLGREEN+Colour.RED) # for background as fullgreen and foreground as RED
```
- SrbBank - A class to store things for later use of a program. can act as a database
```
    a = SrbBank('db_name') #say the db_name is your database name
    a['hello'] = "world"
    b = SrbBank('db2','password')
    b['hello'] = "peeps"
    # EXIT THE CODE AND START NEW SESSION
    a = SrbBank('db_name')
    print(a['hello']) # 'world'
    b = SrbBank('db2','password')
    print(b['hello']) # 'peeps'
```
- SrbJson - A class to use json file more easily
```
    a = SrbJson('json/path')
    a['hello'] = 'world'
    # EXIT THE CODE AND START NEW SESSION
    a = SrbJson('json/path')
    print(a['hello']) # 'world'
```
- Tabular - A class to user tabular data and read write json,xlsx,csv files
```
    a = Tabular('path/to/file') # can take files with extension as csv,json,xlsx
    print(a) # prints table in tabular form
    data = a.matrix # get data in form of list of lists i.e. matrix
    json_data = a.json # get data in form of list of dictionaries i.e. json
    print(a[1]['name']) # here name is the attribute used to name the columns
    print(a[0]) # prints attributes
    print(a[1]) # prints 1st row (0 based)
    print(a['name']) # prints column with attribute 'name'
    a.write_xls('output/path')
    a.write_csv('output/path')
    a.write_json('output/path')

    NOTE: it reads blank and empty cells from excel file as None
    NOTE: to read excel file in strict mode please call obj.load_xls(path,strict=True)
```
- Module - A class to import a file with variable path
```
    a = Module('/path/to/file')
    a.function_in_that_file()
    print(a.variable_in_that_file)
```
- Soup - A class to help in scrapping, argument should be a url or BeautifulSoup object
```
    soup = BeautifulSoup('<p><div class="good">hello</div><div>world</div></p>','html.parser')
    a = Soup(soup)
    print(a) # prints it in pretty way
    b = a['div',{'class':'good'}] # [<div class="good">hello</div>]
    b = a[lambda tag: tag.name == 'div'] # [<div class="good">hello</div>, <div>world</div>]

    a = Soup('http://gitub.com/srbcheema1')
    b = a['div'][1]['p'] # cascading in [] operators they work similar to find_all function, save space
    text_output = a['div'][1]['p'].text # we can call any function or variable that we could call on soup
    soup = b.soup # get original soup object
```

### Functions Offered

- abs_path - returns absolute path of a path given. works on windows as well as linux.
- get_os_name - returns OS name. values are windows, linux or mac
- is_installed - checks if the following application is installed on machine or not
- file_extension - returns back the extention of a file from filepath, may return '' if no ext
- file_name - returns filename from a filepath
- remove - removes a path recursively. it deletes all files and folders under that path
- verify_file - verify that a file exists. if not it will create one. also creates parents if needed
- verify_folder - verify that a folder exists. creates one if not there. also creates parents if needed
- similarity - returns percentage of similarity in two strings.
- str_hash - hashing a string
- path_hash - hashing a full path


### Variables Offered

- debug - a boolean whose value can be changed in ~/.config/srblib/debug.json
- on_windows - a boolean with value `True` is running on windows
- on_ci - a boolean with value `True` is running on CI


### Contact / Social Media

[![Github](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/github.png)](https://github.com/srbcheema1/)
[![LinkedIn](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/linkedin-48x48.png)](https://www.linkedin.com/in/srbcheema1/)
[![Facebook](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/fb.png)](https://www.facebook.com/srbcheema/)


### Developed by

Developer / Author: [Srb Cheema](https://github.com/srbcheema1/)
