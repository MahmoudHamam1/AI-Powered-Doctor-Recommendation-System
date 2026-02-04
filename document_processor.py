import PyPDF2
import docx

class DocumentProcessor:
    def extract_text(self, file):
        try:
            if file.name.endswith('.pdf'):
                return self._extract_pdf(file)
            elif file.name.endswith('.docx'):
                return self._extract_docx(file)
            elif file.name.endswith('.txt'):
                return file.read().decode('utf-8')
        except Exception as e:
            print(f"Error extracting text: {e}")
            return ""
        return ""
    
    def _extract_pdf(self, file):
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    
    def _extract_docx(self, file):
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])
