// hello.s - Hello World pour Apple Silicon (ARM64 / M2)
    .section __TEXT,__text,regular
    .globl _main
    .p2align 2
_main:
    adrp	x0, Lstr@PAGE
    add		x0, x0, Lstr@PAGEOFF
    bl		_puts
    mov		w0, #0
    ret

    .section __TEXT,__cstring,cstring_literals
Lstr:
    .asciz "Hello, world!"