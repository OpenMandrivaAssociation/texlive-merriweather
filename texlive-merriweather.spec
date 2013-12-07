# revision 32161
# category Package
# catalog-ctan /fonts/merriweather
# catalog-date 2013-11-14 21:49:40 +0100
# catalog-license ofl
# catalog-version undef
Name:		texlive-merriweather
Version:	20131114
Release:	5
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
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_5n6vkx.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_aynzzm.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_fmhdb5.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_ioeeie.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_oaf34p.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_oehznb.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_oorhm5.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_pyutxj.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_r5mufr.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_rheu2i.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_t226xz.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_v4a7hp.enc
%{_texmfdistdir}/fonts/enc/dvips/merriweather/mwth_z4e4wk.enc
%{_texmfdistdir}/fonts/map/dvips/merriweather/merriweather.map
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Heavy-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-HeavyItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-LightItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/Merriweather-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/sorkin/merriweather/MerriweatherSans-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Bold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Heavy.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-HeavyItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Italic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-Light.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather-LightItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/Merriweather.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Bold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-ExtraBold.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Italic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Light.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-LightItalic.ttf
%{_texmfdistdir}/fonts/truetype/sorkin/merriweather/MerriweatherSans-Regular.ttf
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Bold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Heavy.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-HeavyItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Italic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-Light.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather-LightItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/Merriweather.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-ExtraBold.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-ExtraBoldItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Italic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Light.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-LightItalic.pfb
%{_texmfdistdir}/fonts/type1/sorkin/merriweather/MerriweatherSans-Regular.pfb
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Heavy-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Heavy-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Heavy-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-HeavyItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-HeavyItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-HeavyItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-LightItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-LightItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-LightItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/Merriweather-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-ExtraBold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-LightItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-LightItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/sorkin/merriweather/MerriweatherSans-Regular-osf-ts1.vf
%{_texmfdistdir}/tex/latex/merriweather/LY1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/LY1MerriweatherSans-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/Merriweather.sty
%{_texmfdistdir}/tex/latex/merriweather/OT1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/OT1MerriweatherSans-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/T1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/T1MerriweatherSans-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/TS1Merriweather-OsF.fd
%{_texmfdistdir}/tex/latex/merriweather/TS1MerriweatherSans-OsF.fd
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
