import requests
from bs4 import BeautifulSoup

def collect_melon_top100():
    """
    멜론 실시간 차트 TOP 100의 노래 제목, 가수, 앨범, 순위를 수집해 리스트 형태로 반환합니다.
    실제 구조 변경 시 CSS 선택자나 URL 등을 수정해야 합니다.
    """
    # 멜론 차트 주소(예시). 상황에 따라 다른 차트(일간/주간 등) 링크를 사용할 수도 있음.
    base_url = "https://www.melon.com/"

    # 일반 브라우저에서 접근하는 것처럼 User-Agent 헤더를 추가
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.85 Safari/537.36"
        )
    }

    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print("페이지 요청 실패. 상태 코드:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # 1~50위 테이블(클래스 lst50), 51~100위 테이블(클래스 lst100)를 각각 검색
    chart_1_50 = soup.select('tr.lst50')
    chart_51_100 = soup.select('tr.lst100')
    chart_list = chart_1_50 + chart_51_100  # 1~100위 합치기

    top100_data = []
    for item in chart_list:
        # 순위
        rank_tag = item.select_one('span.rank')
        rank = rank_tag.get_text(strip=True) if rank_tag else None
        
        # 곡명
        title_tag = item.select_one('div.ellipsis.rank01 > span > a')
        title = title_tag.get_text(strip=True) if title_tag else None
        
        # 가수명
        singer_tag = item.select_one('div.ellipsis.rank02 > a')
        singer = singer_tag.get_text(strip=True) if singer_tag else None
        
        # 앨범명
        album_tag = item.select_one('div.ellipsis.rank03 > a')
        album = album_tag.get_text(strip=True) if album_tag else None
        
        top100_data.append({
            'rank': rank,
            'title': title,
            'singer': singer,
            'album': album
        })

    return top100_data

if __name__ == "__main__":
    result = collect_melon_top100()
    
    # 결과 출력 예시
    for song in result:
        print(
            f"{song['rank']}위 | "
            f"곡명: {song['title']} | "
            f"가수: {song['singer']} | "
            f"앨범: {song['album']}"
        )
        