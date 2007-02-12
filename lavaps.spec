Summary:	LavaPS - an interactive process-tracking program
Summary(pl.UTF-8):   LavaPS - interaktywny program pokazujący działające procesy
Name:		lavaps
Version:	2.7
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.isi.edu/~johnh/SOFTWARE/LAVAPS/%{name}-%{version}.tar.gz
# Source0-md5:	cf56a2becae9053130768e4dff5b4a59
URL:		http://www.isi.edu/~johnh/SOFTWARE/LAVAPS/
#BuildRequires:	readline-devel >= 4.2
BuildRequires:	problably-some-gnome-things
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LavaPS is an interactive process-tracking program like top, but with a
much different attitude. Rather than presenting lots of specific info
in digital form, it tries to present certain important information in
a graphical analog form. The idea is that you can run it in the
background and get a rough idea of what's happening to your system
without devoting much concentration to the task.

%description -l pl.UTF-8
LavaPS to interaktywny program pokazujący działające procesy podobnie
do topa, ale z całkiem innym nastawiniem. Zamiast prezentowania dużej
ilości konkretnych informacji w postaci cyfrowej, próbuje przedstawić
pewne ważne informacje w graficznej formie analogowej. Idea jest taka,
że można go uruchomić w tle i mieć pojęcie co dzieje się w systemie
bez poświęcania zbytniej uwagi temu zadaniu.

%prep
%setup -q

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sysconfdir}/gconf/schemas/lavaps.schemas
%{_mandir}/man1/%{name}.1*
