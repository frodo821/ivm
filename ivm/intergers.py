from typing import ClassVar

class SizedInt:
  size: ClassVar[int]
  signed: ClassVar[bool]

  def __init_subclass__(cls, *args, size: int = 64, signed: bool = True, **kwargs) -> None:
    cls.size = size
    cls.signed = signed

  def pack(self):
    return self.value.to_bytes(self.size // 8, "little", signed=self.signed)

  @classmethod
  def unpack(cls, value: bytes):
    return cls(int.from_bytes(value, "little", signed=cls.signed))

  @classmethod
  def __clip(cls, value: 'int | SizedInt') -> int:
    value = int(value)
    if cls.signed:
      sign = value >> (cls.size - 1)
      mask = 1 << (cls.size - 1)
      return (value & (mask - 1)) - (mask if sign else 0)
    else:
      return value & ((1 << cls.size) - 1)

  @property
  def real(self) -> int:
    return self.value

  @property
  def imag(self) -> int:
    return 0

  def __init__(self, value: 'int | SizedInt' = 0):
    self.value = self.__clip(value)

  def __add__(self, other):
    return type(self)(int(self) + int(other))

  def __sub__(self, other):
    return type(self)(int(self) - int(other))

  def __mul__(self, other):
    return type(self)(int(self) * int(other))

  def __floordiv__(self, other):
    return type(self)(int(self) // int(other))

  def __mod__(self, other):
    return type(self)(int(self) % int(other))

  def __pow__(self, other):
    return type(self)(int(self) ** int(other))

  def __lshift__(self, other):
    return type(self)(int(self) << int(other))

  def __rshift__(self, other):
    return type(self)(int(self) >> int(other))

  def __and__(self, other):
    return type(self)(int(self) & int(other))

  def __or__(self, other):
    return type(self)(int(self) | int(other))

  def __xor__(self, other):
    return type(self)(int(self) ^ int(other))

  def __neg__(self):
    return type(self)(-int(self))

  def __pos__(self):
    return type(self)(+int(self))

  def __abs__(self):
    return type(self)(abs(int(self)))

  def __invert__(self):
    return type(self)(~int(self))

  def __lt__(self, other):
    return int(self) < int(other)

  def __le__(self, other):
    return int(self) <= int(other)

  def __eq__(self, other):
    return int(self) == int(other)

  def __ne__(self, other):
    return int(self) != int(other)

  def __int__(self) -> int:
    return self.value

  def __str__(self) -> str:
    return f"{int(self)}'{'i' if self.signed else 'u'}{self.size}"

  def __bool__(self) -> bool:
    return bool(int(self))

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}({int(self)})"

  def __hash__(self) -> int:
    return hash(str(self))

class int8(SizedInt, size=8):
  pass

class int16(SizedInt, size=16):
  pass

class int32(SizedInt, size=32):
  pass

class int64(SizedInt, size=64):
  pass

class uint8(SizedInt, size=8, signed=False):
  pass

class uint16(SizedInt, size=16, signed=False):
  pass

class uint32(SizedInt, size=32, signed=False):
  pass

class uint64(SizedInt, size=64, signed=False):
  pass
