from PyPDF2 import PdfReader
'''
with open('LeitorPdf/arquivoteste.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Suponha que você queira extrair o texto da primeira página (índice 0)
    page = pdf_reader.pages[1]
    page_text = page.extract_text()

    print(page_text)
'''



# Nome do arquivo PDF que você deseja ler
pdf_file_path = 'LeitorPdf/arquivoteste.pdf'

def extract_text_from_pdf(pdf_file_path):
    # Open the PDF file in binary read mode
    pdf_reader = PdfReader(pdf_file_path)

    # Loop through the pages of the PDF and extract the text
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        print(page_text)

if __name__ == "__main__":
    extract_text_from_pdf(pdf_file_path)