import json
import os
from datetime import datetime
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
import re

class Evaluator:
    def __init__(self, test_data_folder='../data'):
        self.test_data_folder = test_data_folder
        self.submission_folder = '../data/participant_submissions'

    def load_data(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return [json.loads(line) for line in f]

    def save_report(self, report, task_number, prediction_file_path, evaluationtype=""):
        base_filename = os.path.basename(prediction_file_path)
        base_filename = os.path.splitext(base_filename)[0]
        report_filename = f"../results/task{task_number}/{base_filename}_task{task_number}_report_{evaluationtype}.txt"
        with open(report_filename, 'w') as f:
            f.write(report)
        print(f"Report saved to {report_filename}")

    def match_data_by_id(self, predictions, true_data):
        true_data_dict = {item['ID']: item for item in true_data}
        matched_predictions = []
        matched_true_data = []
        for pred in predictions:
            if pred['ID'] in true_data_dict:
                matched_predictions.append(pred)
                matched_true_data.append(true_data_dict[pred['ID']])
        return matched_predictions, matched_true_data

    def task_1_goldlabel(self, predictions, true_data):
        pred_labels = [item['SDG'] for item in predictions]
        true_labels = [item['SDG'] for item in true_data]
        report = classification_report(true_labels, pred_labels, output_dict=False, zero_division=0)
        print("Task 1 Goldlabel Evaluation:\n", report)
        return report

    def task_1_secondary(self, predictions, true_data):
        for i, item in enumerate(predictions):
            if item['SDG'] in true_data[i]['SDGS']:
                true_data[i]['SDG'] = item['SDG']
        pred_labels = [item['SDG'] for item in predictions]
        true_labels = [item['SDG'] for item in true_data]
        report = classification_report(true_labels, pred_labels, output_dict=False, zero_division=0)
        print("Task 1 Secondary Evaluation:\n", report)
        return report

    def evaluate_task_1(self, predictions, true_data, prediction_file_path):
        predictions, true_data = self.match_data_by_id(predictions, true_data)
        report = self.task_1_goldlabel(predictions, true_data)
        self.save_report(report, 1, prediction_file_path, "goldlabel")
        report = self.task_1_secondary(predictions, true_data)
        self.save_report(report, 1, prediction_file_path, "secondary")

    def evaluate_task_2_goldlabel(self, predictions, true_data):
        lb = LabelBinarizer()
        true_main_targets = lb.fit_transform([item['TARGET'] for item in true_data])
        pred_main_targets = lb.transform([item['TARGET'] for item in predictions])
        main_target_report = classification_report(true_main_targets, pred_main_targets, target_names=lb.classes_, zero_division=0)
        print("Task 2 Goldlabel - Main Target Evaluation\n", main_target_report)
        return main_target_report

    def evaluate_task_2_secondary(self, predictions, true_data):
        mlb = MultiLabelBinarizer()
        true_secondary_targets = mlb.fit_transform([item['TARGETS'] for item in true_data])
        pred_secondary_targets = mlb.transform([item['TARGETS'] for item in predictions])
        secondary_target_report = classification_report(true_secondary_targets, pred_secondary_targets, target_names=mlb.classes_, zero_division=0)
        print("Task 2 Secondary - Secondary Targets Evaluation\n", secondary_target_report)
        return secondary_target_report

    def evaluate_task_2(self, predictions, true_data, prediction_file_path):
        predictions, true_data = self.match_data_by_id(predictions, true_data)
        # Goldlabel Evaluation
        main_target_report = self.evaluate_task_2_goldlabel(predictions, true_data)
        self.save_report(main_target_report, 2, prediction_file_path, "goldlabel")

        # Secondary Evaluation
        secondary_target_report = self.evaluate_task_2_secondary(predictions, true_data)
        self.save_report(secondary_target_report, 2, prediction_file_path, "secondary")

    def evaluate(self, task_number, prediction_file_path):
        original_data_path = f"{self.test_data_folder}/testdata_results.jsonl"
        predictions = self.load_data(prediction_file_path)
        true_data = self.load_data(original_data_path)

        if task_number == 1:
            self.evaluate_task_1(predictions, true_data, prediction_file_path)
        elif task_number == 2:
            self.evaluate_task_2(predictions, true_data, prediction_file_path)
        else:
            print("Invalid task number. Please specify 1 or 2.")

    def evaluate_all_participants(self):
        for folder in os.listdir(self.submission_folder):
            folder_path = os.path.join(self.submission_folder, folder)
            for file in os.listdir(folder_path):
                if file.endswith('.json'):
                    file = self.convert_to_jsonl(file, folder_path)
                if file.endswith('.jsonl'):
                    print(f"################## Evaluating {file} ##################")
                    regex = re.compile(r'task\d+')
                    full_task = regex.findall(file.lower())[0]
                    task_number = int(full_task[-1])
                    self.evaluate(task_number, f"{self.submission_folder}/{folder}/{file}")

    def convert_to_jsonl(self, file, folder_path):
        with open(f"{folder_path}/{file}", 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(f"{folder_path}/{os.path.splitext(file)[0]}.jsonl", 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')
        file = os.path.splitext(file)[0] + '.jsonl'
        return file

if __name__ == '__main__':
    evaluator = Evaluator()
    evaluator.evaluate_all_participants()
