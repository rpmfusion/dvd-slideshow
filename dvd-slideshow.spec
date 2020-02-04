Name:           dvd-slideshow
%global         realversion 0.8.6
%global         revision 1
Version:        %{realversion}.%{revision}
Release:        6%{?dist}
Summary:        Command line programs for creating slideshow style DVDs
License:        GPLv2
URL:            http://dvd-slideshow.sourceforge.net
Source0:        http://download.sf.net/%{name}/dvd-slideshow-%{realversion}-%{revision}.tar.gz
Requires:       dvdauthor > 0.6.11
Requires:       ffmpeg > 0.4.8
Requires:       ImageMagick > 5.5.4
Requires:       jhead
Requires:       lame
Requires:       genisoimage
Requires:       sox
Requires:       vorbis-tools
BuildArch:      noarch

%description
dvd-slideshow is a group of Linux commandline programs that create a
slideshow style dvd from groups of pictures. Slideshow videos can be made from
a directory or some online photo albums. You can add fancy effects like fades,
titles, and the Kenburns effect (slowly zooming and panning at the same time)
along with audio to make your slideshows even nicer. There is also a script
which generates a menu for your dvd (dvd-menu).


%prep
%setup -qn %{name}-%{realversion}-%{revision}


# Note there is no building to be done, but this surpresses rpmlint errors and
# allows injection into the build area if required
%build


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

# Install (except dvd-burn as its useless and perhaps dangerous too!)
install -m0644 man/* %{buildroot}%{_mandir}/man1
install -m0755 dvd-slideshow %{buildroot}%{_bindir}
install -m0755 dvd-menu %{buildroot}%{_bindir}
install -m0755 gallery1-to-slideshow %{buildroot}%{_bindir}
install -m0755 jigl2slideshow %{buildroot}%{_bindir}
install -m0755 dir2slideshow %{buildroot}%{_bindir}


%files
%doc doc/*.html TODO.txt dvd-slideshowrc
%license COPYING.txt
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.8.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.8.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.8.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.8.6.1-3
- Require genisoimage as mkisofs virtual provides was removed
- Remove group tag

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.8.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Sérgio Basto <sergio@serjux.com> - 0.8.6.1-1
- Modify version to reflect it on repology.org

* Wed Feb 28 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.8.6-1.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.8.6-1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.8.6-1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 26 2016 Sérgio Basto <sergio@serjux.com> - 0.8.6-1.1
- Update to 0.8.6-1
- Add License tag.
- Fix URL source.
- Fix License.
- Add dvd-slideshowrc to documentation.

* Sun Jun 07 2015 Sérgio Basto <sergio@serjux.com> - 0.8.4-2.1
- Update to dvd-slideshow-0.8.4-2
- Spec clean up.

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-7
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-6
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8.0-4
- rebuild for new F11 features

* Tue Sep 09 2008 Xavier Lamien <lxtnow[at]gmail.com> - 0.8.0-3
- Rebuild for rpmfusion inclusion.

* Mon Apr 30 2007 Ian Chapman <packages@amiga-hardware.com> 0.8.0-2%{?dist}
- Quietened setup (-q)

* Wed Feb 28 2007 Ian Chapman <packages@amiga-hardware.com> 0.8.0-1%{?dist}
- Initial Release
