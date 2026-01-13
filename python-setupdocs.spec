%define module setupdocs
%define oname SetupDocs

Name:		python-setupdocs
Summary: 	Setuptools extension for building documentation with Sphinx
Version:	1.0.5
Release:	6
# Original source seems dead, but some guys have a cache...
Source0:	https://mse.uk.distfiles.macports.org/py-setupdocs/SetupDocs-%{version}.tar.gz
License:	BSD
Group:		Development/Python
URL:		https://pypi.python.org/pypi/SetupDocs/
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(future)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(sphinx) >= 0.4.2

%description
SetupDocs is a setuptools extension that help doc building
automation. It adds two commands to the setup.py command

%prep
%autosetup -n %{oname}-%{version} -p1
#find . -name "*.py" |xargs futurize -0 -w
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.txt
%license LICENSE.txt
%py_sitedir/%{module}
%py_sitedir/%{oname}-%{version}*.*-info
