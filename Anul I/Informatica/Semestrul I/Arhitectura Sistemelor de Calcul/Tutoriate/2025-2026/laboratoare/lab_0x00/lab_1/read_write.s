# citirea si afisarea unui sir de caractere din terminal

.data
buf_size: .word 256
prompt: .ascii "Input: " 
output: .ascii "Output: "
buffer: .space 256
# ------syscall constants------ #
# 1 - exit:                     #
#       %eax = 0x01             #
#       %ebx = error_code       #
#                               #
# 2 - read:                     #
#       %eax = 0x03             #
#       %ebx = unsigned int fd  #
#       %ecx = char *buf        #
#       %edx = size_t count     #
#                               #
# 3 - write:                    #
#       %eax = 0x04             #
#       %ebx = unsigned int fd  #    
#       %ecx = const char *buf  #
#       %edx = size_t count     #
# ----------------------------- #
# --------TERMINOLOGIE--------- #
# fd = file descriptor (id)     #
# buf = spatiu stocare string   #
# count = marime buffer         #
# ----------------------------- #

.text
.global main
main:
    # afisare mesaj de input
    mov $4, %eax # write id
    mov $1, %ebx # terminal stdout
    mov $prompt, %ecx
    mov $7, %edx
    int $0x80
    
    # citire mesaj de la tastatura in terminal
    mov $3, %eax # read id
    xor %ebx, %ebx # terminal stdin
    mov $buffer, %ecx
    mov buf_size, %edx
    int $0x80

    # afisare mesaj de output
    mov $4, %eax # write id
    mov $1, %ebx # terminal stdout
    mov $output, %ecx
    mov $8, %edx
    int $0x80

    # afisare mesaj primit de la tastatura
    mov $4, %eax # write id
    mov $1, %ebx # terminal stdout
    mov $buffer, %ecx 
    mov buf_size, %edx
    int $0x80

    mov $1, %eax
    xor %ebx, %ebx
    int $0x80

