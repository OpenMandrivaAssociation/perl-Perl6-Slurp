%define upstream_name    Perl6-Slurp
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Implements the Perl 6 'slurp' built-in
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl6/Perl6-Slurp-%{upstream_version}.tar.gz
Patch0:     Perl6-Slurp-0.03-fix-tests.patch

BuildRequires:	perl(Perl6::Export)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This package implements the Perl 6 'slurp' built-in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1

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
