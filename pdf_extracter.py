import sys
import argparse
import PyPDF2  


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pdf', metavar="file", type=str, nargs='+',
                        help='The pdf to extract page from')
    parser.add_argument('-n', dest = 'numbers', metavar="page numbers", type=str, nargs='+',
                        help='the pages to be extracted')
    parser.add_argument('-o', dest='out', type=str, default="result", help='the output file name (default to result)')

    args = parser.parse_args()

    pdf = args.pdf
    numbers = args.numbers
    numbers = [int(x) for x in numbers]
    print("extract page ", numbers, "from " , pdf)


    pdf = PyPDF2.PdfFileReader(pdf[0], strict = False)
    pdf_writer = PyPDF2.PdfFileWriter()
    for nb_page in numbers:
        current_page = pdf.getPage(nb_page-1)
        pdf_writer.addPage(current_page)
    output_filename = args.out
    with open(output_filename,'wb') as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    # execute only if run as a script
   
    main()
