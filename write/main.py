import os

def open_f(path):
    for file in files:
        with open(os.path.join(path, file), encoding="UTF-8") as file_open:
            count = 0
            text = []
            for line in file_open:
                count += 1
                text.append(line.strip())
        file_info[file] = [count, '\n'.join([s for s in text])]

#
def sort(file):
    sorted_file_info = sorted(list(file.items()), key=lambda x: x[1])
    return sorted_file_info

def write_f(file_sorted):
    with open("write_file.txt", "w+", encoding="UTF-8") as file:
        for wr_f in file_sorted:
            file.write(f"{wr_f[0]}\n{wr_f[1][0]}\n{wr_f[1][1]}\n")

if __name__ == '__main__':
    path = os.path.join(os.getcwd(), "files")
    files = os.listdir(path)
    file_info = {}
    open_f(path)
    write_f(sort(file_info))


