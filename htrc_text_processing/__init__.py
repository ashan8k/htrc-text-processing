# Main Library file
# by Ashan Liyanage

import glob
import os
import shutil
from zipfile import ZipFile
from pathlib import Path
import warnings
from typing import List
from tqdm import tqdm
from htrc_text_processing.htrc.models import HtrcPage
from htrc_text_processing.htrc.runningheaders import parse_page_structure


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


def unzip_file(file_name):
    with ZipFile(file_name, 'r') as zipObj:
        zipObj.extractall()


def clean_file_name(file):
    file_path = Path(file)
    if file_path.exists():
        print(file_path.name)
        os.rename(file_path, file_path.parent / file_path.name.split("_")[-1])
    else:
        warnings.warn("Path/File not exists. Path = " + file)


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

    for vol_dir_path in tqdm(vol_dir_path_list):
        print(f"this is vol_dir_path: {vol_dir_path}")
        filename = vol_dir_path.split("/", -1)[-2]
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
