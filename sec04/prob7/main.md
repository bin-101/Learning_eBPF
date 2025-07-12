```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool link list
1: tracing  prog 2  
        prog_type tracing  attach_type modify_return  
        target_obj_id 1  target_btf_id 95085  
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool link list
1: tracing  prog 2  
        prog_type tracing  attach_type modify_return  
        target_obj_id 1  target_btf_id 95085  
24: tracing  prog 234  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35443  
25: tracing  prog 235  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35444  
26: tracing  prog 236  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35445  
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool link pin id 24 /sys/fs/bpf/mylink
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool link list
1: tracing  prog 2  
        prog_type tracing  attach_type modify_return  
        target_obj_id 1  target_btf_id 95085  
24: tracing  prog 234  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35443
```