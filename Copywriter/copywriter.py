import argparse
import re as regex
import sys

"""
Replace the copyright header in a sourcecode file with a new one using a template
A file named 'template' must be defined in the same directory as this file
Usage: python copywriter.py <file>
"""

def fill_template(template_data, file_name):
    #add more template variables as needed
    filename_parts = regex.split("\/", file_name)
    short_filename = regex.sub("\.[a-zA-Z]+", "", filename_parts[-1])
    return regex.sub("\{FILENAME\}", short_filename, template_data)

def load_copyright_template(file_name):
    with open('template', 'r') as infile:
        template_data = infile.read()
    return fill_template(template_data, file_name)

def load_file_data(file_name):
    with open(file_name, 'r') as infile:
        file_data = infile.read()
    return file_data

def strip_copyright_block(file_data):
    #search for "Copyright" and "all rights reserved"
    #ignores case
    return regex.sub("\/\*[^/]*[Cc]opyright[\S\s]*[Aa]ll\s[Rr]ights\s[Rr]eserved[^/]*\*\/", "", file_data)

def write_output(output_data, output_file):
    with open(output_file, 'w') as outfile:
        outfile.write(output_data)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File needing a copyright block")
    parser.add_argument("-n", "--nostrip", help="Omit stripping existing copyright block", action="store_true")
    return parser.parse_args()

def main():
    args = parse_args()
    file_name = args.filename
    template_data = load_copyright_template(file_name)
    file_data = load_file_data(file_name)
    if not args.nostrip:
        file_data = strip_copyright_block(file_data)
    write_output(template_data + file_data, file_name)

if __name__ == "__main__":
    main()
