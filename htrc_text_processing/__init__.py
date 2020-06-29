import glob
import os
import shutil


def get_zips(data_dir, output_dir):
    if os.path.isdir(data_dir):
        if not os.path.isdir(output_dir):
            try:
                os.mkdir(output_dir)
            except OSError:
                print("Creation of the directory %s failed" % output_dir)
            else:
                print("Successfully created the directory %s " % output_dir)

        for x in glob.glob(data_dir + '/**/*.zip', recursive=True):
            print(x)
            shutil.copy(x, output_dir)
    else:
        raise Exception(data_dir + ' path does not exists!')
