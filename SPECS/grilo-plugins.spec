# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global grilo_version 0.3.1
%global goa_version 3.17.91

Name:		grilo-plugins
Version:	0.3.8
Release:	1%{?dist}
Summary:	Plugins for the Grilo framework

License:	LGPLv2+
URL:		https://wiki.gnome.org/Projects/Grilo
Source0:	https://download.gnome.org/sources/grilo-plugins/%{release_version}/grilo-plugins-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:	avahi-gobject-devel
BuildRequires:	grilo-devel >= %{grilo_version}
BuildRequires:	glib2-devel
BuildRequires:	gom-devel
BuildRequires:	gnome-online-accounts-devel >= %{goa_version}
BuildRequires:	gperf
BuildRequires:	libgcrypt-devel
BuildRequires:	libxml2-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libarchive-devel
BuildRequires:	libmediaart-devel
BuildRequires:	libsoup-devel
BuildRequires:	lua-devel
BuildRequires:	rest-devel
BuildRequires:	sqlite-devel
BuildRequires:	libgdata-devel
BuildRequires:	totem-pl-parser-devel
BuildRequires:	tracker-devel
BuildRequires:	libdmapsharing-devel
BuildRequires:	json-glib-devel

Requires:	dleyna-server
Requires:	gnome-online-accounts%{_isa} >= %{goa_version}
Requires:	grilo%{_isa} >= %{grilo_version}

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Euronews
- Filesystem
- Flickr
- Freebox
- Gravatar
- iTunes Music Sharing
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Pocket
- Podcasts
- Radio France
- Shoutcast
- The Guardian Videos
- Tracker
- Vimeo
- Youtube

%prep
%autosetup -p1

%build
%meson \
    -Denable-static=no \
    -Denable-shoutcast=no \
    -Denable-bookmarks=yes \
    -Denable-dleyna=yes \
    -Denable-dmap=yes \
    -Denable-filesystem=yes \
    -Denable-flickr=yes \
    -Denable-freebox=yes \
    -Denable-gravatar=yes \
    -Denable-jamendo=yes \
    -Denable-lua-factory=yes \
    -Denable-metadata-store=yes \
%if 0%{?fedora}
    -Denable-podcasts=yes \
%endif
    -Denable-tmdb=yes \
    -Denable-tracker=yes \
    -Denable-vimeo=yes \
    -Denable-youtube=yes \
    -Denable-tracker=yes

%meson_build

%install
%meson_install

