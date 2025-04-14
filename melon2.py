import requests
 from bs4 import BeautifulSoup
 import random
 import time
 
 # ======================== #
 # 향수 데이터 수집 (Fragrantica)
 # ======================== #
 headers = {"User-Agent": "Mozilla/5.0"}
 fragrantica_url = "https://www.fragrantica.com/perfume-rating/"  # 예시 URL, 실제로 작동하려면 정확한 URL 필요
 response = requests.get(fragrantica_url, headers=headers)
 soup = BeautifulSoup(response.text, "html.parser")
 
 # 향수 랭킹 추출 (사이트 구조에 맞게 선택자 조정 필요)
 scents = soup.select(".cell2 a")
 perfumes = [scent.get_text(strip=True) for scent in scents[:10]]  # 상위 10개만 사용
 
 # 추가 향수 데이터
 extra_perfumes = [
     "코튼", "머스크", "화이트로즈", "가드니아", "블랙베리", "블랙체리", "아쿠아마린", "르네상스",
     "라벤더", "로즈마리", "라일락", "랑데뷰", "히아신스", "백합", "라임", "레더"
 ]
 perfumes.extend(extra_perfumes)
 
 # ======================== #
 # 메뉴 출력
 # ======================== #
 print("==============================")
 print("        향수 추천 시스템")
 print("==============================")
 print("1. 인기 향수 랭킹 보기")
 print("2. 인기 향수 Top 5")
 print("3. 랜덤 향수 추천")
 print("4. 향수 이름 검색")
 print("==============================")
 
 n = input("메뉴를 선택하세요 (1~4): ")
 
 # ======================== #
 # 메뉴 기능
 # ======================== #
 
 if n == "1":
     print("\n📌 인기 향수 랭킹:")
     for i, perfume in enumerate(perfumes, 1):
         print(f"{i}. {perfume}")
 
 elif n == "2":
     print("\n💎 인기 향수 Top 5:")
     for i, perfume in enumerate(perfumes[:5], 1):
         print(f"{i}. {perfume}")
 
 elif n == "3":
     print("\nAI야 향수를 추천해줘!")
     print("""
     알겠습니다.
     제가 열심히 분석해서
     고객님께 향수를 추천합니다
     """)
     dd = ["두", "두", "두", "두둥"]
     for d in dd:
         print(d)
         time.sleep(1)
     ai_perfume = random.choice(perfumes)
     print(f"✨ 추천 향수는: {ai_perfume} 입니다.")
 
 elif n == "4":
     keyword = input("🔍 검색할 향수 이름을 입력하세요: ")
     results = [p for p in perfumes if keyword in p]
     if results:
         print("\n🔎 검색 결과:")
         for r in results:
             print(f"- {r}")
     else:
         print("😢 해당 향수를 찾을 수 없습니다.")
 
 else:
     print("⚠️ 1~4 중에서 입력해주세요.")
     