Name:		python-xdis
Version:	6.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/x/xdis/xdis-%{version}.tar.gz
Summary:	Python cross-version byte-code disassembler and marshal routines
URL:		https://pypi.org/project/xdis/
License:	GPL-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python cross-version byte-code disassembler and marshal routines

%prep
%autosetup -p1 -n xdis-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/pydisasm
%{py_sitedir}/xdis
%{py_sitedir}/xdis-*.*-info
