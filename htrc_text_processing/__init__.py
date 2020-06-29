import glob
import os
import shutil
from zipfile import ZipFile


def get_zips_only(data_dir, output_dir):
    if os.path.isdir(data_dir):
        if not os.path.isdir(output_dir):
            try:
                os.mkdir(output_dir)
            except OSError:
                print("Creation of the directory %s failed" % output_dir)
            else:
                print("Successfully created the directory %s " % output_dir)

        for x in glob.glob(data_dir + '/**/*.zip', recursive=True):
            # print(x)
            shutil.copy(x, output_dir)
    else:
        raise Exception(data_dir + ' path does not exists!')


def get_zips_extract(data_dir, output_dir):
    if os.path.isdir(data_dir):
        if not os.path.isdir(output_dir):
            try:
                os.mkdir(output_dir)
            except OSError:
                print("Creation of the directory %s failed" % output_dir)
            else:
                print("Successfully created the directory %s " % output_dir)

        for x in glob.glob(data_dir + '/**/*.zip', recursive=True):
            # print(x)
            with ZipFile(x, 'r') as zipObj:
                zipObj.extractall(output_dir)
    else:
        raise Exception(data_dir + ' path does not exists!')


def unzip_file(file_name):
    with ZipFile(file_name, 'r') as zipObj:
        zipObj.extractall()