import requests, csv, time

# 获取时间，按照年月日时分秒的格式
time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求不成功则引发异常检查响应的HTTP状态码，如果状态码表示错误，比如 404 表示资源未找到，或者 500 表示服务器内部错误，它就会引发一个HTTPError异常。
        json_data = response.json()  # 将响应内容解析为JSON格式的数据。
        return json_data
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    api_url = "https://api.oioweb.cn/api/common/HotList"  # API接口地址
    api_data = get_api_data(api_url)
    
    if api_data:

        indexs = [item["index"] for item in api_data['result']['微博']]

        titles = [item["title"] for item in api_data['result']['微博']]

        hrefs = [item["href"] for item in api_data['result']['微博']]

        with open("./%s.csv" % time, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["热搜榜排名", "热搜标题", "网址"])  # 写入标题行
            for item1, item2 ,item3 in zip(indexs, titles, hrefs):
                writer.writerow([item1, item2, item3])
        print("Data saved successfully!")
