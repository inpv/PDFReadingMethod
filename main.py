import re
import PyPDF2


def extract_pdf_info(file_path):
    # Open the PDF file and read it
    pdf_info = {}
    text_dict = {}
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Count the number of pages
    pdf_info['TotalPages'] = len(pdf_reader.pages)

    # Extract text from each page
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # Stripping the list of multiple spaces and according to the needed delimiters
    text = re.split('[:\n]', re.sub(' +', ' ', text))

    # Transforming the split list into dict, while getting rid of leading and trailing whitespaces
    for word in range(0, len(text)-1, 2):
        text_dict[text[word].lstrip().rstrip()] = text[word + 1].lstrip().rstrip()

    # Removing empty items and splitting other items where necessary
    for key, value in dict(text_dict).items():
        if value == '' or key == '':
            del text_dict[key]

    pdf_info['Text'] = text_dict
    pdf_file.close()

    return pdf_info


if __name__ == '__main__':
    pdf_file_path = '~/Downloads/test_task.pdf'  # example location
    result = extract_pdf_info(pdf_file_path)
    print(result)
