import json

from .path import abs_path
from .files import verify_file

class srbjson:
    def __init__(self,file_name,template={}):
        self.file_name = abs_path(file_name)
        self.template = self.template
        self.data = srbjson.extract_data(self.file_name,template)
        self.masterkey = srbjson._get_master_key(template)

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
            srbjson.dump_data(self.data,self.file_name,self.template)

    def __contains__(self,value):
        return value in self.data

    def __delitem__(self,index):
        '''
        deletion is not allowed. just modification
        '''
        return


    @staticmethod
    def extract_data(file_name,template={}):
        """
        Extracts json data from the given file
        if there is no such file
            it will create one
        if there is currupt file (only for srb standard templates)
            it will create new
        if file is ok
            it will return its content
        """
        fille = abs_path(file_name)
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
    def dump_data(data,file_name,template):
        """
        create RAW data from LIST
        uses _write_data
        """
        fille = abs_path(file_name)
        dictt = srbjson.extract_data(fille,template)
        for key in data:
            if(key in dictt):
                dictt[key] = data[key]

        masterkey = srbjson._get_master_key(template)
        if(masterkey):
            dictt = {masterkey:dictt}

        jfile = open(abs_path(file_name), 'w')
        json.dump(dictt,jfile,indent = 4,ensure_ascii = False)
        jfile.close()


    srblib_template = {
        "srblib":{
            "debug":False,
        }
    }

    @staticmethod
    def _create_file(fille,template):
        verify_file(fille)
        jfile = open(fille, 'w')
        json.dump(template,jfile,indent = 4,ensure_ascii = False)
        jfile.close()

    @staticmethod
    def _get_master_key(template):
        keys = template.keys() # if template is in srb standard
        if(len(keys) == 1 and type(keys[0]) == dict):
            return keys[0]
        else:
            return None
