#!/usr/bin/python3
from bcc import BPF
import ctypes as ct

# 実行結果
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob4$ sudo python3 main.py
# b'           <...>-5750    [012] ...2.   405.112061: bpf_trace_printk: Another syscall: 321'
# b'           <...>-5750    [012] ...2.   405.112104: bpf_trace_printk: Another syscall: 321'
# b'            code-4740    [014] ...2.   405.112164: bpf_trace_printk: Another syscall: 1'
# b'            code-4740    [014] ...2.   405.112172: bpf_trace_printk: Another syscall: 281'
# b'            code-4740    [014] ...2.   405.112175: bpf_trace_printk: Another syscall: 0'
# b'            code-4740    [014] ...2.   405.112181: bpf_trace_printk: Another syscall: 281'
# b'            code-4740    [014] ...2.   405.112182: bpf_trace_printk: Another syscall: 281'
# b'           <...>-5750    [012] ...2.   405.112194: bpf_trace_printk: Another syscall: 321'
# b'           <...>-5750    [012] ...2.   405.112445: bpf_trace_printk: Another syscall: 321'

program=r"""
BPF_PROG_ARRAY(syscall,500);

RAW_TRACEPOINT_PROBE(sys_enter){
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

