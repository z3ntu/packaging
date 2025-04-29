%if 0%{?suse_version}
Name: libopenrazer0
%else
Name: libopenrazer
%endif
Version: 0.4.0
Release: 1%{?dist}
Summary: Qt wrapper around the D-Bus API from OpenRazer

License: GPL-3.0-or-later
URL: https://github.com/z3ntu/libopenrazer

Source0: https://github.com/z3ntu/libopenrazer/releases/download/v%{version}/libopenrazer-%{version}.tar.xz

BuildRequires: meson
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6DBus)
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

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%description
Qt wrapper around the D-Bus API from OpenRazer

%prep
%autosetup -n libopenrazer-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%{_datadir}/libopenrazer/
%{_libdir}/libopenrazer.so.*

%files devel
%{_libdir}/libopenrazer.so
%{_libdir}/pkgconfig/libopenrazer.pc
%{_includedir}/libopenrazer*
