# Travel Planner 前端

一个基于 **React + TypeScript + MUI + Leaflet** 的旅行计划管理前端项目，支持世界地图展示与旅行计划的可视化管理。后端推荐使用 FastAPI（也可替换为 Flask）。

---

## 🚀 技术栈

- **React 18 + TypeScript**：现代前端开发框架
- **Vite**：极速开发与构建工具
- **MUI (Material UI)**：高质量 UI 组件库
- **Leaflet + react-leaflet**：地图渲染与交互
- **Axios**：与后端 API 通信

---

## 📂 目录结构

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
```

---

## 🛠️ 快速开始

1. 克隆项目

   ```bash
   git clone https://github.com/yourname/travel-planner-frontend.git
   cd travel-planner-frontend
   ```

2. 安装依赖

   ```bash
   npm install
   ```

3. 启动开发环境

   ```bash
   npm run dev
   ```

4. 打开浏览器访问

   ```
   http://localhost:5173/
   ```

---

## 📋 开发计划

### 阶段一：基础功能

- [x] 初始化 Vite + React + TS 项目
- [x] 集成 MUI
- [x] 集成 Leaflet 地图
- [ ] 左侧侧边栏（旅行计划列表 + 操作按钮）
- [ ] “新建计划”弹窗（表单：出发地、目的地、日期等）

### 阶段二：后端联动

- [ ] 使用 Axios 获取后端 travel plans
- [ ] 渲染计划到侧边栏
- [ ] 地图上展示路线
- [ ] 新建计划表单提交到后端并刷新

### 阶段三：优化与拓展

- [ ] 用户登录（JWT 认证）
- [ ] UI 美化与响应式布局
- [ ] 国际化（中英文切换）
- [ ] 部署到 Vercel / Netlify

---

## 💡 说明

- 当前为 MVP（最小可用版本），优先实现核心功能。
- 后续可拓展如 AI 路线推荐、社交分享、数据可视化等高级功能。

---

如有建议或问题，欢迎 issue 或 PR！