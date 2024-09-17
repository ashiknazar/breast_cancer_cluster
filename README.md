# Breast Cancer Data Clustering

This project involves clustering breast cancer data to identify patterns and groupings within the dataset. The goal is to analyze the dataset, preprocess the data, and apply clustering algorithms to uncover meaningful clusters that can provide insights into the characteristics of breast cancer cases.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Clustering Methods](#clustering-methods)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Breast cancer is one of the most common cancers worldwide, and understanding its underlying patterns can aid in better diagnosis and treatment. This project aims to cluster breast cancer data into distinct groups, potentially helping to identify subtypes or characteristics that are common among certain clusters.

## Dataset

The dataset used in this project is named `cancer.csv`, containing 1904 rows and 693 features. Each row represents a patient, and the features include various measurements and observations related to breast cancer.

### Dataset Overview

- **Shape**: (1904, 693)
- **Features**:About features[DATA_DESCRIPTION.md](DATA_DESCRIPTION.md).

### Data Source

The dataset used in this project can be obtained from the following source:

- **[Kaggle: Breast Cancer Dataset](https://www.kaggle.com/datasets/raghadalharbi/breast-cancer-gene-expression-profiles-metabric)**
  - Description: The dataset includes various attributes related to breast cancer cases and is used for clustering and analysis.

Please ensure you have the appropriate permissions to use the dataset and cite the source if required.


## Project Structure

The project is organized as follows:

```bash
breast_cancer_clustering/
│
├── notebooks/
│   ├── data/                          # Contains dataset or related files
│   ├── EDA.ipynb                      # Exploratory Data Analysis notebook
│   └── MODEL_TRAIN.ipynb              # Model training notebook
│
├── src/
│   ├── __init__.py                    # Package initialization for src
│   ├── components/
│   │   ├── __init__.py                # Package initialization for components
│   │   ├── data_ingestion.py          # Data ingestion functionality
│   │   ├── data_transformation.py     # Data transformation functionality
│   │   └── model_train.py             # Model training functionality
│   ├── pipeline/
│   │   ├── __init__.py                # Package initialization for pipeline
│   │   ├── predict_pipeline.py        # Prediction pipeline
│   │   └── train_pipeline.py          # Training pipeline
│   ├── logger.py                      # Logging utility
│   ├── utils.py                       # Utility functions
│   └── exception.py                  # Exception handling
│
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
└── setup.py                           # Setup script for the project



```


## Installation

To run this project, you'll need to have Python 3.x installed. The required libraries are listed in `requirements.txt`. You can install them using pip:

```bash
pip install -r requirements.txt

```

## Usage

1. **Data Preprocessing**: Start by running the data preprocessing notebook to clean and prepare the data for clustering.

    ```bash
    jupyter notebook notebooks/data_preprocessing.ipynb
    ```

2. **Clustering**: Run the clustering script to apply the chosen algorithms and generate clusters.

    ```bash
    python src/clustering.py
    ```

3. **Evaluation**: Use the evaluation script to assess the quality of the clusters and visualize the results.

    ```bash
    python src/evaluation.py
    ```


## Clustering Methods

This project explores various clustering techniques, including:

- **K-Means Clustering**
- **Hierarchical Clustering**
- **DBSCAN**
- **Gaussian Mixture Models (GMM)**

Each method is applied to the preprocessed data, and the results are compared using metrics like silhouette score, Davies-Bouldin index, and others.



## Evaluation

The quality of the clusters is evaluated using several metrics and visualizations:

- **Silhouette Score**: Measures how similar an object is to its own cluster compared to other clusters.
- **Davies-Bouldin Index**: Measures the average similarity ratio of each cluster with its most similar one.
- **Cluster Visualization**: Plots and charts that show the distribution and separation of clusters.

## Results

The final results of the clustering analysis are stored in the `results/` directory. This includes the clustered data, along with visualizations that illustrate the characteristics of each cluster.

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

