import os
import re

INPUT_FILE = "all_code.txt"
# IMPORTANT: Set this to the root of your Django project
# If this script is INSIDE the project root, it can be "."
PROJECT_ROOT = "kyoto_japanese_class_website_django"


def main():
    current_file_path = None
    current_file_content = []

    # Ensure the project root exists if it's not the current directory
    if PROJECT_ROOT != "." and not os.path.exists(PROJECT_ROOT):
        print(f"Error: Project root '{PROJECT_ROOT}' does not exist.")
        # If you're sure your directories are already made, you can remove this check
        # or even os.makedirs(PROJECT_ROOT, exist_ok=True) if needed.

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            # Regex to match "--- path/to/file ---"
            match = re.match(r'^--- (.*?) ---$', line.strip())
            if match:
                # If we were writing to a previous file, save it
                if current_file_path and current_file_content:
                    write_file(current_file_path, "".join(current_file_content))
                    current_file_content = []

                relative_path = match.group(1).strip()
                if PROJECT_ROOT == ".":
                    current_file_path = relative_path
                else:
                    current_file_path = os.path.join(PROJECT_ROOT, relative_path)
                
                print(f"Preparing: {current_file_path}")
            elif current_file_path is not None:
                current_file_content.append(line)

        # Write the last file
        if current_file_path and current_file_content:
            write_file(current_file_path, "".join(current_file_content))

def write_file(file_path, content):
    try:
        # Ensure parent directory exists (the prompt said you created them,
        # but this makes the script more robust)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as wf:
            wf.write(content)
        print(f"  -> Wrote: {file_path}")
    except Exception as e:
        print(f"  -> Error writing {file_path}: {e}")

if __name__ == "__main__":
    # Before running, cd to where all_code.txt and populate_files.py are,
    # OR cd to the PARENT of kyoto_japanese_class_website_django
    # and set PROJECT_ROOT appropriately.
    # For simplicity, let's assume you `cd` into kyoto_japanese_class_website_django
    # and place all_code.txt and populate_files.py there.
    # In that case, PROJECT_ROOT should be "."

    # If you are in the parent directory of 'kyoto_japanese_class_website_django':
    # PROJECT_ROOT = "kyoto_japanese_class_website_django"
    # If you `cd kyoto_japanese_class_website_django` first:
    PROJECT_ROOT = "." # Assuming the script and all_code.txt are in the project root

    if PROJECT_ROOT == ".":
        if not os.path.exists("manage.py"): # A simple check
             print("Warning: Are you sure you are in the Django project root?")
             print("The script expects to be run from within 'kyoto_japanese_class_website_django'")
             print("or have PROJECT_ROOT set to 'kyoto_japanese_class_website_django' if run from its parent.")


    main()
    print("Done populating files.")