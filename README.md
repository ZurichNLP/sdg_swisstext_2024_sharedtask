# SwissText 2024 Shared Task

## Automatic Classification of the United Nations' Sustainable Development Goals (SDGs) and Their Targets in English Scientific Abstracts

This repository will serve as a platform for distributing the data and evaluation scripts for both subtasks.

For questions regarding the shared tasks or data, please open an issue (preferred), or write to simon.clematide@cl.uzh.ch.

Details can be found at the SwissNLP Website: https://www.swisstext.org/call-for-shared-tasks/

## Workshop Program at Swisstext 2024 June 11th 10:30 to 12 "NLP for Sustainable Development Goals Monitoring"

  1. Welcome + Shared-Task Overview: Simon Clematide + Tobias Fankhauser (15-20 min)

  2. Jürgen Bernard (UZH): The DZI Project “SDG Research Scout” and its visualisation aspects (20 min)

  3. Presentation of the Shared Task contributions with System Description Papers (15 min each)

  - Fernando de Meer Pardo, Hanna Hubarava and Vera Bernhard (UZH): System Description Paper for SwissText 2024 Shared Task 1: Classification at the Level of the 17 SDGs
  - Manuel Bolz, Andreas Loizidis, Kevin Bründler (UZH): SwissText - Shared Task (SDG Classification) - Task 1
  - Adrian M.P. Brasoveanu, Albert Weichselbraun, Lyndon J.B. Nixon and Arno Scharl (MODUL University Vienna/webLyzard): An Efficient Workflow Towards Improving Classifiers in Low-Resource Settings with Synthetic Data
  - Norman Süsstrunk, Albert Weichselbraun, Andreas Murk, Roger Waldvogel and André Glatzl (Chur): Scouting out the Border: Leveraging Explainable AI to Generate Synthetic Training Data for SDG Classification

  4. Final discussion «NLP for Sustainability» (15 min)

For online participation via webex, please contact simon.clematideATuzh.ch.

## News

- 2024/05/10: Test data with 156 new abstracts for Task 1 has been released:
  `data/task1_test-covered.jsonl`. Good luck with your submission!
- 2024/05/13: Test data with 91 abstracts for Task 2 has been released:
  `data/task2_test-covered.jsonl`. Good luck with your submission!

## Submissions

- Each team can submit up to 3 runs. Send a zip archive with a JSONL file named `TEAM_RUN1_TASK1.jsonl`.
- The format of the submission should be identical to the format of the training/sample data.
- Hackathon-like submissions (24-48h of work) are welcome. Please indicate in your submission mail whether your submission should be categorized as hackathon-like.

To evaluate your predictions, create a folder in the `data/participant_submissions` directory with your team name. Load the result files as `.jsonl` into this folder and name them: `teamname_task1_run1.jsonl` (for Task 1) or `teamname_task2_run1.jsonl` (for Task 2). From the root folder, run `python evaluation/evaluation.py`. The results will be saved in `results/task1` or `results/task2`, depending on the task.


## Schedule

- 12th February 2024: Announcement of Shared Task on Swiss NLP
- 12th February 2024: Release of first batch of training data for Task 1
- 2nd March 2024: Release of development data for Task 2
- 10th May 2024 08:00 CEST: Release of test data for Task 1 to participants
- 13th May 2024 08:00 CEST: Deadline for submission of results for Task 1 (per mail to tobias.fankhauserATuzh.ch)
- 13th May 2024 08:00 CEST: Release of test data for Task 2 to participants (test data of Task 1 with ground truth labels)
- 15th May 2024 23:59 CEST: Submission of results for Task 2 (per mail to tobias.fankhauserATuzh.ch)
- 21st May 2024: Draft submission for System Descriptions/Papers intended for online publication (official template of SwissText 3-6 pages): Send via E-mail to simon.clematideATuzh.ch
- 21st May 2024: Participants who don't want to publish a workshop-like short paper are strongly invited to send a short description of their approach that will be used for the shared task overview paper written by the organizers
- 24st May 2024: Notification of acceptance of System Description Papers
- 31st May 2024: Deadline for final System Description Papers for online publication (similar to Workshop Papers from SwissText); authors are expected to present their approach in a 8-10 minute presentation at the workshop (onsite if possible)
- 11th June 2024 10:20-12:30 CEST: 2-h Workshop and Lunch Meeting at the SwissText Conference in Chur: “NLP for Sustainable Development Goals Monitoring” (Shared Task Results Presentation and Stakeholder Meeting); Online participation via Webex is possible.

