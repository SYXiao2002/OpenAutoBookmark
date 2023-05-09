import pypdf
from pypdf import PdfReader, PdfWriter
import re

# Open PDF file and get page object
pdf_file = open('example.pdf', 'rb')
reader = PdfReader(pdf_file)
num_pages = len(reader.pages)

# Define the regular expression for header levels
""" 
Default: header_regex = r"^(\d+\.){1,3}\s+([\w\s]+)"
Able to find string like 
    3. THE ACTIVITY RECOGNITION CHAIN
    3.1. Sensor Data Acquisition and Preprocessing
    3.2. Data Segmentation
    3.2.1. Sliding Window.
"""
header_regex = r"^(\d+\.){1,3}\s+([\w\s]+)"


# Create an empty list to store headers
headers = []

# Iterate over each page and search for headers
for page_num in range(num_pages):
    page = reader.pages[page_num]
    content = page.extract_text()
    lines = content.split('\n')
    for line in lines:
        # Match the header level regular expression
        match = re.match(header_regex, line)
        if match:
            # Extract header and page number information
            title_level = match.group(0).count(".")
            header = match.group()
            headers.append((header, title_level, page_num))

# Write header and page number information to a TXT file
with open('headers.txt', 'w') as f:
    for header, title_level, page_num in headers:
        f.write(f'{header} - Title Level {title_level} - Page {page_num}\n')

# Create a PDF writer object and add bookmarks
pdf_writer = PdfWriter()
for page in range(num_pages):
    pdf_writer.add_page(reader.pages[page])

for header, title_level, page in headers:
    # Add bookmarks based on header level
    if title_level == 1:
        level1_bookmark = pdf_writer.add_outline_item(title=header, page_number=page)
    elif title_level == 2:
        level2_bookmark = pdf_writer.add_outline_item(title=header, page_number=page, parent=level1_bookmark)
    elif title_level == 3:
        level3_bookmark = pdf_writer.add_outline_item(title=header, page_number=page, parent=level2_bookmark)

# Write to a new PDF file
with open('example_with_bookmarks.pdf', 'wb') as f:
    pdf_writer.write(f)

# Close file objects
pdf_file.close()
