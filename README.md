# Alzheimer's Disease Prediction Model

## Overview and Objectives

This project aims to develop an accurate deep learning model for Alzheimer's disease prediction from MRI images. The model will classify brain MRI scans into four categories:

1. **No Impairment (CN - Cognitive Normal)**
2. **Very Mild Impairment (EMCI - Early Mild Cognitive Impairment)**
3. **Mild Impairment (LMCI - Late Mild Cognitive Impairment)**
4. **Moderate Impairment (AD - Alzheimer's Disease)**

## Technical Stack

- **Programming Language**: Python
- **Deep Learning Framework**: TensorFlow
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **IDE**: Visual Studio Code
- **Dataset**: Alzheimer's MRI [dataset](https://www.kaggle.com/datasets/lukechugh/best-alzheimer-mri-dataset-99-accuracy?select=Combined+Dataset) (containing train/test splits with 4 classes)

## Data Structure

The dataset is structured as follows:

- Training set: 10,240 images (2,560 per class)
- Test set: 1,279 images
  - No Impairment: 640 images
  - Very Mild Impairment: 448 images
  - Mild Impairment: 179 images
  - Moderate Impairment: 12 images