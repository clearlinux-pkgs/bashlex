#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bashlex
Version  : 0.14
Release  : 6
URL      : https://files.pythonhosted.org/packages/e4/27/c639cb10b965cf4fb5a3b9a9786ecd07edb681522e0d93bfc1ce8704f9d8/bashlex-0.14.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/27/c639cb10b965cf4fb5a3b9a9786ecd07edb681522e0d93bfc1ce8704f9d8/bashlex-0.14.tar.gz
Summary  : Python parser for bash
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: bashlex-license = %{version}-%{release}
Requires: bashlex-python = %{version}-%{release}
Requires: bashlex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# bashlex - Python parser for bash
[![Build Status](https://travis-ci.org/idank/bashlex.svg?branch=master)](https://travis-ci.org/idank/bashlex)

%package license
Summary: license components for the bashlex package.
Group: Default

%description license
license components for the bashlex package.


%package python
Summary: python components for the bashlex package.
Group: Default
Requires: bashlex-python3 = %{version}-%{release}

%description python
python components for the bashlex package.


%package python3
Summary: python3 components for the bashlex package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bashlex package.


%prep
%setup -q -n bashlex-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570827583
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bashlex
cp %{_builddir}/bashlex-0.14/LICENSE %{buildroot}/usr/share/package-licenses/bashlex/8624bcdae55baeef00cd11d5dfcfa60f68710a02
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bashlex/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
