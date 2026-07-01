# class
# 클래스명은 Unit, 멤버변수: 이름 name, 체력 hp, 공격력 damage, 스피드 speed
# 일반유닛
class Unlt:
  # 생성자
  def __init__(self, name, hp, damage, spped):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.spped = spped
    print(f"유닛이름: {self.name} 체력: {self.hp} 공격력:{self.damage} 이동속도:{self.spped} 생성완료")


# 공격유닛생성
# 클래스명은 Attackunit, 멤버함수: name, hp, damage, spped
class AttackUnit:
  def __init__(self, name, hp, damage, spped):
     self.name = name
     self.hp = hp
     self.damage = damage
     self.spped = spped
     print(f"{self.name} 유닛이 체력:{self.hp}, 공격력:{self.damage}, 이동속도:{self.spped} 유닛이 생성")

  # 멤버함수
  def Attack(self, location):
    print(f"{self.name}가 {location}시 방향으로 공격력{self.damage} 으로 공격하고 있습니다.")

  # 멤버함수 (공격을 당하는 함수)
  def damaged(self, damage):
     print(f"{self.name} 상대방으로부터 공격력{damage}으로 공격을 받고 있습니다. ")
     self.hp = self.hp - damage
     print(f"{self.name} 공격을 받아 남아 있는 체력{self.hp} 입니다.")

     if self.hp <= 0:
       print(f"{self.name} 유닛은 사망하셨습니다.")

# 보병
soldier1 = AttackUnit("보병1", 40, 5 ,10)
soldier2 = AttackUnit("보병2", 40, 5 ,10)
soldier3 = AttackUnit("보병3", 40, 5 ,10)
tank1 = AttackUnit("탱크1", 130, 35 ,10)
tank2 = AttackUnit("탱크2", 130, 35 ,10)

# 날아다니면서 공격하는 유닛
# 사용되는 객체가 자시만의 멤버변수를 추가하면 자기자신에만 해당이 된다.
airunit1 = AttackUnit("전투기1", 200, 30 ,40)
airunit1.fly = True

if airunit1.fly == True:
  print(f"{airunit1.name} {airunit1.hp} {airunit1.damage} {airunit1.spped} 공중유닛: {airunit1.fly}")

# if soldier3.fly == True:
#   print(f"{soldier3.name} {soldier3.hp} {soldier3.damage} {soldier3.spped} 공중유닛: {soldier3.fly}")
# else:
#    print(f"{soldier3.name} {soldier3.hp} {soldier3.damage} {soldier3.spped}")


# 배열관리 (공격지시)
attack_list = []
attack_list.append (soldier1)
attack_list.append (soldier2)
attack_list.append (soldier3)
attack_list.append (tank1)
attack_list.append (tank2)
attack_list.append (airunit1)

for unit in attack_list:
  unit.Attack(10)