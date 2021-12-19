file_list = ["1.txt", "2.txt", "3.txt"]
with open("1.txt", encoding="utf-8") as f:
    x = f.readlines()
def merge_files(files: list):
    list_of_lines = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            temp_list = f.readlines()
            temp_list.insert(0, str(len(temp_list)))
            temp_list.insert(0, file)
            list_of_lines += [temp_list]
    list_of_lines = sorted(list_of_lines, key=len)
    with open("merged_file.txt", "at", encoding="utf-8") as f:
        for lines in list_of_lines:
            for line in lines:
                line = line.strip()
                f.write(line + "\n")
    return None

merge_files(file_list)

