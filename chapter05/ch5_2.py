# 딕셔너리(key, value)

# key 값은 절대 중복 허용하지 않는다. value 값은 중복 허용
# caninet = {3: '푸', 100:'피글렛', 3:'수푸', 4:'피글렛'} #{3: '수푸', 100: '피글렛', 4: '피글렛'}
# caninet[5] = '쿠우' # 추가 : {3: '수푸', 100: '피글렛', 4: '피글렛', 5: '쿠우'}
# del caninet[5] # 삭제 : {3: '수푸', 100: '피글렛', 4: '피글렛'}
# caninet[4] = '피글렛2' # 수정: {3: '수푸', 100: '피글렛', 4: '피글렛2'}
# print( 3 in caninet) #키값이 존재하면 True
# print( 7 in caninet) #키값이 존재하면 False
# print(caninet)

# key값 value값 가져오는 방법 = items(두 값 모두 가져옴)
caninet = {100: '피글렛', 3:'수푸', 4:'피글렛2'}
print(caninet.keys()) #dict_keys([100, 3, 4])
print(caninet.values()) #dict_values(['피글렛', '수푸', '피글렛2'])
print(caninet.items()) #dict_items([(100, '피글렛'), (3, '수푸'), (4, '피글렛2')])

# for 문을 출력하시오. (키값 => 조회 value값 출력)
caninet = {100: '피글렛', 3:'수푸', 4:'피글렛2'}

keyList = caninet.keys()
for key in keyList:
  print(caninet[key])

# 피글렛
# 수푸
# 피글렛2

# 전체 삭제하는 기능
caninet = {}
