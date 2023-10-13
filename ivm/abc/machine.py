from abc import ABC
from typing import Callable, TypeAlias

from ivm.intergers import uint64


class AbstractMachine(ABC):
  stack: list[uint64]
  """current operand stack"""

  heap: bytearray
  """heap memory area"""

  rp: list[int]
  """return pointer stack"""

  ip: int
  """instruction pointer"""

  code: bytes
  """code area"""

  flags: uint64
  """flag register
  0: zero flag, set if the result of the last operation is zero
  1: carry flag, set if the last operation resulted in a carry or borrow
  2: overflow flag, set if the last operation resulted in an overflow
  3: sign flag, set if the result of the last operation is negative
  4: interrupt flag, set if interrupts are enabled
  5-63: reserved
  """
  halted: bool
  """halted flag"""

  zero: bool
  """zero flag"""

  carry: bool
  """carry flag"""

  overflow: bool
  """overflow flag"""

  sign: bool
  """sign flag"""

  interrupt: bool
  """interrupt flag"""

Instruction: TypeAlias = Callable[[AbstractMachine, list[uint64]], None]
