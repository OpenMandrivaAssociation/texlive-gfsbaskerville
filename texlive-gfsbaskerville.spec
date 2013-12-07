# revision 19440
# category Package
# catalog-ctan /fonts/greek/gfs/gfsbaskerville
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-gfsbaskerville
Version:	1.0
Release:	5
Summary:	A Greek font, from one such by Baskerville
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsbaskerville
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbaskerville.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbaskerville.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font is a digital implementation of Baskerville's classic
Greek font, provided by the Greek Font Society. The font covers
Greek only, and LaTeX support provides for the use of LGR
encoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfsbaskerville/GFSBaskerville-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsbaskerville/gpgfsbaskerville.enc
%{_texmfdistdir}/fonts/map/dvips/gfsbaskerville/gfsbaskerville.map
%{_texmfdistdir}/fonts/opentype/public/gfsbaskerville/GFSBaskerville.otf
%{_texmfdistdir}/fonts/tfm/public/gfsbaskerville/ggfsbaskervillerg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbaskerville/ggfsbaskervillerg6r.tfm
%{_texmfdistdir}/fonts/type1/public/gfsbaskerville/GFSBaskerville-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsbaskerville/ggfsbaskervillerg6a.vf
%{_texmfdistdir}/tex/latex/gfsbaskerville/gfsbaskerville.sty
%{_texmfdistdir}/tex/latex/gfsbaskerville/lgrgfsbaskerville.fd
%doc %{_texmfdistdir}/doc/fonts/gfsbaskerville/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfsbaskerville/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfsbaskerville/README
%doc %{_texmfdistdir}/doc/fonts/gfsbaskerville/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/gfsbaskerville/gfsbaskerville.pdf
%doc %{_texmfdistdir}/doc/fonts/gfsbaskerville/gfsbaskerville.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752267
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718547
- texlive-gfsbaskerville
- texlive-gfsbaskerville
- texlive-gfsbaskerville
- texlive-gfsbaskerville

