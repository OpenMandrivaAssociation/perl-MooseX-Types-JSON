%define upstream_name    MooseX-Types-JSON
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	JSON datatype for Moose

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/uperl/MooseX-Types-JSON
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/MooseX-Types-JSON-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:  perl(namespace::autoclean)
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

