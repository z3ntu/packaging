# This spec file was tested on Fedora 25.

Name: razergenie
Version: 0.2
Release: 1%{?dist}
Summary: Standalone Qt application for configuring your Razer devices under GNU/Linux.

License: GPL-3.0
URL: https://github.com/z3ntu/RazerGenie

Source0: https://github.com/z3ntu/RazerGenie/archive/v%{version}.tar.gz

#BuildArch: noarch

Summary: Qt GUI for Razer drivers
BuildRequires: cmake extra-cmake-modules
Requires: razer-daemon
%if 0%{?suse_version}
BuildRequires: kconfigwidgets-devel
Requires: kconfigwidgets
%else
BuildRequires: kf5-kconfigwidgets-devel
Requires: kf5-kconfigwidgets
%endif
%description
Standalone Qt application for configuring your Razer devices under GNU/Linux.

%prep
%autosetup -n RazerGenie-%{version}

%build
%cmake .
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
