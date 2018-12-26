import json

from .path import abs_path
from .files import verify_file

class srbjson:
    '''
    A json class with common functionality.
    parameters:
        file_path - name/path of file
        template  - a basic template for file.
                    can be of two forms:
                        1. {}   # default
                        2. { 'app_name':{} } # default embeded in something, helps to check if file is good/bad
    '''
    def __init__(self,file_path,template={}):
        self.file_path = abs_path(file_path)
        self.template = template
        self.masterkey = srbjson._get_master_key(template) # generlly 'app_name'
        self.fetch_data()

    srblib_template = {
        "srblib": # masterkey
        {
            "debug":False,
        }
    }

    def fetch_data(self):
        self.data = srbjson.extract_data(self.file_path,self.template) # also creates empty if not there
        return self.data

    def keys(self):
        return self.data.keys()

    def __getitem__(self,index):
        if(index in self.data):
            return self.data[index]
        else:
            return None

    def __setitem__(self,index,value):
        if(index in self.data):
            self.data[index]=value
            srbjson.dump_data(self.data,self.file_path,self.template)

    def __contains__(self,value):
        return value in self.data

    def __delitem__(self,index):
        '''
        deletion is not allowed. just modification is permitted
        better to set value to None
        to preserve template structure
        '''
        return


    @staticmethod
    def extract_data(file_path,template={}):
        """
        Extracts json data from the given file
        if there is no such file
            it will create one
        if there is currupt file (only for srb standard templates)
            it will create new
        if file is ok
            it will return its content
        """
        fille = abs_path(file_path)
        try:
            jfile = open(fille)
        except FileNotFoundError:
            srbjson._create_file(fille,template)
        jfile = open(fille)
        data = json.load(jfile)

        masterkey = srbjson._get_master_key(template) # if template is in srb standard
        if(masterkey):
            if(not masterkey in data.keys()):
                srbjson._create_file(fille,template)
                jfile = open(fille)
                data = json.load(jfile)
            return data[masterkey]
        else:
            return data


    @staticmethod
    def dump_data(data,file_path,template):
        """
        burns data to original file
        """
        fille = abs_path(file_path)
        dictt = srbjson.extract_data(fille,template)
        for key in data:
            if(key in dictt):
                dictt[key] = data[key]

        masterkey = srbjson._get_master_key(template) # just to avoid passing extra parameter as masterkey
        if(masterkey):
            dictt = {masterkey:dictt}

        jfile = open(abs_path(file_path), 'w')
        json.dump(dictt,jfile,indent = 4,ensure_ascii = False)
        jfile.close()



    @staticmethod
    def _create_file(fille,template):
        verify_file(fille)
        jfile = open(fille, 'w')
        json.dump(template,jfile,indent = 4,ensure_ascii = False)
        jfile.close()

    @staticmethod
    def _get_master_key(template):
        keys = template.keys() # if template is in srb standard
        if(len(keys) == 1 and type(template[list(keys)[0]]) == dict):
            return list(keys)[0]
        else:
            return None
