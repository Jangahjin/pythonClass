# 라이브러리 함수 기능만 있는 모듈

# 일반인이 영화를 관람했을 때 요금을 계산하는 라이브러리
def price(count):
  price = 14000
  print(f"{count}명은 영화의 1인당 가격{price}이며 전체 금액은 {count * price} 입니다.")

# 조조 영화를 관람했을 때 요금을 계산하는 라이브러리 (40% 할인)
def price_morning(count):
  price = int(14000 * 0.6)
  print(f"{count}명은 영화의 1인당 조조 가격{price}이며 전체 금액은 {count * price} 입니다.")

# 군인 영화를 관람했을 때 요금을 계산하는 라이브러리 (60% 할인)
def price_soldier(count):
  price = int(14000 * 0.4)
  print(f"{count}명은 영화의 1인당 군인 가격{price}이며 전체 금액은 {count * price} 입니다.")
