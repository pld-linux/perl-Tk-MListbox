%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	MListbox
Summary:	Tk::MListbox Perl module - another "column" or "table" widget
Summary(pl):	Modu³ Perla Tk::MListbox - widget "kolumnowy" lub "tabelkowy"
Name:		perl-Tk-MListbox
Version:	1.11
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::MListbox is another "column" or "table" widget. It works much like
a Listbox, but instead of storing each row as a scalar, each row in
the MListbox is a list or an array, each element in the list/array
represents a column in the row. Tk::MListbox lets the user resize the
columns by dragging a separator bar between each column. The user
might change the order of the column by dragging the column headers.
The data in the widget might be sorted by clicking one of the column
headers. A new click, and the sort order is reversed.

%description -l pl
Tk::MListbox to jeszcze jeden widget "kolumnowy" lub "tabelkowy".
Dzia³a podobnie do Listbox, ale zamiast przechowywania ka¿dego wiersza
jako skalaru, ka¿dy wiersz MListbox jest list± lub tablic±, w której
ka¿dy element reprezentuje kolumnê w wierszu. Tk::MListBox pozwala
u¿ytkownikowi zmieniaæ rozmiar kolumn ci±gn±c separator pomiêdzy
kolumnami. U¿ytkownik mo¿e zmieniæ kolejno¶æ kolumn przeci±gaj±c ich
nag³ówki. Dane mog± byæ posortowane przez klikniêcie jednego z
nag³ówków kolumn. Po ponownym klikniêciu kolejno¶æ jest odwracana.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme
%{perl_sitelib}/Tk/MListbox.pm
%{_mandir}/man3/*
