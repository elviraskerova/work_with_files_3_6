import zipfile
from os.path import basename
from zipfile import ZipFile
import os
import glob

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')


 # создание зип
def test_create_archive():
    files = os.listdir(path)
    with ZipFile('resources/info.zip', 'w') as zip_file:
        for file in files:
            file_name = os.path.join(path, file)
            zip_file.write(file_name, basename(file_name))

#распаковка зип
# extract_dir = 'extract_dir'
#
# with zipfile.ZipFile('resources/info.zip') as zf:
#     zf.extractall(extract_dir)
#
# for file in glob.glob(extract_dir + '/**', recursive=True):
#     print(file)


    # Чтение и проверка pdf
def test_read_pdf():
    my_zipfile = ZipFile(path)
    with zipfile.ZipFile(path) as zf:
        r_pdf = my_zipfile.extract('PDF_file.pdf')
        reader1 = PdfReader(r_pdf)
        text = reader1.pages[0].extract_text()
        print(text)
        assert 'Пример pdf' in text
        os.remove(r_pdf)


    # Чтение и проверка csv
def test_read_csv():
    my_zipfile = ZipFile(path)
    text = str(my_zipfile.read('csv_file.csv'))
    print(text)
    assert 'Hello World' in text


    # Чтение и проверка xlsx
def test_read_xlsx():
    my_zipfile = ZipFile(path)
    workbook = my_zipfile.extract('xlsx_file.xlsx')
    xlsx_book = load_workbook(workbook)
    sheet = xlsx_book.active
    print(sheet.cell(row=1, column=1).value)
    assert 'Desktop' in sheet.cell(row=1, column=1).value
    os.remove(workbook)





