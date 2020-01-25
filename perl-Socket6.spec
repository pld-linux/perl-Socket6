#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Socket6
%define		pnam	Socket6
Summary:	Socket6 Perl module - IPv6-related part of the C socket.h defines and structure manipulators
Summary(pl.UTF-8):	Moduł Perla Socket6 - definicje i operacje na strukturach socket.h związanych z IPv6
Name:		perl-Socket6
Version:	0.29
Release:	2
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Socket6/%{pnam}-%{version}.tar.gz
# Source0-md5:	dab4b2dcc76f81b8bedea72d8fd1bc28
URL:		http://search.cpan.org/dist/Socket6/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Socket6 module provides glue routines to the various IPv6
functions.

%description -l pl.UTF-8
Moduł Socket6 udostępnia perlowy interfejs do różnych funkcji IPv6.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
pod2man --section=3pm Socket6.pm >Socket6.3pm

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install Socket6.3pm $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Socket6.pm
%dir %{perl_vendorarch}/auto/Socket6
%attr(755,root,root) %{perl_vendorarch}/auto/Socket6/Socket6.so
%{_mandir}/man3/Socket6.3pm*
