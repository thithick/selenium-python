import os
import natsort
from operator import itemgetter
from datetime import datetime, timedelta
from xlrd import open_workbook, cellname, xldate_as_tuple, \
    XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_TEXT, XL_CELL_BOOLEAN, \
    XL_CELL_ERROR, XL_CELL_BLANK, XL_CELL_EMPTY, error_text_from_code
from xlwt import easyxf, Workbook
from xlutils.copy import copy as copy


class ExcelLib:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        self.wb = None
        self.tb = None
        self.sheetNum = None
        self.sheetNames = None
        self.fileName = None
        if os.name is "nt":
            self.tmpDir = "Temp"
        else:
            self.tmpDir = "tmp"

    def get_column_values_test(self, sheetname, column, includeEmptyCells=True):

        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        data = []
        for row_index in range(sheet.nrows):
            cell = cellname(row_index, int(column))
            value = sheet.cell(row_index, int(column)).value
            data[] = value
        if includeEmptyCells is True:
            sortedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return sortedData
        else:
            data = dict([(k, v) for (k, v) in data.items() if v])
            OrderedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return OrderedData

    def get_row_values_test(self, sheetname, row, includeEmptyCells=True):

        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        data = {}
        for col_index in range(sheet.ncols):
            cell = cellname(int(row), col_index)
            value = sheet.cell(int(row), col_index).value
            data[cell] = value
        if includeEmptyCells is True:
            sortedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return sortedData
        else:
            data = dict([(k, v) for (k, v) in data.items() if v])
            OrderedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return OrderedData




