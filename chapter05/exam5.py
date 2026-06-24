# Quiz) 게임에서 플레이어가 얻은 점수들을 가진 scores 리스트가 있다. 가장 높은 점
# 수를 찾는 프로그램을 작성해 보세요. scores = [120, 150, 180, 200, 170] 
# 힌트) max_score 변수를 하나 생성해 준다.

# 실행결과
# 최고점수 : 200

score = [120, 150, 180, 200, 170] 
max_score = max(score)
print(f'최고점수 :{max_score}')



# Quiz)게임에서 각 방에 숨겨진 아이템 개수를 나타내는 2차원 리스트가 있다. 모든 
# 방을 돌아다니며 아이템을 수집하는 프로그램을 작성하세요. 아이템이 없는 방은 0
# 으로 표시된다.
# rooms = [ [3, 1, 2], [2, 0, 1], [1, 3, 2] ] 
# 힌트) sum(리스트)는 리스트의 합계를 계산해 준다.
# for room in rooms:
# total += sum(room)
# 실행결과
# 총 수집한 아이템 수 : 15

rooms = [ [3, 1, 2], [2, 0, 1], [1, 3, 2] ] 
total = 0
for room in rooms:
 total += sum(room)
print(f"총 수집한 아이템 수 : {total}")




# Quiz) 여러 회사의 주식 가격이 회사별로 딕셔너리에 리스트로 저장되어 있다. 각 
# 회사별 주식 가격의 평균을 계산하는 프로그램을 작성하세요.
# stock_prices = {
# '삼성전자': [81000, 81500, 82000],
# 'SK하이닉스': [140000, 141000, 139500],
# '네이버': [350000, 355000, 345000]
# }
# 실행결과
# # 삼성전자 평균 주식 가격: 81500
# # SK하이닉스 평균 주식 가격: 140166 
# # 네이버 평균 주식 가격: 350000

# stock_prices = {
# '삼성전자': [81000, 81500, 82000],
# 'SK하이닉스': [140000, 141000, 139500],
# '네이버': [350000, 355000, 345000]
# }

# keyList = stock_prices.keys()
# print(keyList)

# for key in keyList:
#   value = stock_prices[key]
#   total = 0
#   for data in value:
#     total += data
#   # print("{} 평균 주식 가격: {}".format(key,round(sum/len(value), 2)))
#   print("{} 평균 주식 가격: {}".format(key,round(total/ len(value), 2)))


# for key, value in stock_prices.items():
  # print(key, "평균 주식 가격", round(sum(value)/len(value),2))



#   Quiz) 여러 회사의 주식 정보가 다음과 같은 형식으로 저장되어 있다. 각 회사별로 '
# 최고가'와 '최저가'를 출력하는 프로그램을 작성하세요.
# stocks_info = {
# '삼성전자': {'최고가': 85000, '최저가': 80000, '현재가': 82000},
# 'SK하이닉스': {'최고가': 145000, '최저가': 139000, '현재가': 140500},
# '네이버': {'최고가': 360000, '최저가': 340000, '현재가': 350000}
# }
# 실행결과
# 삼성전자 -최고가: 85000, 최저가: 80000 SK하이닉스 -최고가: 145000, 최저가: 
# 139000 네이버 -최고가: 360000, 최저가: 340000




stocks_info = {
'삼성전자': {'최고가': 85000, '최저가': 80000, '현재가': 82000},
'SK하이닉스': {'최고가': 145000, '최저가': 139000, '현재가': 140500},
'네이버': {'최고가': 360000, '최저가': 340000, '현재가': 350000}
}

# keyList = stocks_info.keys()
# for key in keyList:
#   value = stocks_info[key] #{'최고가': 85000, '최저가': 80000, '현재가': 82000}
#   print(value, value['최고가'],value['최저가'])
#   print("{}-최고가 : {}, 최저가 : {}".format(key, value['최고가'], value['최저가']))

for key, value in stocks_info.items():
  # print(key, value)
  print("{}-최고가 : {}, 최저가 : {}".format(key, value['최고가'], value['최저가']))