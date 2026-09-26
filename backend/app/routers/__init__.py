"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import signal_light as router_signal_light
from app.routers import switch_machine as router_switch_machine
from app.routers import track_circuit as router_track_circuit
from app.routers import interlock as router_interlock
from app.routers import axle_counter as router_axle_counter
from app.routers import power_panel as router_power_panel
from app.routers import cable_box as router_cable_box
from app.routers import atp as router_atp
from app.routers import balise as router_balise
from app.routers import inspect_plan as router_inspect_plan
from app.routers import fault_record as router_fault_record
from app.routers import measure as router_measure
from app.routers import spare_part as router_spare_part
from app.routers import tool as router_tool
from app.routers import shift_log as router_shift_log
from app.routers import train_detect as router_train_detect
from app.routers import ground_equip as router_ground_equip
from app.routers import tsr as router_tsr

ROUTERS = [router_signal_light, router_switch_machine, router_track_circuit, router_interlock, router_axle_counter, router_power_panel, router_cable_box, router_atp, router_balise, router_inspect_plan, router_fault_record, router_measure, router_spare_part, router_tool, router_shift_log, router_train_detect, router_ground_equip, router_tsr]
