# htrc-text-processing Library [Under Development]
## Table of Contents
1. [What is htrc-text-processing Library](#what-is)
2. [How to Install/Use](#install)
3. [Usage](#usage)
4. [Examples](#examples)
5. [What else?](#what-else)

## About htrc-text-processing Library<a name="what-is"></a>
Description goes here.

## How to  Install <a name="install"></a>

currenlty only by downloading `htrc_text_processing` folder and placed in your working directory.

easiest way is, just clone the repo and run `example1.py`.

TODO 
need to create a pip install verion (after creating all functionalities)  

## What you can do with this. <a name="usage"></a>

A function that finds the zip files at the end of the pairtree, moves them to a new folder and expands them, removing the zips

```python
import htrc_text_processing as htrc_tp 

# Expand all zip files seperately into a given folder
htrc_tp.get_zips_extract('sample-pairtree-data-parent/sample-pairtree-data', 'output_unziped_files') 

# In case you only need zip files use this function 
htrc_tp.get_zips_only('pairtree-data', 'output_only_zip_files') 
```

