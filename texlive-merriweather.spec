# revision 34263
# category Package
# catalog-ctan /fonts/merriweather
# catalog-date 2014-05-30 01:13:36 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-merriweather
Version:	20140530
Release:	2
Summary:	Merriweather and MerriweatherSans fonts, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/merriweather
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/merriweather.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/merriweather.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_5q2vgd.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_cn5sfl.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_fuknsh.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_jnnjab.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_libw2m.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_lnkfbl.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_oaf34p.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_xz5wux.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_ywgpba.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_z4e4wk.enc
%{_texmfdistdir}/fonts/map/dvips/merriweather/Merriweather.map
%{_texmfdistdir}/fonts/map/dvips/merriweather/merriweather.map
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightIt-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightIt-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightIt-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightIt-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightIt-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightIt-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBdIt-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBdIt-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBdIt-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBdIt-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBdIt-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBdIt-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-UltraBold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Bold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-BoldIt.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Italic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Light.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-LightIt.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Regular.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-UltraBdIt.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-UltraBold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Bold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-ExBoldIt.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-ExtraBold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Italic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Light.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-LightItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Regular.ttf
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Bold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-BoldIt.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Italic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Light.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-LightIt.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Regular.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-UltraBdIt.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-UltraBold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-ExBoldIt.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-ExtraBold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Italic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Light.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-LightItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Regular.pfb
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-LightIt-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-LightIt-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-UltraBdIt-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-UltraBdIt-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-UltraBold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-UltraBold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Regular-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/merriweather/LY1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/LY1MerriweatherSans-TLF.fd
%{_texmfdistdir}/tex/latex/merriweather/OT1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/OT1MerriweatherSans-TLF.fd
%{_texmfdistdir}/tex/latex/merriweather/T1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/T1MerriweatherSans-TLF.fd
%{_texmfdistdir}/tex/latex/merriweather/TS1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/TS1MerriweatherSans-TLF.fd
%{_texmfdistdir}/tex/latex/merriweather/merriweather.sty
%doc %{_texmfdistdir}/doc/fonts/merriweather/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/merriweather/README
%doc %{_texmfdistdir}/doc/fonts/merriweather/merriweather-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/merriweather/merriweather-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
