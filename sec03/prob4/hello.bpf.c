#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

int counter=0;

SEC("xdp")
int hello(struct xdp_md *ctx) {
    bpf_printk("Hello World %d",counter);
    return XDP_ABORTED;
}

char LICENSE[] SEC("license")="Dual BSD/GPL";

/*
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob4$ clang -target bpf -c -g -O2 -I /usr/include/x86_64-linux-gnu/ hello.bpf.c -o hello.bpf.o
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob4$ sudo ip link set dev lo xdp obj hello.bpf.o sec xdp
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob4$ sudo ip link set dev wlp2s0 xdp obj hello.bpf.o sec xdp
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob4$ sudo ip link set dev virbr0 xdp obj hello.bpf.o sec xdp

bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob4$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
^C
--- 8.8.8.8 ping statistics ---
10 packets transmitted, 0 received, 100% packet loss, time 9228ms
*/