# Remove files that will not be packaged
rm -f $RPM_BUILD_ROOT%{_libdir}/grilo-%{release_version}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/*

%find_lang grilo-plugins --with-gnome

%files -f grilo-plugins.lang
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/*/examples/example-tmdb.c
%{_datadir}/grilo-plugins/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/grilo-%{release_version}/*.so*

%changelog
* Mon Sep 24 2018 Victor Toso <victortoso@redhat.com> - 0.3.8-1
- Update to 0.3.8

* Fri Jul 27 2018 Victor Toso <victortoso@redhat.com> - 0.3.7-1
- Update to 0.3.7
- Switch build to meson
- Drop gmime requirement

* Wed Jul 18 2018 Victor Toso <victortoso@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Kalev Lember <klember@redhat.com> - 0.3.5-2
- Switch to gmime 3.0

* Fri Aug 25 2017 Bastien Nocera <bnocera@redhat.com> - 0.3.5-1
+ grilo-plugins-0.3.5-1
- Update to 0.3.5

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 0.3.4-4
- Rebuilt for libtotem-plparser soname bump

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 0.3.4-3
- Rebuilt for libtotem-plparser soname bump

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Kalev Lember <klember@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 0.3.3-1
- Update to 0.3.3
- Don't set group tags
- Use make_install macro

* Mon Jul 25 2016 Kalev Lember <klember@redhat.com> - 0.3.2-2
- Update required grilo version

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Tue Mar 22 2016 Bastien Nocera <bnocera@redhat.com> 0.3.1-1
- Update to 0.3.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Kalev Lember <klember@redhat.com> - 0.3.0-1
- Update to 0.3.0
- Update project URL

* Wed Sep 23 2015 Kalev Lember <klember@redhat.com> - 0.2.16-1
- Update to 0.2.16

* Fri Sep 11 2015 Kalev Lember <klember@redhat.com> - 0.2.15-1
- Update to 0.2.15
- Tighten deps with _isa macro
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 David King <amigadave@amigadave.com> - 0.2.14-3
- Rebuild for libgdata soname bump

* Fri Mar 27 2015 Ray Strode <rstrode@redhat.com> 0.2.14-2
- Conditionalize dleyna-server requirement

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.14-1
- Update to 0.2.14

* Sun Feb 15 2015 Bastien Nocera <bnocera@redhat.com> 0.2.13-3
- Add missing dleyna-server requirement so DLNA works

* Mon Jan 26 2015 David King <amigadave@amigadave.com> - 0.2.13-2
- Port to libmediaart-2.0

* Tue Aug 26 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.13-1
- Update to 0.2.13

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.12-6
- Rebuilt with libmediaart 0.6.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Adam Williamson <awilliam@redhat.com> - 0.2.12-3
- rebuild for new libgdata

* Wed Apr 02 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.12-2
- Build additional freebox, lua-factory and pocket plugins

* Wed Mar 19 2014 Richard Hughes <rhughes@redhat.com> - 0.2.12-1
- Update to 0.2.12

* Wed Feb 19 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.11-1
- Update to 0.2.11

* Thu Dec 19 2013 Adam Williamson <awilliam@redhat.com> - 0.2.9-3
- patch to build against newer tracker, rebuild for tracker bump

* Thu Sep 19 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.9-2
- Rebuilt for totem-pl-parser soname bump

* Sun Aug 25 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.9-1
- Update to 0.2.9

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.8-4
- Fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.8-2
- Backport a patch to avoid DNS delays at plugin init (#969123)

* Sat May 25 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.8-1
- Update to 0.2.8

* Sat May 18 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.7-1
- Update to 0.2.7

* Sat May 18 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.6-2
- Use the find_lang --with-gnome macro for help files
- Drop the dep on yelp (#964421)

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Mon Jan 28 2013 Matthias Clasen <mclasen@redhat.com> - 0.2.5-3
- Fix build against newer tracker

* Sun Jan 27 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.5-2
- Rebuild for tracker

* Thu Dec 20 2012 Bastien Nocera <bnocera@redhat.com> 0.2.5-1
- Update to 0.2.5

* Tue Dec 04 2012 Bastien Nocera <bnocera@redhat.com> 0.2.4-1
- Update to 0.2.4

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> 0.2.3-1
- Update to 0.2.3

* Fri Oct 05 2012 Bastien Nocera <bnocera@redhat.com> 0.2.2-1
- Update to 0.2.2

* Wed Oct 03 2012 Bastien Nocera <bnocera@redhat.com> 0.2.1-1
- Update to 0.2.1

* Fri Aug 31 2012 Debarshi Ray <rishi@fedoraproject.org> 0.2.0-1
- update to 0.2.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Bastien Nocera <bnocera@redhat.com> 0.1.19-1
- Update to 0.1.19

* Fri Mar 16 2012 Adam Williamson <awilliam@redhat.com> - 0.1.18-4
- Rebuild for new tracker again

* Tue Feb 28 2012 Matthias Clasen <mclasen@redhat.com> - 0.1.18-3
- Rebuild for new tracker

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Bastien Nocera <bnocera@redhat.com> 0.1.18-1
- Update to 0.1.18

* Thu Nov 17 2011 Daniel Drake <dsd@laptop.org> 0.1.17-2
- rebuild for libquvi.so.7

* Mon Oct 17 2011 Bastien Nocera <bnocera@redhat.com> 0.1.17-1
- Update to 0.1.17

* Mon Jul 04 2011 Bastien Nocera <bnocera@redhat.com> 0.1.16-1
- Update to 0.1.16

* Fri Jun 17 2011 Peter Robinson <pbrobinson@gmail.com> 0.1.15-5
- rebuild for new gupnp/gssdp

* Fri May 20 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-4
- Update with more comments from Kalev Lember <kalev@smartlink.ee>

* Fri May 20 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-3
- Update with comments from Kalev Lember <kalev@smartlink.ee>

* Fri May 20 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-2
- Fix a few rpmlint warnings

* Thu Apr 21 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-1
- Fist package, based on upstream work by Juan A.
  Suarez Romero <jasuarez@igalia.com>

