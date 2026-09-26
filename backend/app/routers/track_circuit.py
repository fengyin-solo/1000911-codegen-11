"""轨道电路接口：维护轨道区段，覆盖登记红光带、登记分路不良、销记恢复等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.track_circuit import TrackCircuitService

router = APIRouter(prefix="/api/track_circuit", tags=["轨道电路"])

service = TrackCircuitService()

LIST_FIELDS = ["区段编号", "区段长度", "发送电压", "接收电压", "分路灵敏度", "绝缘类型", "相邻区段", "区段状态"]
STATUSES = ["空闲", "占用", "红光带", "分路不良"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按区段编号检索"),
    status: str | None = Query(default=None, description="空闲、占用、红光带、分路不良"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按区段编号与状态过滤轨道电路列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条轨道区段明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"轨道区段 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条轨道区段，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="轨道区段已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条轨道区段执行登记红光带、登记分路不良、销记恢复；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出轨道电路清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "track_circuit", "total": total, "items": items}
