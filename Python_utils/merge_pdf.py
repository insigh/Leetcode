# -*- encoding:utf-8 -*-

from PyPDF2 import PdfFileMerger
import fnmatch
import os
path= r"D:\coursera\Deep_learning"
matches = []
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.pdf'):
        matches.append(os.path.join(root, filename))
merger = PdfFileMerger()

for pdf in matches:
    try:
        merger.append(open(pdf, 'rb'))
    except:
        pass

with open('nlp-sequence-models.pdf', 'wb') as fout:
    merger.write(fout)
merger.close()