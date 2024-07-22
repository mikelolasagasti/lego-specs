# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/nrdcg/mailinabox
%global goipath         github.com/nrdcg/mailinabox
Version:                0.2.0

%gometa -L -f

%global common_description %{expand:
Go library for accessing the Mail-in-a-Box API.}

%global golicenses      LICENSE
%global godocs          readme.md

Name:           golang-github-nrdcg-mailinabox
Release:        %autorelease
Summary:        Go library for accessing the Mail-in-a-Box API

License:        MPL-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

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
