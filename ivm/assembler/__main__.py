from ivm.assembler.assembly import Assembly
from argparse import ArgumentParser

parser = ArgumentParser(description="IVM Assembler")
parser.add_argument("--input", "-i", help="Input file", nargs="+", default=[], dest="files")

args = parser.parse_args()

for file in args.files:
  with open(file) as f:
    assembly = Assembly()
    asm = assembly.assemble(f.read().splitlines())
    dest = file.rsplit(".", 1)[0] + ".iv"

    with open(dest, "wb") as f:
      f.write(asm)