### Data

The distributed data will be in JSON Lines (JSONL) format, where each line is a separate JSON object representing a scientific abstract. Below is the structure and explanation of fields present in the dataset:

```json
{
  "ID": "unique identifier for the abstract (string)",
  "TITLE": "the title of the scientific abstract (string)",
  "ABSTRACT": "the full text of the abstract (string)",
  "URL": "a link to the full document (string)",
  "SDG": "for Task 1, an integer representing the SDG the abstract is classified under. SDGs are numbered from 0 to 17, where 0 represents the ‘non-relevant’ category.",
  "TARGET": "for Task 2, a string representing the primary SDG target the abstract addresses",
  "TARGETS": "for Task 2, an array of strings representing all SDG targets the abstract addresses"
}
```

#### Example Data Task 1: Classification at the Level of the 17 SDGs

```json
{
  "ID": "oai:www.zora.uzh.ch:126666",
  "TITLE": "Identifying phrasemes via interlingual association measures - A data-driven approach on dependency-parsed and word-aligned parallel corpora",
  "ABSTRACT": "In corpus linguistics, statistical association measures play a major role in identifying collocations such as ‘play’ and ‘role’ in ‘play a role’.  Those two words that appear considerably more often in the same context than one would expect from a random distribution are collocates.  They typically constitute meaning beyond the bare combination of both words’ semantics.\r\nWe employ the same association measures on interlingual word co-occurrences based on statistical word alignment and combine them with intralingual association measures on syntactical dependency relations in order to identify phrasemes.  Support verb constructions exemplify our approach.  They are characterized by the respective verb contributing little to the semantics of the whole construction, which we can determine with the aid of our intralingual association measures.",
  "URL": "https://www.zora.uzh.ch/id/eprint/126666",
  "SDG": 0
}
```

#### Example Data Task 2: Multi-label Classification at the Level of SDG Targets

```json
{
  "ID": "oai:www.zora.uzh.ch:89201",
  "TITLE": "Enhancing arsenic mitigation in Bangladesh: Findings from institutional, psychological, and technical investigations",
  "ABSTRACT": "As part of a trans-disciplinary research project, a series of surveys and interventions were conducted in different arsenic-affected regions of rural Bangladesh. Surveys of institutional stakeholders identified deep tubewells and piped water systems as the most preferred options, and the same preferences were found in household surveys of populations at risk. Psychological surveys revealed that these two technologies were well-supported by potential users, with self-efficacy and social norms being the principle factors driving behavior change. The principle drawbacks of deep tubewells are that installation costs are too high for most families to own private wells, and that for various socio-cultural-religious reasons, people are not willing to walk long distances to access communal tubewells. In addition, water sector planners have reservations about greater exploitation of the deep aquifer, out of concern for current or future geogenic contamination. Groundwater models and field studies have shown that in the great majority of the affected areas, the risk of arsenic contamination of deep groundwater is small; salinity, iron, and manganese are more likely to pose problems. These constituents can in some cases be avoided by exploiting an intermediate depth aquifer of good chemical quality, which is hydraulically and geochemically separate from the arsenic-contaminated shallow aquifer. Deep tubewells represent a technically sound option throughout much of the arsenic-affected regions, and future mitigation programs should build on and accelerate construction of deep tubewells. Utilization of deep tubewells, however, could be improved by increasing the tubewell density (which requires stronger financial support) to reduce travel times, by considering water quality in a holistic way, and by accompanying tubewell installation with motivational interventions based on psychological factors. By combining findings from technical and social sciences, the efficiency and success of arsenic mitigation in general - and installation of deep tubewells in particular - can be significantly enhanced.",
  "URL": "https://www.zora.uzh.ch/id/eprint/89201",
  "SDG": 6,
  "TARGET": "6.1",
  "TARGETS": ["6.1", "6.3", "6.5"]
}
```

In addition, the `data` folder contains the following subdirectories:

- `participant_submissions`: This folder stores the submissions from participants, specifically their classification results.
- `synthetic_data`: This folder holds the synthetic data provided by participants, organized in subfolders named after each participating group.


## Results and Baseline Models

### Baseline Models

