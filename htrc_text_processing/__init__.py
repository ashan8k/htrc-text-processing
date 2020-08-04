# Main Library file
# by Ashan Liyanage

import glob
import os
import shutil
import sys
from zipfile import ZipFile
from pathlib import Path
# import warnings
from typing import List
from tqdm import tqdm
from htrc_text_processing.htrc.models import HtrcPage
from htrc_text_processing.htrc.runningheaders import parse_page_structure

CRED = '\033[91m'
CEND = '\033[0m'
CURL = '\33[4m'
CGREEN = '\33[32m'
CGREY = '\33[100m'
CBLINK = '\33[5m'


def unzip_file(file_name):
    with ZipFile(file_name, 'r') as zipObj:
        zipObj.extractall()


def error_message(msg):
    sys.exit(CRED + msg + CEND)


def get_zips(data_dir, output_dir, cmd='x'):
    data_path = Path(data_dir)
    output_path = Path(output_dir)
    if data_path.exists():  # Checking the given input part
        # print(file_path.name)
        if output_path.exists():
            raise Exception(output_dir + ' is Already created. please delete it or give me a different path')
        else:
            try:
                os.mkdir(output_path.parent / output_path.name)

            except OSError:
                raise Exception("Creation of the directory %s failed" % output_dir +
                                "\n* Possible reason there's no \'" + str(output_path.parent) + "\' folder")
            else:
                print("Successfully created the directory \'%s\' " % output_dir)

            for x in tqdm(glob.glob(data_dir + '/**/*.zip', recursive=True)):
                # print(x)
                if cmd == 'x':
                    with ZipFile(x, 'r') as zipObj:
                        zipObj.extractall(output_path.parent / output_path.name)

                    # for meta data xml
                    x_data = Path(x)
                    xml_path = x_data.parent / x_data.name.replace('.zip', '.mets.xml')
                    folder_name = x_data.name.replace('.zip', '')
                    if xml_path.exists():
                        shutil.copy(xml_path, output_path / folder_name)
                    else:
                        print("missing xml:" + str(xml_path))
                else:
                    shutil.copy(x, output_dir)
    else:
        raise Exception(data_dir + ' path does not exists!')


def rename_file(file_path):
    fname = file_path.name.split("_")[-1]
    file_path_replace = file_path.parent / (
            ''.join([char * (12 - len(str(fname))) for char in '0']) + str(fname))
    os.rename(file_path, file_path_replace)


def clean_txt_file_names(file):
    file_path = Path(file)
    if file_path.exists() and file_path.is_file():
        if '.txt' in str(file_path):
            # print(file_path.name)
            rename_file(file_path)
        else:
            error_message("Not a txt file\nInvalid txt file: " + str(file_path))

    elif file_path.exists() and file_path.is_dir():
        # print('dir')
        for x in tqdm(glob.glob(str(file_path) + '/*.txt', recursive=True)):
            # print(x)
            x_path = Path(x)
            rename_file(x_path)
    else:
        error_message("Path/File not exists. Path = " + str(file_path))


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def normalize_txt_file_names(dir_or_file):
    dir_or_file_path = Path(dir_or_file)
    if dir_or_file_path.exists() and dir_or_file_path.is_dir():
        print('txt file name cleaning started!')
        clean_txt_file_names(dir_or_file_path)
        print('txt file name cleaning done!')
        txt_files = []
        for x in (glob.glob(str(dir_or_file_path) + '/*.txt', recursive=True)):
            x_path = Path(x)
            txt_file_name = x_path.name.split(".")[0]
            if is_integer(txt_file_name):
                # print(txt_file_name)
                txt_files.append(txt_file_name)
            else:
                print("Invalid txt file format \nInvalid txt file: " + str(x_path))

        if not txt_files:
            error_message("No txt filed found in " + str(dir_or_file_path) +
                          "\nPlease give a directory which have txt files")

        ll = [int(j) for j in txt_files]
        ll = sorted(ll)
        # print(ll)
        count = ll[0]
        renamed_list = []
        for i in tqdm(ll):
            if count != i:
                file_path = dir_or_file_path / (''.join([char * (8 - len(str(i))) for char in '0']) + str(i) + ".txt")
                file_path_replace = dir_or_file_path / (
                        ''.join([char * (8 - len(str(count))) for char in '0']) + str(count) + ".txt")
                os.rename(file_path, file_path_replace)
                renamed_list.append(
                    str(file_path) + CBLINK + " -> " + CEND + CGREEN + str(file_path_replace) + CEND)
                # print(file_path, file_path_replace)
                # print(str(dir_path) + "/" + i + "," + str(dir_path) + "/" + ''.join(
                #    [char * (len(ll[0]) - len(str(count))) for char in '0']) + str(count))
            count += 1

        if not renamed_list:
            print("No normalization is needed!")
        else:
            print("Normalized files")
            print("\n".join(renamed_list))

    elif dir_or_file_path.exists() and dir_or_file_path.is_file():
        print('txt file name cleaning started!')
        clean_txt_file_names(dir_or_file)
        print('txt file name cleaning done!')
    else:
        error_message("Directory/File not exists !!!. \nDirectory/File Path = " + str(dir_or_file_path))


