Name:		kaudiocreator
Summary:	CD ripper and audio encoder fron-tend for KDE4
Version:	1.3
Release:	2
Source:		http://opendesktop.org/CONTENT/content-files/107645-%{name}-%{version}.tar.bz2
URL:		https://opendesktop.org/content/show.php/KAudioCreator?content=107645
License:	GPLv2+
Group:		Graphical desktop/KDE
#kdemulitimedia4-devel missing
BuildRequires:	kde4-audiocd-devel
BuildRequires:	libkcddb-devel
BuildRequires:	libkcompactdisc-devel
BuildRequires:	juk
BuildRequires:	kmix
BuildRequires:	kscd
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libdiscid)
Requires:	kdebase4-runtime
Obsoletes:	kdemultimedia-kaudiocreator < 1:3.5.10-2

%description
CD ripper and audio encoder front-end.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}


%files -f %{name}.lang
%doc Changelog COPYING TODO
%{_kde_bindir}/kaudiocreator
%{_kde_datadir}/applications/kde4/kaudiocreator.desktop
%{_kde_appsdir}/kaudiocreator
%{_kde_appsdir}/kconf_update/kaudiocreator-libkcddb.upd
%{_kde_appsdir}/kconf_update/kaudiocreator-meta.upd
%{_kde_appsdir}/kconf_update/upgrade-kaudiocreator-metadata.sh
%{_kde_datadir}/config.kcfg/kaudiocreator.kcfg
%{_kde_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_kde_iconsdir}/hicolor/*/apps/kaudiocreator.png
%{_kde_datadir}/kde4/services/ServiceMenus/audiocd_extract.desktop


