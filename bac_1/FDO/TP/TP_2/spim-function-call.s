main:
    move $t0, $ra

    addi	$sp, $sp, -4
    sw      $ra, 0($sp)

    jal fct
    lw		$ra, 0($sp)
    addi    $sp, $sp, 4
    jr		$ra					# jump to $ra

    

fct:
    jr $ra