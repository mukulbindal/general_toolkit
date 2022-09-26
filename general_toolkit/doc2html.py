import mammoth
import os

def convert2html(filepath,doctype):
    try:
        in_file=os.path.abspath(filepath)
        f = open(in_file, 'rb')
        output=filepath.replace(doctype,r".html")
        out_file = os.path.abspath(output)
        b = open(out_file, 'wb')
        document = mammoth.convert_to_html(f)
        b.write(document.value.encode('utf8'))
        f.close()
        b.close()
        print("Completed")
    except Exception as e:
        print("Something went wrong",e)
