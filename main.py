from validator import Validator


def main():
    result = Validator.check_pdf_structure('~/Downloads/test_task.pdf',
                                           '~/Downloads/test_task (copy 1).pdf')  # example locations
    if result == {}:
        result = "The files are identical."
    else:
        print("The files are NOT identical, see below:")

    print(result)


if __name__ == '__main__':
    main()
