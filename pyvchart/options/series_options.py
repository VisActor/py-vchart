from typing import Any, Optional, Sequence, Tuple, Union

from ..commons.utils import JsCode

Numeric = Union[int, float]
JSFunc = Union[str, JsCode]


class BasicOpts:
    __slots__ = ("opts",)

    def update(self, **kwargs):
        self.opts.update(kwargs)

    def get(self, key: str) -> Any:
        return self.opts.get(key)


class AnimationOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        duration: Optional[Numeric] = None,
        delay: Optional[Numeric] = None,
        easing: Optional[str] = None,
        mode: Optional[str] = None,
        is_increase_effect: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "duration": duration,
            "delay": delay,
            "easing": easing,
            "mode": mode,
            "increaseEffect": is_increase_effect,
        }
