from ivm import INSTRUCTION_SET
from ivm.intergers import uint64

name_op_map = {
  f.__name__.replace('_', ''): (op, operands, flags) for op, (f, operands, flags) in INSTRUCTION_SET.items()
}

def parse_operand(operand: str) -> uint64:
  operand = operand.lower()
  if operand.startswith('0x'):
    return uint64(int(operand[2:], 16))
  if operand.startswith('0b'):
    return uint64(int(operand[2:], 2))
  if operand.startswith('0o'):
    return uint64(int(operand[2:], 8))
  if operand.endswith('h'):
    return uint64(int(operand[:-1], 16))
  if operand.endswith('b'):
    return uint64(int(operand[:-1], 2))
  if operand.endswith('o'):
    return uint64(int(operand[:-1], 8))
  return uint64(int(operand))

class Assembly:
  labels: dict[str, int]
  label_candidates: dict[str, uint64]
  code: bytearray

  def __init__(self):
    self.labels = {}
    self.label_candidates = {}
    self.code = bytearray()

  def directive(self, name: str, operands: list[str]):
    raise NotImplementedError()

  def next(self, line: str):
    line = line.split(';')[0].strip()

    if not line:
      return

    name, *operands = line.split(' ')

    if name.endswith(':'):
      label = name[:-1]
      self.labels[label] = len(self.code)
      if label in self.label_candidates:
        self.code.replace(self.label_candidates[label].pack(), uint64(self.labels[label]).pack())
      return

    if name.startswith('.'):
      self.directive(name, operands)

    if name not in name_op_map:
      raise ValueError(f"Invalid instruction {name}")

    op, num_operands, flags = name_op_map[name]
    if len(operands) != num_operands:
      raise ValueError(f"Invalid number of operands for {name}")

    self.code.extend(op.pack())

    if flags.is_jump:
      if operands[0] in self.labels:
        self.code.extend(uint64(self.labels[operands[0]]).pack())
      elif operands[0] in self.label_candidates:
        self.code.extend(uint64(self.label_candidates[operands[0]]).pack())
      else:
        candidate_label = uint64(0xAC00000000000000 | len(self.label_candidates))
        self.label_candidates[operands[0]] = candidate_label
        self.code.extend(candidate_label.pack())
      return

    for operand in operands:
      self.code.extend(parse_operand(operand).pack())

  def assemble(self, lines: list[str]) -> bytearray:
    for line in lines:
      self.next(line)
    return self.code
