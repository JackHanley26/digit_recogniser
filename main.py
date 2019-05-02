import os
import kaggle

kaggle.api.authenticate()

comp = 'digit-recognizer'
files = ['train.csv', 'test.csv']
path = './data'

for file in files:
    if not os.path.exists(os.path.join(path, file)):
        kaggle.api.competition_download_file(competition=comp, file_name=file, path=path)


