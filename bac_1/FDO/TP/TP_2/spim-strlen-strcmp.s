.data
str: .asciiz "Helor dugs, sjdh kjydhuihijfijijfdjshukhfskuiuhfhdskfuuishufhsduhuifhuhsu"

.text
main:
    la $a0, str

    addi $sp, $sp, -4
    sw $ra, 0($sp)

    jal strlen
    nop

    # afficher la longueur
    move $a0, $v0
    li $v0, 1
    syscall

    lw $ra, 0($sp)
    addi $sp, $sp, 4

    jr $ra
    nop


strlen:
    li $v0, 0

bouclelen:
    lb $t1, 0($a0)
    beq $t1, $zero, finlen
    nop

    addi $v0, $v0, 1
    addi $a0, $a0, 1

    j bouclelen
    nop

finlen:
    jr $ra
    nop