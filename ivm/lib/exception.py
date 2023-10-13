from ivm.intergers import uint64


class MachineExecutionError(Exception):
  def __init__(self, ip: int, opcode: uint64, message: str):
    self.ip = ip
    self.opcode = opcode
    self.message = message
    super().__init__(f"Machine execution error at {ip}: {message} (opcode: {opcode})")

class InvalidOpcodeError(MachineExecutionError):
  def __init__(self, ip: int, opcode: uint64):
    super().__init__(ip, opcode, "Invalid opcode")

class StackUnderflowError(MachineExecutionError):
  def __init__(self, ip: int, opcode: uint64):
    super().__init__(ip, opcode, "Stack underflow")
