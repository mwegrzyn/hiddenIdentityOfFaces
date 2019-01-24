# The hidden identity of faces: a case of lifelong prosopagnosia

[![PUB](https://img.shields.io/badge/PUB-10.1186%2Fs40359--019--0278--z-yellow.svg)](http://dx.doi.org/10.1186/s40359-019-0278-z) 
[![PREPRINT](https://img.shields.io/badge/PREPRINT-10.31219%2Fosf.io%2Fdv7am-red.svg)](https://doi.org/10.31219/osf.io/dv7am) 
[![ZENODO](https://zenodo.org/badge/DOI/10.5281/zenodo.1486122.svg)](https://doi.org/10.5281/zenodo.1486122) 
[![NEURO](https://img.shields.io/badge/NEURO-collections%2F4017-green.svg)](https://neurovault.org/collections/4017/)  



Martin Wegrzyn, Annika Garlichs, Richard W.K. Heß, Friedrich G. Woermann & Kirsten Labudda  

### Abstract

Not being able to recognize a person's face is a highly debilitating condition from which people with developmental prosopagnosia (DP) suffer their entire life. Here we describe the case of J, a 30 year old woman who reports being unable to recognize her parents, her husband, or herself in the mirror.  
We set out to assess the severity of J's prosopagnosia using tests with unfamiliar as well as familiar faces and investigated whether impaired configural processing explains her deficit. To assess the specificity of the impairment, we tested J's performance when evaluating emotions, intentions, and the attractiveness and likability of faces. Detailed testing revealed typical brain activity patterns for faces and normal object recognition skills, and no evidence of any brain injury. However, compared to a group of matched controls, J showed severe deficits in learning new faces, and in recognizing familiar faces when only inner features were available. Her recognition of uncropped faces with blurred features was within the normal range, indicating preserved configural processing when peripheral features are available. J was also unimpaired when evaluating intentions and emotions in faces. In line with healthy controls, J rated more average faces as more attractive. However, she was the only one to rate them as less likable, indicating a preference for more distinctive and easier to recognize faces.  
Taken together, the results illustrate both the severity and the specificity of DP in a single case. While DP is a heterogeneous disorder, an inability to integrate the inner features of the face into a whole might be the best explanation for the difficulties many individuals with prosopagnosia experience.

### Table of Contents

- code to run the experiments
  - [Cambridge Face Memory Test](CFMT/experiment)
  - [famous faces](famousInner/experiment)  
  - [famous filtered faces](famousFiltered/experiment)
  - [familiarity with famous persons test](famousCheck/experiment)   
  - [emotion expressions](faceEmotion/experiment)  

- the data
  - [fMRI localizer result maps](brainImaging/fsavg_maps) (unthresholded t-Maps in fsaverage space)
  - [Cambridge Face Memory Test](CFMT/experiment/data)
  - [famous faces](famousInner/experiment/data)  
  - [famous filtered faces](famousFiltered/experiment/data)
  - [familiarity with famous persons test](famousCheck/experiment/data)   
  - [emotion expressions](faceEmotion/experiment/data)  
  - [face attractivenss and likability](faceAttract/experiment/data)  

- the analysis code
  - [fMRI Freesurfer Analysis](brainImaging/notebooks/freesurferAnalysisNative.ipynb)
  - [fMRI Freesufer Visualisation](brainImaging/notebooks/plot_native_result.ipynb)
  - [fMRI All Analyses](brainImaging/notebooks)
  - [Cambridge Face Memory Test](notebooks/cambridgeFaceMemory.ipynb)
  - [famous faces: familiarity+context](notebooks/famousFaces_002_innerChoice.ipynb)
  - [famous faces: naming](notebooks/famousFaces_001_innerName_analysis.ipynb)
  - [famous filtered faces: familiarity+context (pt.1)](notebooks/famousFaces_003a_filteredChoiceLog.ipynb)
  - [famous filtered faces: familiarity+context (pt.2)](notebooks/famousFaces_003b_filteredChoice.ipynb)
  - [famous filtered faces: naming ](notebooks/famousFaces_004_filteredName.ipynb)  
  - [familiarity with famous persons check](notebooks/famousFaces_000_checkingForFamiliarity.ipynb)
  - [famous faces: result summary ](notebooks/famousFaces_005_resultSummary.ipynb)
  - [emotion expressions](notebooks/faceEmotion.ipynb) 
  - [face attractiveness and likability: stimulus generation](notebooks/faceAttract_001_stimulusPreparation.ipynb)
  - [face attractiveness and likability: data analysis](notebooks/faceAttract_002_analysis.ipynb)
  - [pen and paper tests](notebooks/otherTests_getNormativeScores.ipynb)
  - [collecting all results](notebooks/main_results.ipynb)  

- in-house written modules
  - [compare individual with sample](modules/case_stats)  

- the results
  - [tables](reports/tables)
  - [figures](reports/figures)  

### Requirements

Data analysis was performed with Python 2.7 [www.python.org](http://www.python.org) using mainly numpy, scipy, pandas, scikit-learn, matplotlib, seaborn and jupyter.


To run all the scipts, you can create a virtual environment, by first installing virtualenv


```shell
pip install virtualenv
```
Then you can create a virtual environment in the folder into which you cloned this repository

```shell
virtualenv venv
```

and then install all modules using pip and the requirements file provided in this repository


```shell
venv/bin/pip install -r requirements.txt
```

The main experiments were written and rendered with [PsychoPy](http://psychopy.org).

### Contact

For questions or comments please write to [martin.wegrzyn@uni-bielefeld.de](mailto:martin.wegrzyn@uni-bielefeld.de)

