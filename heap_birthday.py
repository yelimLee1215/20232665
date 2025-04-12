import heapq
import pandas as pd
from datetime import datetime

# CSV 파일 불러오기 (같은 폴더에 있어야 함!)
df = pd.read_csv("birthdays.csv")

birthdays = []

for _, row in df.iterrows():
    name = row['이름']
    bday_raw = row['생년월일8자리(예.20040101)']
    
    if pd.notnull(bday_raw):
        raw_birthday = str(bday_raw).split('.')[0]
        try:
            birthday_date = datetime.strptime(raw_birthday, '%Y%m%d')
            heapq.heappush(birthdays, (-birthday_date.timestamp(), name, raw_birthday))
        except ValueError:
            continue  # 날짜가 이상하면 건너뛰기

# 결과 출력
print("🎂 생일이 느린 순서 Top 10")
for _ in range(min(10, len(birthdays))):
    _, name, bday_str = heapq.heappop(birthdays)
    print(f"{name}: {bday_str}")
