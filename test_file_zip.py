from os.path import basename
from zipfile import ZipFile
import os
import csv

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

def test_create_archive():
    files = os.listdir(path)
    with ZipFile('resources/info.zip', 'w') as zip_file:
        for file in files:
            file_name = os.path.join(path, file)
            zip_file.write(file_name, basename(file_name))






