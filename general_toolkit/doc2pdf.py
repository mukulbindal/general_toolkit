
# -*- coding: utf-8 -*-
"""
@author: prakhar newatia
"""

import win32com.client as client
import os
# this fuction convert each doc/docx to pdf inside a particular folder


def convertingpdf(filepath, val):
    try:
        # DispatchEx opens a new instance (an entirely new .exe)
        word = client.DispatchEx("Word.Application")
        in_file = os.path.abspath(filepath)
        output = filepath.replace(val, r".pdf")
        out_file = os.path.abspath(output)
        doc = word.Documents.Open(in_file)
        print('Exporting', out_file)
        # fileformat is the format for the pdf conversion
        doc.SaveAs(out_file, FileFormat=17)
        doc.Close()
        word.Quit()
    except Exception as e:
        print("some error is coming", e)
    print("done")



