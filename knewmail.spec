%define name knewmail
%define version 3.1
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: K Desktop Environment mail notifier
Summary(fr): Notificateur de mail pour l'Environment de Bureau K
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: X11/KDE/Applications/Networking
Copyright: GPL
Vendor: Mike Pilone <mpilone@slac.com>
Packager: Troy Engel <tengel@sonic.net>
Distribution: KDE
Source: %{name}-%{version}.src.tar.gz
Url: http://www.slac.com/mpilone/knewmail_home/
Requires: qt >= 1.40 kdelibs >= 1.0
Buildroot: /tmp/build-%{name}-%{version}

%description
Knewmail is a POP3 aware mail notifier for the K Desktop
Environment.

%description -l fr
Knewmail est un notificateur de mail avec support POP3 
pour l'Environment de Bureau K.

%prep
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%setup
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
make

%install
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
make prefix=$RPM_BUILD_ROOT$KDEDIR install-strip

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}

%files -f ../file.list.%{name}
