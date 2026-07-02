# 외부패키지를 다운로드 해서 설치하는 방법
# https://pypi.org/project/beautifulsoup4/ <== 현재 시점 80만개의 패키지가 들어있음.
# 설치방법 : 복사 + 터미널에 붙여넣기
# 해당되는 패키지에 사용하는 방법들이 설명되어 있다. (Read.me)


from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 우리가 필요한 정보를 찾는 것
print(soup.find(string="bad"))

find_str = input("딩신이 찾고자 하는 단어 >>")
if soup.find(string=find_str) :
  print("원하는 데이터를 찾았습니다")
else:
  print("원하는 데이터를 찾지 못했습니다.")

print(soup.p)