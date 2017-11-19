# This spec file was tested on Fedora 25.

Name: razergenie
Version: 0.5
Release: 1%{?dist}
Summary: Standalone Qt application for configuring your Razer devices under GNU/Linux.

License: GPL-3.0
URL: https://github.com/z3ntu/RazerGenie

Source0: https://github.com/z3ntu/RazerGenie/releases/download/v%{version}/RazerGenie-%{version}.tar.xz

BuildRequires: meson
%if 0%{?suse_version}
BuildRequires: libqt5-qtbase-devel libqt5-linguist
%else
BuildRequires: qt5-qtbase-devel qt5-linguist
%endif
Requires: razer-daemon
%description
Standalone Qt application for configuring your Razer devices under GNU/Linux.

%prep
%autosetup -n RazerGenie-%{version}

%build
%meson
%meson_build

%install
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/razergenie
%{_libdir}/libopenrazer.so*
%{_datadir}/applications/razergenie.desktop
%{_datadir}/icons/hicolor/scalable/apps/razergenie.svg
