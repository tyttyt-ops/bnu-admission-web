# 北京师范大学招生网站

这是一个北京师范大学招生网站项目，包含了招生相关的各种信息和功能。

## 项目结构

```
├── css/             # 样式文件
├── js/              # JavaScript文件
├── python/          # Python脚本
├── 北师美景/         # 校园美景图片和页面
├── 北师美食/         # 校园美食图片和页面
├── index.html       # 主页
├── newfont.html     # 新版主页
├── china.html       # 中国地图页面
├── ciyun.html       # 专业词云页面
├── yuanxi.html      # 院系介绍页面
├── zhexian.html     # 分数线分析页面
├── option.html      # 选项页面
├── 分数线报告.html   # 分数线报告页面
├── bnu_beijing_2024_scores.csv  # 2024年北京地区分数线数据
└── README.md        # 项目说明文件
```

## 功能介绍

1. **主页**：项目的入口页面，提供各种功能的导航链接
2. **新版主页**：更新后的主页设计，提供更全面的招生信息
3. **中国地图**：展示中国各地区的相关信息
4. **专业词云**：通过词云展示专业相关信息
5. **院系介绍**：介绍北京师范大学的各个院系
6. **分数线分析**：分析北京师范大学各专业的录取分数线
7. **校园美景**：展示北京师范大学的美丽校园风光
8. **校园美食**：介绍北京师范大学的特色美食

## 本地运行

1. 克隆项目到本地
   ```bash
   git clone https://github.com/tyttyt-ops/bnu-admission-web.git
   ```

2. 进入项目目录
   ```bash
   cd bnu-admission-web
   ```

3. 启动本地服务器
   ```bash
   # 使用Python 3
   python -m http.server 8000
   
   # 或使用Python 2
   python -m SimpleHTTPServer 8000
   ```

4. 在浏览器中访问
   ```
   http://localhost:8000
   ```

## 在线访问

项目已部署到GitHub Pages，可以通过以下链接访问：

https://tyttyt-ops.github.io/bnu-admission-web/

## 技术栈

- HTML5
- CSS3
- JavaScript
- Python
- 各种前端库和框架

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用MIT许可证。
