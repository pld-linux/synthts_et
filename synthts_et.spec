%define		commit	19fde41
Summary:	Estonian language HTS voice synthesis
Summary(et.UTF-8):	Eesti keele HTS-kõnesüntees
Name:		synthts_et
Version:	0.01
Release:	0.1
License:	BSD
Group:		Applications/Sound
Source0:	https://github.com/ikiissel/synthts_et/archive/%{commit}/%{name}-%{version}-%{commit}.tar.gz
# Source0-md5:	eb348115671adb2b46d2403e744aa047
URL:		https://github.com/ikiissel/synthts_et
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HMM-Based Speech Synthesis Engine "hts_engine API"

%prep
%setup -qc
mv synthts_et-*/* .
mv synthts_et/* .
install -d config

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md README COPYING
%doc %lang(et) ChangeLog
%attr(755,root,root) %{_bindir}/synthts_et
