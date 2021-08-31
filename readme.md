# Content analysis tools

This repo contains code to analyse text that contains tagged content, which I used to analyse an [interview with driving examiners](https://www.researchgate.net/publication/353807732_Driving_Examiners'_Views_on_Data-Driven_Assessment_of_Test_Candidates_An_Interview_Study). 

For a demonstration of the package with a mockup interview transcript, see `demo.ipynb`. This notebook can be executed in the browser with binder: 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tomdries/content-analysis-tools/HEAD)

Currently, it supports loading strings and word (docx) documents, and it assumes all text in the document is preceded by participant numbers (formatted as, for example, `P1:`), and tagged with the following grammar `#tag-stem.suffix1.suffix2{elaborate comment}`. 


## Usage
Please cite the preprint or the main article (under review).  

Preprint:

Driessen, T., Picco, A., Dodou, D., de Waard, D., & de Winter, J. (2021). *Driving Examiners' Views on Data-Driven Assessment of Test Candidates: An Interview Study*. Researchgate. [https://www.researchgate.net/publication/353807732_Driving_Examiners'_Views_on_Data-Driven_Assessment_of_Test_Candidates_An_Interview_Study](https://www.researchgate.net/publication/353807732_Driving_Examiners'_Views_on_Data-Driven_Assessment_of_Test_Candidates_An_Interview_Study)


## Requirements
|             | version  |
|-------------|----------|
| python      | 3.8.6    |
| lxml        | 4.6.3    |
| python-docx | 0.8.10   |
| regex       | 2021.4.4 |
| pandas      | 1.2.4    |
