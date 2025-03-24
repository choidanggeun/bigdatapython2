import requests
from bs4 import BeautifulSoup

def get_titles(url):
    # 1. 웹페이지 요청 보내기
    response = requests.get(url)
    
    # 2. 응답에서 HTML 문서 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. 원하는 태그 선택 (예: h2 태그 중 클래스가 "title"인 요소)
    titles = soup.select('h2.title')
    
    # 4. 텍스트만 추출
    return [title.get_text().strip() for title in titles]

if __name__ == "__main__":
    url = "http://example.com"
    extracted_titles = get_titles(url)
    for i, t in enumerate(extracted_titles, 1):
        print(f"{i}. {t}")