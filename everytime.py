import requests
from bs4 import BeautifulSoup

# (예시용) 저장된 시간표 HTML 파일을 불러옴
with open("timetable.html", "r", encoding="utf-8") as file:
    html = file.read()

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 📌 과목 정보가 들어 있는 div 탐색 (class는 실제 구조에 맞게 수정 필요)
subjects = soup.find_all("div", class_="subject")

# 예시 결과용 수동 데이터 (스크래핑 성공 시 여기에 append하는 구조)
timetable = {
    '월': [],
    '화': [],
    '수': [],
    '목': [],
    '금': []
}

# 예시용 수동 파싱 결과 (실제 스크래핑에서는 아래 데이터를 자동 추출)
example_data = [
    ('월', '10:00', '13:00', '미디어콘텐츠의 이해'),
    ('월', '14:00', '17:00', 'AI응용빅데이터프로그램'),
    ('화', '10:00', '13:00', '미디어읽기와 표현'),
    ('화', '14:00', '17:00', '캡스톤디자인워크숍'),
    ('수', '14:00', '17:00', '전공탐색 (미콘리터러리시실습)'),
]

# 파싱된 데이터를 timetable에 삽입
for day, start, end, subject in example_data:
    timetable[day].append((start, end, subject))

# ✅ 출력 함수
def print_schedule(tt):
    print("📅 다은이의 일주일 스케줄표 📅\n")
    for day in ['월', '화', '수', '목', '금']:
        print(f"▶ {day}요일")
        if not tt[day]:
            print("  ❌ 수업 없음")
        else:
            for start, end, subject in tt[day]:
                print(f"  ⏰ {start} ~ {end}  -  {subject}")
        print()
        