%define pkgname tmail
Summary:	TMail mail library
Summary(pl.UTF-8):	TMail - biblioteka do obsługi poczty
Name:		ruby-%{pkgname}
# WARNING! TMail >= 1.2.5 is not compatible with ruby 1.9!
Version:	1.2.3.1
Release:	4
License:	GPL
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	06e10d8633619b106e450005454485ca
Patch0:		%{name}-fixes.patch
URL:		http://tmail.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-irb
BuildRequires:	ruby-json
Requires:	ruby-iconv
Requires:	ruby-rchardet >= 1.3
Provides:	ruby-TMail
Obsoletes:	ruby-TMail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail handling module for Ruby.

%description -l pl.UTF-8
Moduł dla języka Ruby obsługujący pocztę.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%package rdoc
Summary:	Documentation files for TMail mail library
Summary(pl.UTF-8):	Pliki dokumentacji do biblioteki TMail służącej do obsługi poczty
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for TMail mail library

%description rdoc -l pl.UTF-8
Pliki dokumentacji do biblioteki TMail służącej do obsługi poczty.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

%build
ruby setup.rb config \
	--rbdir=%{ruby_vendorlibdir} \
	--sodir=%{ruby_archdir} \
	--without_ext yes

ruby setup.rb setup

rdoc --ri -o ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri
rm ri/lib/tmail/page-Makefile.ri
rm -r ri/{Array,FalseClass,File,Hash,NilClass,Numeric,Object,String,TrueClass}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/tmail.rb
%{ruby_vendorlibdir}/tmail

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/TMail
