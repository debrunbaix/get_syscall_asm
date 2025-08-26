# get_syscall_asm

This program permit to know the calling convention for a syscall.

## use

```bash
usage: get_syscall [-h] -a ARCH -s SYSCALL

This program permit to know the calling convention for a syscall.

options:
  -h, --help            show this help message and exit
  -a ARCH, --arch ARCH  x86 || x64 || arm || arm64
  -s SYSCALL, --syscall SYSCALL
                        read, write, etc...
```

## exemple

### execve on x64

```bash
./get_syscall.py -a x64 -s execve
EXECVE :
    rax : 0x3b

    rdi : const char *filename
    rdx : const char *const *envp
```

### write on arm64

```bash
./get_syscall.py -a arm64 -s write
WRITE :
    x0 : 0x40

    x0 : unsigned int fd
    x2 : size_t count
```
