#!/usr/bin/python3

# copy from https://github.com/lizrice/learning-ebpf/blob/main/chapter2/hello-map.py
from bcc import BPF
from time import sleep

program = r"""
BPF_HASH(counter_table);

int hello(void *ctx){
    u64 uid;
    u64 counter=0;
    u64 *p;

    uid=bpf_get_current_uid_gid()&0xFFFFFFFF;
    p=counter_table.lookup(&uid);
    if(p!=0){
        counter=*p;
    }
    counter++;
    counter_table.update(&uid,&counter);
    return 0;
}
"""

b=BPF(text=program)
syscall=b.get_syscall_fnname("execve")
b.attach_kprobe(event=syscall,fn_name="hello")

while True:
    sleep(2)
    s=""
    for k,v in b["counter_table"].items():
        s+=f"ID {k.value}: {v.value}\t"
    print(s)
