from os import rename
import PyPDF2

pdfFile1 = open('combinedminutes.pdf',mode='rb')
pdfFile2 = open('combinedminutes.pdf',mode='rb')

reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader1.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

opfile = open('combinedms.pdf','wb')
writer.write(opfile)
opfile.close()
pdfFile1.close()
pdfFile2.close()