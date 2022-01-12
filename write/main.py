import os
import operator
from pprint import pprint

files = os.listdir(os.path.join(os.getcwd(), "files"))
file_info = {}
for file in files:
    with open(os.path.join(os.getcwd(), "files", file)) as file_open:
        count = 0
        text = []
        for line in file_open:
            count += 1
            text.append(line.strip())
    file_info[file] = [count, text]

sorted_file_info = sorted(file_info.items(), key=lambda x : x[1])
# pprint(sorted_file_info)

# print(sorted_file_info[2][1][1][0])

with open("write_file.txt", "w+") as file:
    for wr_f in sorted_file_info:
        file.write(wr_f[0] + '\n')
        count = int(wr_f[1][0])
        file.write(str(wr_f[1][0])+ '\n')
        for i in range(count):
            file.write(wr_f[1][1][i]+ '\n')






