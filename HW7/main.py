from os.path import exists
from file_create import creating
from file_write import writing_scv
from file_write import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()

