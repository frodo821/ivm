_start:
  push 0
  push 100
.loop:
  dup
  swap2
  add
  swap
  dec
  jnz .loop
; loop ここまで
  pop
  hlt
