Name:		texlive-merriweather
Version:	64452
Release:	2
Summary:	Merriweather and MerriweatherSans fonts, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/merriweather
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/merriweather.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/merriweather.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Merriweather features a very large x height, slightly condensed
letterforms, a mild diagonal stress, sturdy serifs and open
forms. The Sans family closely harmonizes with the weights and
styles of the serif family. There are four weights and italics
for each.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/merriweather
%{_texmfdistdir}/fonts/map/dvips/merriweather
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather
%{_texmfdistdir}/fonts/opentype/sorkin/merriweather
%{_texmfdistdir}/fonts/type1/sorkin/merriweather
%{_texmfdistdir}/fonts/vf/sorkin/merriweather
%{_texmfdistdir}/tex/latex/merriweather
%doc %{_texmfdistdir}/doc/fonts/merriweather

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
