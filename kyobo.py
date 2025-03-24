import requests
from bs4 import BeautifulSoup

def get_kyobo_top10():
    """
    교보문고 베스트셀러 Top 10 목록을 수집해 반환합니다.
    실제 교보문고 사이트 구조가 변경될 수 있으므로, 
    HTML 태그, 클래스명, URL 등을 확인 후 적절히 수정하세요.
    """
    # 교보문고 베스트셀러 페이지(예시)
    # 다른 카테고리, 날짜별 페이지 등 필요 시 URL 변경 가능
    base_url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=Dla"
    
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

    # 실제 HTML 구조와 맞지 않을 수 있으므로, 
    # 교보문고 사이트 열람 후 Selector를 확인해서 수정하세요.
    # 예: 베스트셀러 목록을 감싸는 ul/ol/li 태그 구조를 찾은 뒤 해당 클래스/태그를 select()
    book_items = soup.select('ul.list_type01 li')

    # 상위 10개만 추출(실제로는 20~30권 이상 표시될 수 있음)
    top10_books = book_items[:10]

    result = []
    for idx, item in enumerate(top10_books, start=1):
        # 책 제목
        title_tag = item.select_one('div.title a')
        title = title_tag.get_text(strip=True) if title_tag else None

        # 저자
        author_tag = item.select_one('div.author')
        # 저자 정보가 여러 줄로 표시될 수 있으므로 필요한 부분만 정제
        author = author_tag.get_text(separator=" ", strip=True) if author_tag else None

        # 출판사
        pub_tag = item.select_one('div.author > a:last-child')
        publisher = pub_tag.get_text(strip=True) if pub_tag else None

        # 가격
        price_tag = item.select_one('div.price strong')
        price = price_tag.get_text(strip=True) if price_tag else None

        book_info = {
            'rank': idx,
            'title': title,
            'author': author,
            'publisher': publisher,
            'price': price
        }
        result.append(book_info)

    return result

if __name__ == "__main__":
    top10 = get_kyobo_top10()
    for book in top10:
        print(
            f"{book['rank']}위 | "
            f"제목: {book['title']} | "
            f"저자: {book['author']} | "
            f"출판사: {book['publisher']} | "
            f"가격: {book['price']}"
        )
