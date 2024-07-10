import os

def convert_txt_to_py(directory):
    """Converts all .txt files in a directory and its subdirectories to .py extension.

    Args:
        directory (str): The path to the directory containing the .txt files.
    """

    for filename in os.listdir(directory):
        # Check if it's a directory (not a file)
        if os.path.isdir(os.path.join(directory, filename)):
            # Recursively call the function for subdirectories
            convert_txt_to_py(os.path.join(directory, filename))
        elif filename.endswith(".txt"):
            new_filename = filename[:-4] + ".py"  # Replace .txt with .py
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Example usage:
# Assuming the script is running in your current directory
current_directory = os.getcwd()
convert_txt_to_py(current_directory)
