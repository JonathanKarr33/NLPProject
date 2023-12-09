import os
import json
folder_path1 = "../data/short/main_paper"
folder_path2 = "../data/short/abstracts"
files1 = sorted(os.listdir(folder_path1))
files2 = sorted(os.listdir(folder_path2))
with open('test.jsonl', 'w') as jsonl_file:
    # Loop over each pair of files
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
            jsonl_file.write(json_line + '\n')

