%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Turn the board pieces to get all computers connected
Name:		plasma6-knetwalk
Version:	24.01.90
Release:	2
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/knetwalk/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/knetwalk-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6TextWidgets)

%description
KNetWalk is a small game where you have to build up a computer network by
rotating the wires to connect the terminals to the server. When the network is
build, a highscore-list comes up where competitions can be fought out.

%files -f knetwalk.lang
%{_bindir}/knetwalk
%{_datadir}/applications/org.kde.knetwalk.desktop
%{_datadir}/knetwalk
%{_iconsdir}/hicolor/*/apps/knetwalk.*
%{_datadir}/metainfo/org.kde.knetwalk.appdata.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n knetwalk-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang knetwalk --with-html
