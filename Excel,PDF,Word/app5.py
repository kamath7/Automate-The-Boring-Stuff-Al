import docx

d = docx.Document('./demo.docx')
print(d.paragraphs[0].text)
