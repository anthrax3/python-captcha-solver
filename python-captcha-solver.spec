# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	captcha-solver
Summary:	Univeral API to different captcha solving services
Name:		python-%{module}
Version:	0.0.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/captcha-solver/captcha-solver-%{version}.tar.gz
# Source0-md5:	5ff32bb9dfef48c6e7b0e433b125d2d3
URL:		https://pypi.python.org/pypi/captcha-solver
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-grab
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-grab
%endif
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Univeral API to different captcha solving services.

%package -n python3-%{module}
Summary:	Univeral API to different captcha solving services
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Univeral API to different captcha solving services.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/captcha_solver

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/captcha_solver-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/captcha_solver
%{py3_sitescriptdir}/captcha_solver-%{version}-py*.egg-info
%endif
