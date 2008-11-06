%define name affinity-search
%define version 0.1
%define svn 43
%if %svn
%define release %mkrel 0.%svn.3
%else
%define release %mkrel 1
%endif

Summary:        Desktop search tool providing front-end to various desktop information
Name:           %{name}
Version:        %{version}
Release:        %{release}
%if %svn
Source:         %{name}-%{version}-%{svn}.tar.bz2
%else
Source:         %{name}-%{version}.tar.bz2
%endif
Patch:		affinity-search-0.1-fix-linking.patch
License:        GPLv3+
Group:          Graphical desktop/GNOME
Url:            http://code.google.com/p/affinity-search/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gnome-common 
BuildRequires:  gnome-desktop-devel 
BuildRequires:  gnome-menus-devel 
BuildRequires:  gnome-panel-devel 
BuildRequires:  gtk-doc
BuildRequires:  libgnomeui2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  librsvg2-devel

BuildRequires:  libbeagle-devel
BuildRequires:  tracker-devel

BuildRequires:  intltool
BuildRequires:  desktop-file-utils

%description
Affinty is a desktop search tool, which hopes to provide a quick way 
to get at all the different information on your desktop. It achieves this 
by having various back-ends, but implemented through one standard interface.

%prep
%setup -q
%patch -p1

%build
./autogen.sh -V
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/affinity-preferences.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/affinity.desktop

%clean
rm -rf $RPM_BUILD_ROOT


%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/affinity
%{_bindir}/affinity-preferences
%{_libdir}/affinity-applet
%{_libdir}/bonobo/servers/GNOME_Affinity.server
%{_datadir}/affinity/
%{_datadir}/applications/affinity-preferences.desktop
%{_datadir}/applications/affinity.desktop
%{_datadir}/icons/hicolor/16x16/actions/search.png
%{_datadir}/icons/hicolor/16x16/actions/system-lock-screen.png
%{_datadir}/icons/hicolor/16x16/actions/system-log-out.png
%{_datadir}/icons/hicolor/16x16/apps/gnome-control-center.png
%{_datadir}/icons/hicolor/16x16/apps/system-installer.png
%{_datadir}/icons/hicolor/22x22/actions/search.png
%{_datadir}/icons/hicolor/22x22/actions/system-lock-screen.png
%{_datadir}/icons/hicolor/22x22/actions/system-log-out.png
%{_datadir}/icons/hicolor/22x22/apps/gnome-control-center.png
%{_datadir}/icons/hicolor/22x22/apps/system-installer.png
%{_datadir}/icons/hicolor/24x24/actions/search.png
%{_datadir}/icons/hicolor/24x24/actions/system-lock-screen.png
%{_datadir}/icons/hicolor/24x24/actions/system-log-out.png
%{_datadir}/icons/hicolor/24x24/apps/gnome-control-center.png
%{_datadir}/icons/hicolor/24x24/apps/system-installer.png
%{_datadir}/icons/hicolor/48x48/actions/search.png
%{_datadir}/icons/hicolor/scalable/actions/search.svg
%{_datadir}/icons/hicolor/scalable/actions/system-lock-screen.svg
%{_datadir}/icons/hicolor/scalable/actions/system-log-out.svg
%{_datadir}/icons/hicolor/scalable/apps/gnome-control-center.svg
%{_datadir}/icons/hicolor/scalable/apps/system-installer.svg
