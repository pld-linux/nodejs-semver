%define		pkg	semver
Summary:	The semantic versioner for npm
Name:		nodejs-%{pkg}
Version:	1.0.13
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-semver
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	769e21c9aeed3f3ddf3470fe0890b14e
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The semantic version comparison library for the Node.js package
manager (npm).

%prep
%setup -qc
mv package/* .

#%nodejs_fixshebang bin/%{pkg}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p package.json %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_bindir}
install -p bin/%{pkg} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/%{pkg}
%{nodejs_libdir}/%{pkg}
