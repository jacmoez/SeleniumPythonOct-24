from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

data = [
    ["Header 1", "Header 2", "Header 3"],
    ["Row 1 col 1", "Row 1 col 2", "Row 1 Col 3"],
    ["Row 2 col 1", "Row 2 col 2", "Row 2 Col 3"],
    ["Row 3 col 1", "Row 3 col 2", "Row 3 Col 3"]
]


def pdf(pdf_file= "test.pdf"):
    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    table = Table(data)
    table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1), 1, colors.brown)
    ]))
    elements = [table]
    doc.build(elements)


pdf()
