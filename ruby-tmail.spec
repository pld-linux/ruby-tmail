%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	TMail mail library
Summary(pl):	TMail - biblioteka do obs³ugi poczty
Name:		ruby-TMail
Version:	0.10.8
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://i.loveruby.net/archive/tmail/tmail-%{version}.tar.gz
# Source0-md5:	abd5916459691aec669f1bbf78e201d3
URL:		http://i.loveruby.net/en/prog/tmail.html
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail handling module for Ruby.

%description -l pl
Modu³ dla jêzyka Ruby obs³uguj±cy pocztê.

%prep
%setup -q -n tmail-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README.en README.en README.ja NEWS BUGS TODO lib/* doc/* doc.en/* doc.ja/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/tmail
%{ruby_rubylibdir}/tmail.rb
%attr(755,root,root) %{ruby_archdir}/tmail/*.so
%{ruby_ridir}/TMail
%{ruby_ridir}/StringInput
%{ruby_ridir}/StringOutput
