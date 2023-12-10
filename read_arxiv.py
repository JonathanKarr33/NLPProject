import json

# okay to only select 100 smallest from test since that is 6440 files and the train is too llong 13GB
file_path = 'short_pdfs/arxiv-dataset/test.txt'
output_file_path = 'data/smallest_100/smallest_arxiv_600_700.txt'

# Function to read lines from the file and convert them to dictionaries


def read_file(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                data = json.loads(line)
                data_list.append(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line}")
                print(e)
    return data_list


# Read all lines as dictionaries
result = read_file(file_path)

# Sort by the size (in bytes) of "article_text" values
sorted_result = sorted(result, key=lambda x: len(
    json.dumps(x.get("article_text", []))))

# Print the sorted result and the size of the "article_text" for the first 100 entries
print("Sorted Result:")
for i, data in enumerate(sorted_result[600:700], start=1):
    article_text_size = len(json.dumps(data.get("article_text", [])))
    print(f"Entry {i}: Size={article_text_size}")

# Write the first 100 entries to a new file
with open(output_file_path, 'w') as output_file:
    for data in sorted_result[600:700]:
        json.dump(data, output_file)
        output_file.write('\n')

# Print a message indicating the operation is complete
print(
    f"\nFirst 100 entries based on article_text size written to {output_file_path}")