The baseline models for this shared task are LLAMA 3 ([source](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)). These models are used to evaluate the scientific abstracts and assign them to the most appropriate United Nations Sustainable Development Goal (SDG).

#### Baseline LLAMA 3

```python
message = [
{
   "role": "system",
   "content": "As an SDG assignment assistant, your task is to evaluate scientific abstracts and assign them to the most appropriate United Nations Sustainable Development Goal (SDG) based on a specific target within the SDG. You should only assign an SDG if there is a clear and direct connection between the abstract content and a concrete target of the SDG. If the abstract generally relates to the SDG but does not align with a specific target, or if no SDG target is applicable, assign it to 'SDG 0'.\n\n{sdg_descriptions}\n"
},
{
   "role": "user",
   "content": "For the following scientific abstract: \"{TITLE}\n{ABSTRACT}\", identify and assign the most appropriate SDG based on a concrete target within that SDG that the abstract covers. If no specific target is applicable, return 'SDG 0'. Assigned SDG:"
}
]
```

##### LLAMA 3, Chain of Thought (CoT)
    
```python
cot_message = [
   {
       "role": "system",
       "content": "As an SDG assignment assistant, your task involves a three-step reasoning process: 1) Analyze the main topics and objectives of the provided scientific abstract. 2) Justify which concrete target within the United Nations Sustainable Development Goals (SDG) aligns directly with these topics. 3) Determine the appropriate SDG based on this target. Only assign an SDG if a specific target is directly covered by the abstract; otherwise, assign 'SDG 0'. Use the following examples to guide your response:\n\nExample 1:\nAbstract: \"The Success of Job Applications: A New Approach to Program Evaluation. In this paper, we suggest a novel approach to program evaluation...\"\nResponse: First, analyze the main topics... Then, identify Target 4.4... Final determination: SDG 4, focusing on Target 4.4.\n\nExample 2:\nAbstract: \"Approval of Equal Rights and Gender Differences in Well-Being. Women earn less than men but are not less satisfied with life...\"\nResponse: First, describe the main topics... Since no specific target applies, assign 'SDG 0'.\n"
   },
   {
       "role": "user",
       "content": "For this scientific abstract: \"{TITLE}\n{ABSTRACT}\", first describe its main topics, then identify and justify the specific SDG target it covers, and conclude with the corresponding SDG assignment. If no specific target applies, assign 'SDG 0'. Final determination:"
   }
]
```

### Results Task 1
| Team                      | Run                  | ACC  | MACRO-F                                                 | MACRO-P | MACRO-R | W-P  | W-R  | W-F  |
|---------------------------|----------------------|------|---------------------------------------------------------|---------|---------|------|------|------|
| NLPChur                   | badwords             | <span style="background-color: yellow">**52%**</span>  | 51%                                                     | 53%     | 60%     | 65%  | **52%**  | **55%**  |
| test_roberta_base_synth   | 33                   | 49%  | <span style="background-color: lightgrey">**56%**</span> | **65%**     | 66%     | 74%  | 49%  | 53%  |
| MANUEL_ANDREAS_KEVIN      | GPT4                 | 47%  | 44%                                                     | 46%     | 52%     | 65%  | 47%  | 51%  |
| bcode                     | 1                    | 47%  | 35%                                                     | 42%     | 37%     | 56%  | 47%  | 49%  |
| NLPChur                   | synthetic data       | 46%  | 44%                                                     | 49%     | 51%     | 59%  | 46%  | 49%  |
| test_roberta_base_synth   | 31                   | 46%  | 51%                                                     | 61%     | 58%     | 69%  | 46%  | 49%  |
| MANUEL_ANDREAS_KEVIN      | ensemble             | 45%  | 43%                                                     | 46%     | 52%     | 68%  | 45%  | 49%  |
| MANUEL_ANDREAS_KEVIN      | MIXTRAL              | 45%  | 45%                                                     | 54%     | 56%     | 74%  | 45%  | 50%  |
| test_roberta_base_synth   | 32                   | 40%  | 51%                                                     | 58%     | 61%     | 64%  | 40%  | 42%  |
| MeHuBe                    | 1                    | 39%  | 42%                                                     | 45%     | 53%     | 58%  | 39%  | 41%  |
| MeHuBe                    | 2                    | 38%  | 41%                                                     | 41%     | 53%     | 55%  | 38%  | 40%  |
| MeHuBe                    | 3                    | 38%  | 41%                                                     | 41%     | 53%     | 55%  | 38%  | 39%  |
| PRONTO                    | 1                    | 38%  | 52%                                                     | 54%     | **71%**     | 70%  | 38%  | 36%  |
| llama3_cot                | 1                    | 37%  | 52%                                                     | 54%     | 64%     | 65%  | 37%  | 36%  |
| llama3                    | 1                    | 32%  | 45%                                                     | 50%     | 67%     | **77%**  | 32%  | 25%  |
| AVERAGE                   |                      | 43%  | 46%                                                     | 51%     | 57%     | 65%  | 43%  | 44%  |

