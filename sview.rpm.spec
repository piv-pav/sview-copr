Name:           sview
Version:        20.08
Release:        1
Summary:        stereoscopic media player sView

License:        GPLv3
URL:            https://sview.ru/en/
Source0:        https://github.com/gkv311/sview/archive/24e7c3219ca5ad6c512ba094b40bd500584e8a86.zip

BuildRequires:  ffmpeg-free-devel
BuildRequires:  libconfig-devel
BuildRequires:  glew-devel
BuildRequires:  openal-soft-devel
BuildRequires:  gtk+-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXpm-devel
BuildRequires:  gcc-c++

%description
sView is a stereoscopic Image Viewer and Movie Player.
Requires OpenGL2.0+ for rendering and OpenAL for sound output.

%prep
%setup -q -n %{name}-%{version}-%{release}

%build
make %{?_smp_mflags} INC='-I3rdparty/include -Iinclude -I/usr/include/ffmpeg' all

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT USR_LIB=%{_lib} install

%files
%license docs/LICENSE
%defattr(-,root,root)
/usr/bin/sView
/usr/%{_lib}/sView/*
/usr/share/application-registry/sView.applications
/usr/share/applications/sViewIV.desktop
/usr/share/applications/sViewMP.desktop
/usr/share/menu/sViewIV
/usr/share/menu/sViewMP
/usr/share/sView/*

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%changelog
* Fri June 17 2022 Pavel Pivovarov
- Updated to build on Fedora 36
* Sat May 19 2012 Kirill Gavrilov
- Initial build
