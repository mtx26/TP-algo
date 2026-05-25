main:
    li      $a0, 5
    li      $a1, 6

    addi    $sp, $sp, -4
    sw      $ra, 0($sp)
    jal     mult_rec
    nop
    lw      $ra, 0($sp)  
    addi    $sp, $sp, 4 
mult_rec:
    beq		$a0, $zero, casbase	# if $t0 == $t1 then goto target

    addi    $sp, $sp, -8
    sw      $ra, 4($sp)
    sw      $a0, 0($sp)

    addi    $a0, $a0, -1

    jal     mult_rec

    lw      $a0, 0($sp)
    lw      $ra, 4($sp)
    addi    $sp, $sp, 8

    add		$v0, $v0, $a1

    jr		$ra					# jump to $ra
    
    
casbase:
    li      $v0, 0
    jr		$ra					# jump to $ra
    