import unittest
from doctor_matcher import DoctorMatcher
from document_processor import DocumentProcessor

class TestDoctorMatcher(unittest.TestCase):
    def setUp(self):
        self.matcher = DoctorMatcher()
    
    def test_find_cardiology_doctors(self):
        doctors = self.matcher.find_doctors("Cardiology", "medium")
        self.assertEqual(len(doctors), 3)
        self.assertTrue(all(d["specialty"] == "Cardiology" for d in doctors))
    
    def test_low_price_preference(self):
        doctors = self.matcher.find_doctors("Dermatology", "low")
        self.assertEqual(len(doctors), 2)
        self.assertTrue(doctors[0]["price"] <= doctors[1]["price"])
    
    def test_high_price_preference(self):
        doctors = self.matcher.find_doctors("Neurology", "high")
        self.assertEqual(len(doctors), 2)
        self.assertTrue(doctors[0]["rating"] >= doctors[1]["rating"])

class TestDocumentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DocumentProcessor()
    
    def test_extract_txt(self):
        with open('test_files/sample_health_record.txt', 'rb') as f:
            f.name = 'test.txt'
            text = self.processor.extract_text(f)
            self.assertIn("chest pain", text.lower())
            self.assertIn("shortness of breath", text.lower())
    
    def test_extract_pdf(self):
        with open('test_files/dermatology_case.pdf', 'rb') as f:
            f.name = 'test.pdf'
            text = self.processor.extract_text(f)
            self.assertIn("dermatology", text.lower())
    
    def test_extract_docx(self):
        with open('test_files/orthopedic_report.docx', 'rb') as f:
            f.name = 'test.docx'
            text = self.processor.extract_text(f)
            self.assertIn("back pain", text.lower())

if __name__ == '__main__':
    unittest.main()
