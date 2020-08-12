from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage 
from pdfminer.converter import TextConverter,HTMLConverter, XMLConverter
from pdfminer.layout import LAParams
import io

pdf_path = 'D:\\isb superbrain\\warmupday5\\p1.pdf'
pdf=open(pdf_path,'rb')
mem=io.StringIO()

lp=LAParams()
rm=PDFResourceManager()
cnv=HTMLConverter(rm,mem,laparams = lp)
ip=PDFPageInterpreter(rm,cnv)

for i in PDFPage.get_pages(pdf):
	ip.process_page(i)
	text=mem.getvalue()

file = open("D:\\isb superbrain\\warmupday5\\p1.html",'wb')
file.write(text.encode('utf-8'))

print("DONE")