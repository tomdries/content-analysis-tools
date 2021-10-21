# Content analysis tools

This repo contains code to analyse text that contains tagged content, which I used to analyse an [interview with driving examiners](https://www.researchgate.net/publication/355393718_Driving_examiners'_views_on_data-driven_assessment_of_test_candidates_An_interview_study). 

For a demonstration of the package with a mockup interview transcript, see `demo.ipynb`. This notebook can be executed in the browser with binder: 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tomdries/content-analysis-tools/HEAD?filepath=demo.ipynb)

Currently, it supports loading strings and word (docx) documents, and it assumes all text in the document is preceded by participant numbers (formatted as, for example, `P1:`), and tagged with the following grammar `#tag-stem.suffix1.suffix2{elaborate comment}`. 


## Usage
Please cite the following article:

Driessen, T., Picco, A., Dodou, D., de Waard, D., & de Winter, J. (2021). Driving examiners’ views on data-driven assessment of test candidates: An interview study. Transportation Research Part F: Traffic Psychology and Behaviour, 83, 60–79. https://doi.org/10.1016/j.trf.2021.09.021


