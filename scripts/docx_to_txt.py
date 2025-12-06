from docx import Document
import sys
import os

def docx_to_txt(docx_path, txt_path):
    try:
        document = Document(docx_path)
        with open(txt_path, 'w', encoding='utf-8') as f:
            for paragraph in document.paragraphs:
                f.write(paragraph.text + '\n')
        print(f"Successfully converted '{docx_path}' to '{txt_path}'")
    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_txt.py <input_docx_path> <output_txt_path>")
        sys.exit(1)
    
    input_docx_path = sys.argv[1]
    output_txt_path = sys.argv[2]
    docx_to_txt(input_docx_path, output_txt_path)
