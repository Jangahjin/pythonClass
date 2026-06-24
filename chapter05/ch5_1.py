# 파이썬의 리스트 == 자바의 ArrayList<Object>
# 리스트 (추가: append, tkqdlq: insert, 삭제: pop, 수장: ~~[index] = 값,
# 위치: find(), index(), 카운트: count()

# subway = [10, 20, 30]
# subway.append(40)                              # 추가 [10, 20, 30, 40] 
# subway.insert(1, 100)                          # 삽입 [10, 100, 20, 30, 40]
# value = subway.pop()                           # 제거 40 [10, 20, 30, 40]
# subway[0] = 200                                # 수정 [200, 100, 20, 30]
# indexValue = subway.index(100)                 # 검색 1 [200, 100, 20, 30]
# subway.append(100)                             # 추가 [200, 100, 20, 30]
# countValue = subway.count(100)                 # 카운트 2
# subway.clear()                                 # 전체 삭제 []
# print(subway)

# subway = ['감자', '수박', '참외']
# subway.append('오이')                              # 추가 ['감자', '수박', '참외', '오이']
# subway.insert(1, '옥수수')                          # 삽입 ['감자', '옥수수', '수박', '참외', '오이']
# value = subway.pop()                           # 제거 오이 ['감자', '옥수수', '수박', '참외']
# subway[0] = '돼지감자'                             # 수정 ['돼지감자', '옥수수', '수박', '참외']
# indexValue = subway.index('옥수수')                 # 검색 1 ['돼지감자', '옥수수', '수박', '참외']
# subway.append('옥수수')                             # 추가 ['돼지감자', '옥수수', '수박', '참외', '옥수수']
# countValue = subway.count('옥수수')                 # 카운트 2
# subway.clear()                                 # 전체 삭제 []
# print(countValue)
# print(subway)

# 정렬(sort()) 역정렬(reverse())
# 원본에다 정렬 진행 / 원본이 훼손됨
subway = [90, 10, 20, 30, 40, 60]
subway.sort(reverse=True)
# subway.reverse()
print(subway)

# 원본을 훼손시키지 않는 방법 / 깊은 복사 진행으로 정렬 -> 깊은 복사 리스트 =  sorted(원본리스)
# subway = [90, 10, 20, 30, 40, 60]
# print(subway)
# newSubway = sorted(subway)
# print(newSubway)
# print(subway)

# 리스트 합집합
# mixList1 = [10, True, "호박", [1, 2, 3, 4]]
# mixList2 = [30, False, "수박"]
# print(mixList1)
# print(mixList2)

# mixList1.extend(mixList2)
# print(mixList1)