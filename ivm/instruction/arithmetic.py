from ivm.abc.machine import AbstractMachine
from ivm.intergers import int64, uint64
from ivm.lib.instruction import inst

def sign(i: uint64) -> bool:
  return (i >> 63) == 1

@inst(uint64(0x00002000))
def add(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a + b)
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0
  machine.carry = machine.stack[-1] < a
  machine.overflow = sign(a) == sign(b) and sign(a) != machine.sign

@inst(uint64(0x00002001))
def adc(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a + b + int(machine.carry))
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0
  machine.carry = machine.stack[-1] - (1 if machine.carry else 0) < a
  machine.overflow = sign(a) == sign(b) and sign(a) != machine.sign

@inst(uint64(0x00002002))
def sub(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a - b)
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0
  machine.carry = a >= b
  machine.overflow = sign(a) != sign(b) and sign(a) != machine.sign

@inst(uint64(0x00002003))
def sbb(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a - b - int(not machine.carry))
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0
  machine.carry = a > b or (a == b and machine.carry)
  machine.overflow = sign(a) != sign(b) and sign(a) != machine.sign

@inst(uint64(0x00002004))
def mul(machine: AbstractMachine, _):
  machine.stack.append(machine.stack.pop() * machine.stack.pop())
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x00002005))
def idiv(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a // b)
  machine.stack.append(a % b)

@inst(uint64(0x00002006))
def and_(machine: AbstractMachine, _):
  machine.stack.append(machine.stack.pop() & machine.stack.pop())
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x00002007))
def or_(machine: AbstractMachine, _):
  machine.stack.append(machine.stack.pop() | machine.stack.pop())
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

def xor(machine: AbstractMachine, _):
  machine.stack.append(machine.stack.pop() ^ machine.stack.pop())
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x00002009))
def not_(machine: AbstractMachine, _):
  machine.stack.append(~machine.stack.pop())
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x0000200a))
def shl(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a << b)
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x0000200b))
def shr(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(a >> b)
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x0000200c))
def sar(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(uint64(int64(a) >> b))
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x0000200d))
def sal(machine: AbstractMachine, _):
  a, b = machine.stack.pop(), machine.stack.pop()
  machine.stack.append(uint64(int64(a) << b))
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0

@inst(uint64(0x0000200e))
def inc(machine: AbstractMachine, _):
  machine.stack.append(machine.stack.pop() + 1)
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0
  machine.carry = machine.stack[-1] == 0
  machine.overflow = machine.stack[-1] == 0

@inst(uint64(0x0000200f))
def dec(machine: AbstractMachine, _):
  machine.stack.append(machine.stack.pop() - 1)
  machine.sign = (machine.stack[-1] >> 63) == 1
  machine.zero = machine.stack[-1] == 0
  machine.carry = machine.stack[-1] == 0xFFFFFFFFFFFFFFFF
