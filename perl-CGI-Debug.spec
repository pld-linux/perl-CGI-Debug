#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Debug
Summary:	CGI::Debug perl module
Summary(pl):	Modu� perla CGI::Debug
Name:		perl-CGI-Debug
Version:	1.0
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4aa24a6e4aad4a488cf8bfe15cad7c25
BuildRequires:	perl-devel >= 1:5.8.0
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
Modu� perla CGI::Debug - wy�apuj�cy (prawie) wszystkie b��dy
kompilacji i uruchomienia oraz ostrze�enia i wy�wietlaj�cy je w
przegl�darce.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo root@localhost | perl Makefile.PL \
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
%{perl_vendorlib}/CGI/Debug.pm
%{_mandir}/man3/*
