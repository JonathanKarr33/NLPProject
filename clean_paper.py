import re
import codecs
import os
# Define a custom error handler
def ignore_errors(exception):
    return ('', exception.start + 1)

# Register the custom error handler
codecs.register_error('ignore_errors', ignore_errors)

def remove_figures(text):
    # Example pattern to match a figure or table caption
    figure_pattern = r"Figure \d+:.*?\.(\n|$)"
    table_pattern = r"Table \d+:.*?(\n|$)"

    # Remove figures and tables
    text = re.sub(figure_pattern, '', text, flags=re.DOTALL)
    #text = re.sub(table_pattern, '', text, flags=re.DOTALL)

    return text

def process_paper(file_path):
    with open(file_path, 'r', errors="ignore_errors") as file:
        content = file.read()

    # Regular expression to find an integer followed by 'Experiment' or 'Experiments'
    # For example, '3 Experiment' or '4 Experiments'
    experiment_section_regex = r"\b\d+\s+(Experiment|Experiments)\b"
    experiment_section = re.search(experiment_section_regex, content, re.IGNORECASE)

    # Regular expression to find the beginning of any of the next possible sections
    next_sections_regex = r"\b\d+\s+(Results|Future Work|Conclusion|Discussion)\b"
    next_section = re.search(next_sections_regex, content, re.IGNORECASE)

    if experiment_section:
        if next_section and next_section.start() > experiment_section.start():
            # Truncate the content at the beginning of the next section
            content = content[:next_section.start()]
        else:
            # If no next section is found, keep everything after 'Experiment'
            content = content[experiment_section.start():]

    # Return the processed content
    content = remove_figures(content)
    content = re.sub(r'\n+', '\n', content)
    return content

folder_path = "data/short/main_paper/"
for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):            
            processed_content = process_paper(file_path=file_path)


            with open(file_path, 'w') as file:
                file.write(processed_content)
            print(f"Modified file: {filename}")

