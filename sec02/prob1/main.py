# 実行結果
# bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec02/prob1$ sudo python3 main.py 
# 17947 1000 code odd
# 17948 1000 sh even
# 17949 1000 code odd
# 17950 1000 sh even
# 17951 1000 code odd
# 17952 1000 sh even
# 17953 1000 cpuUsage.sh odd

from bcc import BPF

program = r"""
BPF_PERF_OUTPUT(output);

struct data_t {
    int pid;
    int uid;
    char command[16];
    char message[12];
};

int hello(void *ctx){
    struct data_t data = {};
    char odd_message[]="odd";
    char even_message[]="even";
    data.pid=bpf_get_current_pid_tgid()>>32;
    data.uid=bpf_get_current_uid_gid()&0xFFFFFFFF;

    if(data.pid%2==0){
        bpf_probe_read_kernel(&data.message,sizeof(data.message),even_message);    
    }else {
        bpf_probe_read_kernel(&data.message,sizeof(data.message),odd_message);   
    }

    bpf_get_current_comm(&data.command,sizeof(data.command));

    output.perf_submit(ctx,&data,sizeof(data));

    return 0;
}
"""

b=BPF(text=program)
syscall=b.get_syscall_fnname("execve")
b.attach_kprobe(event=syscall,fn_name="hello")

def print_event(cpu,data,size):
    data=b["output"].event(data);
    print(f"{data.pid} {data.uid} {data.command.decode()} {data.message.decode()}")

b["output"].open_perf_buffer(print_event)
while True:
    b.perf_buffer_poll()
