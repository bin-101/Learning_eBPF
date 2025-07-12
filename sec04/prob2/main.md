straceなしで出力
```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF$ sudo bpftool map dump name config
[{
        "id": 74,
        "type": "hash",
        "name": "config",
        "flags": 0,
        "elements": [{
                "key": 0,
                "value": {
                    "message": "Hey root!"
                }
            },{
                "key": 501,
                "value": {
                    "message": "Hi user 501!"
                }
            }
        ]
    },{
        "id": 76,
        "type": "hash",
        "name": "config",
        "flags": 0,
        "elements": [{
                "key": 501,
                "value": {
                    "message": "Hi user 501!"
                }
            },{
                "key": 0,
                "value": {
                    "message": "Hey root!"
                }
            }
        ]
    }
]
```
strace -e bpfをつけて実行
```
bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF$ sudo strace -e bpf bpftool map dump name config
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=35471, si_uid=0, si_status=0, si_utime=0, si_stime=0} ---
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=35472, si_uid=0, si_status=0, si_utime=0, si_stime=0} ---
bpf(BPF_MAP_GET_NEXT_ID, {start_id=0, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=2, next_id=0, open_flags=0}, 12) = 3
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=2, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=3, next_id=0, open_flags=0}, 12) = 3
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=3, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=4, next_id=0, open_flags=0}, 12) = 3
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=4, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=73, next_id=0, open_flags=0}, 12) = 3
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=73, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=74, next_id=0, open_flags=0}, 12) = 3
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=74, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=75, next_id=0, open_flags=0}, 12) = 4
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=4, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=75, next_id=0, open_flags=0}, 12) = 0
bpf(BPF_MAP_GET_FD_BY_ID, {map_id=76, next_id=0, open_flags=0}, 12) = 4
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=4, info_len=88, info=0x7ffffda36bf0}}, 16) = 0
bpf(BPF_MAP_GET_NEXT_ID, {start_id=76, next_id=0, open_flags=0}, 12) = -1 ENOENT (そのようなファイルやディレクトリはありません)
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36d90}}, 16) = 0
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=4, info_len=88, info=0x7ffffda36d90}}, 16) = 0
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=88, info=0x7ffffda36d30}}, 16) = 0
bpf(BPF_BTF_GET_FD_BY_ID, {btf_id=283}, 12) = 5
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=5, info_len=32, info=0x7ffffda36bf0}}, 16) = 0 # MAPから情報を取り出している行
[{
        "id": 74,
        "type": "hash",
        "name": "config",
        "flags": 0,
bpf(BPF_MAP_GET_NEXT_KEY, {map_fd=3, key=NULL, next_key=0x5797553fe6f0}, 24) = 0 # key=NULLとして、1つめのキーを見つけている
bpf(BPF_MAP_LOOKUP_ELEM, {map_fd=3, key=0x5797553fe6f0, value=0x5797553fe710, flags=BPF_ANY}, 32) = 0 # MAPからエントリを取り出している
        "elements": [{
                "key": 0,
                "value": {
                    "message": "Hey root!"
                }
bpf(BPF_MAP_GET_NEXT_KEY, {map_fd=3, key=0x5797553fe6f0, next_key=0x5797553fe6f0}, 24) = 0
bpf(BPF_MAP_LOOKUP_ELEM, {map_fd=3, key=0x5797553fe6f0, value=0x5797553fe710, flags=BPF_ANY}, 32) = 0
            },{
                "key": 501,
                "value": {
                    "message": "Hi user 501!"
                }
bpf(BPF_MAP_GET_NEXT_KEY, {map_fd=3, key=0x5797553fe6f0, next_key=0x5797553fe6f0}, 24) = -1 ENOENT (そのようなファイルやディレクトリはありません)
            }
        ]
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=4, info_len=88, info=0x7ffffda36d30}}, 16) = 0
bpf(BPF_BTF_GET_FD_BY_ID, {btf_id=284}, 12) = 3
bpf(BPF_OBJ_GET_INFO_BY_FD, {info={bpf_fd=3, info_len=32, info=0x7ffffda36bf0}}, 16) = 0
    },{
        "id": 76,
        "type": "hash",
        "name": "config",
        "flags": 0,
bpf(BPF_MAP_GET_NEXT_KEY, {map_fd=4, key=NULL, next_key=0x5797553fe710}, 24) = 0
bpf(BPF_MAP_LOOKUP_ELEM, {map_fd=4, key=0x5797553fe710, value=0x5797553fe6f0, flags=BPF_ANY}, 32) = 0
        "elements": [{
                "key": 501,
                "value": {
                    "message": "Hi user 501!"
                }
bpf(BPF_MAP_GET_NEXT_KEY, {map_fd=4, key=0x5797553fe710, next_key=0x5797553fe710}, 24) = 0
bpf(BPF_MAP_LOOKUP_ELEM, {map_fd=4, key=0x5797553fe710, value=0x5797553fe6f0, flags=BPF_ANY}, 32) = 0
            },{
                "key": 0,
                "value": {
                    "message": "Hey root!"
                }
bpf(BPF_MAP_GET_NEXT_KEY, {map_fd=4, key=0x5797553fe710, next_key=0x5797553fe710}, 24) = -1 ENOENT (そのようなファイルやディレクトリはありません)
            }
        ]
    }
]
+++ exited with 0 +++
```