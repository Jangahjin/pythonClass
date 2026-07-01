# 다중 상속 진행 (모호성을 해결하는 방법을 구현)

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 체력: {self.hp} 이동 속도: {self.speed} 유닛이 생성되었습니다")
  
    def move(self, location):
     print(f"{self.name} 유닛이 {location} 방향으로 가고 있습니다.")

# 공격력이 있는 유닛(상속)
class AttackUnit(Unit): 
    # 생성자
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    # 멤버함수
    def attack(self, location):
        # self.flying_speed 대신 self.name으로 수정
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage): # 메서드 이름을 damaged로 통일
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}은 파괴 되었습니다.")
        else:
            print(f"{self.name} 유닛은 체력이 {self.hp}가 남아있습니다.")

# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    # 멤버함수
    def fly(self, name, location): # name을 인자로 받도록 수정
        print(f"{name}이 {location} 방향으로 날아가고 있습니다. [속도: {self.flying_speed}]")

# 다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, speed, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, speed, damage)
        Flyable.__init__(self, flying_speed)

  # 오버라이딩

    def move(self, location):
     print(f"{self.name} 공중유닛이 {location} 방향으로 {self.flying_speed}로 가고 있습니다.")


# 공격 기능을 가진 interceptor 객체 생성
interceptor = FlyableAttackUnit("요격기", 300, 0, 80, 200)
# interceptor.attack("2시방향")
# interceptor.damaged(60) 
# interceptor.fly(interceptor.name, "4시")
interceptor.move("3시")
