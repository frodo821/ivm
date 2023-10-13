from ivm.assembler.assembly import Assembly
from argparse import ArgumentParser

from ivm.machine import VirtualMachine

parser = ArgumentParser(description="IVM Assembler")
parser.add_argument("file", help="Input file", nargs=1)

args = parser.parse_args()

with open(args.file[0], 'rb') as f:
  asm = f.read()

machine = VirtualMachine(asm)
machine.exec()
print(machine.stack)
