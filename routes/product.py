import requests
import json
from bs4 import BeautifulSoup


def get_product():
    merch_info = []
    product_urls = [
        'https://marpple.shop/kr/gbbul_nocharim/products/14154311',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154317',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154327',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154336',
        'https://marpple.shop/kr/gbbul_nocharim/products/14004110',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154264',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154234',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154184',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154065',
        'https://marpple.shop/kr/gbbul_nocharim/products/14154008',
        'https://marpple.shop/kr/gbbul_nocharim/products/14153869',
        'https://marpple.shop/kr/gbbul_nocharim/products/14130904',
        'https://marpple.shop/kr/gbbul_nocharim/products/14130600'
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }


    # 하위 URL 리스트

    # 상위 URL에서 카테고리 이름 추출
    # base_url = 'https://marpple.shop/kr/gbbul_nocharim/'
    # response = requests.get(base_url)
    # soup = BeautifulSoup(response.content, 'html.parser')
    # category_names = soup.find_all('div', class_='app-product-item__category-name')
    # for category in category_names:
    #     print(category.text.strip())
    #

    # for link in category_names:
    #     product_url = link.get('href')

    # 하위 URL에서 제품 정보 추출
    for url in product_urls:
        try:
            response = requests.get(url, headers=headers)
            print(f"status code : {response.status_code}")
            soup = BeautifulSoup(response.text, 'html.parser')

            # 제품 정보 추출
            product_name = soup.find('h2', {'class': 'pd-product__name'}).get_text(strip=True)
            product_image = soup.find('img', {'class': 'mp-product-img'})['src']
            product_price = soup.find('span', {'class': 'pd-product__price'}).get_text(strip=True)

            merch_info.append({
                'url': url,
                'name': product_name,
                'image': product_image,
                'price': product_price
            })

        except Exception as e:
            print(f"Error processing URL {url}: {e}")


    # JSON으로 변환 및 출력
    json_data = json.dumps(merch_info, ensure_ascii=False, indent=4)
    print(json_data)
    for i in merch_info:
        print(i)
    return json_data

get_product()







