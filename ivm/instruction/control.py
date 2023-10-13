from ivm.abc.machine import AbstractMachine
from ivm.intergers import uint64
from ivm.lib.instruction import inst

@inst(uint64(0x00001000))
def nop(machine: AbstractMachine, _):
  pass

@inst(uint64(0x00001001), operands=1, is_jump=True)
def jmp(machine: AbstractMachine, operands):
  machine.ip = int(operands[0])

@inst(uint64(0x00001002), operands=1, is_jump=True)
def jz(machine: AbstractMachine, operands):
  if machine.zero:
    machine.ip = int(operands[0])

@inst(uint64(0x00001003), operands=1, is_jump=True)
def jnz(machine: AbstractMachine, operands):
  if not machine.zero:
    machine.ip = int(operands[0])

@inst(uint64(0x00001004), operands=1, is_jump=True)
def jn(machine: AbstractMachine, operands):
  if machine.sign:
    machine.ip = int(operands[0])

@inst(uint64(0x00001005), operands=1, is_jump=True)
def jp(machine: AbstractMachine, operands):
  if not machine.sign:
    machine.ip = int(operands[0])

@inst(uint64(0x00001006), operands=1, is_jump=True)
def jc(machine: AbstractMachine, operands):
  if machine.carry:
    machine.ip = int(operands[0])

@inst(uint64(0x00001007), operands=1, is_jump=True)
def jnc(machine: AbstractMachine, operands):
  if not machine.carry:
    machine.ip = int(operands[0])

@inst(uint64(0x00001008), operands=1, is_jump=True)
def jof(machine: AbstractMachine, operands):
  if machine.overflow:
    machine.ip = int(operands[0])

@inst(uint64(0x00001009), operands=1, is_jump=True)
def jnof(machine: AbstractMachine, operands):
  if not machine.overflow:
    machine.ip = int(operands[0])

@inst(uint64(0x0000100a))
def jmpd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  machine.ip = int(to)

@inst(uint64(0x0000100b))
def jzd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if machine.zero:
    machine.ip = int(to)

@inst(uint64(0x0000100c))
def jnzd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if not machine.zero:
    machine.ip = int(to)

@inst(uint64(0x0000100d))
def jnd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if machine.sign:
    machine.ip = int(to)

@inst(uint64(0x0000100e))
def jpd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if not machine.sign:
    machine.ip = int(to)

@inst(uint64(0x0000100f))
def jcd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if machine.carry:
    machine.ip = int(to)

@inst(uint64(0x00001010))
def jncd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if not machine.carry:
    machine.ip = int(to)

@inst(uint64(0x00001011))
def jofd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if machine.overflow:
    machine.ip = int(to)

@inst(uint64(0x00001012))
def jnofd(machine: AbstractMachine, operands):
  to = machine.stack.pop()
  if not machine.overflow:
    machine.ip = int(to)

@inst(uint64(0x00001013), operands=1, is_jump=True)
def call(machine: AbstractMachine, operands):
  machine.rp.append(machine.ip)
  machine.ip = int(operands[0])

@inst(uint64(0x00001014))
def calld(machine: AbstractMachine, operands):
  machine.rp.append(machine.ip)
  to = machine.stack.pop()
  machine.ip = int(to)

@inst(uint64(0x00001015))
def ret(machine: AbstractMachine, _):
  machine.ip = machine.rp.pop()

@inst(uint64(0x00001016))
def sez(machine: AbstractMachine, _):
  machine.zero = True

@inst(uint64(0x00001017))
def clz(machine: AbstractMachine, _):
  machine.zero = False

@inst(uint64(0x00001018))
def sec(machine: AbstractMachine, _):
  machine.carry = True

@inst(uint64(0x00001019))
def clc(machine: AbstractMachine, _):
  machine.carry = False

@inst(uint64(0x0000101a))
def sev(machine: AbstractMachine, _):
  machine.overflow = True

@inst(uint64(0x0000101b))
def clv(machine: AbstractMachine, _):
  machine.overflow = False

@inst(uint64(0x0000101c))
def sen(machine: AbstractMachine, _):
  machine.sign = True

@inst(uint64(0x0000101d))
def cln(machine: AbstractMachine, _):
  machine.sign = False

@inst(uint64(0x0000101e))
def sei(machine: AbstractMachine, _):
  machine.interrupt = True

@inst(uint64(0x0000101f))
def cli(machine: AbstractMachine, _):
  machine.interrupt = False

@inst(uint64(0x00001020))
def hlt(machine: AbstractMachine, _):
  machine.halted = True

@inst(uint64(0x00001021), operands=1, is_jump=True)
def jl(machine: AbstractMachine, operands):
  if machine.sign != machine.overflow:
    machine.ip = int(operands[0])

@inst(uint64(0x00001022), operands=1, is_jump=True)
def jle(machine: AbstractMachine, operands):
  if machine.sign != machine.overflow or machine.zero:
    machine.ip = int(operands[0])

@inst(uint64(0x00001023), operands=1, is_jump=True)
def jg(machine: AbstractMachine, operands):
  if machine.sign == machine.overflow and not machine.zero:
    machine.ip = int(operands[0])

@inst(uint64(0x00001024), operands=1, is_jump=True)
def jge(machine: AbstractMachine, operands):
  if machine.sign == machine.overflow:
    machine.ip = int(operands[0])

@inst(uint64(0x00001025))
def jld(machine: AbstractMachine, _):
  if machine.sign != machine.overflow:
    machine.ip = int(machine.stack.pop())

@inst(uint64(0x00001026))
def jled(machine: AbstractMachine, _):
  if machine.sign != machine.overflow or machine.zero:
    machine.ip = int(machine.stack.pop())

@inst(uint64(0x00001027))
def jgd(machine: AbstractMachine, _):
  if machine.sign == machine.overflow and not machine.zero:
    machine.ip = int(machine.stack.pop())

@inst(uint64(0x00001028))
def jged(machine: AbstractMachine, _):
  if machine.sign == machine.overflow:
    machine.ip = int(machine.stack.pop())

@inst(uint64(0x10101021))
def dbg(machine: AbstractMachine, _):
  print("stack:", machine.stack)
  print("ip:", machine.ip)
  print("rp:", machine.rp)
  print("flags:")
  print("  zero:     ", machine.zero)
  print("  carry:    ", machine.carry)
  print("  overflow: ", machine.overflow)
  print("  sign:     ", machine.sign)
  print("  interrupt:", machine.interrupt)
  print("  halted:   ", machine.halted)
  print()
