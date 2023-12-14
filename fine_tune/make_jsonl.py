import os
import json
json_path = "../data/tenth_percentile_600_700/parsed_data.json"

total_files = 50
train_files = 30
val_file = open('data/val.jsonl', 'w')
with open('data/train.jsonl', 'w') as jsonl_file:
    i = 0
    with open(json_path, 'r') as json_file:
        data_list = json.load(json_file)
    for row in data_list:
        paper = row["article_text"]
        abstract = row["abstract_text"]
    
        format = {"messages": [{"role": "system", "content": ""}, {"role": "user", "content": ""}, {"role": "assistant", "content": ""}]}
        format["messages"][0]["content"] = "You are an abstract creator who takes in papers and generates good scientific abstracts"
        format["messages"][1]["content"] = f"Make an abstract for the following paper: \n{paper}" #paper
        format["messages"][2]["content"] = abstract

        json_line = json.dumps(format)
        if i < train_files:
            jsonl_file.write(json_line + '\n')
        elif i > total_files:
            break #do not want to go over
        else:
            val_file.write(json_line + '\n') #! saving to validation file?

        i += 1

