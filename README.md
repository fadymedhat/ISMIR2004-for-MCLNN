
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/fadymedhat/ISMIR2004-for-MCLNN/blob/master/LICENSE)

# ISMIR2004 dataset for MCLNN

The [ISMIR2004](http://ismir2004.ismir.net/genre_contest/) music genre dataset.
The clips are provided from [here](http://magnatune.com). If you could not access it, you could use the dataset is hosted [here](http://mirg.city.ac.uk/datasets/magnatagatune/index1.html)
, but it requires custom handling to extract clips that overlap with the original ISMIR2004 dataset.



| Clip Duration  | Format | Count | Categories|
|:---:|:---:|:---:|:---:|
| Full recordings | .mp3 | 1458 | 6 |

Dataset Summary:
 * A 729-training/729-testing split is defined for the dataset, we combined both splits for a 10-folds cross-validation.

 
 This folder contains:
  * Scripts required to prepare the ISMIR2004 dataset for the MCLNN processing.
  * Pretrained weights and indices for the 10-fold cross-validation in addition to the standardization parameters 
  to replicate the results in:
  
  _Fady Medhat, David Chesmore and John Robinson, "Masked Conditional Neural Networks for Audio Classification,"   International Conference on Artificial Neural Networks and Machine Learning (ICANN)_
 
 
 ## Prepossessing
 
The preprocessing involved in preparing the ISMIR2004 dataset is resampling to .wav at 22050 Hz.


#### Preparation scripts prerequisites

The [preparation scripts](https://github.com/fadymedhat/ISMIR2004-for-MCLNN/tree/master/ISMIR2004_preparation_scripts) require the following packages to be installed beforehand:
   * [ffmpeg](https://www.ffmpeg.org/) version N-81489-ga37e6dd
   * numpy 1.11.2+mkl
   * librosa 0.4.0
   * h5py 2.6.0
 
#### Steps
1. Download the dataset and execute the scripts in the [preparation scripts](https://github.com/fadymedhat/ISMIR2004-for-MCLNN/tree/master/ISMIR2004_preparation_scripts) following the order of their labels.
2. Make sure the files are ordered following the [ISMIR2004_storage_ordering](https://github.com/fadymedhat/ISMIR2004-for-MCLNN/blob/master/ismir2004_storage_ordering.txt) file.
3. Configure the spectrogram transformation within the [Dataset Transformer](https://github.com/fadymedhat/MCLNN/tree/master/dataset_transformer) and generate the MCLNN-Ready hdf5 for the dataset.
4. Generate the indices for the folds using the [Index Generator](https://github.com/fadymedhat/MCLNN/tree/master/index_generator) script.