#### Secondary Evaluation Results

The secondary evaluation considers a prediction correct if the predicted label is relevant to the abstract, even if it is not the main SDG.

| Team                      | Run                  | ACC                                                   | MACRO-F                                                  | MACRO-P | MACRO-R | W-P  | W-R  | W-F  |
|---------------------------|----------------------|-------------------------------------------------------|----------------------------------------------------------|---------|---------|------|------|------|
| NLPChur                   | badwords             | <span style="background-color: yellow">**55%**</span> | 56%                                                      | 61%     | 55%     | 68%  | **55%**  | **58%**  |
| test_roberta_base_synth   | 33                   | 52%                                                   | <span style="background-color: lightgrey">**68%**</span> | **67%**     | **59%**     | 75%  | 52%  | 55%  |
| NLPChur                   | synthetic data       | 50%                                                   | 55%                                                      | 53%     | 49%     | 64%  | 50%  | 53%  |
| MANUEL_ANDREAS_KEVIN      | MIXTRAL              | 50%                                                   | 59%                                                      | 61%     | 52%     | 75%  | 50%  | 54%  |
| test_roberta_base_synth   | 31                   | 50%                                                   | 66%                                                      | 63%     | 58%     | 69%  | 50%  | 53%  |
| MANUEL_ANDREAS_KEVIN      | ensemble             | 49%                                                   | 51%                                                      | 58%     | 49%     | 69%  | 49%  | 53%  |
| MANUEL_ANDREAS_KEVIN      | GPT4                 | 49%                                                   | 49%                                                      | 54%     | 47%     | 66%  | 49%  | 53%  |
| bcode                     | 1                    | 48%                                                   | 46%                                                      | 39%     | 38%     | 58%  | 48%  | 51%  |
| test_roberta_base_synth   | 32                   | 43%                                                   | 62%                                                      | 63%     | 56%     | 65%  | 43%  | 45%  |
| MeHuBe                    | 1                    | 42%                                                   | 49%                                                      | 58%     | 47%     | 60%  | 42%  | 43%  |
| MeHuBe                    | 2                    | 42%                                                   | 45%                                                      | 57%     | 45%     | 58%  | 42%  | 42%  |
| PRONTO                    | 1                    | 42%                                                   | 57%                                                      | 73%     | 57%     | 70%  | 42%  | 38%  |
| MeHuBe                    | 3                    | 41%                                                   | 45%                                                      | 56%     | 45%     | 57%  | 41%  | 42%  |
| llama3_cot                | 1                    | 40%                                                   | 59%                                                      | 68%     | 56%     | 68%  | 40%  | 39%  |
| llama3                    | 1                    | 36%                                                   | 54%                                                      | **69%**     | 50%     | **77%**  | 36%  | 29%  |
| AVERAGE                   |                      | 46%                                                   | 55%                                                      | 60%     | 51%     | 67%  | 46%  | 47%  |

#### Legend

- **Team**: Name of the team participating in the shared task.
- **Run**: Specific run or configuration submitted by the team.
- **ACC**: Accuracy of the model in classifying the abstracts.
- **MACRO-F**: Macro-averaged F1 score, measuring the balance between precision and recall across all classes.
- **MACRO-P**: Macro-averaged Precision, measuring the proportion of true positive results among all positive results predicted.
- **MACRO-R**: Macro-averaged Recall, measuring the proportion of true positive results among all actual positive instances.
- **W-P**: Weighted Precision, accounting for the number of true instances for each class.
- **W-R**: Weighted Recall, accounting for the number of true instances for each class.
- **W-F**: Weighted F1 score, balancing precision and recall while considering the number of true instances for each class.
