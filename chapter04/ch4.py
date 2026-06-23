# 문자열 """ ~~~~ """ : 여백 또는 공백 기능까지 모두 포함해서 문자열 취급 ***


# message = "파이썬을 공부하고 있습니다."
# print(message, type(message))

# message2 = """
# 파이썬을
# 공부
# 하고 있습니다.

# """
# print(message2, type(message2))


# 슬라이싱

# jumin = "990829-1550823"

# print("사용자 성별번호 :", jumin[7])
# print("사용자 태어난 연도 :", jumin[0:2]) 
# print("사용자 태어난 월 :", jumin[2:4]) 
# print("사용자 태어난 일 :", jumin[4:6]) 
# print("사용자 태어난 생년월일 :", jumin[0:6]) 
# print("사용자 태어난 생년월일 :", jumin[:6]) 
# print("주민번호 뒷자리 :", jumin[7:]) 
# print("주민번호 뒷자리 검증번호 이전까지:", jumin[7:-1]) 
# print("주민번호 문자열 길이:", len(jumin)) 

# # 반복문을 이용해서 주민번호 한자리씩을 출력하시오. '-' 생략하시오.
# for i in range(0, len(jumin)):
#    if jumin[i] == "-":
#        continue
#    print(jumin[i], end=" ")]

# 문자열 처리함수
# message = "python os Amazing"

# print(message.lower()) #"python os Amazing"
# print(message.upper()) #"PYTHON OS AMAZING"
# print(message.isupper()) #"False"
# print(message[0].isupper()) #"True"
# print(message[1:3].islower()) #"True"
# # replace *** 문자열에서 필요한 영역을 다른 글로 교체가 가능(자바에선 이런 기능을 사용하려면 많은 메모리가 필요함)
# print(message.replace("python","java")) #"java os Amazing"

# # find, index 차이점을 체크
# # find 진행에서 찾는 것이 없으면 -1로, 다음 문장을 실행
# # index 진행에서 찾는 것이 없으면 valueError 발생시키고 다음 문장 실행 안함.
# # index 개념보다는 find를 사용하는 것이 좋다. ***  

# message = "python os Amazing"
# findIndex = message.index("n") 
# print(findIndex) #5

# findIndex2 = message.index("n", findIndex+1)
# print(findIndex2) #15

# findIndex3 = message.index("os")
# print(findIndex3) #7

# findIndex4 = message.index("kim") #찾지 못하면 valueError (-1)
# print(findIndex4) #-1
# print("hello")

# findIndex5 = message.index("n", 6, -1)
# print(findIndex5)


# 문자열에서 자주 사용하는 방법: sliceing [], find(), count(), replace()
message = "python os Amazing"
print(message.count("n")) #2
print(message.count("k")) #0
print(len(message)) #17

# 문자열포맷
print("java"+"python")
print("java"+"python") # java python (주석 오타 수정)

age = 20
print("나는 %d살입니다." % 20)
print("나는 %d살입니다." % age)
print("나는 {}살입니다.".format(age)) 
print(f"나는 {age}살입니다.")

like = "파이썬" 
print("나는 %s을 좋아합니다." % like)
print("나는 {}을 좋아합니다.".format(like))

grade = "A"
print("java언어의 정수는 %c 등급입니다." % "A")
print("java언어의 정수는 %c 등급입니다." % grade)
print("java언어의 정수는 {} 등급입니다.".format(grade)) 

score = 96.59
print("점수는 %f 입니다" % 96.59) 
print("점수는 %f 입니다" % score)

flag = True
print("내가 자바를 좋아하는 것은 %s 입니다." % flag)
print("내가 자바를 좋아하는 것은 %s 입니다." % "true")

fruit1 = "수박"
fruit2 = "참외"

print("내가 좋아하는 과일은 %s와 %s 입니다." % ("수박", "참외"))
print("내가 좋아하는 과일은 %s와 %s 입니다." % (fruit1, fruit2))
print("내가 좋아하는 과일은 {0}와 {1} 입니다.".format(fruit1, fruit2)) 
print("내가 좋아하는 과일은 {1}와 {0} 입니다.".format(fruit1, fruit2)) 

# 탈출문자 \n \t \b \r \' \"
print("파이썬 \n 자바")
print("파이썬 \t 자바")
print("파이썬 \b 자바")
print("파이썬 \r 자바")
print("파이썬 \' 자바")
print("파이썬보다 \"자바\"가 더 좋아요")
print('파이썬보다 \'자바\'가 더 좋아요')

print("D:\javaTest")