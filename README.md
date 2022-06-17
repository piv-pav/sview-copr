# sView COPR

RPM Specfile for [sView](https://www.sview.ru/en/) stereoscopic player to build for using [COPR](https://copr.fedorainfracloud.org).

sView compiles using `ffmpeg` from [RPMFusion](https://rpmfusion.org/Configuration) instead of Fedora provided `ffmpeg-free`, hence you might need to install RPMFusion Free repository first.

Alternatively you can replace `ffmpeg`, `ffmpeg-devel`, `libswscale` and `libswscale-devel` with `ffmpeg-free`, `ffmpeg-free-devel`, `libswscale-free` and `libswscale-free-devel` accordingly in spec file.

You can install sView from COPR by running following commands

```bash
sudo dnf copr enable pivpav/sView 
sudo dnf install sview
```

or you can compile it manually

```bash
dnf install wget fedora-packager git -y
rpmdev-setuptree
git clone https://github.com/piv-pav/sview-copr /tmp/sview-copr
cp /tmp/sview-copr/sview.rpm.spec ~/rpmbuild/SPECS/
cd ~/rpmbuild/SOURCES
wget https://github.com/gkv311/sview/archive/24e7c3219ca5ad6c512ba094b40bd500584e8a86.zip
cd ~/rpmbuild/SPECS
yum-builddep sview.rpm.spec -y
rpmbuild -ba sview.rpm.spec
dnf install ~/rpmbuild/RPMS/x86_64/sview-20.08-1.x86_64.rpm
```
