# Travel Planner Frontend

一个基于 **React + TypeScript + MUI + Leaflet** 的前端项目，用于展示世界地图并管理旅行计划。  
后端使用 FastAPI 提供数据支持（可选替换为 Flask）。

## 🚀 技术栈

- **React 18 + TypeScript**
- **Vite** (开发和构建工具)
- **MUI (Material UI)** (UI 组件库)
- **Leaflet + react-leaflet** (地图展示)
- **Axios** (请求后端 API)

## 📂 项目结构

```

travel-planner-frontend/
├── src/
│   ├── components/   # 可复用 UI 组件
│   ├── pages/        # 页面组件（如 TravelMapPage）
│   ├── App.tsx       # 应用主入口
│   ├── main.tsx      # React 挂载入口
│   └── index.css     # 全局样式
├── public/           # 静态资源
├── package.json
└── vite.config.ts

````

## 🔧 启动方式

1. 克隆项目：
   ```bash
   git clone https://github.com/yourname/travel-planner-frontend.git
   cd travel-planner-frontend
````

2. 安装依赖：

   ```bash
   npm install
   ```

3. 启动开发环境：

   ```bash
   npm run dev
   ```

4. 打开浏览器访问：

   ```
   http://localhost:5173/
   ```

---

## ✅ ToDoList

### 第一阶段：基础页面搭建

* [x] 初始化 Vite + React + TS 项目
* [x] 集成 MUI
* [x] 添加 Leaflet 地图并成功渲染
* [ ] 左侧侧边栏 UI（分上下两块：旅行计划展示 + 操作按钮）
* [ ] “新建计划”按钮点击后弹出对话框（表单：出发地、目的地、日期等）

### 第二阶段：与后端交互

* [ ] 使用 Axios 调用 FastAPI 后端获取已有 travel plans
* [ ] 将计划渲染到左侧列表
* [ ] 点击计划后在地图上绘制路线
* [ ] 新建计划时提交表单数据到后端并刷新页面

### 第三阶段：优化与拓展

* [ ] 添加用户登录（JWT 认证）
* [ ] 美化 UI（MUI Theme + 响应式布局）
* [ ] 国际化（i18n，支持英文 / 中文）
* [ ] 部署到 Vercel / Netlify

---

## 📌 备注

* 本项目目前处于 MVP（最小可行版本）阶段，优先保证核心功能实现。
* 未来可拓展更多功能（如 AI 推荐路线、社交分享、数据可视化等）。

```

---