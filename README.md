# Bayesian power-law sensitivity data release

Data release supporting:

_Is your stochastic signal really detectable?_

Federico Pozzoli, Jonathan Gair, Riccardo Buscicchio, Lorenzo Speri. 
[arXiv: 2412.10468](https://arxiv.org/abs/2412.10468).

## Credits

You are welcome to use this dataset in your research. We kindly ask you to cite the paper above. 
If you want to cite specifically the data release, its DOI is: 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14384634.svg)](https://doi.org/10.5281/zenodo.14384634)

## Binder
Each figure is also available for reproducibility as a Binder image. 

- Figure 1: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RiccardoBuscicchio/BPLS-data-release/binder?labpath=notebooks%2Fjupyter%2FFigure1.ipynb)
- Figure 2: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RiccardoBuscicchio/BPLS-data-release/binder?labpath=notebooks%2Fjupyter%2FFigure2.ipynb)
- Figure 3: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RiccardoBuscicchio/BPLS-data-release/binder?labpath=notebooks%2Fjupyter%2FFigure3.ipynb)

## Data

Data behind figures are provided within the repository in the `./data/` subfolder, and they are minimal in size.
[github release page](https://github.com/RiccardoBuscicchio/BPLS-data-release/releases). 

## Content
In `./notebooks/jupyter/`, we provide a jupyter notebook for each figure.

## Requirements
Feel free to use `./bpls.yaml` to create a conda environment to reproduce our figures, with 
```bash
conda env create -f bpls.yaml
```

Or install the following dependencies:
- `numpy`
- `matplotlib`
- `scipy`
- `scikit-image`
