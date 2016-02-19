%global pkg_name ant-antunit
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       antunit

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.2
Release:          10.11%{?dist}
Summary:          Provide antunit ant task
License:          ASL 2.0
URL:              http://ant.apache.org/antlibs/%{base_name}/
Source0:          http://www.apache.org/dist/ant/antlibs/%{base_name}/source/apache-%{pkg_name}-%{version}-src.tar.bz2
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}ant-junit
BuildRequires:    %{?scl_prefix_java_common}ant-testutil

Requires:         %{?scl_prefix_java_common}ant


%description
The <antunit> task drives the tests much like <junit> does for JUnit tests.

When called on a build file, the task will start a new Ant project for that
build file and scan for targets with names that start with "test". For each
such target it then will:

   1. Execute the target named setUp, if there is one.
   2. Execute the target itself - if this target depends on other targets the
      normal Ant rules apply and the dependent targets are executed first.
   3. Execute the target names tearDown, if there is one.


%package javadoc
Summary:          Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.


%prep
%setup -q -n apache-%{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
mv CONTRIBUTORS CONTRIBUTORS.orig
iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS.orig > CONTRIBUTORS
touch -r CONTRIBUTORS.orig CONTRIBUTORS
%{?scl:EOF}


%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
ant package
%{?scl:EOF}


%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 build/lib/%{pkg_name}-%{version}.jar %{buildroot}%{_javadir}/%{pkg_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{pkg_name}-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap JPP-%{pkg_name}.pom %{pkg_name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}/

# OPT_JAR_LIST fragments
mkdir -p %{buildroot}%{_sysconfdir}/%{pkg_name}.d
echo "ant/ant-antunit" > %{buildroot}%{_sysconfdir}/%{pkg_name}.d/antunit
%{?scl:EOF}


%files -f .mfiles
%doc CONTRIBUTORS LICENSE NOTICE README README.html WHATSNEW
%dir %{_sysconfdir}/%{pkg_name}.d
%config(noreplace) %{_sysconfdir}/%{pkg_name}.d/antunit

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}


%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.2-10.11
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.2-10.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.2-10.9
- BR/R on packages from rh-java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.2-10.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.4
- Remove requires on java

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-10
- Mass rebuild 2013-12-27

* Wed Jul 17 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9
- Update to current packaging guidelines

* Wed Jun 12 2013 Orion Poplawski <orion@cora.nwra.com> 1.2-7
- Update spec for new Java guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-5
- Remove ppc64 ExcludeArch

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 6 2012 Orion Poplawski <orion@cora.nwra.com> 1.2-3
- Drop junit4 references

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 4 2012 Orion Poplawski <orion@cora.nwra.com> 1.2-1
- Update to 1.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-4
- ExcludeArch ppc64 - no java >= 1:1.6.0 on ppc64

* Mon Dec 6 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-3
- Rename to ant-antunit
- Drop BuildRoot and %%clean
- Drop unneeded Provides

* Fri Oct 29 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-2
- Add /etc/ant.d/antunit
- Add Requires: ant

* Thu Oct 28 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-1
- Initial package
