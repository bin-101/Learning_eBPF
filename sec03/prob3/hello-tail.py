#!/usr/bin/python3
from bcc import BPF
import ctypes as ct

program=r"""
BPF_PROG_ARRAY(syscall,500);

int hello(struct bpf_raw_tracepoint_args *ctx){
    int opcode=ctx->args[1];
    syscall.call(ctx,opcode);
    bpf_trace_printk("Another syscall: %d", opcode);
    return 0;
}

int hello_exec(void *ctx){
    bpf_trace_printk("Executing a program");
    return 0;
}

int hello_timer(struct bpf_raw_tracepoint_args *ctx){
    int opcode=ctx->args[1];
    switch(opcode){
        case 222:
            bpf_trace_printk("Creating a timer");
            break;
        case 226:
            bpf_trace_printk("Deleting a timer");
            break;
        default:
            bpf_trace_printk("Some other timer operation");
            break;
    }
    return 0;
}

int ignore_opcode(void *ctx){
    return 0;    
}
"""

b=BPF(text=program)
b.attach_raw_tracepoint(tp="sys_enter",fn_name="hello")

ignore_fn=b.load_func("ignore_opcode",BPF.RAW_TRACEPOINT)
exec_fn=b.load_func("hello_exec",BPF.RAW_TRACEPOINT)
timer_fn=b.load_func("hello_timer",BPF.RAW_TRACEPOINT)

prog_array=b.get_table("syscall")

for i in range(len(prog_array)):
    prog_array[ct.c_int(i)]=ct.c_int(ignore_fn.fd)

prog_array[ct.c_int(59)]=ct.c_int(exec_fn.fd)
prog_array[ct.c_int(222)]=ct.c_int(exec_fn.fd)
prog_array[ct.c_int(223)]=ct.c_int(exec_fn.fd)
prog_array[ct.c_int(224)]=ct.c_int(exec_fn.fd)
prog_array[ct.c_int(225)]=ct.c_int(exec_fn.fd)
prog_array[ct.c_int(226)]=ct.c_int(exec_fn.fd)

b.trace_print()

# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob2$ sudo bpftool prog list
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 152: raw_tracepoint  name hello  tag 9b77eaf7d1a6840f  gpl
#         loaded_at 2025-07-07T22:49:17+0900  uid 0
#         xlated 160B  jited 183B  memlock 4096B  map_ids 55
#         btf_id 260
# 153: raw_tracepoint  name ignore_opcode  tag a04f5eef06a7f555  gpl
#         loaded_at 2025-07-07T22:49:17+0900  uid 0
#         xlated 16B  jited 20B  memlock 4096B
#         btf_id 260
# 154: raw_tracepoint  name hello_exec  tag d0e36209a2ef1b3e  gpl
#         loaded_at 2025-07-07T22:49:17+0900  uid 0
#         xlated 112B  jited 80B  memlock 4096B
#         btf_id 260
# 155: raw_tracepoint  name hello_timer  tag 4db4fdc0ba974dc5  gpl
#         loaded_at 2025-07-07T22:49:17+0900  uid 0
#         xlated 352B  jited 211B  memlock 4096B
#         btf_id 260
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob2$ sudo bpftool prog dump xlated id 152
# int hello(struct bpf_raw_tracepoint_args * ctx):
# ; int opcode=ctx->args[1];
#    0: (79) r6 = *(u64 *)(r1 +8)
# ; bpf_tail_call_((void *)bpf_pseudo_fd(1, -1), ctx,opcode);
#    1: (18) r2 = map[id:55]
# ; ((void (*)(void *, u64, int))BPF_FUNC_tail_call)(ctx, (u64)map_fd, index);
#    3: (bf) r3 = r6
#    4: (85) call bpf_tail_call#12
#    5: (b7) r1 = 6563104
# ; ({ char _fmt[] = "Another syscall: %d"; bpf_trace_printk_(_fmt, sizeof(_fmt), opcode); });
#    6: (63) *(u32 *)(r10 -16) = r1
#    7: (18) r1 = 0x3a6c6c6163737973
#    9: (7b) *(u64 *)(r10 -24) = r1
#   10: (18) r1 = 0x20726568746f6e41
#   12: (7b) *(u64 *)(r10 -32) = r1
#   13: (bf) r1 = r10
# ; 
#   14: (07) r1 += -32
# ; ({ char _fmt[] = "Another syscall: %d"; bpf_trace_printk_(_fmt, sizeof(_fmt), opcode); });
#   15: (b7) r2 = 20
#   16: (bf) r3 = r6
#   17: (85) call bpf_trace_printk#-114816
# ; return 0;
#   18: (b7) r0 = 0
#   19: (95) exit