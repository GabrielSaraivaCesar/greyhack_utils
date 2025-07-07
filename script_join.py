# This script join the .src files into a single file. This is useful for importing the source code into the game
# 1. Join the source code using this script
# 2. Separate the source code using the script_separate (in game)

import os

content_list = []

def search_files(directory):
    """Recursively search for .src files in the given directory."""
    global content_list

    src_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.src'):
                # get content
                file_path = os.path.join(root, file)
                print("Found:", file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Add metadata
                    content = f"CRASH-FILE-DELIMITER{file_path.replace("./", "").replace("\\", "/")}\n" + content
                    content_list.append(content)
    return src_files

def join_files():
    """Join all collected content into a single string."""
    global content_list

    full_content = "\n".join(content_list)
    with open("joined_source_code.crash", 'w', encoding='utf-8') as f:
        f.write(full_content)

if __name__ == "__main__":
    search_files("./")
    join_files()