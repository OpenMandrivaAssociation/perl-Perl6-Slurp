%define realname Perl6-Slurp

Summary: Implements the Perl 6 'slurp' built-in
Name: perl-Perl6-Slurp
Version: 0.03
Release: %mkrel 1
License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/dist/Perl6-Slurp/
Source: http://www.cpan.org/modules/by-module/Perl6/Perl6-Slurp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires:	perl-Perl6-Export

%description
This package implements the Perl 6 'slurp' built-in.

%prep
%setup -q -n %{realname}-%{version}

%build
yes y | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Perl6/Slurp.pm
