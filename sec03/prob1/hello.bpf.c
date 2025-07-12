#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

int counter=0;

SEC("xdp")
int hello(struct xdp_md *ctx) {
    bpf_printk("Hello World %d",counter);
    counter++;
    return XDP_PASS;
}

char LICENSE[] SEC("license")="Dual BSD/GPL";


// https://bugzilla.redhat.com/show_bug.cgi?id=1618958&utm_source=chatgpt.com

/*
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob1$ clang -target bpf -c -g -O2 -I /usr/include/x86_64-linux-gnu/ hello.bpf.c -o hello.bpf.o
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob1$ sudo bpftool prog load hello.bpf.o /sys/fs/bpf/hello
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob1$ sudo ip link set dev lo xdp obj hello.bpf.o sec xdp
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob1$ sudo cat /sys/kernel/debug/tracing/trace_pipe
 Chrome_ChildIOT-3453    [002] ..s21 87997.197112: bpf_trace_printk: Hello World 18
 Chrome_ChildIOT-3453    [002] ..s21 87997.197195: bpf_trace_printk: Hello World 19
 Chrome_ChildIOT-3453    [002] ..s21 87997.197246: bpf_trace_printk: Hello World 20
 systemd-resolve-721     [014] ..s21 87997.495730: bpf_trace_printk: Hello World 21
 systemd-resolve-721     [014] ..s21 87997.530469: bpf_trace_printk: Hello World 22
 systemd-resolve-721     [014] ..s21 87997.533756: bpf_trace_printk: Hello World 23
            code-4662    [011] ..s21 87998.696105: bpf_trace_printk: Hello World 24
 systemd-resolve-721     [014] ..s21 87998.696400: bpf_trace_printk: Hello World 25
            code-4662    [011] ..s21 87998.696459: bpf_trace_printk: Hello World 26
 systemd-resolve-721     [014] ..s21 87998.741940: bpf_trace_printk: Hello World 27
^C
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob1$ sudo bpftool map dump name hello.bss
[{
        "id": 47,
        "type": "array",
        "name": "hello.bss",
        "flags": 1024,
        "elements": [{
                "value": {
                    ".bss": [{
                            "counter": 0
                        }
                    ]
                }
            }
        ]
    },{
        "id": 52,
        "type": "array",
        "name": "hello.bss",
        "flags": 1024,
        "elements": [{
                "value": {
                    ".bss": [{
                            "counter": 28
                        }
                    ]
                }
            }
        ]
    }
]
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob1$ sudo ip link set dev lo xdp off
*/