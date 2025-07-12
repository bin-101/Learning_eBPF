
sudo python3 hello-buffer-config.py の出力
- 途中で、`bin101@bin101-Inspiron-16-5635:~/code/Learning_eBPF$ sudo bpftool map update name config  key hex e8 03 00 00  value hex 63 68 61 6e 67 65 64 68 65 6c 6c 6f 00`を実行
    - 参考: https://dencode.com/ja/string
```
49285 1000 bash Hello World;
49287 0 sudo Hey root!
49288 0 bpftool Hey root!
49289 0 bpftool Hey root!
49287 0 bpftool Hey root! # 
49291 1000 cpuUsage.sh changedhello
49292 1000 cpuUsage.sh changedhello
49294 1000 cpuUsage.sh changedhello
49296 1000 cpuUsage.sh changedhello
49298 1000 cpuUsage.sh changedhello
```