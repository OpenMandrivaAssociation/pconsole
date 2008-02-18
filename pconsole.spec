%define name	pconsole
%define	version 1.0
%define release	%mkrel 12

Summary:	Administrative tool for working with clusters nodes
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Remote access
URL:		http://www.heiho.net/pconsole/
Source:		http://www.xs4all.nl/~walterj/pconsole/%{name}-%{version}.tar.gz
patch0:		%{name}.sh-iconic.bz2
patch1:		%{name}-sh.patch.bz2
patch2:		%{name}-makefile.patch.bz2
Requires:	openssh-clients, xterm
Provides:	%{name}-%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Prefix:		%{_prefix}

%description
pconsole allows you to connect to each node of your cluster 
simultaneously, and you can type your administrative commands 
in a specialized window that 'multiplies' the input to each 
to the connections you have opened. pconsole is best run from 
within X Windows, although it is possible to employ it without 
X (in console mode) as well.

%prep
rm -rf ${buildroot}
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
%configure --prefix=%{buildroot}/usr
make

%install
myname=`id -un`
mygroup=`id -gn`
%makeinstall INSTALL_USER=$myname INSTALL_GROUP=$mygroup

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root) 
%doc ChangeLog README.pconsole public_html/pconsole.html public_html/images/*
%{_bindir}/pconsole
%attr(755,root,root)%{_bindir}/pconsole
%attr(755,root,root)%{_bindir}/pconsole_wrap

