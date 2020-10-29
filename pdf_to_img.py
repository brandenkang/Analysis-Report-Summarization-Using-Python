import PyPDF2
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import pdftotext
import pathlib
import glob

file_path = '/Users/BrandenKang/Document-AI/trial_000.pdf'

def pdf2text(file_path): 
    count=0 
    for pdf_file in pathlib.Path(file_path):
    # for pdf_file in pathlib.Path('/Users/BrandenKang/Desktop/analysis_samples_all/samples').glob('*.pdf'):
        with open(pdf_file,"rb") as f: 
            count+=1 
            pdf = pdftotext.PDF(f)
            new_file = "%s.text" % ("sample_" + str(count))
            file_ = open(new_file,'w')
            for page in pdf: 
                file_.write(page)
            return new_file
            file_.close()

def get_pdf(): 
    converted_pdf = convert_from_path(file_path)
    count=0
    two_pages = False 
    for img in converted_pdf: 
        count+=1 
        # new_file = "%s.jpg" % ("converted_" + str(count))
        # img.save(new_file,'JPEG')
        if count == 2: 
            new_file = pdf2text(file_path)
            with open(new_file,'rb') as f: 
                file_text = f.readlines() 
                i=0 
                for line in file_text: 
                    if i+1 < len(file_text):
                        i+=1 
                        if len(line.split(" ")) > 8: 
                            two_pages = True 
                            break 
            break 
    if two_pages == False:
        new_file = "%s.jpg" % ("converted_" + str(count))
        img.save(new_file,'JPEG')

get_pdf() 











# with open('2.pdf','rb') as fin:
#     pdf = PyPDF2.PdfFileReader(fin)
#     page = pdf.getPage(0)

#     # Coordinates found by inspection.
#     # Can these coordinates be found automatically?
#     page.cropBox.lowerLeft=(88,322)
#     page.cropBox.upperRight = (508,602)

#     output = PyPDF2.PdfFileWriter()
#     output.addPage(page)

#     with open('cropped-5.pdf','wb') as fo:
#         output.write(fo)


# ----------------------------------------------------------------------------------------------------------------------------- # 

# Now merge document2.pdf with cropped_document.pdf
# insert_tree_into_page('cropped_document.pdf', 'document2.pdf')


# from pathlib import Path
# from PyPDF2 import PdfFileReader, PdfFileWriter

# pdf_path = (
#     Path.home()
#     /"Document-AI/sample.pdf"
#     # "sample.pdf"
# )

# pdf_reader = PdfFileReader(str(pdf_path))
# first_page = pdf_reader.getPage(0)

# print(first_page.mediaBox)
