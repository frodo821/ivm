_start:
  push 20
  call fib
  hlt
fib:
  dup
  push 2
  sub
  jge fib_end
  pop
  dec
  dup
  call fib
  swap
  dec
  call fib
  add
  ret
fib_end:
  pop
  push 1
  swap
  pop
  ret
