main:
    li $a0, 5

boucle:
    addi $a0, $a0, -1
    bgtz $a0, boucle

    jr $ra
