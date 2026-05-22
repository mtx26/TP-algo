        .data
text:   .asciiz "test test testghggggggggggggggggggggggggggggggggggggggggg"

        .text
main:
    la		$a0, text
    li		$v0, 4		# $v0 =4 
    syscall
    
    jr $ra
