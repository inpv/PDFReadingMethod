import PyPDF2


class Validator:

    @staticmethod
    def check_pdf_structure(filename, original_dict):
        required_elements = [key for key in original_dict]
        missing_elements = []

        with open(filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text = page.extract_text()

                for element in required_elements:
                    if element not in text:
                        missing_elements.append(element)

        if not missing_elements:
            print("All elements are present and in compliance with the structure.")
        else:
            print("Missing elements or structure non-compliance:")
            for element in missing_elements:
                print("- " + element)
