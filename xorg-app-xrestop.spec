Summary:	X Resource Monitor
Summary(pl.UTF-8):	Monitor zasobów X
Name:		xorg-app-xrestop
Version:	0.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xrestop-%{version}.tar.xz
# Source0-md5:	8c351345e8a101bfb3e8918bc64cec64
URL:		https://xorg.freedesktop.org/
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	xrestop < 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

%description -l pl.UTF-8
Narzędzie do monitorowania wykorzystania zasobów serwera X i
wyświetlania ich w sposób podobny do programu top.

%prep
%setup -q -n xrestop-%{version}

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/xrestop
%{_mandir}/man1/xrestop.1*
