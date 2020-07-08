import tqdm

import htrc_text_processing as htrc_tp
from pathlib import Path
# If you only need to get ZIP files into a directory
# htrc_tp.get_zips_only('sample-pairtree-data', 'output_only_zip_files')

# If you need to get extracted zip folders into a directory
# htrc_tp.get_zips_extract('sample-pairtree-data', 'output_unziped_files')

# clean file names if Path Exists
# giving Warning if file not exists
# htrc_tp.clean_file_name('output_unziped_files/ark+=13960=t3mw3px6k/something_00000001.txt')

# load text files
txt_files = htrc_tp.load_vol('output_unziped_files/ark+=13960=t3mw3px6k',2)

x = htrc_tp.swinburne_clean_vol(['output_unziped_files/ark+=13960=t3mw3px6k/00000001.txt'], 'temp')