def load_vol(path: str, num_pages: int) -> List[HtrcPage]:
    pages = []
    py_num_pages = num_pages - 1
    for n in range(py_num_pages):
        if n == 0:
            n = 1
            page_num = str(n).zfill(8)
            with open('{}/{}.txt'.format(path, page_num), encoding='utf-8') as f:
                lines = [line.rstrip() for line in f.readlines()]
                pages.append(HtrcPage(lines))
        else:
            page_num = str(n).zfill(8)
            with open('{}/{}.txt'.format(path, page_num), encoding='utf-8') as f:
                lines = [line.rstrip() for line in f.readlines()]
                pages.append(HtrcPage(lines))

    return pages


def clean_vol(vol_dir_path_list: list, out_dir: str):
    vol_num = 0

    assert isinstance(vol_dir_path_list,
                      list), 'clean_vol() 1st parameter vol_dir_path_list="{}" not of <class "list">'.format(
        vol_dir_path_list)
    assert isinstance(out_dir, str), 'clean_vol() 2nd parameter out_dir="{}" not of <class "str">'.format(
        out_dir)

    for vol_dir_path in tqdm(vol_dir_path_list):
        print(f"this is vol_dir_path: {vol_dir_path}")
        # filename = vol_dir_path.split("/", -1)[-2]
        filename = Path(vol_dir_path).name
        filename = str(filename)
        print(f"this is filename: {filename}")
        page_paths = sorted(glob.glob(vol_dir_path + '/*.txt'))
        print(page_paths)
        file_count = len(page_paths)
        loaded_vol = load_vol(vol_dir_path, file_count)
        pages = parse_page_structure(loaded_vol)
        outfile = filename + '.txt'
        # print(outfile)
        vol_num += 1

        with open(outfile, 'w') as f:
            clean_file_path = os.getcwd() + '/' + outfile
            for n, page in enumerate(pages):
                # print('.')
                f.write(page.body + '\n')
            shutil.move(clean_file_path, out_dir)

    return print(f"Cleaned {vol_num} volume(s)")


def check_vol(vol_dir_path_list: list, clean_dir_path: str):
    assert isinstance(vol_dir_path_list,
                      list), 'clean_vol() 1st parameter vol_dir_path_list="{}" not of <class "list">'.format(
        vol_dir_path_list)
    assert isinstance(clean_dir_path, str), 'clean_vol() 2nd parameter out_dir="{}" not of <class "str">'.format(
        clean_dir_path)
    print(f"There are {len(vol_dir_path_list)} total volumes to clean.")
    clean_volume_list = glob.glob(clean_dir_path + '/*.txt')
    list_clean_files = []
    for file in clean_volume_list:
        p = Path(file)
        list_clean_files.append(p.name)
        # print(p.name)
    count = 0
    need_to_clean = []
    for path in vol_dir_path_list:
        p = Path(path)
        ps = (p.name + ".txt")
        if ps not in list_clean_files:
            # print(p)
            need_to_clean.append(str(p))
        else:
            count += 1

    print(f"{count} volumes have already been cleaned.")

    if need_to_clean:
        print("Following Directories need to clean")
        print(CRED + "\n".join(need_to_clean) + CEND)

    return need_to_clean

