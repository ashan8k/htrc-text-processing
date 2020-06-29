import htrc_text_processing as htrc_tp

# If you only need to get ZIP files into a directory
htrc_tp.get_zips_only('sample-pairtree-data', 'output_only_zip_files')

# If you need to get extracted zip folders into a directory
htrc_tp.get_zips_extract('sample-pairtree-data', 'output_unziped_files')