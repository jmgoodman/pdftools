from PyPDF2 import PdfWriter, PdfReader
import sys, os



def pdfsplitter(docname):
    inputpdf = PdfReader(open(docname, "rb"))
    noext,_  = os.path.splitext(docname)

    for i in range(len(inputpdf.pages)):
        output = PdfWriter()
        output.add_page(inputpdf.pages[i])
        with open(f"{noext}-page{i}.pdf", "wb") as outputStream:
            output.write(outputStream)

def main(argv):
    try:
        docname = argv[1]
        pdfsplitter(docname)
    except:
        print('usage: pdfSplitter.py <filename>')
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv)