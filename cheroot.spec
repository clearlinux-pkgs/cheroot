#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cheroot
Version  : 6.2.4
Release  : 9
URL      : https://files.pythonhosted.org/packages/e7/73/5cca1fe3f66777d267f9981b1b586511fc895b2ab0cabfaecf05ecc9ea03/cheroot-6.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/73/5cca1fe3f66777d267f9981b1b586511fc895b2ab0cabfaecf05ecc9ea03/cheroot-6.2.4.tar.gz
Summary  : Highly-optimized, pure-python HTTP server
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cheroot-python3
Requires: cheroot-license
Requires: cheroot-python
Requires: alabaster
Requires: docutils
Requires: more-itertools
Requires: six
BuildRequires : more-itertools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm_git_archive
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
Patch1: deps.patch

%description
.. image:: https://img.shields.io/pypi/v/cheroot.svg
:target: https://pypi.org/project/cheroot

%package license
Summary: license components for the cheroot package.
Group: Default

%description license
license components for the cheroot package.


%package python
Summary: python components for the cheroot package.
Group: Default
Requires: cheroot-python3

%description python
python components for the cheroot package.


%package python3
Summary: python3 components for the cheroot package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cheroot package.


%prep
%setup -q -n cheroot-6.2.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530399999
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cheroot
cp LICENSE.md %{buildroot}/usr/share/doc/cheroot/LICENSE.md
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/cheroot/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
