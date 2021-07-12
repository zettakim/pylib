import re

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
