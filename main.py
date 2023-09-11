import io
from validator import Validator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


class Extractor:
    result_dict = {}
    device = None

    @staticmethod
    def pdf_to_text(path):
        resource_manager = PDFResourceManager()
        text_stream = io.StringIO()
        laparams = LAParams()
        Extractor.device = TextConverter(resource_manager, text_stream, laparams=laparams)

        with open(path, 'rb') as pdf_file:
            interpreter = PDFPageInterpreter(resource_manager, Extractor.device)

            for page in PDFPage.get_pages(pdf_file, check_extractable=True):
                interpreter.process_page(page)

        text = text_stream.getvalue()

        Extractor.device.close()
        text_stream.close()

        return text

    @staticmethod
    def extract_pdf_info(file_path):
        pdf_text = Extractor.pdf_to_text(file_path)

        lines = pdf_text.split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                Extractor.result_dict[key.strip()] = value.strip()

        return Extractor.result_dict


if __name__ == '__main__':
    pdf_file_path = '~/Downloads/test_task.pdf'  # example location
    result = Extractor.extract_pdf_info(pdf_file_path)
    print(result)

    Validator.check_pdf_structure(pdf_file_path, Extractor.result_dict)
