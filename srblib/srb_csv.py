import os
import csv

from .srb_json import SrbJson
from .path import abs_path
from .files import verify_file
from .util import top


def csv_to_json(inp_path,out_path):
    json = SrbJson(out_path,[]) # create a SrbJson Object
    json.data = csv_to_json_data(inp_path)
    json._burn_data_to_file() # force update


def csv_to_json_data(inp_path): # return SrbJson object with list template
    data = csv_to_data(inp_path) # get data it is in form of matrix
    header = data[0] # get header
    data = data[1:] # rest is data

    json_data = []
    for row in data:
        item = {}
        for index in range(len(header)):
            item[header[index]] = row[index]
        json_data.append(item)

    return json_data



def csv_to_data(inp_path):
    inp_path = abs_path(inp_path)
    if(not os.path.exists(inp_path)):
        raise Exception('missing input csv file')

    # header write
    inp = open(inp_path)
    inp = csv.reader(inp,delimiter=',')
    return list(inp)


def json_to_csv(inp_path,out_path,header=None):
    inp_path = abs_path(inp_path)
    if(not os.path.exists(inp_path)):
        raise Exception('missing json file')

    data = SrbJson(inp_path).data
    data_to_csv(data,out_path,header)

def data_to_csv(data,out_path,header=None):
    if type(data) is not set and type(data) is not list:
        raise Exception('data should be in form list/set of lists')

    data = list(data)
    first_item = top(data)
    if type(first_item) is list:
        _matrix_data_to_csv(data,out_path,header)
    elif type(first_item) is dict:
        _json_data_to_csv(data,out_path,header)
    else:
        raise Exception('data item should be in form of dict or list')

def _matrix_data_to_csv(data,out_path,header):
    if(header):
        if(type(header) is list):
            data = header + data
        else:
            raise Exception('header shoul be a list')

    out_path = abs_path(out_path)
    verify_file(out_path)
    out = open(out_path, 'w')
    out = csv.writer(out)
    for row in data:
        out.writerow(row)


def _json_data_to_csv(data,out_path,header):
    if(not header):
        first_item = data[0]
        header = list(first_item.keys())

    if(type(header) != list):
        raise Exception('required arguments as list')

    out_path = abs_path(out_path)
    verify_file(out_path)

    # header write
    out = open(out_path, 'w')
    out = csv.writer(out)
    out.writerow(header)

    for row in data:
        row_vals = []
        for key in header:
            row_vals.append(row[key])
        out.writerow(row_vals)
