#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cheroot
Version  : 8.4.1
Release  : 39
URL      : https://files.pythonhosted.org/packages/a8/42/44eeb44a595105a3248e8e29999e7d74de9eec3db98f76d5b731a3d60836/cheroot-8.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/42/44eeb44a595105a3248e8e29999e7d74de9eec3db98f76d5b731a3d60836/cheroot-8.4.1.tar.gz
Summary  : Highly-optimized, pure-python HTTP server
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cheroot-bin = %{version}-%{release}
Requires: cheroot-license = %{version}-%{release}
Requires: cheroot-python = %{version}-%{release}
Requires: cheroot-python3 = %{version}-%{release}
Requires: jaraco.functools
Requires: more-itertools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : jaraco.functools
BuildRequires : more-itertools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : setuptools_scm_git_archive-python
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/cheroot.svg
:target: https://pypi.org/project/cheroot

%package bin
Summary: bin components for the cheroot package.
Group: Binaries
Requires: cheroot-license = %{version}-%{release}

%description bin
bin components for the cheroot package.


%package license
Summary: license components for the cheroot package.
Group: Default

%description license
license components for the cheroot package.


%package python
Summary: python components for the cheroot package.
Group: Default
Requires: cheroot-python3 = %{version}-%{release}

%description python
python components for the cheroot package.


%package python3
Summary: python3 components for the cheroot package.
Group: Default
Requires: python3-core
Provides: pypi(cheroot)
Requires: pypi(jaraco.functools)
Requires: pypi(more_itertools)
Requires: pypi(six)

%description python3
python3 components for the cheroot package.


%prep
%setup -q -n cheroot-8.4.1
cd %{_builddir}/cheroot-8.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595863807
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cheroot
cp %{_builddir}/cheroot-8.4.1/LICENSE.md %{buildroot}/usr/share/package-licenses/cheroot/feae831d4a94f4681630f513de63446524956d3d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cheroot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cheroot/feae831d4a94f4681630f513de63446524956d3d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
