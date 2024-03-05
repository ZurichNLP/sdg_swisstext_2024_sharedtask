# SwissText 2024 Shared Task 
## Automatic Classification of the United Nations' Sustainable Development Goals (SDGs) and Their Targets in English Scientific Abstracts
This repository will serve as a platform for distributing the data and evaluation scripts for both subtasks.
The release of the first data set will be by the 12th of February 2024.

For questions regarding the shared tasks or data, please open an issue (preferred), or write to simon.clematide@cl.uzh.ch. 

More information to come as soon as the official announcement is online.

### Data
The distributed data will be in JSON Lines (JSONL) format, where each line is a separate JSON object representing a scientific abstract. Below is the structure and explanation of fields present in the dataset:

```json
{
  "ID": "unique identifier for the abstract (string)",
  "TITLE": "the title of the scientific abstract (string)",
  "ABSTRACT": "the full text of the abstract (string)",
  "URL": "a link to the full document (string)",
  "SDG": "for Task 1, an integer representing the SDG the abstract is classified under. SDGs are numbered from 0 to 17, where 0 represents the ‘non-relevant’ category.",
  "MAIN_TARGET": "for Task 2, a string representing the primary SDG target the abstract addresses",
  "SECONDARY_TARGETS": "for Task 2, an array of strings representing additional SDG targets the abstract addresses"
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
    "TITLE": "Enhancing arsenic mitigation in Bangladesh: Findings from institutional, psychological, and technical investigations","ABSTRACT":"As part of a trans-disciplinary research project, a series of surveys and interventions were conducted in different arsenic-affected regions of rural Bangladesh. Surveys of institutional stakeholders identified deep tubewells and piped water systems as the most preferred options, and the same preferences were found in household surveys of populations at risk. Psychological surveys revealed that these two technologies were well-supported by potential users, with self-efficacy and social norms being the principle factors driving behavior change. The principle drawbacks of deep tubewells are that installation costs are too high for most families to own private wells, and that for various socio-cultural-religious reasons, people are not willing to walk long distances to access communal tubewells. In addition, water sector planners have reservations about greater exploitation of the deep aquifer, out of concern for current or future geogenic contamination. Groundwater models and field studies have shown that in the great majority of the affected areas, the risk of arsenic contamination of deep groundwater is small; salinity, iron, and manganese are more likely to pose problems. These constituents can in some cases be avoided by exploiting an intermediate depth aquifer of good chemical quality, which is hydraulically and geochemically separate from the arsenic-contaminated shallow aquifer. Deep tubewells represent a technically sound option throughout much of the arsenic-affected regions, and future mitigation programs should build on and accelerate construction of deep tubewells. Utilization of deep tubewells, however, could be improved by increasing the tubewell density (which requires stronger financial support) to reduce travel times, by considering water quality in a holistic way, and by accompanying tubewell installation with motivational interventions based on psychological factors. By combining findings from technical and social sciences, the efficiency and success of arsenic mitigation in general - and installation of deep tubewells in particular - can be significantly enhanced.",
    "URL": "https://www.zora.uzh.ch/id/eprint/89201",
    "SDG": 6,
    "MAIN_TARGET": "6.1",
    "SECONDARY_TARGETS": ["6.3","6.5"]
}
```
