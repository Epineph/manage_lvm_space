#!/usr/bin/env python3

import os
import sys
from fpdf import FPDF

def list_large_folders(directory="."):
    folder_sizes = []
    for root, dirs, files in os.walk(directory):
        size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        folder_sizes.append((root, size))
    folder_sizes.sort(key=lambda x: x[1], reverse=True)
    return folder_sizes[:20]

def generate_pdf_report(folder_sizes, output="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for folder, size in folder_sizes:
        pdf.cell(200, 10, txt=f"{folder}: {size} bytes", ln=True)
    
    pdf.output(output)

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    folder_sizes = list_large_folders(directory)
    generate_pdf_report(folder_sizes)
