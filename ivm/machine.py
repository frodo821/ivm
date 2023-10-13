from ivm.abc.machine import AbstractMachine
from ivm.intergers import uint64
from ivm.lib.exception import InvalidOpcodeError
import ivm.instruction.arithmetic
import ivm.instruction.condition
import ivm.instruction.control
import ivm.instruction.memory
from ivm.lib.instruction import INSTRUCTION_SET


class VirtualMachine(AbstractMachine):
  def __init__(self, code: bytes):
    self.stack: list[uint64] = []
    self.rp: list[int] = []
    self.ip = 0
    self.code = code
    self.flags = uint64(0)
    self.halted = False

  @property
  def zero(self) -> bool:
    return bool(self.flags & 1)

  @zero.setter
  def zero(self, value: bool):
    if value:
      self.flags |= uint64(1)
    else:
      self.flags &= ~uint64(1)

  @property
  def carry(self) -> bool:
    return bool((self.flags >> 1) & 1)

  @carry.setter
  def carry(self, value: bool):
    if value:
      self.flags |= uint64(1 << 1)
    else:
      self.flags &= ~uint64(1 << 1)

  @property
  def overflow(self) -> bool:
    return bool((self.flags >> 2) & 1)

  @overflow.setter
  def overflow(self, value: bool):
    if value:
      self.flags |= uint64(1 << 2)
    else:
      self.flags &= ~uint64(1 << 2)

  @property
  def sign(self) -> bool:
    return bool((self.flags >> 3) & 1)

  @sign.setter
  def sign(self, value: bool):
    if value:
      self.flags |= uint64(1 << 3)
    else:
      self.flags &= ~uint64(1 << 3)

  @property
  def interrupt(self) -> bool:
    return bool((self.flags >> 4) & 1)

  @interrupt.setter
  def interrupt(self, value: bool):
    if value:
      self.flags |= uint64(1 << 4)
    else:
      self.flags &= ~uint64(1 << 4)

  def execute_one_inst(self):
    opcode = uint64.unpack(self.code[self.ip:self.ip + 8])
    inst = INSTRUCTION_SET.get(opcode, None)

    if inst is None:
      raise InvalidOpcodeError(self.ip, opcode)

    self.ip += 8

    func, num_op, _ = inst
    operands: list[uint64] = []

    for _ in range(num_op):
      operands.append(uint64.unpack(self.code[self.ip:self.ip + 8]))
      self.ip += 8

    func(self, operands)

  def exec(self):
    while not self.halted and self.ip < len(self.code):
      self.execute_one_inst()
