# ip 类

> ubuntu (提前安装 net-tools)

## 查看 ip 地址

```shell
##### windows
# cmd
ipconfig

##### ubuntu
# 1: inet 对应 ipv4；inet6 对应 ipv6；
ip addr show
# ip a

# 2: 最简洁
hostname -I
```

## 查看 mac 地址

```shell
##### windows
# 1: cmd 物理地址即为 mac 地址
ipconfig/all
# or ipconfig -all

# 2: powershell （查看网卡与其对应的 mac 地址）
Get-NetAdapter

##### ubuntu
# 1: ether 对应为 mac 地址
ifconfig

# 2: wlp*，不同电脑可能不一样，至少我的和我参考的文章的不一样
cat /sys/class/net/wlp0s20f3/address

# 3：查看连接到本电脑的 ip 对应的 mac 地址
cat /proc/net/arp
```
