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
