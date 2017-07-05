# This spec file was tested on Fedora 25.

Name: razergenie
Version: 0.3
Release: 1%{?dist}
Summary: Standalone Qt application for configuring your Razer devices under GNU/Linux.

License: GPL-3.0
URL: https://github.com/z3ntu/RazerGenie

Source0: https://github.com/z3ntu/RazerGenie/archive/v%{version}.tar.gz

#BuildArch: noarch

Summary: Qt GUI for Razer drivers
BuildRequires: cmake extra-cmake-modules
Requires: razer-daemon
%description
Standalone Qt application for configuring your Razer devices under GNU/Linux.

%prep
%autosetup -n RazerGenie-%{version}

%build
%if 0%{?suse_version}
%cmake ..
%else
%cmake .
%endif
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/razergenie
%{_libdir}/librazer.so*
%{_datadir}/applications/razergenie.desktop
%{_datadir}/icons/hicolor/scalable/apps/razergenie.svg
