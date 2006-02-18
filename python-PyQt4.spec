%define		module	PyQt4
%define		_snap	20060216

Summary:	Python bindings for the Qt4 toolkit
Summary(pl):	Dowi±zania do toolkitu Qt4 dla Pythona
Name:		python-%{module}
Version:	4.0
Release:	0.%{_snap}.1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/Downloads/Snapshots/PyQt4/%{module}-gpl-snapshot-%{_snap}.tar.gz
# Source0-md5:	2b4fd9f51f5d16c462c02d4f2cc095ea
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	QtAssistant-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtXml-devel
BuildRequires:	python-sip-devel >= 4.4
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
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
Summary(pl):	Przyklady do PyQt4
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt4.

%description examples -l pl
Przyk³adowy kod demonstruj±cy jak u¿ywaæ PyQt4.

%prep
%setup -q -n %{module}-gpl-snapshot-%{_snap}

%build
export QMAKESPEC="%{_datadir}/qt4/mkspecs/default"
echo 'yes' | python configure.py \
	-c -j 3 \
	-b %{_bindir} \
	-d %{py_sitedir} \
	-q %{_prefix} \
	-v %{_sipfilesdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/PyQt4/*.so*
%{py_sitedir}/PyQt4/*.py[co]
%{py_sitedir}/PyQt4/elementtree
%{py_sitedir}/PyQt4/uic

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python/PyQt4
