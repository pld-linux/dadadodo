Summary:	Exterminate All Rational Thought
Summary(pl):	Zniszczyæ Wszystkie Racjonalne My¶li
Name:		dadadodo
Version:	1.04
Release:	3
License:	GPL-like
Group:		Applications/Text
Source0:	http://www.jwz.org/dadadodo/%{name}-%{version}.tar.gz
# Source0-md5:	d3ff69c4e71c328586b1c6ca2130a4b3
Patch0:		%{name}-ctype.patch
URL:		http://www.jwz.org/dadadodo/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DadaDodo is a program that analyses texts for word probabilities, and
then generates random sentences based on that. Sometimes these
sentences are nonsense; but sometimes they cut right through to the
heart of the matter, and reveal hidden meanings.

%description -l pl
DadaDodo jest programem analizuj±cym teksty pod k±tem
prawdopodobieñstwa pojawiania siê s³ów, a nastêpnie generuj±cym losowe
zdania. Czasami te zdania s± bez sensu, lecz zdarza siê, ¿e trafiaj± w
sedno, lub ods³aniaj± ukryte znaczenia.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dadadodo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dodotodo
%attr(755,root,root) %{_bindir}/*
