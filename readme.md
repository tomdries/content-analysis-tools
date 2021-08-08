# Content analysis tools
This repo contains code to analyse text that contains tagged content, which I used to analyse the interview in a publication that's under review. 

Currently, it supports loading word (docx) documents, and it assumes all text in the document is preceded by participant numbers (formatted as, for example, `P1:`), and tagged with the following grammar `#tag-stem.suffix1.suffix2{elaborate comment}`. 

For a demonstration of the package with a mockup interview transcript, see `demo.ipynb`. This notebook can be previewed on github or alternatively via https://nbviewer.jupyter.org/.


## Requirements
lxml                4.6.3
python-docx         0.8.10
regex               2021.4.4
pandas              1.2.4


## Usage
It would be appreciated if you cite the article (currently under review, ref will be added here). 

