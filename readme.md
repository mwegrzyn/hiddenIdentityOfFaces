# Data & Code Supplement
## The hidden identity of faces: a case of life-long prospagnosia


Martin Wegrzyn, Annika Garlichs, Richard W.K. Heß, Friederich G. Woermann & Kirsten Labudda  


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

