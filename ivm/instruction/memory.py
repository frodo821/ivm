from ivm.abc.machine import AbstractMachine
from ivm.intergers import uint64
from ivm.lib.instruction import inst

@inst(uint64(0x00000000), operands=1)
def push(machine: AbstractMachine, operands):
  machine.stack.append(operands[0])

@inst(uint64(0x00000001), operands=0)
def dup(machine: AbstractMachine, _):
  machine.stack.append(machine.stack[-1])

@inst(uint64(0x00000002), operands=0)
def pop(machine: AbstractMachine, _):
  machine.stack.pop()

@inst(uint64(0x00000003), operands=0)
def swap(machine: AbstractMachine, _):
  machine.stack[-1], machine.stack[-2] = machine.stack[-2], machine.stack[-1]

@inst(uint64(0x00000004), operands=0)
def swap2(machine: AbstractMachine, _):
  machine.stack[-1], machine.stack[-3] = machine.stack[-3], machine.stack[-1]

@inst(uint64(0x00000005), operands=0)
def swap3(machine: AbstractMachine, _):
  machine.stack[-1], machine.stack[-4] = machine.stack[-4], machine.stack[-1]

@inst(uint64(0x00000006), operands=0)
def swap4(machine: AbstractMachine, _):
  machine.stack[-1], machine.stack[-5] = machine.stack[-5], machine.stack[-1]

@inst(uint64(0x00000007), operands=0)
def swap5(machine: AbstractMachine, _):
  machine.stack[-1], machine.stack[-6] = machine.stack[-6], machine.stack[-1]
