import requests
import json

# Base URL cho API
BASE_URL = "https://jsonplaceholder.typicode.com"

def create_post(title, body, user_id):
    """
    1. Tạo một bài viết: Create – POST /posts
    """
    url = f"{BASE_URL}/posts"
    
    payload = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print("=== TẠO BÀI VIẾT MỚI ===")
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    print("-" * 50)
    
    return response.json()

def get_all_posts():
    """
    2. Lấy danh sách bài viết: GET - /posts
    """
    url = f"{BASE_URL}/posts"
    
    response = requests.get(url)
    
    print("=== DANH SÁCH TẤT CẢ BÀI VIẾT ===")
    print(f"Status Code: {response.status_code}")
    print(f"Tổng số bài viết: {len(response.json())}")
    print("5 bài viết đầu tiên:")
    
    posts = response.json()[:5]  # Chỉ hiển thị 5 bài đầu
    for post in posts:
        print(f"ID: {post['id']} - Title: {post['title'][:50]}...")
    
    print("-" * 50)
    return response.json()

def get_post_by_id(post_id):
    """
    3. Lấy chi tiết một bài viết: GET - /posts/1
    """
    url = f"{BASE_URL}/posts/{post_id}"
    
    response = requests.get(url)
    
    print(f"=== CHI TIẾT BÀI VIẾT ID: {post_id} ===")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print("Không tìm thấy bài viết!")
    
    print("-" * 50)
    return response.json() if response.status_code == 200 else None

def update_post(post_id, title, body, user_id):
    """
    4. Cập nhật một bài viết: PUT - /posts/1
    """
    url = f"{BASE_URL}/posts/{post_id}"
    
    payload = {
        'id': post_id,
        'title': title,
        'body': body,
        'userId': user_id
    }
    
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(f"=== CẬP NHẬT BÀI VIẾT ID: {post_id} ===")
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    print("-" * 50)
    
    return response.json()

def delete_post(post_id):
    """
    5. Xóa một bài viết: DELETE - /posts/1
    """
    url = f"{BASE_URL}/posts/{post_id}"
    
    response = requests.delete(url)
    
    print(f"=== XÓA BÀI VIẾT ID: {post_id} ===")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("Xóa bài viết thành công!")
        print("Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print("Có lỗi khi xóa bài viết!")
    
    print("-" * 50)
    return response.status_code == 200

def interactive_menu():
    """
    Menu tương tác để người dùng chọn chức năng
    """
    while True:
        print("\n" + "=" * 50)
        print("🔧 MENU QUẢN LÝ BÀI VIẾT - JSONPlaceholder API")
        print("=" * 50)
        print("1. Tạo bài viết mới (POST)")
        print("2. Xem danh sách bài viết (GET)")
        print("3. Xem chi tiết bài viết (GET)")
        print("4. Cập nhật bài viết (PUT)")
        print("5. Xóa bài viết (DELETE)")
        print("0. Thoát")
        print("-" * 50)
        
        choice = input("Chọn chức năng (0-5): ").strip()
        
        if choice == "1":
            title = input("Nhập tiêu đề: ")
            body = input("Nhập nội dung: ")
            user_id = int(input("Nhập User ID: "))
            create_post(title, body, user_id)
            
        elif choice == "2":
            get_all_posts()
            
        elif choice == "3":
            post_id = int(input("Nhập ID bài viết: "))
            get_post_by_id(post_id)
            
        elif choice == "4":
            post_id = int(input("Nhập ID bài viết cần cập nhật: "))
            title = input("Nhập tiêu đề mới: ")
            body = input("Nhập nội dung mới: ")
            user_id = int(input("Nhập User ID: "))
            update_post(post_id, title, body, user_id)
            
        elif choice == "5":
            post_id = int(input("Nhập ID bài viết cần xóa: "))
            delete_post(post_id)
            
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    # Chạy menu tương tác
    interactive_menu()