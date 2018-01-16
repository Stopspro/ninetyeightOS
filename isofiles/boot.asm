global start

section .text
bits 32
start:
    mov word [0xb8000], 0x0248 ; n
    mov word [0xb8002], 0x0265 ; i
    mov word [0xb8004], 0x026c ; n
    mov word [0xb8006], 0x026c ; e
    mov word [0xb8008], 0x026f ; t
    mov word [0xb800a], 0x022c ; y
    mov word [0xb800c], 0x0220 ; e
    mov word [0xb800e], 0x0277 ; i
    mov word [0xb8010], 0x026f ; g
    mov word [0xb8012], 0x0272 ; h
    mov word [0xb8014], 0x026c ; t
    mov word [0xb8016], 0x0264 ; O
    mov word [0xb8018], 0x0221 ; S
    section .bss
    hlt

section .bss

align 4096

p4_table:
    resb 4096
p3_table:
    resb 4096
p2_table:
    resb 4096
