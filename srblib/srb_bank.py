import getpass
import hashlib
import os
import pickle

from .path import abs_path
from .files import verify_file

class srbbank:
    def __init__(self,file_name="temp",password=None):
        self._password = password
        self._loggedin = False
        self._data = dict()

        self._file_name = abs_path('.'+file_name+'.bank')
        if not os.path.exists(self._file_name):
            self._loggedin = True
            self._save() # needs loggedin

        self._login(self._password)
        self.load()


    def _login(self,password):
        data = pickle.load(open(self._file_name,'rb'))
        _password = data.get('password')
        if(not _password):
            self._password = None
            self._loggedin = True
            return

        if(not password): raise Exception('password protected')

        if(srbbank._md5(password) == _password): self._loggedin = True
        else: raise Exception('wrong password')


    def _authenticator(func):
        def wrapper(self, *args, **kargs):
            if not self._loggedin:
                raise Exception('Function only available when logged in')
            return func(self, *args, **kargs)
        return wrapper


    @_authenticator
    def setpass(self,password=None):
        if(password):
            self._password = srbbank._md5(password)
        else:
            password = getpass.getpass('Enter your password:')
            _pasword = getpass.getpass('Enter your password:')
            if(password == _pasword):
                self._password = srbbank._md5(password)
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
