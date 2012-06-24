%include	/usr/lib/rpm/macros.perl
Summary:	perl-Socket6 perl module
Summary(pl):	Modu� perla perl-Socket6
Name:		perl-Socket6
Version:	0.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Socket6/Socket6-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl-Socket6 is a module that implements a IPv6 API for Perl programs.

%description -l pl
perl-Socket6 jest modu�em umo�liwiaj�cych dost�p do us�ug IPv6 z
poziomu program�w perla.

%prep
%setup -q -n Socket6-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Socket6.pm
%{perl_sitearch}/auto/Socket6/Socket6.so
%{perl_sitearch}/auto/Socket6/Socket6.bs
