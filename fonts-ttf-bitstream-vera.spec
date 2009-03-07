Name: fonts-ttf-bitstream-vera
Version: 1.10
Release: %mkrel 8
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


