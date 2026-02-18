import os

# path = "hometask_os.txt"
# encoding = "utf-8"

# 1

# with open(
#     file = path,
#     mode = "w",
#     encoding = encoding,
# ) as f:
#     for i in range(6):
#         f.write(input() + "\n")
#
# # 2
#
# with open(
#     file = path,
#     mode = "a",
#     encoding = encoding,
# ) as f:
#     for i in range(3):
#         f.write(input() + "\n")

# 3

# with open(
#     file = path,
#     mode = "r",
#     encoding = encoding,
# ) as f:
#     print(len(f.read().replace("\n", "")))

# 4

# with open(
#     file =path,
#     mode="r",
#     encoding=encoding
# ) as f:
#     ls = []
#     for line in f:
#         line = line.strip('\n')
#         ls.append(line)
#
# with open(
#     file =path,
#     mode="w",
#     encoding=encoding
# ) as f:
#     f.write(str(ls))

# 5

# with open(
#     file =path,
#     mode="r",
#     encoding=encoding
# ) as f:
#     ls = []
#     for line in f:
#         line = line.strip('\n')
#         if line[-1] == "!":
#             ls.append(line)
#
# with open(
#     file =path,
#     mode="w",
#     encoding=encoding
# ) as f:
#     for item in ls:
#         f.write(item + "\n")

# 6

import json

# path = "flights.json"
# city = input("Введите город: ")
# with open(
#         file = path,
#         mode = "r",
#         encoding="utf-8"
# ) as f:
#     ls = []
#     data = json.loads(f.read())
#     for d in data:
#         if d["destination"] == city:
#             ls.append(d["flight_number"])
#
# for i in ls:
#     print(i)

# 7

# path = "student_grades.json"
# with open(
#         file = path,
#         mode = "r",
#         encoding="utf-8"
# ) as f:
#     data = json.loads(f.read())
#     lst_student = []
#     for lst in data:
#         if sum(lst["grades"]) / len(lst["grades"]) > 7:
#             lst_student.append(lst["full_name"] + " - средний бал: " + str(sum(lst["grades"]) / len(lst["grades"])))
#
# for i in lst_student:
#     print(i)