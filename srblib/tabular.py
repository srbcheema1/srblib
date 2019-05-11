import os
import json
import csv

from terminaltables import AsciiTable
import xlwt # only writes into excel workbook
import xlrd # only reads from excel workbook

from .srb_json import SrbJson
from .path import abs_path
from .files import verify_file, file_extension, remove
from .util import top


class Tabular:
    '''
    this class assumes that your data has got a header
    say first row in excel sheet is header
    if your data is header-less then you may extract out matrix directly
    x = Tabular('file-path').matrix
    now operate on x directly
    '''
    def __init__(self,data=None):
        self.matrix = []
        self.json = []
        self.json_str = ""
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
        self.matrix = []

        inp = open(inp_path)
        inp = csv.reader(inp,delimiter=delimit)
        self.matrix = list(inp)
        self._sync()

    def load_xls(self,inp_path,strict = False):
        '''
        in strict mode we skip those rows which have first cell empty
        can be used for commenting purposes
        '''
        inp_path = abs_path(inp_path)
        if(not os.path.exists(inp_path)):
            raise Exception('missing input excel file')
        self.matrix = []

        sheet = xlrd.open_workbook(inp_path).sheets()[0]
        for i in range(sheet.nrows):
            if strict and sheet.cell_type(i,0) in (0,6):
                continue
            row = []
            sheet_row = sheet.row_values(i)
            for j in range(len(sheet_row)):
                if sheet.cell_type(i,j) in (0,6): row.append(None)
                else: row.append(sheet_row[j])
            self.matrix.append(row)
        for i in range(sheet.ncols):
            if not self.matrix[0][i]:
                raise Exception('header should not be none')
        self._sync()


    def load_matrix(self,matrix):
        refined_matrix = []
        cols = 0
        for row in matrix:
            cols = max(len(row),cols)

        for row in matrix:
            refined_row = []
            for i in range(cols):
                elem = row[i] if i < len(row) else None
                refined_row.append(elem)
            refined_matrix.append(refined_row)

        self.matrix = refined_matrix
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
        if os.path.isfile(out_path): remove(out_path) # remove an existing one
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
        header = [str(x) for x in data[0]] # get header
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
        if type(index) is slice:
            header = [self.matrix[0]]
            data = self.matrix[index]
            header.extend(data)
            return Tabular(header)
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
        self._sync()

    def extend(self,othermatrix):
        if type(othermatrix) is Tabular:
            self.extend(othermatrix.matrix[1:])
        self.matrix.extend(item)
        self._sync()

    def __str__(self):
        return AsciiTable(self.matrix).table
        return self.matrix.__str__() # simple way

    def __iter__(self):
        for x in self.matrix[1:]:
            yield Tabular.row(x,self.matrix[0])

    def sort(self,fun,*args,**kwargs):
        '''
        a = Tabular('file')
        a.sort(lambda x: int(x[0]),reverse = True)
        '''
        header = [self.matrix[0]]
        data = self.matrix[1:]
        data = sorted(data,key=fun,*args,**kwargs)
        header.extend(data)
        self.matrix=header
        self._sync()



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
            self.load_matrix(ans)
            return

        header = list(first_row.keys()) # random order header
        ans.append(header)
        for row in data:
            row_vals = []
            for key in header:
                row_vals.append(row[key])
            ans.append(row_vals)
        self.load_matrix(ans)

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

