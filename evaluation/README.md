# Evaluation Script for SwissText 2024 Shared Task

This evaluation script is designed to facilitate the evaluation of submissions for the SwissText 2024 Shared Task on Automatic Classification of the United Nations' Sustainable Development Goals (SDGs) and Their Targets in English Scientific Abstracts. The script supports evaluation for two tasks:
1. Classification at the level of the 17 SDGs.
2. Multi-label classification at the level of SDG targets.

## Features

- **Task 1 Evaluation:** Calculates and reports the performance metrics (precision, recall, F1-score) for the classification of abstracts into the 17 SDGs.
- **Task 2 Evaluation:** Offers detailed performance metrics for the main target, secondary targets, and combined targets, providing a comprehensive overview of the model's capability to identify SDG targets accurately.

## Requirements

To use this evaluation script, you will need Python >=3.6 and the following packages:

- fire
- json
- os
- datetime
- scikit-learn

## Installation

First, ensure you have Python >=3.6 installed on your system. Then, install the necessary Python packages using the following command:

`pip install fire scikit-learn`


## Usage

To evaluate your predictions, follow the steps below:

1. **Prepare Your Predictions:** Ensure your predictions are in a JSON Lines format (.jsonl) with the same structure as the provided dataset.

2. **Execute the Evaluation Script:** Use the command line to navigate to the folder containing the `evaluate.py` script and run the following command, specifying the path to your predictions file and the task number (1 or 2):

`python evaluate.py --prediction_file_path="path/to/your/predictions.jsonl" --task_number=<task_number>`


For example, to evaluate Task 1 predictions located at `predictions/task1_predictions.jsonl`, you would run:

`python evaluate.py --prediction_file_path="predictions/task1_predictions.jsonl" --task_number=1`


The script will print the evaluation results to the console and save a detailed report to a file in the current directory. The report filename will be generated based on the task number, the name of your predictions file, and the current date.

## Report

The evaluation report provides a detailed breakdown of the model's performance, including precision, recall, and F1-score for each category. For Task 2, separate sections are included for the main target, secondary targets, and combined evaluation.