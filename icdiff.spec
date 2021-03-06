#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icdiff
Version  : 2.0.0
Release  : 31
URL      : https://github.com/jeffkaufman/icdiff/archive/release-2.0.0/icdiff-2.0.0.tar.gz
Source0  : https://github.com/jeffkaufman/icdiff/archive/release-2.0.0/icdiff-2.0.0.tar.gz
Summary  : improved colored diff
Group    : Development/Tools
License  : Python-2.0
Requires: icdiff-bin = %{version}-%{release}
Requires: icdiff-license = %{version}-%{release}
Requires: icdiff-python = %{version}-%{release}
Requires: icdiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Icdiff
Improved colored diff
![screenshot](http://www.jefftk.com/icdiff-css-demo.png)

%package bin
Summary: bin components for the icdiff package.
Group: Binaries
Requires: icdiff-license = %{version}-%{release}

%description bin
bin components for the icdiff package.


%package license
Summary: license components for the icdiff package.
Group: Default

%description license
license components for the icdiff package.


%package python
Summary: python components for the icdiff package.
Group: Default
Requires: icdiff-python3 = %{version}-%{release}

%description python
python components for the icdiff package.


%package python3
Summary: python3 components for the icdiff package.
Group: Default
Requires: python3-core
Provides: pypi(icdiff)

%description python3
python3 components for the icdiff package.


%prep
%setup -q -n icdiff-release-2.0.0
cd %{_builddir}/icdiff-release-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614699497
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/icdiff
cp %{_builddir}/icdiff-release-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/icdiff/ee7904173585b2506078dc8dac150638f1b3e537
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-icdiff
/usr/bin/icdiff

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/icdiff/ee7904173585b2506078dc8dac150638f1b3e537

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
