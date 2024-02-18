import os

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

def sort_files_by_lines(directory):
    file_line_count = []
    for root, dirs, files in os.walk(directory):
        python_files = [file for file in files if file.endswith('.py')]
        if len(python_files) > 1:
            continue
        for file in python_files:
            file_path = os.path.join(root, file)
            line_count = count_lines(file_path)
            file_line_count.append((os.path.basename(root), file, line_count))

    sorted_files = sorted(file_line_count, key=lambda x: x[2])
    return sorted_files

if __name__ == "__main__":
    directory_path = 'C:/Users/HP/GitHub/python-mini-projects/projects'
    output_file_path = 'C:/Users/HP/GitHub/python-mini-projects/Notebooks/file1.txt'

    sorted_files = sort_files_by_lines(directory_path)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for subdir, file, line_count in sorted_files:
            output_file.write(f"Sub-directory: {subdir}\nPython file: {file}\nLine count: {line_count}\n\n")