# the shell

---

学习材料：[Course overview + the shell](https://missing.csail.mit.edu/2020/course-shell/)

---

## Exercises

1.

```sh
$ echo $SHELL
# /bin/zsh
```

2.

```sh
cd ../../tmp/
mk missing
ll
# drwxr-xr-x  2 yum  yum  4.0K Jan 17 13:44 missing
# drwx------  2 root root 4.0K Jan 17 13:42 snap-private-tmp
# drwx------  3 root root 4.0K Jan 17 13:42 systemd-private-4b8346d81de84738be2ed5b6fc7968da-systemd-logind.service-Nts4Aw
# drwx------  3 root root 4.0K Jan 17 13:42 systemd-private-4b8346d81de84738be2ed5b6fc7968da-systemd-resolved.service-Dbj3vc
```

3.

```sh
$ man touch

# TOUCH(1)                  User Commands                 TOUCH(1)
#
# NAME
#        touch - change file timestamps
#
# SYNOPSIS
#        touch [OPTION]... FILE...
#
# DESCRIPTION
#        Update  the access and modification times of each FILE to
#        the current time.
#
#        A FILE argument that does not exist is created empty, un-
#        less -c or -h is supplied.
#
#        A  FILE  argument  string  of  - is handled specially and
#        causes touch to change the times of the  file  associated
#        with standard output.
#
#        Mandatory  arguments  to  long  options are mandatory for
#        short options too.
#
#        -a     change only the access time
#
#        -c, --no-create
#               do not create any files
#
#        -d, --date=STRING
#               parse STRING and use it instead of current time
#
#  Manual page touch(1) line 1 (press h for help or q to quit)
```

4.

```sh
cd missing
touch semester.sh
ll
# -rw-r--r-- 1 yum yum  0 Jan 17 13:46 semester.sh
```

5.

```sh
vim semester.sh
```

6.

```sh
./semester
# zsh: permission denied: ./semester.sh
ll
# -rw-r--r-- 1 yum yum  0 Jan 17 13:46 semester.sh
# 只有读写权限，没有执行权限
```

7.

```sh
$ sh semester.sh
# HTTP/1.1 200 Connection established

# HTTP/2 200
# server: GitHub.com
# content-type: text/html; charset=utf-8
# last-modified: Mon, 08 Jan 2024 22:40:31 GMT
# access-control-allow-origin: *
# etag: "659c79df-2015"
# expires: Tue, 16 Jan 2024 11:56:07 GMT
# cache-control: max-age=600
# x-proxy-cache: MISS
# x-github-request-id: 8D3E:2FA3:CC6032:100D6C3:65A66C7F
# accept-ranges: bytes
# date: Wed, 17 Jan 2024 05:50:55 GMT
# via: 1.1 varnish
# age: 0
# x-served-by: cache-maa10225-MAA
# x-cache: HIT
# x-cache-hits: 1
# x-timer: S1705470655.919879,VS0,VE299
# vary: Accept-Encoding
# x-fastly-request-id: ecdf1eec3bf959bf7553bbd3b158e2f6b5994cd9
# content-length: 8213
```

8.

```sh
man chmod
# CHMOD(1)                  User Commands                 CHMOD(1)
#
# NAME
#        chmod - change file mode bits
#
# SYNOPSIS
#        chmod [OPTION]... MODE[,MODE]... FILE...
#        chmod [OPTION]... OCTAL-MODE FILE...
#        chmod [OPTION]... --reference=RFILE FILE...
#
# DESCRIPTION
#        This  manual  page  documents  the  GNU version of chmod.
#        chmod changes the file mode bits of each given  file  ac-
#        cording to mode, which can be either a symbolic represen-
#        tation of changes to make, or an octal number  represent-
#        ing the bit pattern for the new mode bits.
#
#        The      format     of     a     symbolic     mode     is
#        [ugoa...][[-+=][perms...]...], where perms is either zero
#        or  more  letters from the set rwxXst, or a single letter
#        from the set ugo.  Multiple symbolic modes can be  given,
#        separated by commas.
#
#        A  combination  of the letters ugoa controls which users'
#        access to the file will be changed: the user who owns  it
#        (u), other users in the file's group (g), other users not
#        in the file's group (o), or all users (a).   If  none  of
#        these  are given, the effect is as if (a) were given, but
#        bits that are set in the umask are not affected.
#
#  Manual page chmod(1) line 1 (press h for help or q to quit)
```

9.

```sh
chmod +x semester.sh
ll
# -rwxr-xr-x 1 yum yum 63 Jan 17 13:49 semester.sh
```

10.

```sh
$ stat -c %y semester.sh | > last-modified.txt
ll
# -rw-r--r-- 1 yum yum 36 Jan 17 14:23 last-modified.txt
# -rwxr-xr-x 1 yum yum 63 Jan 17 13:49 semester.sh
cat last-modified.txt
# 2024-01-17 13:49:56.660115012 +0800
```

11.

```sh

```
