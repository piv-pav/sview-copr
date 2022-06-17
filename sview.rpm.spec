Name:           sview
Version:        20.08
Release:        1%{?dist}
%global commit_id 24e7c3219ca5ad6c512ba094b40bd500584e8a86
Summary:        stereoscopic media player sView

License:        GPLv3
URL:            https://sview.ru/en/
Source0:        https://github.com/gkv311/sview/archive/%{commit_id}.zip

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
%setup -n %{name}-%{commit_id}

%build
make %{?_smp_mflags} INC='-I3rdparty/include -Iinclude -I/usr/include/ffmpeg' all

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{_prefix} USR_LIB=%{_libdir} install

%files
%defattr(-,root,root)
%licence {_datadir}/sView/info/license.txt
%{_bindir}/sView
%{_libdir}/sView/*
%{_datadir}/sView/*

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig
