import requests
import os
import os.path
import sys

# tested with Python 3.5.2 on Ubuntu 16.04 (AMD64)
# pip install requests may be needed

OUTPUT_POSTFIX='.json'

def tagpos(input_file, output_file):
    for line in input_file:
        r = requests.post('http://localhost:9000?properties={%22annotators%22%3A%22tokenize%2Cssplit%2Cpos%2Cparse%22%2C%22outputFormat%22%3A%22json%22}', data=line)
        tags = r.text
        print(tags, file=output_file)

def tagpos_dir(input_dir, output_dir):
    # remove path of directory
    input_filenames = [filename for filename in
                       os.listdir(input_dir)
                       if os.path.isfile(os.path.join(input_dir, filename))]

    for input_filename in input_filenames:
        input_path = os.path.join(input_dir, input_filename)
        output_path = os.path.join(output_dir, input_filename) + OUTPUT_POSTFIX
        print("Tagging " + input_path, file=sys.stderr)
        with open(input_path) as fi:
            with open(output_path, 'w') as fo:
                tagpos(fi, fo)

if len(sys.argv) != 3:
    print("Usage: python " + sys.argv[0] + " <input directory> <output directory>")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = sys.argv[2]

tagpos_dir(input_dir, output_dir)
