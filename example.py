import glob
import time

import htrc_text_processing as htrc_tp
from pathlib import Path

# to get extracted ZIP files to a folder
# htrc_text_processing.get_zips('<path to pairtree parent/s>', 'path to output directory')
# htrc_tp.get_zips('data_sets/sample-pairtree-data-set-2', 'outputs/unzipped2')

# clean file names if Path Exists
# giving Warning if file not exists
# htrc_tp.clean_file_name('outputs/zips/35556044272359/something_00000001.txt')  # file will renamed to 00000001.txt

# htrc_tp.clean_txt_file_names('outputs/unzips2/39002002224252/')
# htrc_tp.normalize_txt_file_names('outputs/unzips2/39015059701311/')

page_directory_list = glob.glob('outputs/unzipped2/*/')
clean_vol_out_dir = 'outputs/cleaned_vols'
htrc_tp.check_vols(page_directory_list, clean_vol_out_dir)
# htrc_tp.normalize_txt_file_names('outputs/unzipped2/39002018496662/')
# htrc_tp.clean_vol(['outputs/unziped/39002002224252'], 'temp')
#
# page_directory_list = glob.glob('outputs/unzipped2/*/')
# print(len(page_directory_list))
# htrc_tp.clean_vol(page_directory_list, clean_vol_out_dir)

# htrc_tp.clean_vol(page_directory_list,1)
