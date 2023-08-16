import requests, time, os

time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
year, month, day = time.split()[0].split("-")

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
        for key in list(api_data['result'].keys())[1:-1]:
            print(key)
            indexs = [item["index"] for item in api_data['result']['%s' % key]]

            titles = [item["title"] for item in api_data['result']['%s' % key]]

            hots = [item["hot"] for item in api_data['result']['%s' % key]]

            hrefs = [item["href"] for item in api_data['result']['%s' % key]]
            
            path = os.path.join('archives',key,year,month,day)
            os.makedirs(path, exist_ok=True)

            with open(os.path.join(path,time), mode="w", newline="", encoding="utf-8") as file:
                file.write("## %s \n### %s\n\n" % (key,time))
                for i in range(len(indexs)):
                    file.write("%s. [%s](%s)\n\n" % (indexs[i], titles[i], hrefs[i]))
            print("Data saved successfully!")
