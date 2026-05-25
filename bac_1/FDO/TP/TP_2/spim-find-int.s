.data
tableau:
    .word   -17, 5, 9, 123, 1024

.text
main:
    la      $a0, tableau
    li      $a1, 5
    li      $a2, 9

    addi    $sp, $sp, -4
    sw      $ra, 0($sp)

    jal     find_int
    nop

    lw      $ra, 0($sp)
    addi    $sp, $sp, 4

    jr      $ra


find_int:
    li      $v0, 0
    move    $t1, $a0

boucle:
    lw      $t2, 0($t1)
    beq     $t2, $a2, find_fin

    addi    $v0, $v0, 1
    addi    $t1, $t1, 4
    blt     $v0, $a1, boucle

    li      $v0, -1

find_fin:
    jr      $ra