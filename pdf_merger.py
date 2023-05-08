import sys
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs_alternating(pdf1_path, pdf2_path, output_path):
    pdf1 = PdfReader(pdf1_path)
    pdf2 = PdfReader(pdf2_path)
    output_pdf = PdfWriter()

    max_pages = max(len(pdf1.pages), len(pdf2.pages))

    for i in range(max_pages):
        if i < len(pdf1.pages):
            output_pdf.add_page(pdf1.pages[i])

        if i < len(pdf2.pages):
            output_pdf.add_page(pdf2.pages[i])

    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python pdf_merger.py <pdf1> <pdf2> <output>")
        sys.exit(1)

    pdf1_path = sys.argv[1]
    pdf2_path = sys.argv[2]
    output_path = sys.argv[3]

    merge_pdfs_alternating(pdf1_path, pdf2_path, output_path)
