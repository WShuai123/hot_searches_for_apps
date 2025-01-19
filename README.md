### 使用api接口获取各平台热搜

从**2023年8月16**日开始。

每1个小时获取一次，按天归档。

获取到的热搜以markdown的形式保存在[archives](https://github.com/iiecho1/hot_searches_for_apps/tree/main/archives)文件夹中，按照`软件名称/年/月/日`的路径保存。

### 更新日志：
+ 2025-01-10: 本懒狗终于修复了。重新写的api，目前支持获取30个网站的热搜。更多网站再慢慢添加吧。
+ 2024-10-18：教书先生api不再提供服务，过几天有时间了再切换成自己的api。
+ 2023-12-16: 教书先生api恢复。
+ 2023-12-15: api出现故障。打算自己写。没时间，所以写的很慢:<https://github.com/iiecho1/api-for-hot-search-golang>
+ 2023-10-22: 过滤各平台当天的重复热搜，合并为一个文件夹,改为每1小时运行一次。

共包含以下平台的热搜：

| 网站/应用 | 网站/应用 | 网站/应用 | 网站/应用 | 网站/应用 | 网站/应用 |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| [360搜索](./archives/360搜索/360搜索.md) | [AcFun](./archives/AcFun/AcFun.md) | [CSDN](./archives/CSDN/CSDN.md) | [GitHub](./archives/GitHub/GitHub.md) | [IT之家](./archives/IT之家/IT之家.md) | [V2EX](./archives/V2EX/V2EX.md) |
| [今日头条](./archives/今日头条/今日头条.md) | [历史上的今天](./archives/历史上的今天/历史上的今天.md) | [哔哩哔哩](./archives/哔哩哔哩/哔哩哔哩.md) | [国家地理](./archives/国家地理/国家地理.md) | [少数派](./archives/少数派/少数派.md) | [微博](./archives/微博/微博.md) |
| [懂球帝](./archives/懂球帝/懂球帝.md) | [抖音](./archives/抖音/抖音.md) | [搜狗](./archives/搜狗/搜狗.md) | [新京报](./archives/新京报/新京报.md) | [梨视频](./archives/梨视频/梨视频.md) | [澎湃新闻](./archives/澎湃新闻/澎湃新闻.md) |
| [知乎](./archives/知乎/知乎.md) | [网易新闻](./archives/网易新闻/网易新闻.md) | [腾讯新闻](./archives/腾讯新闻/腾讯新闻.md) | [虎扑](./archives/虎扑/虎扑.md) | [豆瓣](./archives/豆瓣/豆瓣.md) |[夸克](./archives/夸克/夸克.md)|
|[百度](./archives/百度/百度.md)|[搜狐](./archives/搜狐/搜狐.md)|[人民网](./archives/人民网/人民网.md)|[南方周末](./archives/南方周末/南方周末.md)|[360doc](./archives/360doc/360doc.md)|[CCTV新闻](./archives/CCTV新闻/CCTV新闻.md)||
