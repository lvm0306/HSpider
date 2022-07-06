from docx import Document


class MDoc():

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.filename = None
        self.mode = None
        self.document = None

    def createFile(self, filename):
        self.filename = filename
        self.mode = "create"
        self.document = Document()
        pass

    def openFile(self, filename):
        self.filename = filename
        self.mode = 'open'
        self.document = Document(filename)

    def add_paragraph(self,text):
        paragraph = self.document.add_paragraph()
        paragraph.add_run(text)
        return paragraph

    def textInParagraph(self, paragraph):

        pass

    def close(self):
        if self.mode == 'open':
            self.document.save()
        elif self.mode == 'create':
            self.document.save(self.filename)

    pass
