.data
mesaj: .ascii "salut, x86\n"

.text
.global main
main:
    # 1 character takes up one byte - ASCII
    mov $4, %eax     # id of write instruction for syscall
    mov $1, %ebx     # id of "place" to write
    mov $mesaj, %ecx # pointer to start of string
    mov $11, %edx    # number of characters from string
    int $0x80         # syscall for write

    mov $1, %eax     # exit instruction id
    xor %ebx, %ebx    # movl $0, %ebx
    int $0x80         # syscall for exit