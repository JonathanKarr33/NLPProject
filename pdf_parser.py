import os
import re
from pdfminer.high_level import extract_text
# pip install pdfminer-six

# papers from https://arxiv.org/list/cs.AI/recent

# Define the input and output folders
pdf_folder = 'data/short/pdfs'
entire_paper_folder = 'data/short/entire_paper'
abstract_folder = 'data/short/abstracts'
main_paper_folder = 'data/short/main_paper'

# Ensure the output folder exists, create it if not
if not os.path.exists(entire_paper_folder):
    os.makedirs(entire_paper_folder)
if not os.path.exists(abstract_folder):
    os.makedirs(abstract_folder)
if not os.path.exists(main_paper_folder):
    os.makedirs(main_paper_folder)

# Initialize a counter for the converted PDFs
converted_count = 0

# Regular expressions to identify the start and end of the abstract and introduction sections
abstract_start_pattern = re.compile(r'\babstract\b', re.IGNORECASE)
introduction_pattern = re.compile(r'\bintroduction\b', re.IGNORECASE)

# Iterate through the PDF files in the input folder
already_done = ["2310.08569", "2312.03758", "2312.04318", "2312.04379","2312.04479"] #! need to skip these as these have been cleaned already
for root, _, files in os.walk(pdf_folder):
    for file in files:
        if file[:-4] in already_done:
            print("Skipping", file[:-4])
            continue
        if file.endswith('.pdf'):
            pdf_file_path = os.path.join(root, file)
            # Extract text from the PDF
            text = extract_text(pdf_file_path)

            # Find the positions of "abstract" and "introduction"
            abstract_start_match = abstract_start_pattern.search(text)
            introduction_match = introduction_pattern.search(text)

            if abstract_start_match and introduction_match:
                # If both "abstract" and "introduction" are found
                # Create the abstract text that ends before "introduction"
                abstract_text = text[abstract_start_match.start(
                ):introduction_match.start()]

                # Create a corresponding "abstract" text file in the output folder
                abstract_file_path = os.path.join(
                    abstract_folder, os.path.splitext(file)[0] + '.txt')
                with open(abstract_file_path, 'w', encoding='utf-8') as abstract_file:
                    abstract_file.write(abstract_text)

                # Create the "rest_of_paper" starting with "introduction"
                rest_of_paper_text = text[introduction_match.start():]

                # stop at conclusion
                conclusion_pattern = re.compile(
                    r'\b[C][Oo][Nn][Cc][Ll][Uu][Ss][Ii][Oo][Nn]\b')
                references_pattern = re.compile(
                    r'\b[R][Ee][Ff][Ee][Rr][Ee][Nn][Cc][Ee][Ss]\b')
                conclusion_match = conclusion_pattern.search(
                    rest_of_paper_text)
                references_match = references_pattern.search(
                    rest_of_paper_text)
                if conclusion_match:
                    rest_of_paper_text = rest_of_paper_text[:conclusion_match.start(
                    )]
                elif references_match:
                    rest_of_paper_text = rest_of_paper_text[:references_match.start(
                    )]
                # Create a corresponding "rest_of_paper" text file in the output folder
                rest_of_paper_file_path = os.path.join(
                    main_paper_folder, os.path.splitext(file)[0] + '.txt')
                with open(rest_of_paper_file_path, 'w', encoding='utf-8') as rest_of_paper_file:
                    rest_of_paper_file.write(rest_of_paper_text)

            # Create a corresponding text file containing the entire paper
            text_file_path = os.path.join(
                entire_paper_folder, os.path.splitext(file)[0] + '.txt')
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            # Increment the counter for converted PDFs
            converted_count += 1

# Print the total number of converted PDFs
print(f"PDF to text conversion complete. {converted_count} PDFs converted.")
