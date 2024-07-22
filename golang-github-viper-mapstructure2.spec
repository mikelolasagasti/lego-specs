# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/go-viper/mapstructure
%global goipath         github.com/go-viper/mapstructure/v2
Version:                2.0.0

%gometa -L -f

%global common_description %{expand:
Go library for decoding generic map values into native Go structures and vice
versa.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           golang-github-viper-mapstructure2
Release:        %autorelease
Summary:        Go library for decoding generic map values into native Go structures and vice versa

License:        MIT
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
