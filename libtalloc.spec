Name: libtalloc
Version: 2.1.8
Release: 1%{?dist}
Group: System Environment/Daemons
Summary: The talloc library
License: LGPLv3+
URL: http://talloc.samba.org/
Source: http://samba.org/ftp/talloc/talloc-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: python2-devel

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Group: Development/Libraries
Summary: Developer tools for the Talloc library
Requires: libtalloc = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the Talloc library.

%package -n python-talloc
Group: Development/Libraries
Summary: Python bindings for the Talloc library
Requires: libtalloc = %{version}-%{release}
Provides: pytalloc%{?_isa} = %{version}-%{release}
Provides: pytalloc = %{version}-%{release}
Obsoletes: pytalloc < 2.1.3

%description -n python-talloc
Python libraries for creating bindings using talloc

%package -n python-talloc-devel
Group: Development/Libraries
Summary: Development libraries for python-talloc
Requires: python-talloc = %{version}-%{release}
Provides: pytalloc-devel%{?_isa} = %{version}-%{release}
Provides: pytalloc-devel = %{version}-%{release}
Obsoletes: pytalloc-devel < 2.1.3

%description -n python-talloc-devel
Development libraries for python-talloc

%prep
%setup -q -n talloc-%{version}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libtalloc.a
rm -f $RPM_BUILD_ROOT/usr/share/swig/*/talloc.i


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libtalloc.so.*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%files -n python-talloc
%defattr(-,root,root,-)
%{_libdir}/libpytalloc-util.so.*
%{python_sitearch}/talloc.so

%files -n python-talloc-devel
%defattr(-,root,root,-)
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.pc
%{_libdir}/libpytalloc-util.so

%post -n python-talloc -p /sbin/ldconfig
%postun -n python-talloc -p /sbin/ldconfig
