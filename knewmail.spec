Summary:	K Desktop Environment mail notifier
Summary(fr):	Notificateur de mail pour l'Environment de Bureau K
Summary(pl):	Powiadamianie o nowej poczcie dla KDE
Name:		knewmail
Version:	4.0alpha3
Release:	1
License:	GPL
Vendor:		Mike Pilone <mpilone@slac.com>
Group:		X11/Applications/Networking
Source0:	http://www.slac.com/mpilone/projects/knewmail/%{name}-%{version}.tar.gz
# Source0-md5:	a43933779781c5a6341085e18988a182
URL:		http://www.slac.com/mpilone/projects/knewmail.phtml
BuildRequires:	kdelibs-devel >= 2.0
BuildRequires:	kdepim-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
KDEDIR="%{_prefix}"; export KDEDIR
%configure2_13

# workaround - don't rebuild auto*
touch configure.in aclocal.m4 Makefile.in stamp-h.in configure \
	knewmail/Makefile.in knewmail/config/Makefile.in \
	config.status

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
