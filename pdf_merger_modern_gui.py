import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk
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

def select_pdf1():
    pdf1_path.set(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))
    
def select_pdf2():
    pdf2_path.set(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))
    
def save_output():
    output_path.set(filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]))

def merge_pdfs():
    if pdf1_path.get() and pdf2_path.get() and output_path.get():
        merge_pdfs_alternating(pdf1_path.get(), pdf2_path.get(), output_path.get())
        result_label.config(text="PDFs erfolgreich verbunden!")
    else:
        result_label.config(text="Bitte wähle beide PDFs und einen Speicherort aus.")

root = ThemedTk(theme="arc")
root.title("PDF Merger")

pdf1_path = tk.StringVar()
pdf2_path = tk.StringVar()
output_path = tk.StringVar()

style = ttk.Style()
style.configure("TButton", padding=(0, 5, 0, 5), font='helvetica 10')

tk.Label(root, text="PDF 1:").grid(row=0, column=0, sticky="e", padx=(10, 5), pady=(10, 5))
ttk.Entry(root, textvariable=pdf1_path, width=50).grid(row=0, column=1, padx=(0, 5), pady=(10, 5))
ttk.Button(root, text="Auswählen", command=select_pdf1).grid(row=0, column=2, padx=(0, 10), pady=(10, 5))

tk.Label(root, text="PDF 2:").grid(row=1, column=0, sticky="e", padx=(10, 5), pady=(0, 5))
ttk.Entry(root, textvariable=pdf2_path, width=50).grid(row=1, column=1, padx=(0, 5), pady=(0, 5))
ttk.Button(root, text="Auswählen", command=select_pdf2).grid(row=1, column=2, padx=(0, 10), pady=(0, 5))

tk.Label(root, text="Ausgabe:").grid(row=2, column=0, sticky="e", padx=(10, 5), pady=(0, 5))
ttk.Entry(root, textvariable=output_path, width=50).grid(row=2, column=1, padx=(0, 5), pady=(0, 5))
ttk.Button(root, text="Speichern unter", command=save_output).grid(row=2, column=2, padx=(0, 10), pady=(0, 5))

ttk.Button(root, text="PDFs verbinden", command=merge_pdfs).grid(row=3, column=1, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1)

root.mainloop()
