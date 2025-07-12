- opensnoop
    - https://github.com/iovisor/bcc/blob/master/tools/opensnoop.py

```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool link list
1: tracing  prog 2  
        prog_type tracing  attach_type modify_return  
        target_obj_id 1  target_btf_id 95085  
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool link list # opensnoop 実行後
1: tracing  prog 2  
        prog_type tracing  attach_type modify_return  
        target_obj_id 1  target_btf_id 95085  
18: tracing  prog 224  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35443  
19: tracing  prog 225  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35444  
20: tracing  prog 226  
        prog_type tracing  attach_type trace_fexit  
        target_obj_id 1  target_btf_id 35445
```

```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob5$ sudo bpftool prog list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
224: tracing  name __x64_sys_open  tag 43c00fcb73af8b7f  gpl
        loaded_at 2025-07-12T19:51:58+0900  uid 0
        xlated 304B  jited 242B  memlock 4096B  map_ids 85
        btf_id 291
225: tracing  name kretfunc__vmlinux____x64_sys_openat  tag d4962b13b99994de  gpl
        loaded_at 2025-07-12T19:51:58+0900  uid 0
        xlated 304B  jited 242B  memlock 4096B  map_ids 85
        btf_id 291
226: tracing  name kretfunc__vmlinux____x64_sys_openat2  tag 6ee9a496853481e6  gpl
        loaded_at 2025-07-12T19:51:58+0900  uid 0
        xlated 344B  jited 311B  memlock 4096B  map_ids 85
        btf_id 291
```