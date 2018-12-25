
import requests

from utils.UserAgentSeed import *
from utils.GetEncoding import GetEncoding

from bs4 import BeautifulSoup as bs

class BsUtil():
    def __init__(self, bs):
        self.bs = bs

    def fa_t(self,tag):
        return self.bs.find_all(tag)

    def fa_t_c(self,tag,classNmae):
        return self.bs.find_all(tag,class_=classNmae)

    def fa_c(self,classNmae):
        return self.bs.find_all(class_=classNmae)

    def fa_id(self,idNmae):
        return self.bs.find_all(id=idNmae)

    def fa_t_c_last(self,tag,classNmae):
        return self.bs.find_all(tag,class_=classNmae)[-1]

    def fa_t_c_first(self,tag,classNmae):
        return self.bs.find_all(tag,class_=classNmae)[0]

    def fa_id_last(self,tag,idNmae):
        return self.bs.find_all(tag,id=idNmae)[-1]

    def fa_id_first(self,tag,idNmae):
        return self.bs.find_all(tag,id=idNmae)[0]

    def fa_c_last(self,classNmae):
        return self.bs.find_all(class_=classNmae)[-1]

    def fa_c_first(self,classNmae):
        return self.bs.find_all(class_=classNmae)[0]

    def fa_t_last(self,tag):
        return self.bs.find_all(tag)[-1]

    def fa_t_first(self,tag):
        return self.bs.find_all(tag)[0]