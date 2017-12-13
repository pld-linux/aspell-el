Summary:	Greek dictionary for aspell
Summary(pl.UTF-8):	Grecki słownik dla aspella
Name:		aspell-el
Version:	0.08
%define	subv	0
Release:	1
Epoch:		2
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/el/aspell6-el-%{version}-%{subv}.tar.bz2
# Source0-md5:	cf0e677c37ffb64e4b8ebe13acd233c7
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Greek dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Grecki słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-el-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} doc/README README-ispell.el

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README*
%{_libdir}/aspell/el.multi
%{_libdir}/aspell/el.rws
%{_libdir}/aspell/gr.alias
%{_libdir}/aspell/greek.alias
%{_datadir}/aspell/el*.dat
%{_datadir}/aspell/el.kbd
