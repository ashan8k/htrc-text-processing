import glob
import os
import shutil
from zipfile import ZipFile
from pathlib import Path
import warnings

from typing import List

from tqdm import tqdm

from htrc.models import HtrcPage
from htrc.runningheaders import parse_page_structure


def get_zips_only(data_dir, output_dir):
    #file_path = Path(file)
    #if file_path.exists():
    #    print(file_path.name)
    if os.path.isdir(data_dir):
        if not os.path.isdir(output_dir):
            try:
                os.mkdir(output_dir)
            except OSError:
                print("Creation of the directory %s failed" % output_dir)
            else:
                print("Successfully created the directory %s " % output_dir)

        for x in tqdm(glob.glob(data_dir + '/**/*.zip', recursive=True)):
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


def swinburne_clean_vol(vol_dir_path_list: list, out_dir: str):
    vol_num = 0
    for vol_dir_path in tqdm(vol_dir_path_list):
        print(f"this is vol_dir_path: {vol_dir_path}")
        filename = vol_dir_path.split("/", -1)[-2]
        # print(f"this is filename: {filename}")
        page_paths = sorted(glob.glob(vol_dir_path + '/*.txt'))
        # print(page_paths)
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