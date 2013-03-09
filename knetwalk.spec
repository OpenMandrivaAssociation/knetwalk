Name:		knetwalk
Version:	4.10.1
Release:	1
Epoch:		1
Summary:	Turn the board pieces to get all computers connected
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/knetwalk/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KNetWalk is a small game where you have to build up a computer network by
rotating the wires to connect the terminals to the server. When the network is
build, a highscore-list comes up where competitions can be fought out.

%files
%{_kde_bindir}/knetwalk
%{_kde_applicationsdir}/knetwalk.desktop
%{_kde_appsdir}/knetwalk
%{_kde_docdir}/*/*/knetwalk
%{_kde_iconsdir}/hicolor/*/apps/knetwalk.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

