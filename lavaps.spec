Summary:	LavaPS is an interactive process-tracking program
Summary(pl):	LavaPS to interaktywny program pokazuj±cy dzia³aj±ce procesy
Name:		lavaps
Version:	2.7
Release:	1
License:	GPL v2
Group:		Utilities
######		Unknown group!
######		Unknown group!
Source0:	http://www.isi.edu/~johnh/SOFTWARE/LAVAPS/%{name}-%{version}.tar.gz
URL:		http://www.isi.edu/~johnh/SOFTWARE/LAVAPS/
#BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LavaPS is an interactive process-tracking program like top, but with a
much different attitude. Rather than presenting lots of specific info
in digital form, it tries to present certain important information in
a graphical analog form. The idea is that you can run it in the
background and get a rough idea of what's happening to your system
without devoting much concentration to the task.

%description -l pl
LavaPS to interaktywny program pokazuj±cy dzia³aj±ce procesy, w stylu
top'a, ale z ca³kiem innym nastawiniem.

%prep
%setup -q

%build
%configure
make
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
%{_mandir}/man1/%{name}.*
