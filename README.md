# 🔬 FabLab数据分析器

一个智能的FabLab实验室和学生数据分析工具，支持2016-2025年的数据格式，具有动态国家管理系统。

## ✨ 主要功能

- 📊 **智能统计**：实验室和学生数量统计
- 🌍 **动态国家管理**：自动发现和统计新国家
- 🇨🇳 **中国实验室识别**：准确识别中国相关实验室
- 📋 **详细表格**：中国实验室和学生信息展示
- 🔄 **自动代理**：自动启用代理服务解决CORS问题
- 📈 **实时分析**：支持多种数据格式的实时分析

## 🚀 快速开始

### 方法1：直接使用（推荐）
1. 下载 `fablab_analyzer.html`
2. 在浏览器中打开文件
3. 选择数据格式并输入FabLab网址
4. 点击"分析数据"开始分析

### 方法2：本地服务器
```bash
python3 start_server.py
```
然后在浏览器中访问 `http://localhost:8000`

## 📊 支持的数据格式

### 2016-2017格式（JSON数据）
- `https://archive.fabacademy.org/archives/2016/master/students.html`
- `https://archive.fabacademy.org/archives/2017/master/students.html`

### 2018-2025格式（HTML页面）
- `https://archive.fabacademy.org/2018/people.html`
- `https://archive.fabacademy.org/2019/people.html`
- `https://archive.fabacademy.org/2020/people.html`
- `https://archive.fabacademy.org/2021/people.html`
- `https://archive.fabacademy.org/2022/people.html`
- `https://archive.fabacademy.org/2023/people.html`
- `https://archive.fabacademy.org/2024/people.html`
- `https://archive.fabacademy.org/2025/people.html`

## 🔧 核心特性

### 动态国家管理系统
- **自动发现**：遇到新国家时自动添加到映射表
- **智能标准化**：统一国家名称格式
- **实时统计**：自动统计各国实验室和学生数量
- **中国识别**：准确识别Taipei、Taiwan、Hong Kong等中国地区

### 智能数据分析
- **实验室统计**：去重统计实验室数量
- **学生统计**：基于唯一标识符统计学生数量
- **国家分布**：按学生数量排序的各国统计
- **中国专项**：专门的中国实验室和学生统计

### 技术优势
- **自动代理**：无需手动配置，自动解决CORS问题
- **多格式支持**：支持JSON和HTML两种数据格式
- **响应式设计**：适配桌面和移动设备
- **实时反馈**：分析过程实时显示进度

## 📁 项目结构

```
fablab-analyzer/
├── fablab_analyzer.html    # 主程序文件
├── start_server.py         # 本地服务器脚本
└── README.md              # 项目说明文档
```

## 🛠️ 技术栈

- **前端**：原生JavaScript、HTML5、CSS3
- **数据获取**：Fetch API、代理服务
- **数据处理**：动态国家管理、智能匹配算法
- **部署**：纯静态文件，无需服务器

## 📈 统计内容

- **总实验室数量**：去重统计
- **总学生数量**：基于唯一标识符统计
- **参与国家数量**：动态发现的国家总数
- **中国实验室数量**：包括所有中国地区
- **中国学生数量**：来自中国地区的学生
- **各国详细统计**：按学生数量排序的完整统计

## 🔍 使用示例

1. **打开工具**：在浏览器中打开 `fablab_analyzer.html`
2. **选择格式**：选择对应的数据格式（2016-2017 或 2018-2025）
3. **输入网址**：输入FabLab网址，如：
   ```
   https://archive.fabacademy.org/2021/people.html
   ```
4. **开始分析**：点击"分析数据"按钮
5. **查看结果**：查看统计数据和详细表格

## 🎯 最新版本特性

### v3.0 更新内容
- ✅ **动态国家管理**：自动发现和添加新国家
- ✅ **自动代理服务**：无需手动配置，自动启用代理
- ✅ **精简界面**：移除冗余警告和表格
- ✅ **智能识别**：改进中国实验室识别算法
- ✅ **性能优化**：更高效的数据处理流程

## 📝 开发说明

### 动态国家管理系统
```javascript
// 自动发现新国家
const countryManager = new DynamicCountryManager();
const country = countryManager.normalizeCountry('New Country');
// 自动添加到动态映射表并开始统计
```

### 智能实验室识别
- 支持多种实验室名称格式
- 自动从实验室名称提取国家信息
- 智能匹配和标准化国家名称

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个工具！

## 📄 许可证

MIT License

---

**注意**：此工具仅用于数据分析，请遵守相关网站的使用条款。 
