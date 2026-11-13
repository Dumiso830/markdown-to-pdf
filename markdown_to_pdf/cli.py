#!/usr/bin/env python
import argparse
import markdown2pdf

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('input', help='Markdown file to convert')
    parser.add_argument('output', help='Output PDF file')
    args = parser.parse_args()
    markdown2pdf.convert(args.input, args.output)

if __name__ == '__main__':
    main()
