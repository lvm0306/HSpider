from urllib import request

import requests
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/http.ui')

        self.ui.btn_add.clicked.connect(self.btadd)
        self.ui.btn_clear.clicked.connect(self.btclear)
        self.ui.btn_send.clicked.connect(self.btsend)
        self.ui.btn_sub.clicked.connect(self.btsub)
        # self.ui.comboBox.clicked.connect(self.btsub)
        self.ui.et_req
        self.ui.et_respone
        self.ui.et_url
        self.ui.table

    def show(self,show):
        QMessageBox.about(self.ui,
                    'show',
                    f'''{show}'''
                    )
    def btadd(self):
        print(str(self.ui.table.currentRow()))
        self.ui.table.insertRow(self.ui.table.rowCount())
        pass
    def btsub(self):
        print(str(self.ui.table.currentRow()))
        if self.ui.table.currentRow() != -1:
            self.ui.table.removeRow( self.ui.table.currentRow())
        else:
            self.ui.table.removeRow( self.ui.table.rowCount())
        # self.show(self.ui.comboBox.currentText())
        pass

    def btclear(self):
        pass
    def btsend(self):
        #发送逻辑
        if self.ui.et_url.toPlainText()!='':
            print(self.ui.et_url.toPlainText())
            # self.show(self.ui.et_url.toPlainText())
            html = requests.get(self.ui.et_url.toPlainText())
            print(html.content.__str__())
            self.ui.et_respone.setPlainText(f''' {html.content.__str__()}''')

        pass
    def requestget(self):
        pass


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()