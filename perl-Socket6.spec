#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Socket6
%define		pnam	Socket6
Summary:	Socket6 Perl module
Summary(cs.UTF-8):	Modul Socket6 pro Perl
Summary(da.UTF-8):	Perlmodul Socket6
Summary(de.UTF-8):	Socket6 Perl Modul
Summary(es.UTF-8):	Módulo de Perl Socket6
Summary(fr.UTF-8):	Module Perl Socket6
Summary(it.UTF-8):	Modulo di Perl Socket6
Summary(ja.UTF-8):	Socket6 Perl モジュール
Summary(ko.UTF-8):	Socket6 펄 모줄
Summary(nb.UTF-8):	Perlmodul Socket6
Summary(pl.UTF-8):	Moduł Perla Socket6
Summary(pt.UTF-8):	Módulo de Perl Socket6
Summary(pt_BR.UTF-8):	Módulo Perl Socket6
Summary(ru.UTF-8):	Модуль для Perl Socket6
Summary(sv.UTF-8):	Socket6 Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Socket6
Summary(zh_CN.UTF-8):	Socket6 Perl 模块
Name:		perl-Socket6
Version:	0.23
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Socket6/%{pnam}-%{version}.tar.gz
# Source0-md5:	2c02adb13c449d48d232bb704ddbd492
URL:		http://search.cpan.org/dist/Socket6/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socket6 is a module that implements a IPv6 API for Perl programs.

%description -l pl.UTF-8
Socket6 jest modułem umożliwiającym dostęp do usług IPv6 z poziomu
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
%{perl_vendorarch}/Socket6.pm
%dir %{perl_vendorarch}/auto/Socket6
%{perl_vendorarch}/auto/Socket6/Socket6.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Socket6/Socket6.so
%{_mandir}/man3/*
