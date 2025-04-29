Name: razergenie
Version: 1.2.0
Release: 1%{?dist}
Summary: Configure and control your Razer devices

License: GPL-3.0
URL: https://github.com/z3ntu/RazerGenie

Source0: https://github.com/z3ntu/RazerGenie/releases/download/v%{version}/RazerGenie-%{version}.tar.xz

BuildRequires: meson
BuildRequires: pkgconfig(libopenrazer)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Xml)
%if 0%{?suse_version}
BuildRequires: libqt5-linguist hicolor-icon-theme
%else
%if 0%{?mageia}
BuildRequires: qttools5
%else
BuildRequires: qt5-linguist
%endif
%endif
Requires: openrazer-daemon
%description
Configure and control your Razer devices

%prep
%autosetup -n RazerGenie-%{version} -p1

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
%{_datadir}/applications/xyz.z3ntu.razergenie.desktop
%{_datadir}/icons/hicolor/scalable/apps/xyz.z3ntu.razergenie.svg
%{_datadir}/metainfo/xyz.z3ntu.razergenie.appdata.xml
%{_datadir}/razergenie/
