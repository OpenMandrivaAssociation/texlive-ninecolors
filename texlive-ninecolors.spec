Name:		texlive-ninecolors
Version:	62006
Release:	2
Summary:	Select colors with proper WCAG color contrast
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ninecolors
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ninecolors.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ninecolors.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package carefully selects and defines 9 colors for 13 hues
each. All colors with the same suffix number have equal
luminance level. Also the color black is of level 0, and the
color white is of level 10. By simply choosing two colors in
the above list, which differ in level by at least 5, as
foreground and background colors, you will get proper WCAG
Color Contrast.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ninecolors
%doc %{_texmfdistdir}/doc/latex/ninecolors

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
