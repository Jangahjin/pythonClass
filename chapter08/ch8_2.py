# 파일 입출력 데이타 베이스 => 파일에 저장하며 가져오고, 저장하고, 삭제하고, 수정하고


# score.txt utf-8 방식으로 입력하고, 새로 쓸 거야
# file_handle = open("score.txt", "w", encoding="utf8")
# print("국어: 90",file=file_handle)
# print("영어: 100",file=file_handle)
# print("수학: 100",file=file_handle)
# file_handle.close()

# score.txt 추가 기능을 설정해서 객체를 생성해야 된다.
# file_handle = open("score.txt","a",encoding="utf-8")
# print("자바: 100",file=file_handle)
# print("파이썬: 100",file=file_handle)
# file_handle.close()

# score.txt 추가 기능을 설정해서 객체를 생성해야 된다.
# file_handle = open("score.txt","a",encoding="utf-8")
# write() /n 기능이 없으니 마지막에 \n 가눙울 입력해야 함.
# file_handle.write("HTML : 100\n")
# file_handle.write("CSS :90\n ")
# file_handle.close()

# 파일에서 "r" 사용하는 것 => 읽어옴 
# file_handle = open("score.txt","r",encoding="utf-8")
# print(file_handle.read()) #모두 읽어버린다.
# file_handle.close()

# file_handle = open("score.txt","r",encoding="utf-8")
# print(file_handle.readline(),end="") 
# print(file_handle.readline(),end="") 
# print(file_handle.readline(),end="") 
# print(file_handle.readline(),end="") 
# print(file_handle.readline(),end="") 
# file_handle.close()


# file_handle = open("score.txt","r",encoding="utf-8")
# exit_Flag = False
# while not exit_Flag:
#  line = file_handle.readline()
# #  EOF이면 line False
#  if not line:
#   print(line, end="")
# else:
#  exit_Flag = True
 
 
# file_handle.close()


file_handle = open("score.txt", "r", encoding="utf-8")
line_list = file_handle.readlines()
file_handle.close()
# print(list, type(list))
for data in list:
  print(data, end="")


