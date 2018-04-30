# pipi

> TODO: Add project goal

## Project Status

The project is under development. Currently just testing out Docker, Go, Python and GPIO.

### Tasks

- [x] Setup development environment on Raspbian
- [x] Connect to Bennington Public
- [x] Install Docker
- [x] Build a hello-world dockerized application in Go
- [x] Make a Dockerfile to install Python and GPIO
- [x] Install Humidity and Temperature Sensor ([Datasheet SHT3x-DIS](https://cdn-shop.adafruit.com/product-files/2857/Sensirion_Humidity_SHT3x_Datasheet_digital-767294.pdf))

## Table of Contents

- [Raspberry Pi 3 Info](#info)
  - Debian's version
  - OS Release Notes
  - Kernel's version
  - Hardware's version

## Info

**Debian's version**
```
$ cat /etc/debian_version
9.4
```

**OS Release Notes**
```
$ cat /etc/os-release
PRETTY_NAME="Raspbian GNU/Linux 9 (stretch)"
NAME="Raspbian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
```

**Kernel's version**
```
$ uname -a
Linux raspberrypi15 4.14.30-v7+ #1102 SMP Mon Mar 26 16:45:49 BST 2018 armv7l GNU/Linux
```

**Hardware's version**
```
processor   : 0
model name  : ARMv7 Processor rev 4 (v7l)
BogoMIPS    : 38.40
Features    : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
crc32 
CPU implementer : 0x41
CPU architecture: 7
CPU variant : 0x0
CPU part    : 0xd03
CPU revision    : 4

processor   : 1
model name  : ARMv7 Processor rev 4 (v7l)
BogoMIPS    : 38.40
Features    : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
crc32 
CPU implementer : 0x41
CPU architecture: 7
CPU variant : 0x0
CPU part    : 0xd03
CPU revision    : 4

processor   : 2
model name  : ARMv7 Processor rev 4 (v7l)
BogoMIPS    : 38.40
Features    : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
crc32 
CPU implementer : 0x41
CPU architecture: 7
CPU variant : 0x0
CPU part    : 0xd03
CPU revision    : 4

processor   : 3
model name  : ARMv7 Processor rev 4 (v7l)
BogoMIPS    : 38.40
Features    : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
crc32 
CPU implementer : 0x41
CPU architecture: 7
CPU variant : 0x0
CPU part    : 0xd03
CPU revision    : 4

Hardware    : BCM2835
Revision    : a22082
Serial      : 00000000cb1d00f0
```
