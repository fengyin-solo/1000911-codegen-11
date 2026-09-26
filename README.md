# 轨道交通信号设备检修管理平台

覆盖信号机、道岔转辙、轨道电路、联锁设备、计轴、电源屏及检修计划的轨道交通信号设备全生命周期管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 信号机管理 | `signal_light` | 信号机 | 信号机编号、信号机类型、显示距离 |
| 道岔转辙机 | `switch_machine` | 转辙机 | 转辙机编号、转辙机型号、所属道岔 |
| 轨道电路 | `track_circuit` | 轨道区段 | 区段编号、区段长度、发送电压 |
| 联锁设备 | `interlock` | 联锁机 | 联锁机编号、联锁制式、软件版本 |
| 计轴设备 | `axle_counter` | 计轴磁头 | 磁头编号、所属区段、计轴数量 |
| 信号电源屏 | `power_panel` | 电源屏 | 电源屏编号、输入电压、输出电压 |
| 电缆箱盒 | `cable_box` | 电缆箱盒 | 箱盒编号、箱盒类型、所属区段 |
| 列控车载设备 | `atp` | ATP设备 | 设备编号、所属列车、ATP型号 |
| 应答器管理 | `balise` | 应答器 | 应答器编号、应答器类型、报文字数 |
| 检修计划 | `inspect_plan` | 检修计划 | 计划编号、检修对象、检修内容 |
| 故障记录 | `fault_record` | 故障记录 | 故障编号、故障设备、故障现象 |
| 电气特性测试 | `measure` | 测试记录 | 测试编号、测试对象、测试项目 |
| 备件管理 | `spare_part` | 信号备件 | 备件编号、备件名称、适用设备 |
| 工器具管理 | `tool` | 检修工器具 | 器具编号、器具名称、器具类别 |
| 值班记录 | `shift_log` | 值班记录 | 记录编号、值班日期、值班人员 |
| 列车检测 | `train_detect` | 列车检测记录 | 检测编号、列车车次、检测日期 |
| 地面电子单元 | `ground_equip` | LEU设备 | 设备编号、LEU型号、关联信号机 |
| 临时限速 | `tsr` | 限速命令 | 命令编号、限速区段、限速值 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
