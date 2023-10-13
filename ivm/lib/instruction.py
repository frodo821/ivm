from dataclasses import dataclass
from ivm.abc.machine import Instruction
from ivm.intergers import uint64

@dataclass
class Flags:
  is_jump: bool = False

INSTRUCTION_SET: dict[uint64, tuple[Instruction, int, Flags]] = {}

def inst(opcode: uint64, operands: int = 0, is_jump: bool = False):
  def _inst(func: Instruction):
    if opcode in INSTRUCTION_SET:
      print(f"WARNING: Overwriting instruction {opcode:x}")
    INSTRUCTION_SET[opcode] = (func, operands, Flags(is_jump))
    return func
  return _inst
