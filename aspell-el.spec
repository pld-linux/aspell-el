Summary:	Greek dictionary for aspell
Summary(pl):	Grecki s³ownik dla aspella
Name:		aspell-el
Version:	0.50
%define	subv	3
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/el/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	0ea2c42ceb9b91f7f5de2c017234ad37
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Greek dictionary (i.e. word list) for aspell.

%description -l pl
Grecki s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f doc/README README-ispell.el

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README* doc/Contributors
%{_libdir}/aspell/*
%{_datadir}/aspell/*
