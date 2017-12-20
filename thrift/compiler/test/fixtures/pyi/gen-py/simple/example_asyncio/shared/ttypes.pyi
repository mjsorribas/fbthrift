#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
import typing as t

from thrift import Thrift
from thrift.protocol.TProtocol import TProtocolBase

import simple.dependent_asyncio.dependent.ttypes

UTF8STRINGS: bool


class AnEnum:
    ONE: int
    TWO: int
    THREE: int
    FOUR: int

    _VALUES_TO_NAMES: t.Dict[int, str]
    _NAMES_TO_VALUES: t.Dict[str, int]


class SimpleException(Thrift.TException):
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        err_code: t.Optional[int] = ...
    ) -> None:
        self.err_code: t.Optional[int]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...


class SimpleStruct:
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        is_on: t.Optional[bool] = ...,
        tiny_int: int = ...,
        small_int: t.Optional[int] = ...,
        nice_sized_int: t.Optional[int] = ...,
        big_int: t.Optional[int] = ...,
        coarse_real: t.Optional[float] = ...,
        precise_real: t.Optional[float] = ...,
        a_str: t.Optional[str] = ...,
        a_bytes: t.Optional[bytes] = ...
    ) -> None:
        self.is_on: t.Optional[bool]
        self.tiny_int: int
        self.small_int: t.Optional[int]
        self.nice_sized_int: t.Optional[int]
        self.big_int: t.Optional[int]
        self.coarse_real: t.Optional[float]
        self.precise_real: t.Optional[float]
        self.a_str: t.Optional[str]
        self.a_bytes: t.Optional[bytes]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...


class ComplexStruct:
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        structOne: t.Optional[SimpleStruct] = ...,
        structTwo: t.Optional[SimpleStruct] = ...,
        an_integer: t.Optional[int] = ...,
        name: t.Optional[str] = ...,
        an_enum: t.Optional[int] = ...,
        values: t.Optional[t.List[int]] = ...,
        structs: t.Optional[t.List[SimpleStruct]] = ...,
        amap: t.Optional[t.Dict[str, str]] = ...,
        aset: t.Optional[t.Set[str]] = ...,
        item: t.Optional[simple.dependent_asyncio.dependent.ttypes.Item] = ...
    ) -> None:
        self.structOne: t.Optional[SimpleStruct]
        self.structTwo: t.Optional[SimpleStruct]
        self.an_integer: t.Optional[int]
        self.name: t.Optional[str]
        self.an_enum: t.Optional[int]
        self.values: t.Optional[t.List[int]]
        self.structs: t.Optional[t.List[SimpleStruct]]
        self.amap: t.Optional[t.Dict[str, str]]
        self.aset: t.Optional[t.Set[str]]
        self.item: t.Optional[simple.dependent_asyncio.dependent.ttypes.Item]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...