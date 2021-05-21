import PyPDF2
import os 

pdfFile = open('./combinedminutes.pdf',mode='rb')
reader =  PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())