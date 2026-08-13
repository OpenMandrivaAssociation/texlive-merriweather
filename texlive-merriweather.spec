%global tl_name merriweather
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Merriweather and MerriweatherSans fonts, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/merriweather
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/merriweather.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/merriweather.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the Merriweather and MerriweatherSans families of
fonts, designed by Eben Sorkin, with support for LaTeX, pdfLaTeX,
XeLaTeX, and LuaLaTeX. Merriweather features a very large x height,
slightly condensed letterforms, a mild diagonal stress, sturdy serifs
and open forms. The Sans family closely harmonizes with the weights and
styles of the serif family. There are four weights and italics for each.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from merriweather:
Map merriweather.map
TL_DROPIN_EOF
