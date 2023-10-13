_start:
  push 0
  push 100
.loop:
  dup
  swap2
  add
  swap
  dec
  jz .end
  jmp .loop
; loop ここまで
.end:
  pop
  hlt
