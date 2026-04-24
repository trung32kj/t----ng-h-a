import requests

def get_url():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
# get_url()

def get_url_1(n):
    url = "https://jsonplaceholder.typicode.com/posts/" + str(n)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
# n = int(input("Nhập id "))
# get_url_1()

def post_url(title, body, userid):
    url = "https://jsonplaceholder.typicode.com/posts/"
    payload = {'title': title,
               'body': body,
               'userid': userid}
    files=[]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

post_url("23CT1", "Đây là bài tập API", 23)
post_url("23CT2", "Đây là bài tập API2", 24)