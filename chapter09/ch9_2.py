# 자바 상속 (부모의 것은 내것, 자식은 반드시 super(), 오버라이딩) 다중상속(모호성) 때문에 안됨
# 파이썬 상속 (부모의 것은 내것, 자식은 반드시 부모.__init__(self, 매개변수)
# ,super(self가 들어가지 않음), 오버라이딩) 다중상속됨 (모호성 발동 안됨 : 순서가 정해져있음)

# 일반유닛(공격력이 없는 유닛)
class Unit:
   def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"{self.name} 체력: {self.hp} 이동 속도: {self.speed} 유닛이 생성되었습니다")

nurse1 = Unit("간호사", 40, 5)
nurse2 = Unit("간호사", 40, 5)
   
# 공격력이 있는 유낫(상속)
class AttackUnit(Unit):
  # 생성자
  def __init__(self, name, hp, speed, damage):
    # 다중상속때 문제가 발생하니 super 사용 금지
    # super().__init__(name, hp, speed)
    # 부모를 책임짐
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

  # 멤버함수
  def attack(self, location):
    print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

  def damaged(self, damage):
    print(f"{self.name} : {damage} 데미지를 입었습니다.")
    self.hp -= damage
    if self.hp <= 0:
      print(f"{self.name}은 파괴 되었습니다.")
    else:
      print(f"{self.name} 유닛은 체력이 {self.hp}가 남아있습니다.")


 # 화염 방사병: 공격 유닛
fireSoldier = AttackUnit("화염방사병", 40, 10, 5)


# 화염방사병 공격명령(2시 방향)
fireSoldier.attack("2시")

# 화염방사병이 공격을 받겠습니다.
fireSoldier.damaged(20)
fireSoldier.damaged(10)
fireSoldier.damaged(10)