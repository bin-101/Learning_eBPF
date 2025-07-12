## コマンド実行結果
```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec04/prob1$ sudo strace -e bpf ./hello-buffer-config.py
bpf(BPF_PROG_LOAD, {prog_type=BPF_PROG_TYPE_SOCKET_FILTER, insn_cnt=2, insns=0x7ffe6b568410, license="GPL", log_level=0, log_size=0, log_buf=NULL, kern_version=KERNEL_VERSION(0, 0, 0), prog_flags=0, prog_name="", prog_ifindex=0, expected_attach_type=BPF_CGROUP_INET_INGRESS, prog_btf_fd=0, func_info_rec_size=0, func_info=NULL, func_info_cnt=0, line_info_rec_size=0, line_info=NULL, line_info_cnt=0, attach_btf_id=0, attach_prog_fd=0, fd_array=NULL}, 148) = 3
bpf(BPF_BTF_LOAD, {btf="\237\353\1\0\30\0\0\0\0\0\0\0\10\5\0\0\10\5\0\0\360\3\0\0\1\0\0\0\0\0\0\10"..., btf_log_buf=NULL, btf_size=2320, btf_log_size=0, btf_log_level=0}, 40) = 3
bpf(BPF_PROG_LOAD, {prog_type=BPF_PROG_TYPE_SOCKET_FILTER, insn_cnt=2, insns=0x7ffe6b5680e0, license="GPL", log_level=0, log_size=0, log_buf=NULL, kern_version=KERNEL_VERSION(0, 0, 0), prog_flags=0, prog_name="libbpf_nametest", prog_ifindex=0, expected_attach_type=BPF_CGROUP_INET_INGRESS, prog_btf_fd=0, func_info_rec_size=0, func_info=NULL, func_info_cnt=0, line_info_rec_size=0, line_info=NULL, line_info_cnt=0, attach_btf_id=0, attach_prog_fd=0, fd_array=NULL}, 148) = 4
bpf(BPF_MAP_CREATE, {map_type=BPF_MAP_TYPE_PERF_EVENT_ARRAY, key_size=4, value_size=4, max_entries=16, map_flags=0, inner_map_fd=0, map_name="output", map_ifindex=0, btf_fd=0, btf_key_type_id=0, btf_value_type_id=0, btf_vmlinux_value_type_id=0, map_extra=0}, 80) = 4
bpf(BPF_MAP_CREATE, {map_type=BPF_MAP_TYPE_HASH, key_size=4, value_size=13, max_entries=10240, map_flags=0, inner_map_fd=0, map_name="config", map_ifindex=0, btf_fd=3, btf_key_type_id=1, btf_value_type_id=4, btf_vmlinux_value_type_id=0, map_extra=0}, 80) = 5
bpf(BPF_PROG_LOAD, {prog_type=BPF_PROG_TYPE_KPROBE, insn_cnt=44, insns=0x7ef57ac2e000, license="GPL", log_level=0, log_size=0, log_buf=NULL, kern_version=KERNEL_VERSION(6, 8, 12), prog_flags=0, prog_name="hello", prog_ifindex=0, expected_attach_type=BPF_CGROUP_INET_INGRESS, prog_btf_fd=3, func_info_rec_size=8, func_info=0x60b43b10b5a0, func_info_cnt=1, line_info_rec_size=16, line_info=0x60b43bf85110, line_info_cnt=21, attach_btf_id=0, attach_prog_fd=0, fd_array=NULL}, 152) = 6
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=5, key=0x7ef579ecc490, value=0x7ef579ecc810, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=5, key=0x7ef579ecc810, value=0x7ef579ecc490, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc990, value=0x7ef579ecc910, flags=BPF_ANY}, 32) = 0
bpf(BPF_MAP_UPDATE_ELEM, {map_fd=4, key=0x7ef579ecc910, value=0x7ef579ecc990, flags=BPF_ANY}, 32) = 0
21697 1000 code Hello World;
21698 1000 sh Hello World;
```
- カーネルにロードしている部分
```
bpf(BPF_PROG_LOAD, {prog_type=BPF_PROG_TYPE_KPROBE, insn_cnt=44, insns=0x7ef57ac2e000, license="GPL", log_level=0, log_size=0, log_buf=NULL, kern_version=KERNEL_VERSION(6, 8, 12), prog_flags=0, prog_name="hello", prog_ifindex=0, expected_attach_type=BPF_CGROUP_INET_INGRESS, prog_btf_fd=3, func_info_rec_size=8, func_info=0x60b43b10b5a0, func_info_cnt=1, line_info_rec_size=16, line_info=0x60b43bf85110, line_info_cnt=21, attach_btf_id=0, attach_prog_fd=0, fd_array=NULL}, 152) = 6
```
- 翻訳後のeBPFバイトコード
        - 2バイト使っている命令: 9,21,36,41
