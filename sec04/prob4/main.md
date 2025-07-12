```
sudo python3 hello-buffer-config.py (別ターミナル)
sudo bpftool prog pin name hello /sys/fs/bpf/hi
sudo python3 hello-buffer-config.py (別ターミナルで終了)
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF$ sudo bpftool prog list | tail -4
206: kprobe  name hello  tag 79064b7172c51cf4  gpl
        loaded_at 2025-07-12T19:04:30+0900  uid 0
        xlated 368B  jited 207B  memlock 4096B  map_ids 80,79
        btf_id 287
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF$ sudo rm /sys/fs/bpf/hi
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF$ sudo bpftool prog list | tail -4
        xlated 64B  jited 59B  memlock 4096B
31: cgroup_device  tag 03b4eaae2f14641a  gpl
        loaded_at 2025-07-06T21:39:55+0900  uid 1000
        xlated 296B  jited 167B  memlock 4096B  map_ids 4
```