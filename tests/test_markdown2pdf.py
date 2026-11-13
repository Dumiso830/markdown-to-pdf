import unittest
from markdown_to_pdf.markdown2pdf import convert

class TestMarkdown2Pdf(unittest.TestCase):
    def test_convert(self):
        self.assertTrue(convert('test.md', 'test.pdf'))
