import os
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
# Not pushing my key to GitHun for privacy reasons
api_key = 'YOUR_API_KEY'


def summarize_text(text):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text: \n{text}",
        max_tokens=50,  # Adjust the number of tokens for your desired summary length
        n=1,  # Number of summaries to generate
        stop=None  # Set custom stop tokens if needed
    )

    summary = response.choices[0].text.strip()
    return summary


# Define the file paths
input_directory = 'data/main_paper'
output_directory = 'data/reference'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all files in the input directory
input_files = os.listdir(input_directory)

# Process each file
for file_name in input_files:
    input_file_path = os.path.join(input_directory, file_name)
    output_file_path = os.path.join(output_directory, file_name)

    with open(input_file_path, 'r') as file:
        text = file.read()

    # Generate the summary
    summary = summarize_text(text)

    # Save the summary in the output directory with the same filename
    with open(output_file_path, 'w') as output_file:
        output_file.write(summary)

    print(f"Summarized and saved {file_name} to {output_file_path}")
