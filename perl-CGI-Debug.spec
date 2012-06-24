%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Debug
Summary:	CGI::Debug perl module
Summary(pl):	Modu� perla CGI::Debug
Name:		perl-CGI-Debug
Version:	1.0
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-MIME-Lite
BuildRequires:	perl-Time-HiRes
Requires:	perl-MIME-Lite
Requires:	perl-Time-HiRes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Debug will catch (almost) all compilation and runtime errors and
warnings and will display them in the browser.

%description -l pl
Modu� perla CGI::Debug

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo root@localhost | perl Makefile.PL
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
%{perl_sitelib}/CGI/Debug.pm
%{_mandir}/man3/*
