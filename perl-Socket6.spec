%include	/usr/lib/rpm/macros.perl
Summary:	perl-Socket6 perl module
Summary(pl):	Modu³ perla perl-Socket6
Name:		perl-Socket6
Version:	0.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Socket6/Socket6-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl-Socket6 is a module that implements a IPv6 API for Perl programs.

%description -l pl
perl-Socket6 jest modu³em umo¿liwiaj±cych dostêp do us³ug IPv6 z
poziomu programów perla.

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
