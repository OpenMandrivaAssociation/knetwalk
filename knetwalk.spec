Summary:	Turn the board pieces to get all computers connected
Name:		knetwalk
Version:	15.08.0
Release:	2
Epoch:		1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/knetwalk/
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)

%description
KNetWalk is a small game where you have to build up a computer network by
rotating the wires to connect the terminals to the server. When the network is
build, a highscore-list comes up where competitions can be fought out.

%files
%{_bindir}/knetwalk
%{_datadir}/applications/org.kde.knetwalk.desktop
%{_datadir}/knetwalk
%{_iconsdir}/hicolor/*/apps/knetwalk.*
%{_datadir}/kxmlgui5/knetwalk
%doc %{_docdir}/*/*/knetwalk

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
