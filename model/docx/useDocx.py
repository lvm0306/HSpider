from docx import Document
from docx.shared import Inches

from model.docx.MDoc import MDoc


def run():
    document = Document()
    paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
    document.add_heading('The REAL meaning of the universe')
    prior_paragraph = paragraph.insert_paragraph_before('Lorem ipsum')
    table = document.add_table(rows=2, cols=3)
    ce = table.cell(0, 0)
    ce.text='mv.jpeg'
    cell = table.cell(0, 1)
    cell.text = 'parrot, possibly dead'
    row = table.rows[1]
    row.cells[0].text = 'Foo bar to you.'
    row.cells[1].text = 'And a hearty foo bar to you too sir!'
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)
    pic = document.add_picture('mv.jpeg',width=Inches(1.0))
    p= document.paragraphs
    print(len(p))


    paragraph.style = 'List Bullet'
    paragraph = document.add_paragraph('Lorem ipsum ')
    paragraph.add_run('dolor sit amet.')
    paragraph_format = paragraph.paragraph_format
    paragraph_format
    paragraph = document.add_paragraph()
    paragraph.add_run('Lorem ipsum ')
    paragraph.add_run('dolor').bold = True
    paragraph = document.add_paragraph('Normal text, ')
    paragraph.add_run('text with emphasis.', 'Emphasis')
    paragraph = document.add_paragraph('Normal text, ')
    run = paragraph.add_run('text with emphasis.')
    run.style = 'Emphasis'
    # except you don't have a reference to `run` afterward
    # items = (
    #     (7, '1024', 'Plush kittens'),
    #     (3, '2042', 'Furbees'),
    #     (1, '1288', 'French Poodle Collars, Deluxe'),
    # )
    # table.add_row()
    # heading_cells = table.rows[2].cells
    # heading_cells[0].text = 'Qty'
    # heading_cells[1].text = 'SKU'
    # heading_cells[2].text = 'Description'
    # for item in items:
    #     cells = table.add_row().cells
    #     cells[0].text = str(item.qty)
    #     cells[1].text = item.sku
    #     cells[2].text = item.desc
    # row = table.add_row()
    document.save('a.docx')
    doc=MDoc()
    doc.createFile('b.docx')
    doc.add_paragraph('tttttttttttttttttttt')
    doc.close()
    pass


if __name__ == '__main__':
    run()
    pass
