    .data
accept: .asciiz "Valeur acceptée"
reject: .asciiz "trop grand"

    .text

main:
    li      $v0, 5   # $v0 = 5
    syscall             # read integer from user input, result stored in $v0
    move    $t0,    $v0 # $t0 = user input integer

    beq		$t0, $zero, fin
    
    li		$t1, 10		# $t0 = 10 
    bgt		$t0, $t1, printfat	# if $t0 > $t1 then goto printfat

    la $a0, accept
    li $v0, 4
    syscall
    j		fin				# jump to fin
    
    
    
    

printfat:
    la $a0, reject
    li $v0, 4
    syscall

fin:
    jr		$ra					# jump to $ra
    


