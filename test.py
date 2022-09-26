from general_toolkit import doc2html,doc2pdf,doc_tools
import os
def test1():
    x = doc_tools.scan_doc_from_image("D:\\HandGestures\\images\\cards.jpg", [[327,207],[556,273],[461,591],[237,526]],verbose=False, w=100, h=100)
    print(x)
def test2():
    directory = 'D:\\General toolkit'
    for filename in os.listdir(directory):
        if filename.endswith("doc"):
            print(filename)
            doc2pdf.convertingpdf(directory+"\\"+filename, ".doc")
        elif filename.endswith("docx"):
            print(filename)
            doc2pdf.convertingpdf(directory+"\\"+filename, ".docx")
def test3():
    directory = 'D:\\Python'
    for filename in os.listdir(directory):
        if filename.endswith("doc"):
            print(filename)
            doc2pdf.convert2html(directory+"\\"+filename, ".doc")
        elif filename.endswith("docx"):
            print(filename)
            doc2html.convert2html(directory+"\\"+filename, ".docx")
test3()