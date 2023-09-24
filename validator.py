from extractor import Extractor
from deepdiff import DeepDiff


class Validator:

    @staticmethod
    def check_pdf_structure(original_file_path, testing_file_path):
        original_dict = Extractor.extract_pdf_info(original_file_path)
        testing_dict = Extractor.extract_pdf_info(testing_file_path)

        diff = DeepDiff(original_dict, testing_dict)
        return diff
