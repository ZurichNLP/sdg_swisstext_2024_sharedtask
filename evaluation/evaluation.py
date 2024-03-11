import fire
import json
import os
from datetime import datetime
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

class Evaluator:
    def __init__(self, data_folder='../data'):
        self.data_folder = data_folder

    def load_data(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return [json.loads(line) for line in f]

    def save_report(self, report, task_number, prediction_file_path):
        base_filename = os.path.basename(prediction_file_path)
        base_filename = os.path.splitext(base_filename)[0]  # Remove file extension
        date_str = datetime.now().strftime("%Y-%m-%d")
        report_filename = f"task{task_number}_{base_filename}_{date_str}_report.txt"
        with open(report_filename, 'w') as f:
            f.write(report)
        print(f"Report saved to {report_filename}")

    def evaluate_task_1(self, predictions, true_data, prediction_file_path):
        pred_labels = [item['SDG'] for item in predictions]
        true_labels = [item['SDG'] for item in true_data]
        report = classification_report(true_labels, pred_labels, output_dict=False)
        print("Task 1 Evaluation:\n", report)
        self.save_report(report, 1, prediction_file_path)

    def evaluate_task_2(self, predictions, true_data, prediction_file_path):
        # Initialize LabelBinarizer and MultiLabelBinarizer
        lb = LabelBinarizer()
        mlb = MultiLabelBinarizer()

        # Main Target Evaluation
        true_main_targets = lb.fit_transform([item['MAIN_TARGET'] for item in true_data])
        pred_main_targets = lb.transform([item['MAIN_TARGET'] for item in predictions])
        main_target_report = classification_report(true_main_targets, pred_main_targets, target_names=lb.classes_, zero_division=0)
        print("Main Target Evaluation\n", main_target_report)

        # Secondary Targets Evaluation
        true_secondary_targets = mlb.fit_transform([item['SECONDARY_TARGETS'] for item in true_data])
        pred_secondary_targets = mlb.transform([item['SECONDARY_TARGETS'] for item in predictions])
        secondary_target_report = classification_report(true_secondary_targets, pred_secondary_targets, target_names=mlb.classes_, zero_division=0)
        print("Secondary Targets Evaluation\n", secondary_target_report)

        # Combined Evaluation
        true_combined_targets = [(item['MAIN_TARGET'],) + tuple(item['SECONDARY_TARGETS']) for item in true_data]
        pred_combined_targets = [(item['MAIN_TARGET'],) + tuple(item['SECONDARY_TARGETS']) for item in predictions]
        true_combined_targets = mlb.fit_transform(true_combined_targets)
        pred_combined_targets = mlb.transform(pred_combined_targets)
        combined_report = classification_report(true_combined_targets, pred_combined_targets, target_names=mlb.classes_, zero_division=0)
        print("Combined Evaluation\n", combined_report)

        # Save combined report to file
        self.save_report("\n".join(['##################\nMain Target Report',
                                    main_target_report,
                                    '##################\nSecondary Target Report',
                                    secondary_target_report,
                                    '##################\nCombined Report',
                                    combined_report]), 2, prediction_file_path)

    def evaluate(self, prediction_file_path, task_number):
        original_data_path = f"{self.data_folder}/task{task_number}_train.jsonl"
        predictions = self.load_data(prediction_file_path)
        true_data = self.load_data(original_data_path)

        if task_number == 1:
            self.evaluate_task_1(predictions, true_data, prediction_file_path)
        elif task_number == 2:
            self.evaluate_task_2(predictions, true_data, prediction_file_path)
        else:
            print("Invalid task number. Please specify 1 or 2.")

if __name__ == '__main__':
    evaluator = Evaluator()
    fire.Fire(evaluator.evaluate)
