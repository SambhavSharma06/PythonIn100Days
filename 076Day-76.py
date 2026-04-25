# Exercise 8 - Merge the PDF in Python!!
from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# List of PDF files in order
pdf_files = [
    "1.CV.pdf",
    "2. Customer Invoice (Paid).pdf",
    "3. Customer Invoice.pdf"
]

# Append each PDF
for pdf in pdf_files:
    merger.append(pdf)

# Write merged output
merger.write("merged_output.pdf")
merger.close()

print("PDFs merged successfully into 'merged_output.pdf'")
