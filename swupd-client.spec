#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-client
Version  : 3.6.6
Release  : 154
URL      : https://github.com/clearlinux/swupd-client/releases/download/v3.6.6/swupd-client-3.6.6.tar.gz
Source0  : https://github.com/clearlinux/swupd-client/releases/download/v3.6.6/swupd-client-3.6.6.tar.gz
Source1  : swupd-client.tmpfiles
Source2  : swupd-update.service
Source3  : swupd-update.timer
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: swupd-client-bin
Requires: swupd-client-config
Requires: swupd-client-lib
Requires: swupd-client-data
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(bsdiff)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev
Patch1: http2.patch
Patch2: count-nonpack.patch
Patch3: fix-verify-bug.patch
Patch4: recursion.patch
Patch5: headeronly.patch
Patch6: print.patch
Patch7: nosync.patch
Patch8: cache-version.patch
Patch9: hashcache.patch
Patch10: linked.patch
Patch11: fasthash.patch

%description
The swupd-client package provides a reference implementation of a software
update client which performs file level updates of an OS, preferentially
using binary deltas whenever possible for efficiency under an assumption
that the OS develops with a release process aimed at rapidly deploying
small incremental changes.

%package bin
Summary: bin components for the swupd-client package.
Group: Binaries
Requires: swupd-client-data
Requires: swupd-client-config

%description bin
bin components for the swupd-client package.


%package config
Summary: config components for the swupd-client package.
Group: Default

%description config
config components for the swupd-client package.


%package data
Summary: data components for the swupd-client package.
Group: Data

%description data
data components for the swupd-client package.


%package dev
Summary: dev components for the swupd-client package.
Group: Development
Requires: swupd-client-lib
Requires: swupd-client-bin
Requires: swupd-client-data
Provides: swupd-client-devel

%description dev
dev components for the swupd-client package.


%package extras
Summary: extras components for the swupd-client package.
Group: Default

%description extras
extras components for the swupd-client package.


%package lib
Summary: lib components for the swupd-client package.
Group: Libraries
Requires: swupd-client-data
Requires: swupd-client-config

%description lib
lib components for the swupd-client package.


%prep
%setup -q -n swupd-client-3.6.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
%configure --disable-static --disable-tests --enable-signature-verification --with-contenturl=https://download.clearlinux.org/update --with-versionurl=https://download.clearlinux.org/update --with-formatid=7
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/swupd-update.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/swupd-update.timer
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/swupd-client.conf
## make_install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d/
install -m644 swupd.bash %{buildroot}/usr/share/defaults/etc/profile.d/50-swupd.bash
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -sf ../swupd-update.timer %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/check-update.service
%exclude /usr/lib/systemd/system/check-update.timer
%exclude /usr/lib/systemd/system/multi-user.target.wants/check-update.timer
%exclude /usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
/usr/lib/systemd/system/swupd-update.service
/usr/lib/systemd/system/swupd-update.timer
/usr/lib/tmpfiles.d/swupd-client.conf

%files data
%defattr(-,root,root,-)
/usr/share/clear/update-ca/157753a5.0
/usr/share/clear/update-ca/425b0f6b.0
/usr/share/clear/update-ca/425b0f6b.key
/usr/share/clear/update-ca/8d28ae65.0
/usr/share/clear/update-ca/d6325660.0
/usr/share/clear/update-ca/d6325660.1
/usr/share/defaults/etc/profile.d/50-swupd.bash

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.so

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
