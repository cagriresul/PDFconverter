from pdf2docx import Converter

pdf_dosyası= "Manchester United Level -3.pdf"

docx_dosyası = "output.docx"

cv = Converter(pdf_file = pdf_dosyası)
cv.convert(docx_dosyası)
cv.close()


