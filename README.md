# SeaSnake

### A client API library and command line interface for the DigitalOcean API.


## Examples
### Command Line

Create a new Droplet:

    $ seasnake droplet --name='MyNewDroplet' --image=0000 --size=0000 --region=1

List active Droplets:

    $ seasnake droplet

    output:

List available sizes:

```sh
$ seasnake size

output:
    Size name:'512MB', id:66
    Size name:'1GB', id:63
    Size name:'2GB', id:62
    Size name:'4GB', id:64
    Size name:'8GB', id:65
    Size name:'16GB', id:61
    Size name:'32GB', id:60
    Size name:'48GB', id:70
    Size name:'64GB', id:69
    Size name:'96GB', id:68
```

List available images:

    $ seasnake image

    output:
        Image name:'Gentoo x64', distro:'Gentoo', id:1607
        Image name:'Open Suse 12.1 x32', distro:'openSUSE', id:13632
        Image name:'Open Suse 12.2 X64', distro:'openSUSE', id:13863
        Image name:'Arch Linux 2012-09 x64', distro:'Arch Linux', id:18414
        Image name:'Arch Linux 2012-09 x64', distro:'Arch Linux', id:23593
        Image name:'Gentoo 2013-1 x64', distro:'Gentoo', id:63749
        Image name:'CentOS 5.8 x64', distro:'CentOS', id:1601
        Image name:'CentOS 5.8 x32', distro:'CentOS', id:1602
        Image name:'Ubuntu 11.10 x32 Server', distro:'Ubuntu', id:1609
        Image name:'CentOS 6.2 x64', distro:'CentOS', id:1611
        Image name:'Fedora 16 x64 Server', distro:'Fedora', id:1615
        Image name:'Fedora 16 x64 Desktop', distro:'Fedora', id:1618
        Image name:'Ubuntu 12.04 x64 Server', distro:'Ubuntu', id:2676
        Image name:'Debian 6.0 x64', distro:'Debian', id:12573
        Image name:'CentOS 6.3 x64', distro:'CentOS', id:12574
        Image name:'Debian 6.0 x32', distro:'Debian', id:12575
        Image name:'CentOS 6.3 x32', distro:'CentOS', id:12578
        Image name:'Ubuntu 10.04 x64 Server', distro:'Ubuntu', id:14097
        Image name:'Ubuntu 10.04 x32 Server', distro:'Ubuntu', id:14098
        Image name:'Ubuntu 12.04 x64 Desktop', distro:'Ubuntu', id:14218
        Image name:'Ubuntu 12.10 x32 Server', distro:'Ubuntu', id:25306
        Image name:'Ubuntu 12.10 x32 Desktop', distro:'Ubuntu', id:25485
        Image name:'Ubuntu 12.10 x64 Server', distro:'Ubuntu', id:25489
        Image name:'Ubuntu 12.10 x64 Desktop', distro:'Ubuntu', id:25493
        Image name:'Fedora 17 x32 Server', distro:'Fedora', id:32387
        Image name:'Fedora 17 x32 Desktop', distro:'Fedora', id:32399
        Image name:'Fedora 17 x64 Desktop', distro:'Fedora', id:32419
        Image name:'Fedora 17 x64 Server', distro:'Fedora', id:32428
        Image name:'Ubuntu 12.04 x32 Server', distro:'Ubuntu', id:42735
        Image name:'Ubuntu 11.04x64 Server', distro:'Ubuntu', id:43458
        Image name:'Ubuntu 11.04x32 Desktop', distro:'Ubuntu', id:43462
        Image name:'LAMP on Ubuntu 12.04', distro:'Ubuntu', id:46964


List available regions:

    $ seasnake region

    output:
        Region name:'New York 1', id:1
        Region name:'Amsterdam 1', id:2

