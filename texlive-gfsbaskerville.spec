%global tl_name gfsbaskerville
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A Greek font, from one such by Baskerville
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsbaskerville
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbaskerville.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbaskerville.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The font is a digital implementation of Baskerville's classic Greek
font, provided by the Greek Font Society. The font covers Greek only,
and LaTeX support provides for the use of LGR encoding.

