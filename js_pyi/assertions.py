from __future__ import annotations
from typing import Any, NoReturn, TypeGuard, TypeVar

T = TypeVar("T")

def unhandled(argument: Any) -> NoReturn:
    raise Exception(f'unhandled type={type(argument)} `{argument}`')


def expect_isinstance(instance: Any, *any_of: type[T]) -> TypeGuard[T]:
    if isinstance(instance, any_of):
        return True

    raise Exception(f'expect instance to be `{any_of}` but instead found to be `{type(instance)}`')
