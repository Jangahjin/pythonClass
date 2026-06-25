# 반복문

 # 반복문 1
# list = [1,2,3,4,5]
# for no in list :
#   print("{}".format(no), end=" ")
# print("")

# # 반복문 2
# for no in [1,2,3,4,5] :
#   print("{}".format(no), end=" ")
#   print("")

# # 반복문3
for no in range(1,10,2) :
  print("{}".format(no), end=" ")
  print("")

# # 반복문4
# orders = ["햄버거","짜장면","짬뽕"]
# for data in orders:
#   print("{}".format(data), end=" ")

# # 반복문5 ( 한줄 for문 (List comprehebsion))
# students = [1,2,3,4,5]
# print(students)
# # students = [11,12,13,14,15] #변경되기를 희망
# students = [ no + 10 for no in students]
# print(students)

menu = ["햄버거","짜장면","짬뽕"]
print(menu)
menu - [len(data) for data in menu]
print(menu)

# Like_subject = ["java", "pythom","html","javascript","spring boot"]
# Like_subject = [ subject.capitalize for subject in Like_subject  ]
# print(Like_subject)

# # 반복문 6
# count = 0
# exitFlag = False
# while not exitFlag:
#     count += 1
#     print("count = {}".format(count))
#     if count >= 100:
#         exitFlag = True
      
# # 반복문 7 변수 in [ list 구조 ]
# data_list = [1,2,3,4,5]
# no = int(input("[1,2,3,4,5] 선택 입력>>"))

# # for i in data_list:
# #    if no == i:
# #     print("있어요")
# #     break
# # else:
# #     print("없어요")

# if no in data_list:
#   print("있어요")
# else:
#   print("없어요")