Summary:	TMail mail library
Summary(pl.UTF-8):	TMail - biblioteka do obsługi poczty
Name:		ruby-TMail
Version:	0.10.8
Release:	4
License:	GPL
Group:		Development/Languages
Source0:	http://i.loveruby.net/archive/tmail/tmail-%{version}.tar.gz
# Source0-md5:	abd5916459691aec669f1bbf78e201d3
URL:		http://i.loveruby.net/en/prog/tmail.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail handling module for Ruby.

%description -l pl.UTF-8
Moduł dla języka Ruby obsługujący pocztę.

%package rdoc
Summary:	Documentation files for TMail mail library
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for TMail mail library

%prep
%setup -q -n tmail-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README.en README.en README.ja NEWS BUGS TODO lib/* doc/* doc.en/* doc.ja/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

rm -f ri/created.rid
# dunno. wasn't packaged before
rm -rf ri/Enumerable
rm -rf ri/File

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/tmail/*.so
%{ruby_rubylibdir}/tmail.rb
%{ruby_rubylibdir}/tmail

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/TMail
%{ruby_ridir}/StringInput
%{ruby_ridir}/StringOutput
