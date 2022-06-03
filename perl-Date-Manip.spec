#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Date-Manip
Version  : 6.88
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/S/SB/SBECK/Date-Manip-6.88.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SB/SBECK/Date-Manip-6.88.tar.gz
Summary  : 'Date manipulation routines'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Date-Manip-bin = %{version}-%{release}
Requires: perl-Date-Manip-license = %{version}-%{release}
Requires: perl-Date-Manip-man = %{version}-%{release}
Requires: perl-Date-Manip-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Inter)

%description
NAME
Date::Manip - Date manipulation routines
DESCRIPTION
Date::Manip is a series of modules designed to make any common date/time
operation easy to do. Operations such as comparing two times,
determining a date a given amount of time from another, or parsing
international times are all easily done. It deals with time as it is
used in the Gregorian calendar (the one currently in use) with full
support for time changes due to daylight saving time.

%package bin
Summary: bin components for the perl-Date-Manip package.
Group: Binaries
Requires: perl-Date-Manip-license = %{version}-%{release}

%description bin
bin components for the perl-Date-Manip package.


%package dev
Summary: dev components for the perl-Date-Manip package.
Group: Development
Requires: perl-Date-Manip-bin = %{version}-%{release}
Provides: perl-Date-Manip-devel = %{version}-%{release}
Requires: perl-Date-Manip = %{version}-%{release}

%description dev
dev components for the perl-Date-Manip package.


%package license
Summary: license components for the perl-Date-Manip package.
Group: Default

%description license
license components for the perl-Date-Manip package.


%package man
Summary: man components for the perl-Date-Manip package.
Group: Default

%description man
man components for the perl-Date-Manip package.


%package perl
Summary: perl components for the perl-Date-Manip package.
Group: Default
Requires: perl-Date-Manip = %{version}-%{release}

%description perl
perl components for the perl-Date-Manip package.


%prep
%setup -q -n Date-Manip-6.88
cd %{_builddir}/Date-Manip-6.88

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Date-Manip
cp %{_builddir}/Date-Manip-6.88/LICENSE %{buildroot}/usr/share/package-licenses/perl-Date-Manip/26e37603333004d59ced7f56dba2aa1ad81b472f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dm_date
/usr/bin/dm_zdump

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Date::Manip.3
/usr/share/man/man3/Date::Manip::Base.3
/usr/share/man/man3/Date::Manip::Calc.3
/usr/share/man/man3/Date::Manip::Changes5.3
/usr/share/man/man3/Date::Manip::Changes5to6.3
/usr/share/man/man3/Date::Manip::Changes6.3
/usr/share/man/man3/Date::Manip::Config.3
/usr/share/man/man3/Date::Manip::ConfigFile.3
/usr/share/man/man3/Date::Manip::DM5.3
/usr/share/man/man3/Date::Manip::DM5abbrevs.3
/usr/share/man/man3/Date::Manip::DM6.3
/usr/share/man/man3/Date::Manip::Date.3
/usr/share/man/man3/Date::Manip::Delta.3
/usr/share/man/man3/Date::Manip::Examples.3
/usr/share/man/man3/Date::Manip::History.3
/usr/share/man/man3/Date::Manip::Holidays.3
/usr/share/man/man3/Date::Manip::Interfaces.3
/usr/share/man/man3/Date::Manip::Lang.3
/usr/share/man/man3/Date::Manip::Lang::catalan.3
/usr/share/man/man3/Date::Manip::Lang::danish.3
/usr/share/man/man3/Date::Manip::Lang::dutch.3
/usr/share/man/man3/Date::Manip::Lang::english.3
/usr/share/man/man3/Date::Manip::Lang::finnish.3
/usr/share/man/man3/Date::Manip::Lang::french.3
/usr/share/man/man3/Date::Manip::Lang::german.3
/usr/share/man/man3/Date::Manip::Lang::index.3
/usr/share/man/man3/Date::Manip::Lang::italian.3
/usr/share/man/man3/Date::Manip::Lang::norwegian.3
/usr/share/man/man3/Date::Manip::Lang::polish.3
/usr/share/man/man3/Date::Manip::Lang::portugue.3
/usr/share/man/man3/Date::Manip::Lang::romanian.3
/usr/share/man/man3/Date::Manip::Lang::russian.3
/usr/share/man/man3/Date::Manip::Lang::spanish.3
/usr/share/man/man3/Date::Manip::Lang::swedish.3
/usr/share/man/man3/Date::Manip::Lang::turkish.3
/usr/share/man/man3/Date::Manip::Migration5to6.3
/usr/share/man/man3/Date::Manip::Misc.3
/usr/share/man/man3/Date::Manip::Obj.3
/usr/share/man/man3/Date::Manip::Objects.3
/usr/share/man/man3/Date::Manip::Problems.3
/usr/share/man/man3/Date::Manip::Recur.3
/usr/share/man/man3/Date::Manip::TZ.3
/usr/share/man/man3/Date::Manip::TZ_Base.3
/usr/share/man/man3/Date::Manip::TZdata.3
/usr/share/man/man3/Date::Manip::Zones.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Date-Manip/26e37603333004d59ced7f56dba2aa1ad81b472f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dm_date.1
/usr/share/man/man1/dm_zdump.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
