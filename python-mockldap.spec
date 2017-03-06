%global        uname mockldap
%global        sum A simple mock implementation of python-ldap.

Name:          python-%{uname}
Version:       0.2.7
Release:       1%{?dist}
Summary:       %{sum}

URL:           https://pypi.python.org/pypi/%{uname}
Source:        https://pypi.io/packages/source/m/%{uname}/%{uname}-%{version}.tar.gz
License:       BSD

BuildArch:     noarch

Buildrequires: python-setuptools
Buildrequires: python2-devel

Requires:      python-funcparserlib
Requires:      python2-mock
Requires:      python-ldap

%description
%{sum}.

%package -n python2-%{uname}
Summary:        %{sum}

%description -n python2-%{uname}
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{uname}
%{python2_sitelib}/*

%changelog
* Mon Mar 6 2017 Nicolas Hicher <nhicher@redhat.com> 0.2.7-1
- initial package
