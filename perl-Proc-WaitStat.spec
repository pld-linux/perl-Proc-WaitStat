#
# Conditional build:
%bcond_with	tests	# perform "make test" - working database connection required

%define		pdir	Proc
%define		pnam	WaitStat
Summary:	Proc::WaitStat perl module
Summary(pl.UTF-8):	Moduł perla Proc::WaitStat
Name:		perl-Proc-WaitStat
Version:	1.00
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b911bd579b6b142391b21de1efa30c95
URL:		http://search.cpan.org/dist/Proc-WaitStat/
BuildRequires:	perl-IPC-Signal
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::WaitStat module contains functions for interpreting and acting
on wait status values.

%description -l pl.UTF-8
Moduł Proc::WaitStat zawiera funkcje do interpretowania wartości
zwracanych przez wait() i podejmowania określonych działań.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Proc/WaitStat.pm
%{_mandir}/man3/*
