import htrc_text_processing as htrc_tp
from pathlib import Path

# to get extracted ZIP files to a folder
# htrc_text_processing.get_zips('<path to pairtree parent/s>', 'path to output directory')
htrc_tp.get_zips('data_sets/sample-pairtree-data-set-2', 'outputs/unzipped')

# clean file names if Path Exists
# giving Warning if file not exists
# htrc_tp.clean_file_name('outputs/zips/35556044272359/something_00000001.txt')  # file will renamed to 00000001.txt

# htrc_tp.clean_vol(['outputs/unziped/39002002224252'], 'temp')
