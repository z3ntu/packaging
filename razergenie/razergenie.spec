Name: razergenie
Version: 1.3.0
Release: 1%{?dist}
Summary: Configure and control your Razer devices

License: GPL-3.0
URL: https://github.com/z3ntu/RazerGenie

Source0: https://github.com/z3ntu/RazerGenie/releases/download/v%{version}/RazerGenie-%{version}.tar.xz

BuildRequires: meson
BuildRequires: pkgconfig(libopenrazer)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Xml)
%if 0%{?suse_version}
BuildRequires: qt6-tools-linguist hicolor-icon-theme
%else
%if 0%{?mageia}
BuildRequires: qttools6
%else
BuildRequires: qt6-linguist
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
