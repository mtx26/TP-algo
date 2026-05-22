    .text
main:
    li $a0, 5

boucle:
    li $v0, 1
    syscall

    addi $a0, $a0, -1
    bgtz $a0, boucle

    jr $ra
