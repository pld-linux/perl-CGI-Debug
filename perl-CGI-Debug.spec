%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	CGI-Debug perl module
Summary(pl):	Modu³ perla CGI-Debug
Name:		perl-CGI-Debug
Version:	0.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Debug-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-MIME-Lite
BuildRequires:	perl-Time-HiRes
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-MIME-Lite
Requires:	perl-Time-HiRes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Debug will catch (almost) all compilation and runtime errors and warnings 
and will display them in the browser.

%description -l pl
Modu³ perla CGI-Debug

%prep
%setup -q -n CGI-Debug-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/Debug
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/CGI/Debug.pm
%{perl_sitearch}/auto/CGI/Debug

%{_mandir}/man3/*
