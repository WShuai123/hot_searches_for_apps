import requests, time, os, shutil

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求不成功则引发异常检查响应的HTTP状态码，如果状态码表示错误，比如 404 表示资源未找到，或者 500 表示服务器内部错误，它就会引发一个HTTPError异常。
        json_data = response.json()  # 将响应内容解析为JSON格式的数据。
        return json_data
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def read_markdown(path):    # 读取文件内容
    with open(path, mode='r', encoding='utf-8') as file:
        markdown_content = file.read()
    return markdown_content

if __name__ == "__main__":
    time = time.strftime("%Y-%m-%d", time.localtime())
    year, month, day = time.split("-")

    api_url = "https://api.oioweb.cn/api/common/HotList"  # API接口地址
    api_data = get_api_data(api_url)
    
    if api_data:
        for key in list(api_data['result'].keys()):
            print(key)
            
            titles = [item["title"] for item in api_data['result']['%s' % key]]

            hrefs = [item["href"] for item in api_data['result']['%s' % key]]
            
            path = os.path.join('archives',key,year,month)
            os.makedirs(path, exist_ok=True)    # 创建目录
            
            with open(os.path.join(path,'%s.md' % time), mode="a", encoding="utf-8") as file:    # 以追加模式打开文件
                markdown_content = read_markdown(os.path.join(path,'%s.md' % time))  # 读取文件内容
                if not markdown_content:    # 如果文件内容为空，则写入文件
                    file.write("## %s \n### %s\n\n" % (key,time))
                for i in range(len(titles)):
                    if titles[i] not in markdown_content:   # 如果标题不在文件内容中，则写入文件
                        file.write("+ [%s](%s)\n\n" % (titles[i], hrefs[i]))
            print("Data saved successfully!")
            shutil.copyfile(os.path.join(path,'%s.md' % time), "./archives/%s/%s.md" % (key,key))    # 复制文件到根目录
