import csv

class CsvUtil():

    def __init__(self,filename,cate):
        self.filename=filename
        self.file=None
        self.csv_write=None
        self.cate=cate
        pass
    def write(self,s):
        if self.file is None:
            self.file = open(self.filename, self.cate, newline='')
            self.csv_write = csv.writer(self.file)
        self.csv_write.writerow(s)
        pass

    def wclear(self):
        self.file=None

    def getWiter(self):
        if self.file is None:
            self.file = open(self.filename,  self.cate, newline='')
            self.csv_write = csv.writer(self.file)
        return self.csv_write

    def read(self):
        if self.file is None:
            self.file = open(self.filename, self.cate, newline='')
        return csv.reader(self.file)
