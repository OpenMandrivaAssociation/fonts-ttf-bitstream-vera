Name: fonts-ttf-bitstream-vera
Version: 1.10
Release: %mkrel 14
Summary: Bitstream Vera ttf fonts
Group: Development/X11
BuildArch: noarch
URL: http://www.gnome.org/fonts/
Source: http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/ttf-bitstream-vera-%{version}.tar.bz2
License: Bitstream Vera Fonts Copyright
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11 <= 6.9.0
Provides: fonts-ttf-vera
Requires(post): mkfontdir mkfontscale
Requires(postun): mkfontdir mkfontscale

%description
Bitstream Vera ttf fonts

%prep
%setup -q -n ttf-bitstream-vera-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/
cp -f *.ttf %{buildroot}%{_datadir}/fonts/TTF/

%post
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%postun
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.TXT COPYRIGHT.TXT RELEASENOTES.TXT
%{_datadir}/fonts/TTF/Vera*.ttf




%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.10-13mdv2011.0
+ Revision: 675411
+ rebuild (emptylog)

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.10-12
+ Revision: 675175
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10-11
+ Revision: 664324
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-10mdv2011.0
+ Revision: 605191
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-9mdv2010.1
+ Revision: 522655
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.10-8mdv2009.1
+ Revision: 351044
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.10-7mdv2009.0
+ Revision: 220860
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.10-6mdv2008.1
+ Revision: 149792
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.10-5mdv2008.0
+ Revision: 64721
- use requires(post(|un)) instead of prereq
- rebuild


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 17:54:04 (47466)
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

