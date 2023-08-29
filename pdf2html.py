import pdfplumber
from bs4 import BeautifulSoup
import sys

def pdf_to_html(pdf_path, html_path):
    with pdfplumber.open(pdf_path) as pdf:
        soup = BeautifulSoup('<html><head><style>.pdf-text { position: absolute; }</style></head><body></body></html>', 'html.parser')
        body = soup.body

        for i, page in enumerate(pdf.pages):
            page_div = soup.new_tag("div", style=f"position: relative; width: {page.width}pt; height: {page.height}pt;")
            body.append(page_div)
            
            for char in page.extract_words():
                left = char['x0']
                top = char['top']
                text = char['text']
                
                span = soup.new_tag("span", **{"class": "pdf-text", "style": f"left: {left}pt; top: {top}pt;"})
                span.string = text
                page_div.append(span)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py pdf_path html_path")
        sys.exit(1)
    pdf_to_html(sys.argv[1], sys.argv[2])
