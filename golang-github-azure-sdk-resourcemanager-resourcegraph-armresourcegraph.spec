# Generated by go2rpm 1.14.0
# Tests require credentials
%bcond check 0
%bcond bootstrap 1

%global debug_package %{nil}
%global module resourcemanager/resourcegraph/armresourcegraph

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/Azure/azure-sdk-for-go
%global goipath         github.com/Azure/azure-sdk-for-go/sdk/%{module}
Version:                0.9.0
%global tag             sdk/%{module}/v%{version}
%global distprefix      %{nil}

%gometa -f

%global common_description %{expand:
Azure SDK for Go - %{module} library.}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md SUPPORT.md\\\
                        SECURITY.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Azure SDK for Go - %{module} library

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

# move building library to the root to match goipath
mv sdk/%{module}/* .
rm -rf .github documentation eng profile sdk

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
