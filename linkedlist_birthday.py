from circularDoublyLinkedList import CircularDoublyLinkedList
import pandas as pd

# 조원 명단
my_team = [
    "이원진", "박찬미", "박혜린", "전민서", "임서영", "이서현", "안소민", "이채민",
    "이예림", "이수빈", "김효리", "이지영", "이진", "김나림", "이가연"
]

# 생일 데이터 읽기
df = pd.read_csv("birthdays.csv")

# 리스트 생성
cdll = CircularDoublyLinkedList()

for _, row in df.iterrows():
    name = row['이름']
    bday_raw = row['생년월일8자리(예.20040101)']
    
    if pd.notnull(bday_raw):
        bday_str = str(bday_raw).split('.')[0]
        cdll.insert((name, bday_str))

# 같은 조 친구들만 출력
print("🌸 내 조원들의 생일 🌸")
for name, bday in cdll:
    if name in my_team:
        print(f"{name}: {bday}")
