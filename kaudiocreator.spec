%define svn    838162

Name:          kaudiocreator
Summary:       CD ripper and audio encoder frontend for KDE4
Version:       1.2
Release:       %mkrel 0.%svn.1
Source:        %{name}-%{version}.%svn.tar.bz2
URL:           http://www.kde.org/
License:       GPL
Group:         Graphical desktop/KDE
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: kdemultimedia4-devel
Requires:      kdebase4-runtime

Conflicts:     kdemultimedia-kaudiocreator < 1:3.5.9-6 

%description
CD ripper and audio encoder frontend.

%files
%defattr(-,root,root)
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


#--------------------------------------------------------------------------

%prep
%setup -q

%build

%cmake_kde4

%make

%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -rf %buildroot



