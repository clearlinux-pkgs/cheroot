#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cheroot
Version  : 6.5.2
Release  : 19
URL      : https://files.pythonhosted.org/packages/c4/ab/b3800499ccec7f058fe080ae7f79207f9b498559edd1467d533a2126767c/cheroot-6.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/ab/b3800499ccec7f058fe080ae7f79207f9b498559edd1467d533a2126767c/cheroot-6.5.2.tar.gz
Summary  : Highly-optimized, pure-python HTTP server
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cheroot-bin = %{version}-%{release}
Requires: cheroot-license = %{version}-%{release}
Requires: cheroot-python = %{version}-%{release}
Requires: cheroot-python3 = %{version}-%{release}
Requires: more-itertools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : more-itertools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm_git_archive
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
Patch1: deps.patch

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

%description python3
python3 components for the cheroot package.


%prep
%setup -q -n cheroot-6.5.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545875174
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cheroot
cp LICENSE.md %{buildroot}/usr/share/package-licenses/cheroot/LICENSE.md
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
/usr/share/package-licenses/cheroot/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
