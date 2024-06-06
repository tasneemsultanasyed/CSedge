import PyPDF2

# Merge PDF files
def merge_pdfs(pdfs, output_file):
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf in pdfs:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_file, 'wb') as fh:
        pdf_writer.write(fh)

# Split PDF file
def split_pdf(input_file, output_prefix):
    pdf_reader = PyPDF2.PdfFileReader(input_file)
    num_pages = pdf_reader.getNumPages()
    for page in range(num_pages):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        output_file = f"{output_prefix}_{page+1}.pdf"
        with open(output_file, 'wb') as fh:
            pdf_writer.write(fh)

# Example usage
pdfs_to_merge = ['mad.pdf', 'Ai.pdf', 'CC.pdf']
# pdf_splitter.py
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}page{}.pdf'.format(
            fname, page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

if _name=='main_':
    path = 'w9.pdf'
    pdf_splitter(path)
    output_file = 'erged.pdf'
merge_pdfs(pdfs_to_merge, output_file)

input_file = 'input.pdf'
output_prefix = 'plit'
split_pdf(input_file,output_prefix)
          