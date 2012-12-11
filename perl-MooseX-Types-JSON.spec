%define upstream_name    MooseX-Types-JSON
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	JSON datatype for Moose
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildArch:	noarch

%description
JSON datatype for Moose.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 655138
- rebuild for updated spec-helper

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 506652
- import perl-MooseX-Types-JSON


* Tue Feb 16 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
