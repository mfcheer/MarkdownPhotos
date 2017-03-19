---

title: 'Linux命令笔记'

date: 2017-02-27 01:54:56

categories: Linux
---

Linux 统计某个字符串出现的次数

```
cat filename |grep str |wc -l
```

定时任务
```
crontab -e 
```

查看文件内容 

```
如果你只想看文件的前5行，可以使用head命令，如： 
head -5 /etc/passwd 
如果你想查看文件的后10行，可以使用tail命令，如： 
tail -10 /etc/passwd 或 tail -n 10 /etc/passwd 
tail -f /var/log/messages 
参数-f使tail不停地去读最新的内容，这样有实时监视的效果 用Ctrl＋c来终止！ 
```
本地文件上传到主机
```
rz -be
```
主机文件下载到本地
```
sz "filename"
```

日志定期清理sh
```
#!/bin/bash
log_path=/opt/web/mFangchanIndex #日志路径

export log_path
expried_time=7      #此处定义你的日志过期时间，如7天

find $log_path -type f -mtime +7 -iname "log.*" | xargs rm  1>/dev/null 2>&1
```
查看进程和删除进程

```
ps 命令用于查看当前正在运行的进程。
grep 是搜索
ps [选项]
-e 显示所有进程,环境变量
-f 全格式
-h 不显示标题
-l 长格式
-w 宽输出
kill 命令用于终止进程
-9 表示强迫进程立即停止

例子：
ps -ef | grep java
ps aux|grep tcp
kill -9 [PID]

```

Linux间进行文件传送-scp命令
```
linux 的 scp 命令可以在 linux 之间复制文件和目录；  
scp 可以在 2个 linux 主机间复制文件； 

命令基本格式： 
scp [可选参数] file_source file_target 

从本地复制到远程：
 
复制文件： 
scp local_file remote_ip:remote_file 
scp /home/space/music/1.mp3 root@www.cumt.edu.cn:/home/root/others/music 

复制目录：  
scp -r local_folder remote_username@remote_ip:remote_folder 
命令执行后需要输入密码； 

例子： 
scp -r /home/space/music/ root@www.cumt.edu.cn:/home/root/others/ 

从远程复制到本地 ，只要将从本地复制到远程的命令的后2个参数调换顺序即可； 

```

解压 .lzop压缩文件

```
# lzop -v test # 创建test.lzo压缩文件，输出详细信息，保留test文件不变

# lzop -Uv test # 创建test.lzo压缩文件，输出详细信息，删除test文件

# lzop -t test.lzo # 测试test.lzo压缩文件的完整性

# lzop –info test.lzo # 列出test.lzo中各个文件的文件头

# lzop -l test.lzo # 列出test.lzo中各个文件的压缩信息

# lzop –ls test.lzo # 列出test.lzo文件的内容，同ls -l功能

# cat test | lzop > t.lzo # 压缩标准输入并定向到标准输出

# lzop -dv test.lzo # 解压test.lzo得到test文件，输出详细信息，保留test.lzo不变
```

rsync命令
```
kinit username
例子：
rsync -av rec/ work@10.12.90.13:/opt/rec --exclude='logs'
--exclude='logs'说明 ： 不拷贝logs文件夹
```

SSH基本的用法
```
SSH主要用于远程登录。假定你要以用户名user，登录远程主机host，只要一条简单命令就可以了。

$ ssh user@host

如果本地用户名与远程用户名一致，登录时可以省略用户名。

$ ssh host

SSH的默认端口是22，也就是说，你的登录请求会送进远程主机的22端口。使用p参数，可以修改这个端口。

$ ssh -p 2222 user@host

上面这条命令表示，ssh直接连接远程主机的2222端口。
```

搜索输入过的命令
```
ctrl+r:搜索某个以前输入过的命令 或者!command
```
cat合并文件
```
使用cat合并文件，如cat 1.txt 2.txt 3.txt > 4.txt；
如果1/2/3.txt中存在多个空行，最终保存到4.txt时，连续的空行会被替换为1行。
如果我们希望去掉空行，可以使用如下：cat -s 1.txt 2.txt 3.txt > 4.txt
```
diff命令
```
在使用diff命令的时候有3种显示，但是如果我们仅仅需要查看2个文件所有不同的记录，
去掉diff加上的123a124或者>或者<,可以先diff a b > difflog，
然后使用grep+sed：cat difflog
```

