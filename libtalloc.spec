Name: libtalloc
Version: 2.0.1
Release: 1%{?dist}
Group: System Environment/Daemons
Summary: The talloc library
License: LGPLv3+
URL: http://talloc.samba.org/
Source: http://samba.org/ftp/talloc/talloc-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: autoconf

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Group: Development/Libraries
Summary: Developer tools for the Talloc library
Requires: libtalloc = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the Talloc library.

%prep
%setup -q -n talloc-%{version}

%build
./autogen.sh
#%configure --enable-talloc-compat1
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

ln -s libtalloc.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtalloc.so.2
ln -s libtalloc.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtalloc.so

#Compatibility library
#ln -s libtalloc-compat1-2.0.0.so $RPM_BUILD_ROOT%{_libdir}/libtalloc.so.1

rm -f $RPM_BUILD_ROOT%{_libdir}/libtalloc.a
rm -f $RPM_BUILD_ROOT/usr/share/swig/*/talloc.i


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libtalloc.so.*
#%{_libdir}/libtalloc-compat1-2.0.0.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
