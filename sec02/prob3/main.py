#!/usr/bin/python3

# 実行結果
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob3$ sudo python3 main.py
# ID 108: 273     ID 1000: 10279  ID 116: 4       ID 0: 21
# ID 113: 2       ID 108: 506     ID 1000: 22366  ID 116: 4       ID 0: 70
# ID 102: 7       ID 113: 2       ID 108: 779     ID 1000: 40164  ID 116: 4       ID 0: 242
# ID 102: 7       ID 113: 4       ID 108: 1053    ID 1000: 52814  ID 116: 8       ID 0: 258
# ID 102: 7       ID 113: 4       ID 108: 1297    ID 1000: 64590  ID 116: 8       ID 0: 295
# ^CTraceback (most recent call last):
#   File "/home/bin101/code/Learning_eBPF/sec02/prob3/main.py", line 29, in <module>
#     sleep(2)
# KeyboardInterrupt
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob3$ id 108
# uid=108(systemd-oom) gid=116(systemd-oom) groups=116(systemd-oom)
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob3$ id 116
# uid=116(rtkit) gid=123(rtkit) groups=123(rtkit)
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob3$ id 0
# uid=0(root) gid=0(root) groups=0(root)
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob3$ id 1000
# uid=1000(bin101) gid=1000(bin101) groups=1000(bin101),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),134(lxd),135(sambashare),139(libvirt)


from bcc import BPF
import ctypes as ct
from time import sleep

program=r"""
BPF_HASH(counter_table);

int hello(struct bpf_raw_tracepoint_args *ctx){
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
b.attach_raw_tracepoint(tp="sys_enter",fn_name="hello")

while True:
    sleep(2)
    s=""
    for k,v in b["counter_table"].items():
        s+=f"ID {k.value}: {v.value}\t"
    print(s)