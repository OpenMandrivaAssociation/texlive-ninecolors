%global tl_name ninecolors
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2022D
Release:	%{tl_revision}.1
Summary:	Select colors with proper WCAG color contrast
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ninecolors
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ninecolors.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ninecolors.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package carefully selects and defines 9 colors for 13 hues each.
All colors with the same suffix number have equal luminance level. Also
the color black is of level 0, and the color white is of level 10. By
simply choosing two colors in the above list, which differ in level by
at least 5, as foreground and background colors, you will get proper
WCAG Color Contrast.

