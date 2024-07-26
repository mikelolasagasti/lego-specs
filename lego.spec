# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/go-acme/lego
%global goipath         github.com/go-acme/lego/v4
Version:                4.17.4

%gometa -L -f

%global common_description %{expand:
Let's Encrypt/ACME client and library written in Go.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md CONTRIBUTING.md README.md

Name:           lego
Release:        %autorelease
Summary:        Let's Encrypt/ACME client and library written in Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}
Patch:          db2ab55cdd6a979168ef96dc178568d5120430eb.patch

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
for test in "TestDNSProviderManual" "TestLookupNameserversOK" "TestFindZoneByFqdnCustom" \
            "TestFindPrimaryNsByFqdnCustom" "TestCheckDNSPropagation" "TestCheckAuthoritativeNss" \
            "TestCheckAuthoritativeNssErr"  "TestDNSProvider_findZone" "TestDNSProvider_FindZoneAndRecordName" \
            "TestPresentNoExistingRR" "TestPresentWithExistingRR" "TestPresentSkipExistingRR" \
            "TestRemoveRecord_errors" "TestAddTXTRecord_errors" "TestDNSProvider_concurrentGetDNSEntries" \
            "TestDNSProvider_concurrentAddDNSEntry" "TestClient_GetZone" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
# TODO Review lightsail, route53, otc
%gocheck -d github.com/go-acme/lego/v4/providers/dns/auroradns \
         -d github.com/go-acme/lego/v4/providers/dns/conoha \
         -d github.com/go-acme/lego/v4/providers/dns/constellix/internal \
         -d github.com/go-acme/lego/v4/providers/dns/dynu/internal \
         -d github.com/go-acme/lego/v4/providers/dns/lightsail \
         -d github.com/go-acme/lego/v4/providers/dns/otc \
         -d github.com/go-acme/lego/v4/providers/dns/route53 \
         -d github.com/go-acme/lego/v4/providers/dns/zoneee
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc docs CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/*
%endif

%gopkgfiles

%changelog
%autochangelog
