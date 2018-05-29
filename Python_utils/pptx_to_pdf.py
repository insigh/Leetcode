import comtypes.client

from PyPDF2 import PdfFileMerger
import fnmatch
import os


def GetPptFiles(path):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.pptx'):
            matches.append(os.path.join(root, filename))
    return matches
def GetPdfFiles(path):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.pdf'):
            matches.append(os.path.join(root, filename))
    return matches


def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()


def merge_pdf(pdffiles,outpath):
    merger = PdfFileMerger()
    for pdf in pdffiles:
        try:
            merger.append(open(pdf, 'rb'))
        except:
            pass
    with open(outpath, 'wb') as fout:
        merger.write(fout)
    merger.close()


# PPTtoPDF(r"D:\coursera\Deep_learning\convolutional-neural-networks\01_foundations-of-convolutional-neural-networks\01_convolutional-neural-networks\01_computer-vision_C4W1L01_ComputerVision.pptx",r"D:\coursera\Deep_learning\convolutional-neural-networks\01_foundations-of-convolutional-neural-networks\01_convolutional-neural-networks\01_computer-vision_C4W1L01_ComputerVision.pdf")

if __name__=="__main__":
    path= r"D:\coursera\Deep_learning"
    out_path=r"D:\coursera\Deep_learning\MergedPdf.pdf"
    # ppt_files=GetPptFiles(path)
    # print(len(ppt_files))
    # i=0
    # for item in ppt_files:
    #     output_file=str(item)[:-4]+'pdf'
    #     item = str(item)
    #     print(item)
    #     print(output_file)
    #     try:
    #         PPTtoPDF(item,output_file)
    #     except:
    #         pass
    #     i+=1
    #     print(i)

    pdf_files=GetPdfFiles(path)
    print(len(pdf_files))
    # for item in pdf_files:
    merge_pdf(pdffiles=pdf_files,outpath=out_path)

