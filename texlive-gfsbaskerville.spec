%global tl_name gfsbaskerville
%global tl_revision 79618
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A Greek font, from one such by Baskerville
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsbaskerville
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbaskerville.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbaskerville.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The font is a digital implementation of Baskerville's classic Greek
font, provided by the Greek Font Society. The font covers Greek only,
and LaTeX support provides for the use of LGR encoding.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from gfsbaskerville:
Map gfsbaskerville.map
TL_DROPIN_EOF
