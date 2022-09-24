from general_toolkit import doc_tools,doc2pdf
import os
x = doc_tools.scan_doc_from_image("D:\\HandGestures\\images\\cards.jpg", [[327,207],[556,273],[461,591],[237,526]],verbose=False, w=100, h=100)
print(x)

directory = 'D:\\General toolkit'
for filename in os.listdir(directory):
    if filename.endswith("doc"):
        print(filename)
        doc2pdf.convertingpdf(directory+"\\"+filename, ".doc")
    elif filename.endswith("docx"):
        print(filename)
        doc2pdf.convertingpdf(directory+"\\"+filename, ".docx")