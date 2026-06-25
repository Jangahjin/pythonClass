# if 문


# "아파요"
# message = input("당신의 몸 상태는(아파요/좋아요)>>")
# if message == "좋아요":
#   print("몸 상태가 좋으니 놀러 가요.")
# else: 
#     print("몸 상태가 좋지 않으니 집에서 쉬어요.")

# 점수 입력을 받아서 등급을 표시하는 프로그램(A,B,C,D,F)
# score =int(input("당신의 수학 점수는 >>"))
# print(score, type(score))

# if score >= 90:
#   grade = "A"
# elif 80 <= score < 90 :
#   grade = "B"
# elif 70 <= score < 80 :
#   grade = "C"
# elif 60 <= score < 70 :
#   grade = "D"
# else:
#   grade = "F"

# print(f"당신의 점수: {score}점 \n 등급: {grade}")


# 파이썬 3.10 이상부터 사용 가능 (자바:swith case, match case)
# score =int(input("당신의 수학 점수는 >>"))
# print(score, type(score))

# match score // 10: 
#   case 10 | 9:
#    grade = "A"
#   case 8:
#    grade = "B"
#   case 7:
#    grade = "C"
#   case 6:
#    grade = "D"
#   case _:
#    grade = "E"
# print(f"당신의 점수: {score}점 \n 등급: {grade}")


# match case 확장가능
score =int(input("당신의 수학 점수는 >>"))
print(score, type(score))

match score // 10: 
  case _ if 90<= score <= 100:
   grade = "A"
  case _ if 80<= score <= 90:
   grade = "B"
  case _ if 70<= score <= 80:
   grade = "C"
  case _ if 60<= score <= 70:
   grade = "D"
  case _:
   grade = "E"
print(f"당신의 점수: {score}점 \n 등급: {grade}")