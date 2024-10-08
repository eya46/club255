from typing import TypeVar

T = TypeVar("T")

UID = TypeVar("UID", int, str)  # 用户id
PID = TypeVar("PID", int, str)  # 帖子id
FID = TypeVar("FID", int, str)  # 楼层id
MID = TypeVar("MID", int, str)  # 消息id

__all__ = ["T", "UID", "PID", "FID", "MID"]
