Summary:	Bitstream Vera ttf fonts
Name:		fonts-ttf-bitstream-vera
Version:	1.10
Release:	23
Group:		Development/X11
License:	Bitstream Vera Fonts Copyright
Url:		http://www.gnome.org/fonts/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/ttf-bitstream-vera-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	pkgconfig(fontutil)
BuildRequires:	pkgconfig(xorg-macros)
Provides:	fonts-ttf-vera
Requires(post,postun):	mkfontdir 
Requires(post,postun):	mkfontscale

%description
Bitstream Vera ttf fonts

%prep
%setup -qn ttf-bitstream-vera-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/
cp -f *.ttf %{buildroot}%{_datadir}/fonts/TTF/

%post
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%postun
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%files
%doc README.TXT COPYRIGHT.TXT RELEASENOTES.TXT
%{_datadir}/fonts/TTF/Vera*.ttf

