## NLP Project Repository

### By: Jonathan Karr and Chris Fakhimi

### Midterm Code, not used anymore

PDFs are in the data/first_attempt/pdfs/ directory

The entire paper goes in the data/first_attempt/entire_paper/ directory

Abstracts go in the data/first_attempt/reference/ directory

rest of the paper goes in the data/first_attempt/main_paper/ directory

GPT summaries go in the data/first_attempt/gpt_results/ directory

### Overall Guide

To test the final code, run python3 main.py

NOTE: You will need to set the OPENAI_API_KEY variable

### Data

Our new Data now comes from the Arxiv Dataset

The file is to large to be uploaded to github and can be found here: https://huggingface.co/datasets/scientific_papers?row=4

### Transforming Data to GPT Results

To read the data run: utils/read_arxiv

To parse the papers run generate_abstracts/data_parser.py

To use gpt 3.5 turbo as the basline run the parsed file using generate_abstracts/gpt_baseline.py which produces gpt_results.json

To use gpt finetuning run the parsed file using fine_tune/finetune_summary.py which produces our_results.json

### To get score metrics

Run generate generate_scores/rouge_result_metric.py and generate_scores/word2vec_metric.py

for the respective gpt_result.json and our_result_json
