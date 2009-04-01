%define tarname SetupDocs
%define name	python-setupdocs
%define version 1.0.2
%define release %mkrel 1

Summary: 	Python setuptools extension for building documentation
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/SetupDocs/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Suggests:	python-sphinx >= 0.4.2
BuildArch:	noarch
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
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt
