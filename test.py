from dip_toolkit import doc_tools

x = doc_tools.scan_doc_from_image("D:\\HandGestures\\images\\cards.jpg", [[327,207],[556,273],[461,591],[237,526]],verbose=False, w=100, h=100)
print(x)