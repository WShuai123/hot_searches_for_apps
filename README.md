### 使用api接口获取各平台热搜

从**2023年8月16**日开始。每两个小时获取一次。

获取到的热搜以markdown的形式保存在[archives](https://github.com/WShuai123/hot_searches_for_apps/tree/main/archives)文件夹中，按照`软件名称/年/月/日`的路径保存。

更新日志：

+ 2023-10-22： 过滤各平台当天的重复热搜，合并为一个文件夹

### 使用[教书先生](https://api.oioweb.cn/doc/common/HotList)的api

`hot_to_csv.py`是将获取到的热搜保存在csv文件中。

`hot_to_md.py`是将获取到的热搜保存在markdown文件中。

共包含以下平台的热搜：

| 网站/应用 | 网站/应用 | 网站/应用 | 网站/应用 | 网站/应用 | 网站/应用 |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| [微博](./archives/微博/微博.md) | [知乎](./archives/知乎/知乎.md) | [微信](./archives/微信/微信.md) | [百度](./archives/百度/百度.md) | [36氪](./archives/36氪/36氪.md) | [少数派](./archives/少数派/少数派.md) |
| [虎嗅网](./archives/虎嗅网/虎嗅网.md) | [IT之家](./archives/IT之家/IT之家.md) | [哔哩哔哩](./archives/哔哩哔哩/哔哩哔哩.md) | [抖音](./archives/抖音/抖音.md) | [煎蛋](./archives/煎蛋/煎蛋.md) | [AcFun](./archives/AcFun/AcFun.md) |
| [吾爱破解](./archives/吾爱破解/吾爱破解.md) | [百度贴吧](./archives/百度贴吧/百度贴吧.md) | [腾讯新闻](./archives/腾讯新闻/腾讯新闻.md) | [虎扑社区](./archives/虎扑社区/虎扑社区.md) | [淘宝](./archives/淘宝/淘宝.md) | [雪球](./archives/雪球/雪球.md) |
| [第一财经](./archives/第一财经/第一财经.md) | [财新网](./archives/财新网/财新网.md) | [新浪财经新闻](./archives/新浪财经新闻/新浪财经新闻.md) | [水木社区](./archives/水木社区/水木社区.md) | [北大未名](./archives/北大未名/北大未名.md) | [北邮人论坛](./archives/北邮人论坛/北邮人论坛.md) |
| [知乎日报](./archives/知乎日报/知乎日报.md) | [开眼视频](./archives/开眼视频/开眼视频.md) | [历史上的今天](./archives/历史上的今天/历史上的今天.md) | [高楼迷](./archives/高楼迷/高楼迷.md) | [宽带山](./archives/宽带山/宽带山.md) | [厦门小鱼](./archives/厦门小鱼/厦门小鱼.md) |
| [过早客（光谷社区）](./archives/光谷社区/光谷社区.md) | [豆瓣电影](./archives/豆瓣电影/豆瓣电影.md) | [微信读书](./archives/微信读书/微信读书.md) | [当当](./archives/当当/当当.md) | [起点中文网](./archives/起点中文网/起点中文网.md) | [纵横中文网](./archives/纵横中文网/纵横中文网.md) |
| [TapTap](./archives/TapTap/TapTap.md) | [3DM游戏网](./archives/3DM游戏网/3DM游戏网.md) | [机核网](./archives/机核网/机核网.md) | [游研社](./archives/游研社/游研社.md) | [新浪体育新闻](./archives/新浪体育新闻/新浪体育新闻.md) | [懂球帝](./archives/懂球帝/懂球帝.md) |
| [人人都是产品经理](./archives/人人都是产品经理/人人都是产品经理.md) | [咖啡日报](./archives/咖啡日报/咖啡日报.md) | [inNeed社区](./archives/inNeed社区/inNeed社区.md) | [Product Hunt](https://github.com/WShuai123/hot_searches_for_apps/blob/main/archives/Product%20Hunt/Product%20Hunt.md) | [GitHub](./archives/GitHub/GitHub.md) | [CSDN博客](./archives/CSDN博客/CSDN博客.md) |
| [掘金](./archives/掘金/掘金.md) | [开发者头条](./archives/开发者头条/开发者头条.md) | [站酷](./archives/站酷/站酷.md) | [Dribbble](./archives/Dribbble/Dribbble.md) | [优设网](./archives/优设网/优设网.md) | [UI中国](./archives/UI中国/UI中国.md) |
| [App Store](https://github.com/WShuai123/hot_searches_for_apps/blob/main/archives/App%20Store/App%20Store.md) | [爱范儿](./archives/爱范儿/爱范儿.md) | [AppSo](./archives/AppSo/AppSo.md) | [汽车之家](./archives/汽车之家/汽车之家.md) | [懂车帝](./archives/懂车帝/懂车帝.md) | [易车网](./archives/易车网/易车网.md) |
| [太平洋汽车网](./archives/太平洋汽车网/太平洋汽车网.md) | [看雪论坛](./archives/看雪论坛/看雪论坛.md) | [安全客](./archives/安全客/安全客.md) | [FreeBuf](./archives/FreeBuf/FreeBuf.md) | [安全脉搏](./archives/安全脉搏/安全脉搏.md) |

