Summary:	K Desktop Environment mail notifier
Summary(fr):	Notificateur de mail pour l'Environment de Bureau K
Summary(pl):	Powiadamianie o nowej poczcie dla KDE
Name:		knewmail
Version:	3.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Vendor:		Mike Pilone <mpilone@slac.com>
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/utils/%{name}-%{version}.src.tar.gz
URL:		http://www.slac.com/mpilone/knewmail_home/
BuildRequires:	qt-devel >= 1.40
BuildRequires:	kdelibs-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Knewmail is a POP3 aware mail notifier for the K Desktop Environment.

%description -l fr
Knewmail est un notificateur de mail avec support POP3 pour
l'Environment de Bureau K.

%description -l pl
Knewmail jest programem powiadamiaj±cym o nowej poczcie dla KDE.

%prep
%setup -q

%build
if [ -z "$KDEDIR" ]; then
	KDEDIR=%{_prefix} ; export KDEDIR
fi
CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
if [ -z "$KDEDIR" ]; then
	KDEDIR=%{_prefix} ; export KDEDIR
fi
%{__make} prefix=$RPM_BUILD_ROOT$KDEDIR install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -r $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
%defattr(644,root,root,755)
