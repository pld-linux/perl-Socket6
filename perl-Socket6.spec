#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Socket6
%define		pnam	Socket6
Summary:	Socket6 Perl module
Summary(cs):	Modul Socket6 pro Perl
Summary(da):	Perlmodul Socket6
Summary(de):	Socket6 Perl Modul
Summary(es):	Módulo de Perl Socket6
Summary(fr):	Module Perl Socket6
Summary(it):	Modulo di Perl Socket6
Summary(ja):	Socket6 Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Socket6 ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Socket6
Summary(pl):	Modu³ Perla Socket6
Summary(pt):	Módulo de Perl Socket6
Summary(pt_BR):	Módulo Perl Socket6
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Socket6
Summary(sv):	Socket6 Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Socket6
Summary(zh_CN):	Socket6 Perl Ä£¿é
Name:		perl-Socket6
Version:	0.19
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	35e4bb7e09ca3154a44bcaa8959780a2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socket6 is a module that implements a IPv6 API for Perl programs.

%description -l pl
Socket6 jest modu³em umo¿liwiaj±cym dostêp do us³ug IPv6 z poziomu
programów Perla.

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
%{perl_vendorarch}/%{pdir}.pm
%dir %{perl_vendorarch}/auto/%{pdir}
%{perl_vendorarch}/auto/%{pdir}/%{pdir}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pdir}.so
%{_mandir}/man3/*
