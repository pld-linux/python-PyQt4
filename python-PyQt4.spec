%define		module	PyQt4
%define		sipver  2:4.5.1-1

Summary:	Python bindings for the Qt4 toolkit
Summary(pl):	Dowi±zania do toolkitu Qt4 dla Pythona
Name:		python-%{module}
Version:	4.1.1
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/Downloads/PyQt4/GPL/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	0e7cb6191603cd18f6f4767e1867f7bc
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	QtAssistant-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtTest-devel
BuildRequires:	python-sip-devel >= %{sipver}
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-libs
Requires:	python-sip >= %{sipver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt4 is a set of Python bindings for the Qt4 toolkit. The bindings
are implemented as a set of Python modules: QtAssistant, QtCore,
QtGui, QtNetwork, QtOpenGL, QtSql, QtSvg and QtXml.

%description -l pl
PyQt4 to zbiór dowi±zañ do Qt4 dla Pythona. Dowi±zania zosta³y
zaimplementowane jako modu³y Pythona: QtAssistant, QtCore, QtGui,
QtNetwork, QtOpenGL, QtSql, QtSvg i QtXml.

%package devel
Summary:	Files needed to build other bindings based on Qt4
Summary(pl):	Pliki potrzebne do budowania innych dowi±zañ bazowanych na Qt4
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt4 classes (e.g. KDE or your own).

%description devel -l pl
Pliki potrzebne do budowania innych dowi±zañ do klas C++
dziedzicz±cych z dowolnej klasy Qt4 (np. KDE lub w³asnych).

%package examples
Summary:	Examples for PyQt4
Summary(pl):	Przyk³ady do PyQt4
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt4.

%description examples -l pl
Przyk³adowy kod demonstruj±cy jak u¿ywaæ PyQt4.

%prep
%setup -q -n PyQt-x11-gpl-%{version}
%{__sed} -i 's,pyuic.py,pyuic.pyc,' configure.py

%build
echo 'yes' | python configure.py \
	-c -j 3 \
	-b %{_bindir} \
	-d %{py_sitedir}/%{module} \
	-q "%{_bindir}/qt4-qmake" \
	-v %{_sipfilesdir}/%{module} \
	LIBDIR_QT="%{_libdir}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/PyQt4
%attr(755,root,root) %{py_sitedir}/PyQt4/*.so*
%{py_sitedir}/PyQt4/*.py[co]
%{py_sitedir}/PyQt4/elementtree
%{py_sitedir}/PyQt4/uic

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
