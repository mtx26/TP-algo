.text
main:
    li $v0, 5
    syscall
    move $t0, $v0
    li $t1, 2

boucle:
    divu $t0, $t1

    mflo $t0       # quotient
    mfhi $a0       # reste = bit de poids faible

    li $v0, 1
    syscall

    bgtz $t0, boucle
    nop

fin:
    jr $ra
    nop