import unittest
from markdown_to_pdf.cli import main


class TestCLIModule(unittest.TestCase):
    def test_cli(self):
        self.assertTrue(main())
