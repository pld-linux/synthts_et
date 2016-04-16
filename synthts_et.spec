Summary:	Estonian language HTS voice synthesis
Summary(et):	Eesti keele HTS-kõnesüntees
Name:		synthts_et
Version:	0
Release:	0.1
License:	BSD
Group:		Applications/Sound
Source0:	https://github.com/ikiissel/synthts_et/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	d5bf7cf6b642562d3577496d647766d3
URL:		https://github.com/ikiissel/synthts_et
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HMM-Based Speech Synthesis Engine "hts_engine API"

%prep
%setup -qc
mv synthts_et-*/* .
mv synthts_et/* .

%build
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
