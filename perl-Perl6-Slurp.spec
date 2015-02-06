%define upstream_name    Perl6-Slurp
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Implements the Perl 6 'slurp' built-in
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl6/Perl6-Slurp-%{upstream_version}.tar.gz
Patch0:		Perl6-Slurp-0.03-fix-tests.patch

BuildRequires:	perl-devel
BuildRequires:	perl(Perl6::Export)

BuildArch:	noarch

%description
This package implements the Perl 6 'slurp' built-in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1

%build
yes y | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Perl6/Slurp.pm


%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-2mdv2010.1
+ Revision: 505004
- tighten spec file & remove duplicated tarball

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 419903
- new perl version macro
- fix tests
- spec cleanup

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2009.0
+ Revision: 258226
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2009.0
+ Revision: 246280
- rebuild

* Sun Mar 23 2008 Stefan van der Eijk <stefan@mandriva.org> 0.03-1mdv2008.1
+ Revision: 189557
- import perl-Perl6-Slurp