```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob2$ sudo bpftool prog dump xlated name hello
[sudo] bin101 のパスワード: 
int hello(void * ctx):
; int hello(void *ctx){
   0: (bf) r6 = r1
   1: (b7) r1 = 0
; struct data_t data={};
   2: (63) *(u32 *)(r10 -8) = r1
   3: (7b) *(u64 *)(r10 -16) = r1
   4: (7b) *(u64 *)(r10 -24) = r1
   5: (7b) *(u64 *)(r10 -32) = r1
   6: (b7) r1 = 996437106
; char message[12]="Hello World;";
   7: (63) *(u32 *)(r10 -48) = r1
   8: (18) r1 = 0x6f57206f6c6c6548 
  10: (7b) *(u64 *)(r10 -56) = r1
; data.pid=bpf_get_current_pid_tgid()>>32;
  11: (85) call bpf_get_current_pid_tgid#255744
; data.pid=bpf_get_current_pid_tgid()>>32;
  12: (77) r0 >>= 32
; data.pid=bpf_get_current_pid_tgid()>>32;
  13: (63) *(u32 *)(r10 -40) = r0
; data.uid=bpf_get_current_uid_gid()&0xFFFFFFFF;
  14: (85) call bpf_get_current_uid_gid#256320
; data.uid=bpf_get_current_uid_gid()&0xFFFFFFFF;
  15: (63) *(u32 *)(r10 -36) = r0
; struct data_t data={};
  16: (bf) r1 = r10
  17: (07) r1 += -32
; bpf_get_current_comm(&data.command,sizeof(data.command));
  18: (b7) r2 = 16
  19: (85) call bpf_get_current_comm#256464
; p=bpf_map_lookup_elem((void *)bpf_pseudo_fd(1, -1), &data.uid);
  20: (18) r1 = map[id:72]
; data.uid=bpf_get_current_uid_gid()&0xFFFFFFFF;
  22: (bf) r2 = r10
  23: (07) r2 += -36
; p=bpf_map_lookup_elem((void *)bpf_pseudo_fd(1, -1), &data.uid);
  24: (85) call __htab_map_lookup_elem#296912
  25: (15) if r0 == 0x0 goto pc+1
  26: (07) r0 += 56
  27: (bf) r3 = r10
; 
  28: (07) r3 += -56
; if(p!=0){
  29: (15) if r0 == 0x0 goto pc+1
  30: (bf) r3 = r0
; struct data_t data={};
  31: (bf) r1 = r10
  32: (07) r1 += -16
; 
  33: (b7) r2 = 12
  34: (85) call bpf_probe_read_kernel#-128352
; bpf_perf_event_output(ctx, (void *)bpf_pseudo_fd(1, -2), CUR_CPU_IDENTIFIER, &data,sizeof(data));
  35: (18) r2 = map[id:71]
  37: (bf) r4 = r10
; struct data_t data={};
  38: (07) r4 += -40
; bpf_perf_event_output(ctx, (void *)bpf_pseudo_fd(1, -2), CUR_CPU_IDENTIFIER, &data,sizeof(data));
  39: (bf) r1 = r6
  40: (18) r3 = 0xffffffff
  42: (b7) r5 = 36
  43: (85) call bpf_perf_event_output#-115872
; return 0;
  44: (b7) r0 = 0
  45: (95) exit
```

```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF/sec03/prob2$ sudo bpftool prog dump xlated id 183 -j   | jq 'length'
42
```