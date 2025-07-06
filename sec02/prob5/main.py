#!/usr/bin/python3

# 実行結果
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob5$ sudo python3 main.py
# ID 32: 1        ID 63: 1        ID 28: 270      ID 33: 24       ID 321: 10      ID 17: 68       ID 318: 27      ID 202: 1183    ID 218: 17      ID 285: 1       ID 233: 17      ID 7: 577       ID 46: 2        ID 12: 51       ID 254: 28      ID 231: 21  ID 39: 24       ID 108: 49      ID 262: 666     ID 87: 1        ID 47: 527      ID 77: 1        ID 158: 34      ID 270: 3       ID 58: 3        ID 157: 9       ID 439: 1       ID 104: 49      ID 302: 19      ID 21: 63       ID 273: 35 ID 11: 39        ID 8: 16        ID 281: 76      ID 72: 15       ID 44: 388      ID 111: 1       ID 56: 18       ID 186: 10      ID 13: 349      ID 0: 1931      ID 14: 227      ID 293: 20      ID 137: 4       ID 10: 91       ID 107: 55      ID 217: 2   ID 79: 1        ID 230: 1       ID 232: 1150    ID 9: 233       ID 15: 21       ID 59: 17       ID 23: 2        ID 53: 9        ID 286: 9       ID 228: 20      ID 16: 174      ID 102: 49      ID 221: 8       ID 257: 1269    ID 332: 4  ID 110: 7        ID 3: 1390      ID 48: 6        ID 334: 17      ID 5: 10        ID 61: 39       ID 1: 530       ID 99: 1


from bcc import BPF
import ctypes as ct
from time import sleep

program=r"""
BPF_HASH(counter_table);

int hello(struct bpf_raw_tracepoint_args *ctx){
    u64 opcode;
    u64 counter=0;
    u64 *p;

    opcode=ctx->args[1];
    p=counter_table.lookup(&opcode);
    if(p!=0){
        counter=*p;
    }
    counter++;
    counter_table.update(&opcode,&counter);
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