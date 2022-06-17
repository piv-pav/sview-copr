Name:           sview
Version:        20.08
Release:        1
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
make DESTDIR=%{buildroot} USR_LIB=%{buildroot}/%{_libdir} install

%files
%defattr(-,root,root)
%licence %{buildroot}/%{_datadir}/sView/info/license.txt
%{buildroot}/%{_bindir}/sView
%{buildroot}/%{_libdir}/sView/*
%{buildroot}/%{_datadir}/sView/*

%clean
make clean
rm -rf %{buildroot}

%post
ldconfig
