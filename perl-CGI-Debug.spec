%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Debug perl module
Summary(pl):	Modu� perla CGI-Debug
Name:		perl-CGI-Debug
Version:	0.07
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Debug-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Lite
BuildRequires:	perl-Time-HiRes
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-MIME-Lite
Requires:	perl-Time-HiRes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Debug will catch (almost) all compilation and runtime errors and
warnings and will display them in the browser.

%description -l pl
Modu� perla CGI-Debug

%prep
%setup -q -n CGI-Debug-%{version}

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
%{perl_sitelib}/CGI/Debug.pm
%{_mandir}/man3/*
