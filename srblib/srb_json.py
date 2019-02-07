import json

from .path import abs_path
from .files import verify_file

class SrbJson:
    '''
    A json class with common functionality.
    parameters:
        file_path - name/path of file
        template  - a basic template for file.
                    can be of two forms:
                        1. {}   # default
                        2. { 'app_name':{} } # default embeded in something, helps to check if file is good/bad
                        3. [] for list type jsons
        strict - strict json follows template strictly and user can only modify values not keys
    '''
    def __init__(self,file_path,template={},strict=False):
        self.strict = strict
        if(type(template) is list and strict):
            raise Exception('strict mode only for dictionary rooted jsons not for list rooted jsons')
        self.file_path = abs_path(file_path)
        self.template = template
        self.masterkey = SrbJson._get_master_key(template) # generlly 'app_name'
        self.fetch_data()

    srblib_template = {
        "srblib": # masterkey
        {
            "debug":False,
        }
    }

    def fetch_data(self):
        self.data = SrbJson.extract_data(self.file_path,self.template) # also creates empty if not there
        if self.strict:
            template = self.template
            if(self.masterkey): template = template[self.masterkey]
            for key in template.keys():
                if not key in self.data:
                    raise Exception('key' +key+ ' missing, json should be similar to template in strict mode')
            for key in self.data:
                if not key in template:
                    raise Exception('Extra key present ' +key+ ', json should be similar to template in strict mode')

        return self.data

    def keys(self):
        return self.data.keys()

    def get(self,index,notfound=None):
        try:
            return self[index]
        except:
            if notfound:
                self[index] = notfound
                return notfound
            else:
                return None

    def __getitem__(self,index):
        notfound = None
        orig_index = index
        if(type(orig_index) is tuple):
            index = orig_index[0]
            notfound = orig_index[1]

        self.fetch_data()
        if index in self.data:
            return self.data[index]

        if type(orig_index) is tuple:
            self[index] = notfound
            return notfound

        if self.masterkey and index in self.template[self.masterkey]:
            self[index] = self.template[self.masterkey][index]
        if not self.masterkey and index in self.template:
            self[index] = self.template[self.masterkey][index]

        return self.data[index]


    def __setitem__(self,index,value):
        if self.strict:
            if index in self.data:
                self.data[index]=value
            else:
                raise Exception('cannot add new key ' +index+ ' in strict mode')
        else:
            self.data[index]=value
        self._burn_data_to_file()

    def append(self,item):
        if not type(self.data) is list:
            raise Exception(' append method only for list type jsons')
        self.data.append(item)
        self._burn_data_to_file()

    def __str__(self):
        return json.dumps(self.data, sort_keys=True, indent=4)

    def __len__(self):
        return len(self.data)

    def __contains__(self,value):
        return value in self.data

    def __delitem__(self,index):
        '''
        deletion is not allowed in strict mode. just modification is permitted
        better to set value to None
        to preserve template structure
        '''
        if self.strict:
            self[index] = None
            return

        del self.data[index]
        data = self.data
        if(self.masterkey):
            data = {self.masterkey:data}

        jfile = open(self.file_path, 'w')
        json.dump(data,jfile,indent = 4,ensure_ascii = False)
        jfile.close()


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
            SrbJson._create_file(fille,template)
        jfile = open(fille)
        data = json.load(jfile)

        masterkey = SrbJson._get_master_key(template) # if template is in srb standard
        if(masterkey):
            if(not masterkey in data.keys()):
                SrbJson._create_file(fille,template)
                jfile = open(fille)
                data = json.load(jfile)
            return data[masterkey]
        else:
            return data

    def _burn_data_to_file(self):
        """
        burns data to original file
        it is insecure way should be avoided to be directly used by user

        """
        data = self.data
        if(self.masterkey):
            data = {self.masterkey:data}

        jfile = open(self.file_path, 'w')
        json.dump(data,jfile,indent = 4,ensure_ascii = False)
        jfile.close()


    @staticmethod
    def dump_data(data,file_path,template):
        """
        adds data to original file
        it is bit secure, doesn't add extra key to data if not present in jfile already
        """
        temp = SrbJson(file_path,template)
        for key in data:
            if(key in temp):
                temp.data[key] = data[key]
        temp._burn_data_to_file() # lazy burning


    @staticmethod
    def _create_file(fille,template):
        verify_file(fille)
        jfile = open(fille, 'w')
        json.dump(template,jfile,indent = 4,ensure_ascii = False)
        jfile.close()

    @staticmethod
    def _get_master_key(template):
        if type(template) is list: # no master key for list
            return None
        keys = template.keys() # if template is in srb standard
        if(len(keys) == 1 and type(template[list(keys)[0]]) == dict):
            return list(keys)[0]
        else:
            return None
