%define tarname SetupDocs
%define name	python-setupdocs
%define version 1.0.5
%define	rel		3
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary: 	Setuptools extension for building documentation with Sphinx
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ETS/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/SetupDocs/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-sphinx >= 0.4.2
BuildArch:	noarch
Requires:	python-setuptools
BuildRequires:	python-setuptools
%py_requires -d

%description
SetupDocs is a setuptools extension that help doc building
automation. It adds two commands to the setup.py command

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%py_sitedir/%{tarname}*
%py_sitedir/setupdocs*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 1.0.5-3
+ Revision: 814645
- Require python-sphinx.

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 1.0.5-2mdv2011.0
+ Revision: 593149
- rebuild for py 2.7

* Sun Oct 17 2010 Lev Givon <lev@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 586455
- Update to 1.0.5.

* Thu Apr 08 2010 Lev Givon <lev@mandriva.org> 1.0.4-1mdv2010.1
+ Revision: 533144
- Update to 1.0.4.

* Fri Aug 21 2009 Lev Givon <lev@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 419028
- Update to 1.0.3.

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 371393
- import python-setupdocs


