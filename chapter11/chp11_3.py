# package === 폴더와 유사하다 (여러개 모듈을 포함하고 있다.)

# travel 이라는 패키지 속에 thailand에 해당되는 모듈 가져옴
# 조심해야 될 부분 (import 안에 해당되는 클래스나 함수 가져오면 안됨)
import travel.thailand
# import travel.vietnam

thailand_obj = travel.thailand.ThailandModule()
thailand_obj.detail_travel()

# vietnam_obj = travel.vietnam.VietnamModule()
# vietnam_obj.detail_travel()


# 자바에서 사용되는 import 기능과 같다.
# 패키지에 해당되는 모듈을 가져오면 된다.
# from travel.thailand import ThailandModule
# thailand_obj = ThailandModule()
# thailand_obj.detail_travel()

# from travel.vietnam import VietnamModule
# vietnam_obj = VietnamModule()
# vietnam_obj.detail_travel()

# 해당되는 패키지에  모두 모듈을 가져오는 방법
# 해당되는 패키지에서 thailand 공개함
from travel import *

# v_obj = vietnam.VietnamModule()
# v_obj.detail_travel()

t_obj = thailand.ThailandModule()
t_obj.detail_travel()

# 패키지 모듈위치
# import inspect
# import random

# inspect를 사용해서 random 패키지 위치를 검사
# print(inspect.getfile(random))

# import inspect
# from travel import *

# print(inspect.getfile(thailand))


# t_obj2 = thailand.ThailandModule()
# t_obj2.detail_travel()

# v_obj2 = vietnam.VietnamModule()
# v_obj2.detail_travel()