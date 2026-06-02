.data
hex: .asciiz "0123456789ABCDEF"

.text
main:
    li      $a0, 123

    jal     to_hex
    nop

    li      $v0, 10
    syscall


to_hex:
    addi    $sp, $sp, -8
    sw      $ra, 4($sp)
    sw      $a0, 0($sp)

    li      $t0, 16
    blt     $a0, $t0, print_digit

    div     $a0, $t0
    mflo    $a0
    mfhi    $t1

    sw      $t1, 0($sp)

    jal     to_hex
    nop

    lw      $t1, 0($sp)
    j       print_remainder


print_digit:
    move    $t1, $a0

print_remainder:
    la      $t2, hex
    add     $t2, $t2, $t1
    lb      $a0, 0($t2)

    li      $v0, 11
    syscall

    lw      $ra, 4($sp)
    addi    $sp, $sp, 8
    jr      $ra