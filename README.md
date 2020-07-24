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

1. `get_zip`

...A function that finds the zip files at the end of the pairtree, moves them to a new folder and expands them, removing the zips

... ```python
    import htrc_text_processing 
    htrc_text_processing.get_zips('<path to pairtree parent/s>', 'path to output directory')
    ```

