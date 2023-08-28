import pdfplumber
from bs4 import BeautifulSoup

def pdf_to_html(pdf_path, html_path):
    with pdfplumber.open(pdf_path) as pdf:
        soup = BeautifulSoup('<html><body></body></html>', 'html.parser')
        body = soup.body

        for page in pdf.pages:
            text = page.extract_text()
            div = soup.new_tag("div", style="page-break-before: always;")
            div.string = text
            body.append(div)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    pdf_to_html("sample.pdf", "output.html")
