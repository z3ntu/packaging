# Thanks to Son_Goku on #opensuse-buildservice (freenode) (https://paste.fedoraproject.org/516838/83214922/)
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?python2_version: %global python2_version %(%{__python2} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")}
%{!?python2_version_nodots: %global python2_version_nodots %(%{__python2} -c "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")}
%{!?py2_build: %global py2_build CFLAGS="%{optflags}" %{__python2} setup.py build}
%{!?py2_install: %global py2_install %{__python2} setup.py install --skip-build --root %{buildroot}}

%{!?__python3: %global __python3 /usr/bin/python3}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python3_sitearch: %global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?python3_version: %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")}
%{!?python3_version_nodots: %global python3_version_nodots %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3].replace('.',''))")}
%{!?py3dir: %global py3dir %{_builddir}/python3-%{name}-%{version}-%{release}}
%{!?py3_build: %global py3_build CFLAGS="%{optflags}" %{__python3} setup.py build}
%{!?py3_install: %global py3_install %{__python3} setup.py install --skip-build --root %{buildroot}}

#define gitcommit fa55635c3f7ec05afd04c34a6ee4f4c144a21e34

Name: polychromatic
Version: 0.3.11.2
Release: 1%{?dist}
Summary: A front-end for configuring Razer devices

License: GPL-2.0
URL: https://github.com/lah7/polychromatic

%if 0%{?gitcommit:1}
Source0: https://github.com/lah7/polychromatic/archive/%{gitcommit}.tar.gz
%else
Source0: https://github.com/lah7/polychromatic/archive/v%{version}.tar.gz
%endif
%if 0%{?suse_version}
Source1: http://download.opensuse.org/repositories/home:/illuusio:/nodejs-bundle/openSUSE_Tumbleweed/noarch/lessc-2.6.1-6.3.noarch.rpm
%endif

BuildArch: noarch

Requires: python3-razer
Requires: python3
# Thanks OpenSUSE for this great package name...
%if 0%{?suse_version}
Requires: libappindicator3-1 pkgconfig(webkit2gtk-4.0) typelib-1_0-WebKit2-4_0
%else
Requires: libappindicator-gtk3 webkitgtk4
%endif
Requires: ImageMagick
BuildRequires: rsync
BuildRequires: python3
%if 0%{?suse_version}
# Use lessc from a prebuilt rpm
BuildRequires: nodejs
%else
BuildRequires: nodejs-less
%endif


%description
Graphical front end and tray applet for configuring Razer peripherals on GNU/Linux

%prep
%if 0%{?gitcommit:1}
%autosetup -n polychromatic-%{gitcommit}
%else
%autosetup -n polychromatic-%{version}
%endif
%if 0%{?suse_version}
pushd %{_sourcedir}
rpm2cpio %{_sourcedir}/lessc-2.6.1-6.3.noarch.rpm | cpio -imd --quiet
popd
%endif

%build
# noop


%install
rm -rf $RPM_BUILD_ROOT

%if 0%{?gitcommit:1}
cd %{_builddir}/polychromatic-%{gitcommit}
%else
cd %{_builddir}/polychromatic-%{version}
%endif

%if 0%{?suse_version}
make DESTDIR=$RPM_BUILD_ROOT LESSC=%{_sourcedir}/usr/bin/lessc install
%else
make DESTDIR=$RPM_BUILD_ROOT install
%endif

%find_lang polychromatic-controller
%find_lang polychromatic-tray-applet
%find_lang polychromatic-common

%clean
rm -rf $RPM_BUILD_ROOT


%files -f polychromatic-controller.lang -f polychromatic-tray-applet.lang -f polychromatic-common.lang
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/autostart/polychromatic-tray-applet.desktop
%{_bindir}/polychromatic-*
%{_datadir}/applications/polychromatic-*.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/polychromatic/
%{python3_sitelib}/polychromatic/
%{_mandir}/man1/polychromatic-*

%changelog
* Wed Feb 08 2017 Luca Weiss <luca@z3ntu.xyz> 0.3.6.1.git-1
- Initial RPM release
