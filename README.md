<p align="center">
<a href="https://www.hathitrust.org/htrc"><img src="https://www.hathitrust.org/files/HTRC_logo.jpg" width="200" title="HathiTrust Reseach Center" alt="HTRC"></a>
</p>

# HTRC-Text-Processing Library
>  Tool to process  [pairtree](https://confluence.ucop.edu/display/Curation/PairTree) format data in 17 million digitized works at HathiTrust.
## Table of Contents
1. [About htrc-text-processing Library](#about)
2. [Installation](#install)
3. [Usage](#usage)
4. [Examples](#examples)


## About `htrc-text-processing` Library<a name="about"></a>
Detailed Description goes here.

## Installation <a name="install"></a>

To install,
```bash
pip install htrc-text-processing
```
That's it! This library is written for Python 3.6+. For Python beginners, you'll need [pip](https://pip.pypa.io/en/stable/installing/).
  

## Usage <a name="usage"></a>

* Function: `get_zips()` 

    A function that finds the zip files at the end of the pairtree, moves them to a new folder and expands them, removing the zips.
    
    Inputs:
    
    1. Path (string) to directory that holds the pairtree.
    2. Path (string) to directory that will hold the folders from expanded zips.


    ```python
    htrc_text_processing.get_zips('<path to pairtree parent/s>', 'path to output directory')
    ```
* Function: `clean_file_name()`

    A function that normalizes page file names.
    
    Example: turns `39002088672754_000001.txt` into `00000001.txt`


    ```python
    htrc_text_processing.clean_file_name('outputs/zips/35556044272359/39002088672754_000001.txt') #this will rename file into `00000001.txt`
    ```
  
* Function: `clean_vol()`

    Inputs:
    
    1. List of paths (strings) to directories that holds page files, one per volume
    2. Path (string) to output directory where clean single text files will be stored after cleaning and concatenating pages together
    
