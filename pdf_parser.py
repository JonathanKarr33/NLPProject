import os
from pdfminer.high_level import extract_text

# Define the input and output folders
pdf_folder = 'data/pdfs'
text_folder = 'data/text'

# Ensure the output folder exists, create it if not
if not os.path.exists(text_folder):
    os.makedirs(text_folder)

# Iterate through the PDF files in the input folder
for root, _, files in os.walk(pdf_folder):
    for file in files:
        if file.endswith('.pdf'):
            pdf_file_path = os.path.join(root, file)
            # Extract text from the PDF
            text = extract_text(pdf_file_path)
            # Create a corresponding text file in the output folder
            text_file_path = os.path.join(text_folder, os.path.splitext(file)[0] + '.txt')
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

print("PDF to text conversion complete.")
