#
# Conditional build:
%bcond_without	doc	# API documentation

%define		module	sphinx_basic_ng
Summary:	A modern skeleton for Sphinx themes
Summary(pl.UTF-8):	Nowoczesny szkielet motywów Sphinksa
Name:		python3-%{module}
Version:	1.0.0b2
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	fa57208da1afb5bf7e8926a761d10620
URL:		https://pypi.org/project/sphinx-basic-ng/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-ipython
BuildRequires:	python3-myst_parser
BuildRequires:	python3-sphinx_copybutton
BuildRequires:	python3-sphinx_inline_tabs
BuildRequires:	sphinx-pdg-3 >= 4.0
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modernised skeleton for Sphinx themes.

%description -l pl.UTF-8
Zmodernizowany szkielet motywów Sphinksa.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
rm -rf docs/_build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/theme
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
