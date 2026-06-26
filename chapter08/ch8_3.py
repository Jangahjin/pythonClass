# pickle

import pickle 
# binary 파일로 저장할때 -> encoding 필요하지 않음

# profile_handle = open('profile.pickle','wb')

# profile_dic = {
#     '이름' : 'kdj',
#     '나이' : '62',
#     '취미' : ['등산', '배드민턴', '탁구']
#     }

# dictionary를 사용하기 다시 위해서 pickle 파일에 저장
# pickle.dump(profile_dic, profile_handle)
# profile_handle.close()

# pickle 파일을 다시 가져와 사용
# profile_handle = open('profile.pickle','rb')
# list_dic = pickle.load(profile_handle)

# for key, item in list_dic.items() :
#     print(key, item)

# profile_handle.close()

# 파일을 한번에 열고, 자동으로 닫기 : with문 (자바 - try with resouces)
# with open('profile.pickle', 'rb') as profile_handle :
#     list_dic = pickle.load(profile_handle)
#     for key, item in list_dic.items() :
#         print(key, item)
#         if key == '취미' :
#             for data in item :
#                 print('{} : {}'.format(key, data))

# print('with문은 profile_handle.close() 안해도 된다.')

# 일반파일을 with으로 처리하는 방식
# with open('data.txt', 'w', encoding='utf8') as data_handle:
#     data_handle.write('파이썬\n')
#     data_handle.write('자바\n')
#     data_handle.write('스프링 부트\n')

with open('data.txt', 'r', encoding='utf8') as data_handle:
    print(data_handle.read())
