%include	/usr/lib/rpm/macros.perl
Summary:	Proc-WaitStat perl module
Summary(pl):	Modu� perla Proc-WaitStat
Name:		perl-Proc-WaitStat
Version:	1.00
Release:	4
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
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-WaitStat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-IPC-Signal
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-WaitStat module contains functions for interpreting and acting on
wait status values.

%description -l pl
Modu� Proc-WaitStat zawiera funkcje do interpretowania warto�ci
zwracanych przez wait() i podejmowania okre�lonych dzia�a�.

%prep
%setup -q -n Proc-WaitStat-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Proc/WaitStat.pm
%{_mandir}/man3/*
