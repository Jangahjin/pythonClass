# 숫자 자료형
print(5)
print(-5)
print(3.141592)
print(-3.141592)


#숫자 자료형 연산(+,=,*,/,%,//)
#연산식순서(단항, 이항, 산술, 쉬프트, 비교, 논리, 삼항, 치환, 컴마)
# print(5+5)
# print(2*8)
# print(6/4) #1.5
# print(6%4) #2 -> 나머지
# print(6//4) #1*** -> 몫
# print(4 * (5 / 3)) #연산우선순위()

# 문자열 자료형
print("여름과일" + "수박")                         #문자열 + 문자열 => 문자열
print("당신의 나이는" + str(23))                   #문자열 + 숫자열 => 계산 안됨 / 숫자열 => 문자열로 변환 ***
print(int("54") + 24)                              #문자열 + 숫자 => 계산 안됨 / int(문자열)로 변환
print("&"*10)                                      # "&&&&&&&&&&&&&" *** 
print('오렌지','토마토')                           # , => 한 칸 띄워쓰기
print('파이썬')
# escape 문자 \n => new Line    \r =>return   \t => tab 키 기능
print('오늘은 \"정말로\" 공부를 열심히 했습니다.')     #문자 강조
print('오늘은 "정말로" 공부를 열심히 했습니다.')     #문자 강조
print("오늘은 '정말로' 공부를 열심히 했습니다.")     #문자 강조
   
# boolean 형
print(10 > 5)
print(10 < 5)
print(True)
print(False)
print(not(10 > 5))     #파이썬은 !가 아닌 not (not(10 > 5))

# 변수 (변하는 값을 저장하기 위한 방법)
# 전역변수, 지역변수
# print(name+"씨 당신이 좋아하는 동물은 무엇입니까?")
# print("내가 좋아하는 동물은 "+animal+"입니다. 그리고 이름은 "+animalName+"입니다.")
# print(""+animalName+"의 나이는 "+str(age)+"살이고 "+hobby+"을 좋아합니다.")

name = "아진"
animal = "고양이"
animalName = "뽀삐"
age = "4"
hobby = "먹기"

# 문자열 => 숫자형 변환
print(int("3") +4)
print(float("3.5") + 4.2) #int("3.5")
print(int("3.5"))
# print(int("삼")) ValueError: invalid literal for int() with base 10: '삼'

#type 확인
print(type(3))                 # <class 'int'>
print(type("3"))               # <class 'str'>
print(type('a'))               # <class 'str'>
print(type(3.5))               # <class 'float'>
print(type(True))              # <class 'bool'>
print(type(str(3)))            # <class 'str'>

#변수 (조심해야할 부분) 변수 = 상수에 의해 결정이 된다.
age = 10
print(type(age))               #<class 'int'>
age = age > 20
print(type(age))               #<class 'bool'>

# 주석
# 한줄주석 # 이용하면 된다.

# 여러줄주석
"""
print("여기에 있는 모든 내용은 주석처리다.")
print("여기에 있는 모든 내용은 주석처리다.")
print("여기에 있는 모든 내용은 주석처리다.")
print("여기에 있는 모든 내용은 주석처리다.")
"""
...
print("여기에 있는 모든 내용은 주석처리다.")
print("여기에 있는 모든 내용은 주석처리다.")
print("여기에 있는 모든 내용은 주석처리다.")
print("여기에 있는 모든 내용은 주석처리다.")
...