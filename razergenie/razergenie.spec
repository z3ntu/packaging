# This spec file was tested on Fedora 25.

Name: razergenie
Version: 0.4
Release: 1%{?dist}
Summary: Standalone Qt application for configuring your Razer devices under GNU/Linux.

License: GPL-3.0
URL: https://github.com/z3ntu/RazerGenie

Source0: https://github.com/z3ntu/RazerGenie/releases/download/v%{version}/RazerGenie-%{version}.tar.xz

BuildRequires: cmake extra-cmake-modules
%if 0%{?suse_version}
BuildRequires: libqt5-qtbase-devel
%else
BuildRequires: qt5-qtbase-devel
%endif
Requires: razer-daemon
%description
Standalone Qt application for configuring your Razer devices under GNU/Linux.

%prep
%autosetup -n RazerGenie-%{version}

%build
%if 0%{?suse_version}
%cmake
%make_jobs
%else
%cmake .
make %{?_smp_mflags}
%endif

%install
%if 0%{?suse_version}
%cmake_install
%else
make install DESTDIR=%{buildroot}
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/razergenie
%{_libdir}/librazer.so*
%{_datadir}/applications/razergenie.desktop
%{_datadir}/icons/hicolor/scalable/apps/razergenie.svg
