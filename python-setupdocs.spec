%define tarname SetupDocs

Summary: 	Setuptools extension for building documentation with Sphinx
Name:		python-setupdocs
Version:	1.0.5
Release:	6
# Original source seems dead, but some guys have a cache...
Source0:	https://mse.uk.distfiles.macports.org/py-setupdocs/SetupDocs-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/SetupDocs/
Requires:	python-sphinx >= 0.4.2
BuildRequires:	python%{pyver}dist(future)
BuildArch:	noarch
BuildSystem:	python

%description
SetupDocs is a setuptools extension that help doc building
automation. It adds two commands to the setup.py command

%prep -a
find . -name "*.py" |xargs futurize -0 -w

%files
%doc *.txt
%py_sitedir/%{tarname}*
%py_sitedir/setupdocs*
