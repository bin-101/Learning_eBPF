#!/usr/bin/python3

# 実行結果
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob2$ sudo python3 main.py 
# ID 1000: 356    ID 0: 2 ID 116: 1       ID 10000000: 227
# ID 1000: 643    ID 0: 3 ID 116: 1       ID 10000000: 227
# ID 1000: 1005   ID 0: 6 ID 116: 1       ID 10000000: 972
# ID 1000: 1313   ID 0: 14        ID 102: 1       ID 116: 1       ID 10000000: 972
# ID 1000: 1655   ID 0: 15        ID 102: 1       ID 116: 2       ID 10000000: 1635
# ^CTraceback (most recent call last):
#   File "/home/bin101/code/Learning_eBPF/sec02/prob2/main.py", line 52, in <module>
#     sleep(2)
# KeyboardInterrupt

# copy from https://github.com/lizrice/learning-ebpf/blob/main/chapter2/hello-map.py
from bcc import BPF
from time import sleep

program = r"""
BPF_HASH(counter_table);

int hello_execve(void *ctx){
    u64 uid;
    u64 counter=0;
    u64 *p;

    uid=bpf_get_current_uid_gid()&0xFFFFFFFF;
    p=counter_table.lookup(&uid);
    if(p!=0){
        counter=*p;
    }
    counter++;
    uid*=10000;
    counter_table.update(&uid,&counter);
    bpf_trace_printk("execve!\\n");
    return 0;
}

int hello_write(void *ctx){
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
    bpf_trace_printk("write!\\n");
    return 0;
}
"""

b=BPF(text=program)
syscall_execve=b.get_syscall_fnname("execve")
syscall_write=b.get_syscall_fnname("write")

b.attach_kprobe(event=syscall_execve,fn_name="hello_execve")
b.attach_kprobe(event=syscall_write,fn_name="hello_write")

while True:
    sleep(2)
    s=""
    for k,v in b["counter_table"].items():
        s+=f"ID {k.value}: {v.value}\t"
    print(s)
    # b.trace_print()

