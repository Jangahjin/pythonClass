# 내 부모들을 가져와서 사용하기 import 방법

# import chp11_1
# chp11_1.price(3)
# chp11_1.price_morning(3)
# chp11_1.price_soldier(3)

# 가져온 모듈 별칭
# import chp11_1 as tm
# tm.price(3)
# tm.price_morning(3)
# tm.price_soldier(3)

# 가져온 모듈 별칭없이 바로 사용
# from chp11_1 import *
# price(3)
# price_morning(3)
# price_soldier(3)


# 가져온 모듈 별칭없이 바로 price 이것만 사용
from chp11_1 import price, price_morning, price_soldier
price(3)
price_morning(3)
price_soldier(3) #import 안돼서 사용할 수 없음.

# 가져온 모듈 별칭없이 바로 price 이것만 사용(별칭을 이용해서 사용가능)
from chp11_1 import price as p
p(3)

