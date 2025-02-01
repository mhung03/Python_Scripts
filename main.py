import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Kết nối thành công tới {url}")
            print(f"Server: {response.headers.get('Server')}")
            print(f"Loại nội dung phản hồi : {response.headers.get('Content-Type')}")
            print(f"Thời gian phản hồi : {response.headers.get('Date')}")
            print(f"Ngôn ngữ phản hồi : {response.headers.get('Content-Language')}")
        else:
            print(f"Kết nối thất bại tới {url}. Mã lỗi: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Có lỗi xảy ra: {e}")

target = input("Nhập url website mục tiêu: ")
#Sử dụng hàm
check_website(target)
