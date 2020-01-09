%global _hardened_build 1

Summary:        Compat package with upower 0.9 libraries
Name:           compat-upower09
Version:        0.9.20
Release:        1%{?dist}
License:        GPLv2+
Group:          System Environment/Libraries
URL:            http://upower.freedesktop.org/
Source0:        http://upower.freedesktop.org/releases/upower-%{version}.tar.xz
BuildRequires:  sqlite-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  libgudev1-devel
%ifnarch s390 s390x
BuildRequires:  libusb1-devel
BuildRequires:  libimobiledevice-devel
%endif
BuildRequires:  glib2-devel >= 2.6.0
BuildRequires:  dbus-devel  >= 1.2
BuildRequires:  dbus-glib-devel >= 0.82
BuildRequires:  polkit-devel >= 0.92
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc

%description
Compatibility package with upower 0.9 libraries.

%package -n compat-libupower-glib1
Summary: Compat package with upower 0.9 libraries
Conflicts: upower < 0.99

%description -n compat-libupower-glib1
Compatibility package with upower 0.9 libraries.

%prep
%setup -q -n upower-%{version}

%build
%configure \
        --enable-gtk-doc \
        --disable-static \
        --enable-deprecated \
        --enable-introspection \
%ifarch s390 s390x
	--with-backend=dummy
%endif

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/systemd/
rm -rf $RPM_BUILD_ROOT/lib/udev/
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_libexecdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}

%post -n compat-libupower-glib1 -p /sbin/ldconfig

%postun -n compat-libupower-glib1 -p /sbin/ldconfig

%files -n compat-libupower-glib1
%doc COPYING
%{_libdir}/libupower-glib.so.*

%changelog
* Tue May 05 2015 Richard Hughes <rhughes@redhat.com> - 0.9.20-1
- New compat package for RHEL
- Resolves: #1184210
