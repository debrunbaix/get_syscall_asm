#!/usr/bin/env python3
import argparse
import requests

URL_SYSCALL_API = "https://api.syscall.sh/v1"
SYSCALL_EP = "/syscalls"
CONVENTIONS_EP = "/conventions"

def get_syscall(syscall_name: str) -> [dict]:
    url = f"{URL_SYSCALL_API}{SYSCALL_EP}/{syscall_name}"

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        return []

def get_convention(arch_name: str) -> dict:
    url = f"{URL_SYSCALL_API}{CONVENTIONS_EP}/{arch_name}"

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        return {}

def print_syscall_for_arch(arch_name: str, syscall_name: str):
    syscall = get_syscall(syscall_name)
    convention = get_convention(arch_name)
    print(syscall_name.upper(), ":")
    for arch in syscall:
        if arch["arch"] == arch_name:
            for key, value in arch.items():
                if key == "return" and value:
                    print(f"    {convention['return']} : {value}\n")
                if key == "arg0" and value:
                    print(f"    {convention['arg0']} : {value}")
                if key == "arg2" and value:
                    print(f"    {convention['arg2']} : {value}")
                if key == "arg3" and value:
                    print(f"    {convention['arg3']} : {value}")
                if key == "arg4" and value:
                    print(f"    {convention['arg4']} : {value}")
                if key == "arg5" and value:
                    print(f"    {convention['arg5']} : {value}")

def main():
    print_syscall_for_arch(args.arch, args.syscall)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='get_syscall',
        description='This program permit to know the calling convention for a syscall.'
    )
    parser.add_argument('-a', '--arch', help='x86 || x64 || arm || arm64', required=True)
    parser.add_argument('-s', '--syscall', help= 'read, write, etc...', required=True)
    args = parser.parse_args()
    main()
