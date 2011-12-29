# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-uml
# catalog-date 2007-01-04 21:17:26 +0100
# catalog-license lppl
# catalog-version 0.83
Name:		texlive-pst-uml
Version:	0.83
Release:	1
Summary:	UML diagrams with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-uml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-uml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-uml.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-uml.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-multido

%description
pst-uml is a PSTricks package that provides support for drawing
moderately complex UML (Universal Modelling Language) diagrams.
(The PDF documentation is written in French.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-uml/pst-uml.sty
%doc %{_texmfdistdir}/doc/generic/pst-uml/Changes
%doc %{_texmfdistdir}/doc/generic/pst-uml/README
%doc %{_texmfdistdir}/doc/generic/pst-uml/diagCase.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/diagClass.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/diagClass1.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/diagSeq.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/diagState.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/pst-uml-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-uml/pst-uml-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/pst-uml-encapsuled-pdf-fig.pdf
%doc %{_texmfdistdir}/doc/generic/pst-uml/pst-uml-encapsuled-pdf-fig.tex
%doc %{_texmfdistdir}/doc/generic/pst-uml/pst-uml-exemples.pdf
%doc %{_texmfdistdir}/doc/generic/pst-uml/pst-uml-exemples.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-uml/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
