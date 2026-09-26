"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class SignalLightEntry(BaseModel):
    """信号机明细结构。"""

    field_0: str | None = None  # 信号机编号
    field_1: str | None = None  # 信号机类型
    field_2: str | None = None  # 显示距离
    field_3: str | None = None  # 灯位配置
    field_4: str | None = None  # 所属区间
    field_5: str | None = None  # 安装里程
    field_6: str | None = None  # 灯丝转换
    field_7: str | None = None  # 设备状态

class SwitchMachineEntry(BaseModel):
    """转辙机明细结构。"""

    field_0: str | None = None  # 转辙机编号
    field_1: str | None = None  # 转辙机型号
    field_2: str | None = None  # 所属道岔
    field_3: str | None = None  # 动作电流
    field_4: str | None = None  # 转换时间
    field_5: str | None = None  # 表示缺口
    field_6: str | None = None  # 润滑状态
    field_7: str | None = None  # 设备状态

class TrackCircuitEntry(BaseModel):
    """轨道区段明细结构。"""

    field_0: str | None = None  # 区段编号
    field_1: str | None = None  # 区段长度
    field_2: str | None = None  # 发送电压
    field_3: str | None = None  # 接收电压
    field_4: str | None = None  # 分路灵敏度
    field_5: str | None = None  # 绝缘类型
    field_6: str | None = None  # 相邻区段
    field_7: str | None = None  # 区段状态

class InterlockEntry(BaseModel):
    """联锁机明细结构。"""

    field_0: str | None = None  # 联锁机编号
    field_1: str | None = None  # 联锁制式
    field_2: str | None = None  # 软件版本
    field_3: str | None = None  # 主备状态
    field_4: str | None = None  # 运行温度
    field_5: str | None = None  # 当前倒机次数
    field_6: str | None = None  # 通讯状态
    field_7: str | None = None  # 设备状态

class AxleCounterEntry(BaseModel):
    """计轴磁头明细结构。"""

    field_0: str | None = None  # 磁头编号
    field_1: str | None = None  # 所属区段
    field_2: str | None = None  # 计轴数量
    field_3: str | None = None  # 通过列车数
    field_4: str | None = None  # 磁头灵敏度
    field_5: str | None = None  # 安装位置
    field_6: str | None = None  # 最近校验
    field_7: str | None = None  # 设备状态

class PowerPanelEntry(BaseModel):
    """电源屏明细结构。"""

    field_0: str | None = None  # 电源屏编号
    field_1: str | None = None  # 输入电压
    field_2: str | None = None  # 输出电压
    field_3: str | None = None  # 输出电流
    field_4: str | None = None  # 功率因数
    field_5: str | None = None  # 电池组电压
    field_6: str | None = None  # 散热状态
    field_7: str | None = None  # 设备状态

class CableBoxEntry(BaseModel):
    """电缆箱盒明细结构。"""

    field_0: str | None = None  # 箱盒编号
    field_1: str | None = None  # 箱盒类型
    field_2: str | None = None  # 所属区段
    field_3: str | None = None  # 电缆芯数
    field_4: str | None = None  # 密封等级
    field_5: str | None = None  # 接地电阻
    field_6: str | None = None  # 最近巡检
    field_7: str | None = None  # 箱盒状态

class AtpEntry(BaseModel):
    """ATP设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 所属列车
    field_2: str | None = None  # ATP型号
    field_3: str | None = None  # 软件版本
    field_4: str | None = None  # 运行里程
    field_5: str | None = None  # 最近检修
    field_6: str | None = None  # 故障代码
    field_7: str | None = None  # 设备状态

class BaliseEntry(BaseModel):
    """应答器明细结构。"""

    field_0: str | None = None  # 应答器编号
    field_1: str | None = None  # 应答器类型
    field_2: str | None = None  # 报文字数
    field_3: str | None = None  # 安装里程
    field_4: str | None = None  # 所属线路
    field_5: str | None = None  # 最近读写
    field_6: str | None = None  # 安装方式
    field_7: str | None = None  # 设备状态

class InspectPlanEntry(BaseModel):
    """检修计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 检修对象
    field_2: str | None = None  # 检修内容
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 检修班组
    field_5: str | None = None  # 天窗时间
    field_6: str | None = None  # 安全措施
    field_7: str | None = None  # 计划状态

class FaultRecordEntry(BaseModel):
    """故障记录明细结构。"""

    field_0: str | None = None  # 故障编号
    field_1: str | None = None  # 故障设备
    field_2: str | None = None  # 故障现象
    field_3: str | None = None  # 发生时间
    field_4: str | None = None  # 影响列车
    field_5: str | None = None  # 延时分钟
    field_6: str | None = None  # 修复措施
    field_7: str | None = None  # 故障状态

class MeasureEntry(BaseModel):
    """测试记录明细结构。"""

    field_0: str | None = None  # 测试编号
    field_1: str | None = None  # 测试对象
    field_2: str | None = None  # 测试项目
    field_3: str | None = None  # 测试值
    field_4: str | None = None  # 标准值
    field_5: str | None = None  # 偏差
    field_6: str | None = None  # 测试人员
    field_7: str | None = None  # 测试状态

class SparePartEntry(BaseModel):
    """信号备件明细结构。"""

    field_0: str | None = None  # 备件编号
    field_1: str | None = None  # 备件名称
    field_2: str | None = None  # 适用设备
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 存放位置
    field_5: str | None = None  # 供应商
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 备件状态

class ToolEntry(BaseModel):
    """检修工器具明细结构。"""

    field_0: str | None = None  # 器具编号
    field_1: str | None = None  # 器具名称
    field_2: str | None = None  # 器具类别
    field_3: str | None = None  # 检定日期
    field_4: str | None = None  # 有效期至
    field_5: str | None = None  # 保管人
    field_6: str | None = None  # 借用状态
    field_7: str | None = None  # 器具状态

class ShiftLogEntry(BaseModel):
    """值班记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 值班日期
    field_2: str | None = None  # 值班人员
    field_3: str | None = None  # 设备运行概况
    field_4: str | None = None  # 异常处置
    field_5: str | None = None  # 调度命令
    field_6: str | None = None  # 交接事项
    field_7: str | None = None  # 记录状态

class TrainDetectEntry(BaseModel):
    """列车检测记录明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 列车车次
    field_2: str | None = None  # 检测日期
    field_3: str | None = None  # 检测区段
    field_4: str | None = None  # 最高速度
    field_5: str | None = None  # 运行方向
    field_6: str | None = None  # 检测结果
    field_7: str | None = None  # 记录状态

class GroundEquipEntry(BaseModel):
    """LEU设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # LEU型号
    field_2: str | None = None  # 关联信号机
    field_3: str | None = None  # 关联应答器
    field_4: str | None = None  # 通讯状态
    field_5: str | None = None  # 最近校验
    field_6: str | None = None  # 主备状态
    field_7: str | None = None  # 设备状态

class TsrEntry(BaseModel):
    """限速命令明细结构。"""

    field_0: str | None = None  # 命令编号
    field_1: str | None = None  # 限速区段
    field_2: str | None = None  # 限速值
    field_3: str | None = None  # 生效时间
    field_4: str | None = None  # 取消时间
    field_5: str | None = None  # 发布人员
    field_6: str | None = None  # 接收确认
    field_7: str | None = None  # 命令状态
