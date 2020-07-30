import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='htrc-text-processing',  
    version='0.0.2',
    #scripts=['htrc-text-processing'] ,
    author="Ashan Liyanage, Ryan Dubnicek",
    author_email="ashan8k@gmail.com",
    description="Text processing and analysis for HathiTrust Research Center",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashan8k/htrc-text-processing",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: University of Illinois/NCSA Open Source License",
         "Operating System :: OS Independent",
         ],
    python_requires='>=3.6',
 )
