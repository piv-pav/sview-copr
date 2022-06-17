Name:           sview
Version:        20.08
Release:        1
%global commit_id 24e7c3219ca5ad6c512ba094b40bd500584e8a86
Summary:        stereoscopic media player sView

License:        GPLv3
URL:            https://sview.ru/en/
Source0:        https://github.com/gkv311/%{name}/archive/%{commit_id}.zip

Requires: pkgconfig(libavcodec)
Requires: pkgconfig(libavformat)
Requires: pkgconfig(libavutil)
Requires: pkgconfig(libswscale)
Requires: atk
Requires: cairo
Requires: fontconfig
Requires: freetype
Requires: gdk-pixbuf2
Requires: glib2
Requires: glibc
Requires: gtk2
Requires: harfbuzz
Requires: libX11
Requires: libXext
Requires: libXpm
Requires: libXrandr
Requires: libconfig
Requires: libgcc
Requires: libstdc++
Requires: openal-soft
Requires: pango

BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: libconfig-devel
BuildRequires: glew-devel
BuildRequires: openal-soft-devel
BuildRequires: gtk+-devel
BuildRequires: gtk2-devel
BuildRequires: libXpm-devel
BuildRequires: gcc-c++

%description
sView is a stereoscopic Image Viewer and Movie Player.
Requires OpenGL2.0+ for rendering and OpenAL for sound output.

%global debug_package %{nil}

%prep
%setup -n %{name}-%{commit_id}

%build
make %{?_smp_mflags} INC='-I3rdparty/include -Iinclude -I/usr/include/ffmpeg' all

%install
make DESTDIR=%{buildroot} USR_LIB=%{_lib} install

%files
%defattr(-,root,root)
%{_bindir}/sView
%{_libdir}/*
%{_datadir}/*
%license %{_datadir}/sView/info/license.txt

%clean
make clean
rm -rf %{buildroot}

%post
ldconfig
