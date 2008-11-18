# TODO: 
#  - package /usr/lib/qt4/plugins/designer/* ?
#  - better place for %{py_sitedir}/dbus{,/mainloop} dirs ?

%define		module	PyQt4
%define		sipver  2:4.7.8

Summary:	Python bindings for the Qt4 toolkit
Summary(pl.UTF-8):	Dowiązania do toolkitu Qt4 dla Pythona
Name:		python-%{module}
Version:	4.4.4
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	4bd346d56d10452e47ac71e2cbe04229
Patch0:		%{name}-dbuspath.patch
Patch1:		%{name}-64bit.patch
URL:		http://www.riverbankcomputing.com/software/pyqt/
BuildRequires:	QtAssistant-devel
BuildRequires:	QtDesigner-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtHelp-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	pkgconfig
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python-sip-devel >= %{sipver}
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-phonon-devel
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-libs
Requires:	python-dbus
Requires:	python-sip >= %{sipver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt4 is a set of Python bindings for the Qt4 toolkit. The bindings
are implemented as a set of Python modules: QtAssistant, QtCore,
QtDesigner, QtGui, QtHelp, QtNetwork, QtOpenGL, QtScript, QtSql,
QtSvg, QtTest, QtWebKit, QtXmlPatterns and QtXml.

%description -l pl.UTF-8
PyQt4 to zbiór dowiązań do Qt4 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: QtAssistant, QtCore, QtDesigner,
QtGui, QtHelp, QtNetwork, QtOpenGL, QtScript, QtSql, QtSvg, QtTest,
QtWebKit, QtXmlPatterns i QtXml.

%package devel
Summary:	Files needed to build other bindings based on Qt4
Summary(pl.UTF-8):	Pliki potrzebne do budowania innych dowiązań bazowanych na Qt4
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt4 classes (e.g. KDE or your own).

%description devel -l pl.UTF-8
Pliki potrzebne do budowania innych dowiązań do klas C++
dziedziczących z dowolnej klasy Qt4 (np. KDE lub własnych).

%package examples
Summary:	Examples for PyQt4
Summary(pl.UTF-8):	Przykłady do PyQt4
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt4.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt4.

%package -n qscintilla2-%{module}-api
Summary:	PyQt4 API file for QScintilla
Summary(pl.UTF-8):	Plik API PyQt4 dla QScintilli
Group:		Libraries/Python
Requires:	python-qscintilla2 >= 2.2-2

%description -n qscintilla2-%{module}-api
PyQt4 API file can be used by the QScintilla editor component to
enable the use of auto-completion and call tips when editing PyQt4
code.

%description -n qscintilla2-%{module}-api -l pl.UTF-8
Plik API PyQt4 może być używany przez komponent edytora QScintilla aby
umożliwić automatyczne dopełnianie i podpowiedzi przy modyfikowaniu
kodu wykorzystującego PyQt4.

%prep
%setup -q -n PyQt-x11-gpl-%{version}
%{__sed} -i 's,pyuic.py,pyuic.pyc,' configure.py
%patch0 -p1
%patch1 -p1

%build
echo 'yes' | python configure.py \
	-c -j 3 \
	-a \
	-b %{_bindir} \
	-d %{py_sitedir} \
	-q "%{_bindir}/qmake-qt4" \
	-v %{_sipfilesdir}/%{module} \
	--dbus-path="%{py_sitedir}/dbus/mainloop" \
	LIBDIR_QT="%{_libdir}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libpythonplugin.so
%dir %{py_sitedir}/PyQt4
%attr(755,root,root) %{py_sitedir}/PyQt4/*.so*
%dir %{py_sitedir}/dbus
%dir %{py_sitedir}/dbus/mainloop
%attr(755,root,root) %{py_sitedir}/dbus/mainloop/qt.so
%{py_sitedir}/PyQt4/*.py[co]
%{py_sitedir}/PyQt4/uic

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n qscintilla2-%{module}-api
%defattr(644,root,root,755)
%{_datadir}/qt4/qsci/api/python/PyQt4.api
