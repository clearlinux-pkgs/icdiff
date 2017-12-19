#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icdiff
Version  : 1.9.1
Release  : 4
URL      : https://github.com/jeffkaufman/icdiff/archive/release-1.9.1.tar.gz
Source0  : https://github.com/jeffkaufman/icdiff/archive/release-1.9.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Python-2.0
Requires: icdiff-bin
Requires: icdiff-python3
Requires: icdiff-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Icdiff
Improved colored diff
![screenshot](http://www.jefftk.com/icdiff-css-demo.png)

%package bin
Summary: bin components for the icdiff package.
Group: Binaries

%description bin
bin components for the icdiff package.


%package python
Summary: python components for the icdiff package.
Group: Default
Requires: icdiff-python3

%description python
python components for the icdiff package.


%package python3
Summary: python3 components for the icdiff package.
Group: Default
Requires: python3-core

%description python3
python3 components for the icdiff package.


%prep
%setup -q -n icdiff-release-1.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507476478
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-icdiff
/usr/bin/icdiff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
