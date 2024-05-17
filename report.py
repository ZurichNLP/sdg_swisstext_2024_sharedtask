# pip install pandas
# python report.py --output report_secondary.tsv results/task1/*secondary.txt
# python report.py --output report_goldlabel.tsv results/task1/*goldlabel.txt


import os
import re
import pandas as pd


def parse_report(file_content):
    """
    Parse the sklearn classification report from a string and extract the relevant metrics.
    """
    metrics = {}
    accuracy_match = re.search(r"accuracy\s+(\d+\.\d+)", file_content)
    if accuracy_match:
        metrics["accuracy"] = float(accuracy_match.group(1))

    macro_avg_match = re.search(
        r"macro avg\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)", file_content
    )
    if macro_avg_match:
        metrics["macro_precision"] = float(macro_avg_match.group(1))
        metrics["macro_recall"] = float(macro_avg_match.group(2))
        metrics["macro_f1-score"] = float(macro_avg_match.group(3))

    weighted_avg_match = re.search(
        r"weighted avg\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)", file_content
    )
    if weighted_avg_match:
        metrics["weighted_precision"] = float(weighted_avg_match.group(1))
        metrics["weighted_recall"] = float(weighted_avg_match.group(2))
        metrics["weighted_f1-score"] = float(weighted_avg_match.group(3))

    return metrics


def process_files(file_list, output_file):
    """
    Process the list of files and write the extracted metrics to a TSV file.
    """
    records = []

    for file_name in file_list:
        with open(file_name, "r") as file:
            file_content = file.read()
            metrics = parse_report(file_content)
            metrics["file_name"] = os.path.basename(file_name)
            records.append(metrics)

    df = pd.DataFrame(records)
    df = df[
        [
            "file_name",
            "accuracy",
            "macro_precision",
            "macro_recall",
            "macro_f1-score",
            "weighted_precision",
            "weighted_recall",
            "weighted_f1-score",
        ]
    ]
    df.sort_values(by="accuracy", ascending=False, inplace=True)
    df.to_csv(output_file, sep="\t", index=False, float_format="%.2f")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract evaluation metrics from sklearn classification reports."
    )
    parser.add_argument(
        "files", metavar="F", type=str, nargs="+", help="List of files to process"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="evaluation_metrics.tsv",
        help="Output TSV file name",
    )

    args = parser.parse_args()
    process_files(args.files, args.output)
