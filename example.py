import glob

import htrc_text_processing

# to get extracted ZIP files to a folder
# htrc_text_processing.get_zips('<path to pairtree parent/s>', 'path to output directory')
# automatically create the output folder ex: 'output-pairtree-data-set-2'
htrc_text_processing.get_zips('data_sets/sample-pairtree-data-set-2', 'output-pairtree-data-set-2')

# all page directory list
page_directory_list = glob.glob('output-pairtree-data-set-2/*/')

# Iteratively clean and normalize text files
for dir_path in page_directory_list:
    htrc_text_processing.normalize_txt_file_names(dir_path)

# path to store cleaned vols
clean_vol_out_dir = 'outputs/cleaned_vols'

# check if already cleaned vols are there and get a new_page_directory list which is not cleaned yet
new_page_directory_list = htrc_text_processing.check_vol(page_directory_list, clean_vol_out_dir)

# Clean vol
htrc_text_processing.clean_vol(new_page_directory_list, clean_vol_out_dir)
