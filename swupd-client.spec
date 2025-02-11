#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-client
Version  : 3.21.0
Release  : 318
URL      : https://github.com/clearlinux/swupd-client/releases/download/v3.21.0/swupd-client-3.21.0.tar.gz
Source0  : https://github.com/clearlinux/swupd-client/releases/download/v3.21.0/swupd-client-3.21.0.tar.gz
Source1  : swupd-cleanup.service
Source2  : swupd-cleanup.timer
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+
Requires: swupd-client-autostart = %{version}-%{release}
Requires: swupd-client-bin = %{version}-%{release}
Requires: swupd-client-data = %{version}-%{release}
Requires: swupd-client-man = %{version}-%{release}
Requires: swupd-client-services = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : docutils
BuildRequires : pkgconfig(bsdiff)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev
Patch1: 0001-Add-polkit-files.patch
Patch2: always-run-ldconfig.patch
Patch3: 0001-mirror-Removing-invalid-in-check-connection.patch

%description
The swupd-client package provides a reference implementation of a software
update client which performs file level updates of an OS, preferentially
using binary deltas whenever possible for efficiency under an assumption
that the OS develops with a release process aimed at rapidly deploying
small incremental changes.

%package autostart
Summary: autostart components for the swupd-client package.
Group: Default

%description autostart
autostart components for the swupd-client package.


%package bin
Summary: bin components for the swupd-client package.
Group: Binaries
Requires: swupd-client-data = %{version}-%{release}
Requires: swupd-client-services = %{version}-%{release}

%description bin
bin components for the swupd-client package.


%package data
Summary: data components for the swupd-client package.
Group: Data

%description data
data components for the swupd-client package.


%package man
Summary: man components for the swupd-client package.
Group: Default

%description man
man components for the swupd-client package.


%package services
Summary: services components for the swupd-client package.
Group: Systemd services

%description services
services components for the swupd-client package.


%prep
%setup -q -n swupd-client-3.21.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566458171
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-tests \
--enable-signature-verification \
--with-contenturl=https://cdn.download.clearlinux.org/update/ \
--with-versionurl=https://cdn.download.clearlinux.org/update/ \
--with-formatid=29 \
--with-fallback-capaths=/usr/share/ca-certs/.prebuilt-store/anchors \
--with-post-update=/usr/bin/update-helper
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1566458171
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/swupd-cleanup.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/swupd-cleanup.timer
## install_append content
mkdir -p %{buildroot}/usr/share/bash-completion/completions/swupd
install -m644 swupd.bash %{buildroot}/usr/share/bash-completion/completions/swupd
mkdir -p %{buildroot}/usr/share/defaults/swupd/
install -m644 config %{buildroot}/usr/share/defaults/swupd/config
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -sf ../swupd-update.timer %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
mkdir -p %{buildroot}/usr/lib/systemd/system/timers.target.wants/
ln -sf ../swupd-cleanup.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/swupd-cleanup.timer
mkdir -p %{buildroot}/usr/share/polkit-1/actions
mkdir -p %{buildroot}/usr/share/polkit-1/rules.d
install -m644 data/org.clearlinux.swupd.policy %{buildroot}/usr/share/polkit-1/actions/
install -m644 data/org.clearlinux.swupd.rules %{buildroot}/usr/share/polkit-1/rules.d/
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
/usr/lib/systemd/system/timers.target.wants/swupd-cleanup.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd
/usr/bin/verifytime

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/swupd/swupd.bash
/usr/share/defaults/swupd/config
/usr/share/polkit-1/actions/org.clearlinux.swupd.policy
/usr/share/polkit-1/rules.d/org.clearlinux.swupd.rules

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swupd.1
/usr/share/man/man4/check-update.service.4
/usr/share/man/man4/check-update.timer.4
/usr/share/man/man4/swupd-update.service.4
/usr/share/man/man4/swupd-update.timer.4
/usr/share/man/man4/update-triggers.target.4
/usr/share/man/man7/swupd-alias.7

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/check-update.service
%exclude /usr/lib/systemd/system/check-update.timer
%exclude /usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
%exclude /usr/lib/systemd/system/timers.target.wants/swupd-cleanup.timer
/usr/lib/systemd/system/swupd-cleanup.service
/usr/lib/systemd/system/swupd-cleanup.timer
/usr/lib/systemd/system/swupd-update.service
/usr/lib/systemd/system/swupd-update.timer
/usr/lib/systemd/system/verifytime.service
