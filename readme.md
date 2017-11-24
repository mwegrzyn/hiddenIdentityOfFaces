# The hidden identity of faces: a case of life-long prospagnosia

Martin Wegrzyn, Annika Garlichs, Richard Hess, Friederich G. Wörmann & Kirsten Labudda  


### Abstract

Not being able to recognize a person's face is a highly debilitating condition from which patients with developmental prosopagnosia (DP) suffer their entire life. Here we describe the case of JB, a 30 year old woman who reports being unable to recognize her parents, husband or herself in the mirror.
We set out to assess the severity of JB's prosopagnosia using tests with unfamiliar as well as familiar faces and investigated whether an impaired configural processing explains her deficit. To assess the specificity of the impairment, we tested JB's performance when evaluating emotions, intentions, and the attractiveness and likability of faces.
Detailed testing revealed the absence of any brain injury, typical brain activity patterns for faces, and normal object recognition skills. However, compared to a group of matched controls, JB showed severe deficits in learning new faces, and in recognizing familiar faces when only inner features are available. Her recognition of uncropped faces with blurred features was within the normal range, indicating preserved configural processing when peripheral features are available. JB was also unimpaired when evaluating intentions and emotions in faces. In line with healthy controls, JB rated more average faces as more attractive. However, she was the only one to rate them as less likable, indicating a preference for more distinct and easier to recognize faces.
Taken together, the results illustrate both, the severity and the specificity of DP in a single case. While DP is a heterogeneous disorder, an inability to integrate the inner features of the face into a whole might be the best explanation for the difficulties many of the patients experience.


### About

This is a repository containing the full data and code of our paper on developmental prospagnosia.

### Table of Contents

- the experiments and data
  - [CMFT](CMFT/experiment)
  - [face attractivenss](faceAttract/experiment)
- the analysis code
  - [Analysis of CMFT](notebooks/cambridgeFaceMemory.ipynb)

### Requirements

Data analysis was performed with Python 2.7 [www.python.org](http://www.python.org) using mainly numpy, scipy, pandas, scikit-learn, matplotlib, seaborn and jupyter.


To run all the scipts, you can create a virtual environment, by first installing virtualenv


```shell
pip install  virtualenv
```
Then you can create a virtual environment in the folder into which you cloned this repository

```shell
virtualenv venv
```

and then install all modules using pip


```shell
venv/bin/pip install -r requirements.txt
```

The main experiments were written and rendered with [PsychoPy](http://psychopy.org).

### Contact

For questions or comments please write to [martin.wegrzyn@uni-bielefeld.de](mailto:martin.wegrzyn@uni-bielefeld.de)
