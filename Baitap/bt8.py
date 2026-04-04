from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def scrape_books():
    """Scrape book information from books.toscrape.com"""
    base_url = "http://books.toscrape.com"
    data = []
    
    print("Bắt đầu scraping dữ liệu...")
    
    # 1. Lấy 5 trang đầu tiên
    for page in range(1, 6):
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}/catalogue/page-{page}.html"
        
        print(f"Đang scrape trang {page}: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Kiểm tra lỗi HTTP
            soup = BeautifulSoup(response.content, "html.parser")
            
            books = soup.find_all("article", class_="product_pod")
            
            for book in books:
                # 2. Lấy thông tin sách
                
                # Tên sách
                name = book.h3.a["title"]
                
                # Giá
                price = book.find("p", class_="price_color").text
                
                # Đánh giá (rating nằm trong class)
                rating_element = book.find("p", class_="star-rating")
                rating = rating_element["class"][1] if rating_element else "No rating"
                
                # Tình trạng
                availability_element = book.find("p", class_="instock availability")
                availability = availability_element.text.strip() if availability_element else "Unknown"
                
                data.append({
                    "Tên sách": name,
                    "Giá": price,
                    "Đánh giá": rating,
                    "Tình trạng": availability
                })
            
            print(f"Đã lấy {len(books)} sách từ trang {page}")
            
            # Thêm delay nhỏ để tránh quá tải server
            time.sleep(0.5)
            
        except requests.RequestException as e:
            print(f"Lỗi khi truy cập trang {page}: {e}")
            continue
    
    return data

def export_to_excel(data, filename="books.xlsx"):
    """Export data to Excel file"""
    if not data:
        print("Không có dữ liệu để xuất!")
        return
    
    # 3. Xuất kết quả ra Excel
    df = pd.DataFrame(data)
    
    # Tạo file Excel với sheet name được yêu cầu
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name="Danh sách Sách", index=False)
    
    print(f"Đã xuất {len(data)} sách ra file {filename} thành công!")
    print(f"Sheet name: 'Danh sách Sách'")
    
    # Hiển thị một vài dòng đầu
    print("\nMột vài sách đầu tiên:")
    print(df.head())

if __name__ == "__main__":
    # Scrape dữ liệu
    books_data = scrape_books()
    
    # Xuất ra Excel
    export_to_excel(books_data)
    
    print(f"\nTổng cộng đã scrape {len(books_data)} sách từ 5 trang đầu tiên.")