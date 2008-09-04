Name:           dvd-slideshow
Version:        0.8.0
Release:        2%{?dist}
Summary:        Command line programs for creating slideshow style DVDs
Group:          Applications/Multimedia
License:        GPL
URL:            http://dvd-slideshow.sourceforge.net
Source0:        http://dl.sf.net/%{name}/dvd-slideshow-%{version}-1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       dvdauthor > 0.6.11
Requires:       ffmpeg > 0.4.8
Requires:       ImageMagick > 5.5.4
Requires:       jhead
Requires:       lame
Requires:       mkisofs
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
%setup -qn %{name}-%{version}-1


# Note there is no building to be done, but this surpresses rpmlint errors and
# allows injection into the build area if required
%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

# Install (except dvd-burn as its useless and perhaps dangerous too!)
install -m0644 man/* %{buildroot}%{_mandir}/man1
install -m0755 dir2slideshow %{buildroot}%{_bindir}
install -m0755 dvd-menu %{buildroot}%{_bindir}
install -m0755 dvd-slideshow %{buildroot}%{_bindir}
install -m0755 gallery1-to-slideshow %{buildroot}%{_bindir}
install -m0755 jigl2slideshow %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_mandir}/man1/*
%{_bindir}/*
%doc *.html COPYING.txt TODO.txt


%changelog
* Mon Apr 30 2007 Ian Chapman <packages@amiga-hardware.com> 0.8.0-2%{?dist}
- Quietened setup (-q)

* Wed Feb 28 2007 Ian Chapman <packages@amiga-hardware.com> 0.8.0-1%{?dist}
- Initial Release