import os


def count_lines_quantity(file_path: str) -> int:
    """Count the number of lines in a file."""
    with open(file_path, encoding='UTF-8') as file:
        file_lines_quantity = len(file.readlines())
    return file_lines_quantity


def sort_files_by_size(files_paths: list, sizes: list) -> list:
    """Sort files paths by quantity of files lines."""
    files_and_sizes_list = list(zip(files_paths, sizes))
    files_and_sizes_list.sort(key=lambda x: x[1])
    return files_and_sizes_list


def write_to_file(target_file: str, path_size_list: list):
    """Write sorted files content into a new file."""
    with open(target_file, 'w', encoding='UTF-8') as final_file:
        for path, size in path_size_list:
            with open(path, encoding='UTF-8') as reading_file:
                final_file.write(f'{os.path.basename(path)}\n')
                final_file.write(f'{str(size)}\n')
                final_file.write(f'{reading_file.read()}\n')


file_1_path = os.path.join(os.getcwd(), '1.txt')
file_2_path = os.path.join(os.getcwd(), '2.txt')
file_3_path = os.path.join(os.getcwd(), '3.txt')
file_final_path = os.path.join(os.getcwd(), 'final.txt')
files_path_list = [file_1_path, file_2_path, file_3_path]

size_list = list(map(count_lines_quantity, files_path_list))

sorted_by_sizes = sort_files_by_size(files_path_list, size_list)

write_to_file(file_final_path, sorted_by_sizes)
