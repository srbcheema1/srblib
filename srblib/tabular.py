import os
import json
import csv

import pandas
from terminaltables import AsciiTable
import xlwt # only writes into excel workbook

from .srb_json import SrbJson
from .path import abs_path
from .files import verify_file, file_extension
from .util import top


class Tabular:
    def __init__(self,data=None):
        self.matrix = []
        self.json = []
        self.json_str = ""
        self.header = []
        self._parse(data)

    '''
    loader methods, each of them load matrix then call _sync()
    '''
    def load_json(self,inp_path,header=None):
        inp_path = abs_path(inp_path)
        if(not os.path.exists(inp_path)):
            raise Exception('missing input csv file')
        data = SrbJson(inp_path).data
        data = list(data)
        self.matrix = Tabular.json_to_matrix(data,header)
        self._sync()


    def load_csv(self,inp_path,delimit=','): # return tabular
        inp_path = abs_path(inp_path)
        if(not os.path.exists(inp_path)):
            raise Exception('missing input csv file')

        inp = open(inp_path)
        inp = csv.reader(inp,delimiter=delimit)
        self.matrix = list(inp)
        self._sync()

    def load_xls(self,inp_path):
        inp_path = abs_path(inp_path)
        if(not os.path.exists(inp_path)):
            raise Exception('missing input excel file')

        raw_data = pandas.read_excel(inp_path)
        header = list(raw_data.columns)

        data = []
        if(len(header) != 0): # some headers in xls file
            temp_data = []
            for head in header:
                col = list(raw_data[head])
                temp_data.append(col)
            data.append(header)
            for i in range(len(temp_data[0])):
                row = []
                for j in range(len(header)):
                    row.append(temp_data[j][i])
                data.append(row)

        self.matrix = data
        self._sync()

    def load_matrix(matrix):
        self.matrix = matrix
        self._sync()

    def _sync(self):
        self.json = Tabular.matrix_to_json(self.matrix)
        self.json_str = json.dumps(self.json, sort_keys=True, indent=4)

    '''
    writer methods
    '''
    def write_json(self,out_path):
        json = SrbJson(out_path,[]) # create a SrbJson Object
        json.data = self.json
        json._burn_data_to_file() # force update

    def write_csv(self,out_path):
        out_path = abs_path(out_path)
        verify_file(out_path)
        out = open(out_path, 'w')
        out = csv.writer(out)
        for row in self.matrix:
            out.writerow(row)

    def write_xls(self,out_path):
        out_path = abs_path(out_path)
        verify_file(out_path)
        book = xlwt.Workbook(encoding="utf-8")
        sheet = book.add_sheet("Sheet1")
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            for j in range(len(row)):
                sheet.write(i,j,row[j])

        book.save(out_path)

    '''
    helper methods used for conversion
    '''
    @staticmethod
    def matrix_to_json(data): # return list of dictonaries
        header = data[0] # get header
        data = data[1:] # rest is data

        json_data = []
        for row in data:
            item = {}
            for index in range(len(header)):
                item[header[index]] = row[index]
            json_data.append(item)

        return json_data

    @staticmethod
    def json_to_matrix(data,header=None): # provide header to specify order else it will be random
        if(not header):
            first_item = data[0]
            header = list(first_item.keys()) # random order header

        if(type(header) != list):
            raise Exception('required arguments as list')

        ans = []
        ans.append(header)

        for row in data:
            row_vals = []
            for key in header:
                row_vals.append(row[key])
            ans.append(row_vals)
        return ans

    '''
    other operators and functions
    '''
    def __getitem__(self,index):
        if type(index) is str:
            loc = self.matrix[0].index(index)
            ans = []
            for i in range(1,len(self.matrix)):
                ans.append(self.matrix[i][loc])
            return ans
        return Tabular.row(self.matrix[index],self.matrix[0])

    def __len__(self):
        return len(self.matrix)

    def append(self,item):
        self.matrix.append(item)

    def __str__(self):
        return AsciiTable(self.matrix).table
        return self.matrix.__str__() # simple way

    '''
    parsers
    '''

    def _parse(self,data):
        if not data:
            return
        if type(data) is str:
            self._parse_file(data)
            return

        ans = []
        first_row = top(data)
        if type(first_row) is not dict:
            for row in data:
                ans.append(list(row))
            self.matrix = ans
            return

        header = list(first_row.keys()) # random order header
        ans.append(header)
        for row in data:
            row_vals = []
            for key in header:
                row_vals.append(row[key])
            ans.append(row_vals)
        self.matrix = ans

    def _parse_file(self,file_path):
        file_path = abs_path(file_path)
        ext = file_extension(file_path)
        if ext in ['csv']:
            self.load_csv(file_path)
        elif ext in ['json']:
            self.load_json(file_path)
        elif ext in ['xls','xlsx']:
            self.load_xls(file_path)
        else:
            raise Exception('Unknown file extension')

    '''
    helper class that enables named indexing into data
    '''
    class row:
        def __init__(self,data,header):
            self.header = header
            self.row = data
        def __getitem__(self,index):
            if type(index) is str:
                loc = self.header.index(index)
                return self.row[loc]
            return self.row[index]
        def __len__(self):
            return len(self.row)
        def __str__(self):
            return self.row.__str__()
            # parse items

