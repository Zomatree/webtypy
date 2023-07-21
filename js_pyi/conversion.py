from __future__ import annotations

_types_dict = {
    'undefined': 'None',
    'void': 'None',
    'any': 'Any',
    'DOMString': 'str',
    'long': 'int',
    'long long': 'int',
    'unsigned long': 'int',
    'unsigned long long': 'int',
    'unsigned short': 'int',
    'boolean': 'bool',
    'double': 'float',
    'unrestricted double': 'float',
    'unrestricted float': 'float',
    'byte': 'int',
    'short': 'int',
    'octet': 'int',
    'false': 'False',
    'true': 'True',
    # generics
    'sequence': 'Sequence',
    'Promise': 'Awaitable',
    "USVString": "str",
    "CSSOMString": "str",
    "DOMString": "str"
}


def to_py_type(s: str) -> str:
    return _types_dict.get(s, s)


_values_dict = {
    'null': 'None',
    "false": "False",
    "true": "True"
}


def to_py_value(s: str) -> str:
    return _values_dict.get(s, s)


reserved_keywords = {
    'async',
    'from',
    'break',
    'is',
    'continue',
    'assert',
    'in',
}


def to_py_name(s: str) -> str:
    if s in reserved_keywords:
        return s + '_'
    return s
