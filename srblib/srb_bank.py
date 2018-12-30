import getpass
import hashlib
import os
import pickle
import json

from .path import abs_path
from .files import verify_file, file_name, file_extension

class SrbBank:
    '''
    args:
        filename:- filename to be used to store data, it will be a file locally without .bank extension
        password:- password if needed. to open a passwrd protected file you need to send password
    '''
    def __init__(self,filename="temp",password=None):
        self._password = password
        self._loggedin = False
        self._data = dict()

        filename = abs_path('.'+filename)
        file_ext = file_extension(filename)
        if file_ext == '':
            filename += '.bank'
        else:
            raise Exception('file_name should not have extension')
        self._file_name = filename
        if not os.path.exists(self._file_name):
            self._loggedin = True
            self._save() # needs loggedin

        self._login(self._password)
        self.load()


    def _login(self,password):
        '''
        logins into a bank account
        once logged in we can perform read write operations
        '''
        data = pickle.load(open(self._file_name,'rb'))
        _password = data.get('password')
        if(not _password): # not password protected
            self._password = None
            self._loggedin = True
            return

        if(not password): raise Exception('password protected, please provide password')

        if(SrbBank._md5(password) == _password): self._loggedin = True
        else: raise Exception('wrong password')


    def _authenticator(func):
        def wrapper(self, *args, **kargs):
            if not self._loggedin:
                raise Exception('Function only available when logged in')
            return func(self, *args, **kargs)
        return wrapper

    @_authenticator
    def __str__(self):
        return json.dumps(self._data, sort_keys=True, indent=4)

    @_authenticator
    def setpass(self,password=None):
        if(password):
            self._password = SrbBank._md5(password)
        else:
            while True:
                password = getpass.getpass('Enter your password:')
                _pasword = getpass.getpass('ReEnter your password:')
                if(password == _pasword):
                    self._password = SrbBank._md5(password)
                    break
                else:
                    print('passwords do not match')
        self._save()

    @_authenticator
    def removepass(self):
        self._password = None
        self._save()


    @_authenticator
    def load(self):
        data = pickle.load(open(self._file_name,'rb'))
        self._password = data.get('password')
        if(self._password):
            del data['password']
        self._data = data
        return data

    @_authenticator
    def __getitem__(self,index):
        if(index in self._data):
            return self._data[index]
        else:
            return None

    @_authenticator
    def __setitem__(self,index,value):
        self._data[index]=value
        self._save()

    @_authenticator
    def __delitem__(self,index):
        del self._data[index]
        self._save()

    @_authenticator
    def __contains__(self,value):
        return value in self._data

    @_authenticator
    def _save(self):
        data = self._data
        if(self._password):
            data['password'] = self._password
        pickle.dump(data,open(self._file_name,'wb'))

    @staticmethod
    def _md5(inp):
        return hashlib.md5(inp.encode('utf-8')).hexdigest()
