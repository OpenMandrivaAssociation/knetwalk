%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Turn the board pieces to get all computers connected
Name:		knetwalk
Version:	21.08.2
Release:	1
Epoch:		1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/knetwalk/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5TextWidgets)

%description
KNetWalk is a small game where you have to build up a computer network by
rotating the wires to connect the terminals to the server. When the network is
build, a highscore-list comes up where competitions can be fought out.

%files -f %{name}.lang
%{_bindir}/knetwalk
%{_datadir}/applications/org.kde.knetwalk.desktop
%{_datadir}/knetwalk
%{_iconsdir}/hicolor/*/apps/knetwalk.*
%{_datadir}/metainfo/org.kde.knetwalk.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
