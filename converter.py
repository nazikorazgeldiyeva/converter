import PyPDF2  
  
pdf_path = "v0.3-JJ-ColgatePalmolive-Dialexa-Overview.pdf"  
page_contents = []  
  
with open(pdf_path, "rb") as pdf_file:  
    read_pdf = PyPDF2.PdfReader(pdf_file)  
    number_of_pages = len(read_pdf.pages)  
      
    for page in read_pdf.pages:  
        page_content = page.extract_text()  
        page_contents.append(page_content)  
  
print(page_contents)  