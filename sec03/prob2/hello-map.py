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

# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob2$ sudo bpftool prog show name hello
# [sudo] bin101 のパスワード: 
# 134: xdp  name hello  tag 4ae0216d65106432  gpl
#         loaded_at 2025-07-07T22:03:12+0900  uid 0
#         xlated 168B  jited 109B  memlock 4096B  map_ids 47,48
#         btf_id 251
# 143: kprobe  name hello  tag e65cc23946512007  gpl
#         loaded_at 2025-07-07T22:09:10+0900  uid 0
#         xlated 224B  jited 134B  memlock 4096B  map_ids 53
#         btf_id 258