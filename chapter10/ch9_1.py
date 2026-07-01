# 예외처리

# 두 수를 입력받아서 나눗셈해서 결과값을 출력하는 프로그램 작성
# while True:
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>")) 
#     print(" {0} / {1} = {2:.2f}".format(num1, num2, num1 / num2))
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#     continue
#   except Exception as e:
#     print(e)
#     continue
#   finally:
#     print("finally 입니다")
#   break

# print("프로그램 종료")

# 오류를 사용자가 조건에 따라서 발생시킴
# while(True) :
#     try:
#         num1 = int(input('숫자를 입력해주세요 :'))
#         num2 = int(input('숫자를 입력해주세요 :'))
#         # 조건 - 두수는 0보다 크고 10보다 작거나 같다
#         if 0 < num1 <=10 and 0 < num2 <= 10 :
#             print('{} / {} = {:.2f}'.format(num1,num2, num1/num2))
#         else :
#             raise ValueError 
#         break
#     except ValueError :
#         print('오류가 발생')
#     # except ZeroDivisionError as e:
#     #     print(f'0은 안됩니다. 다시 입력해주세요\n{e}')
#     except Exception as e :
#         print(e)
#     finally:
#         print('finally')
# print('프로그램 종료')

# 던더 메서드 만들고 실행하기
# class SpecialClass():
#   def __init__(self):
#    print("생성자가 발생하였습니다.")
# 자바 toString() 같다고 생각하면 됨.
#   def __str__(self):
#     return "내가 만들고 싶은 문자열을 만들어서 전송"
   
# sc = SpecialClass()
# print(sc)

# 사용자가 정의한 예외처리를 설계한다. (정의한 메세지를 던지기 때문에 메세지 정의해야 된다.)
# class MyException(Exception):
#   def __init__(self, message):
#     self.message = message

#   def __str__(self):
#     return "{} 메세지가 발생하였습니다.".format(self.message)
  
# # 사용자가 정의한 예외처리로 진행
# # while(True) :
#     try:
#         num1 = int(input('숫자를 입력해주세요 :'))
#         num2 = int(input('숫자를 입력해주세요 :'))
#         # 조건 - 두수는 0보다 크고 10보다 작거나 같다
#         if 0 < num1 <=10 and 0 < num2 <= 10 :
#             print('{} / {} = {:.2f}'.format(num1,num2, num1/num2))
#         else :
#             raise MyException("입력값 {0}, {1} 값이 범위에 미포함하는".format(num1,num2))
#     except ValueError :
#         print('오류가 발생')
#         continue
#     except MyException as e :
#         print("오류가 발생했습니다. 사용자가 정의한 예외가 발생되었습니다.")
#         print(e)
#         finally:
#         print('finally')
# print('프로그램 종료')



# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다. 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다. 시스템 코
# 드를 확인하고 적절한 예외처리 구문을 넣으시오.
# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리 
# 출력 메시지 : "잘못된 값을 입력하였습니다." 
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정 치킨 소진 시 
# 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료 
# 출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다." 

# [코드] 
# chicken = 10 
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작 
# while(True): 
# print("[남은 치킨 : {0}]".format(chicken)) 
# order = int(input("치킨 몇 마리 주문하시겠습니까?")) 
# if order > chicken: # 남은 치킨보다 주문량이 많을때 
# print("재료가 부족합니다.") 
# else: 
# print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." 
# .format(waiting, order)) 
# waiting += 1 
# chicken -= order

class SoldOutError:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "사용자 정의 에러.".format(self.message)

chicken = 10
waiting = 1

while(True):
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order < 1:
            raise ValueError   
    try:
        if order > chicken:
            print("재료가 부족합니다")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken <= 0:
                raise SoldOutError
    except ValueError as e:
      print(e)
      print("잘못된 값을 입력하였습니다." )
    except SoldOutError as e:
       print(e)
       print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    break
print("프로그램 종료")