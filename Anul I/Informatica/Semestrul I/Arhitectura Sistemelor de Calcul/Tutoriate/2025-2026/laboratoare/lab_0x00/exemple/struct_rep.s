.data
    n: .long 5
    s: .space 4

.text
.global main

# -- Solutia 1 ------ #
main:                 #
    xorl %ecx, %ecx   #
                      #
etloop:               #
    cmp n, %ecx       #
    je etexit         #
                      #
    addl %ecx, s      #
    incl %ecx         #
    jmp etloop        #
                      #
etexit:               #
    movl $1, %eax     #
    xorl %ebx, %ebx   #
    int $0x80         #
# ------------------- #
; # -- Solutia 2 ------ #
; main:                 #
;     decl n            # --------------------------- #
; # necesitatea decrementarii valorii n este data de  # 
; # faptul ca structura repetitiva este intrerupta    #
; # atunci cand valoarea registrului %ECX devine nula #
;     movl n, %ecx      # --------------------------- #
;                       #
; etloop:               #
;     addl %ecx, s      #
;     loop etloop       #
;     jmp etexit        # 
;                       #
; etexit:               #
;     movl $1, %eax     #
;     xorl %ebx, %ebx   #
;     int $0x80         #
; # ------------------- #
