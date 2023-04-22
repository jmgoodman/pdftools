from PyPDF2 import PdfWriter, PdfReader
import sys, os



def pdfmerger(docnames):
    output = PdfWriter()

    for i in range(len(docnames[1:])):
        docname = docnames[i+1]

        inputpdf = PdfReader(open(docname, "rb"))

        for j in range(len(inputpdf.pages)):
            output.add_page(inputpdf.pages[j])

    docname = docnames[0]
    with open(docname, "wb") as outputStream:
        output.write(outputStream)

def main(argv):
    try:
        docnames = argv[1:]
        pdfmerger(docnames)
    except getopt.GetoptError:
        print('python -m pdfSplitter <filename-to-write> <filename-to-merge> <filename-to-merge> ...')
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv)