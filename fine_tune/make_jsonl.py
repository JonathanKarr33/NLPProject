import os
import json
folder_path1 = "../data/short/main_paper"
folder_path2 = "../data/short/abstracts"
files1 = sorted(os.listdir(folder_path1))
files2 = sorted(os.listdir(folder_path2))
total_files = 15
train_files = 10
val_file = open('val.jsonl', 'w')
with open('train.jsonl', 'w') as jsonl_file:
    # Loop over each pair of files
    i = 0
    for filename1, filename2 in zip(files1, files2):
        file_path1 = os.path.join(folder_path1, filename1)
        file_path2 = os.path.join(folder_path2, filename2)

        if os.path.isfile(file_path1) and os.path.isfile(file_path2):
            # Read the contents of both files
            with open(file_path1, 'r', errors="replace") as file1, open(file_path2, 'r', errors="replace") as file2:
                paper = file1.read()
                abstract = file2.read()
            
            format = {"messages": [{"role": "system", "content": ""}, {"role": "user", "content": ""}, {"role": "assistant", "content": ""}]}
            format["messages"][0]["content"] = "You are a paper summarizer who takes in papers and generates good abstracts"
            format["messages"][1]["content"] = f"Summarize the following text: \n{paper}" #paper
            format["messages"][2]["content"] = abstract

            json_line = json.dumps(format)
            if i < train_files:
                jsonl_file.write(json_line + '\n')
            elif i > total_files:
                break #do not want to go over
            else:
                val_file.write(json_line + '\n') #! saving to validation file?

            i += 1

