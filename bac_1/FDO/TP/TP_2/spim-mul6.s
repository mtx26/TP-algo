main:
    addi $sp, $sp, -4
    sw $ra, 0($sp)

    jal params
    move $a0, $v0
    jal params
    move $a1, $v0
    jal params
    move $a2, $v0
    jal params
    move $a3, $v0

    jal params
    addi $sp, $sp, -4
    sw $v0, 0($sp)

    jal params
    addi $sp, $sp, -4
    sw $v0, 0($sp)
    
    jal mul6

    li $v0, 1
    move $a0, $t2
    syscall

    lw $ra, 0($sp)
    addi $sp, $sp, 4

    jr		$ra					# jump to $ra
    


params:
    li $v0, 5
    syscall
    jr		$ra					# jump to $ra
    

mul6:
    lw $t0, 0($sp)
    lw $t1, 4($sp)
    addi $sp, $sp, 8

    mult	$t0, $t1			# $t0 * $t1 = Hi and Lo registers
    mflo	$t2					# copy Lo to $t2
    mult	$t2, $a0			# 2 * $t1 = Hi and Lo registers
    mflo	$t2					# copy Lo to $t2
    mult	$t2, $a1			# 2 * $t1 = Hi and Lo registers
    mflo	$t2	    
    mult	$t2, $a2			# 2 * $t1 = Hi and Lo registers
    mflo	$t2	    
    mult	$t2, $a3			# 2 * $t1 = Hi and Lo registers
    mflo	$t2	    
    jr		$ra					# jump to $ra
    