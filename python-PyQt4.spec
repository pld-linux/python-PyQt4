%define		module	PyQt4
# minimal required sip version
%define		sip_ver	2:4.12.2
# last qt version covered by these bindings (minimal required is currently 4.1.0)
%define		qt_ver	4.7.2

Summary:	Python bindings for the Qt4 toolkit
Summary(pl.UTF-8):	Dowiązania do toolkitu Qt4 dla Pythona
Name:		python-%{module}
Version:	4.8.6
Release:	1
License:	GPL v2 or GPL v3 with FLOSS exception
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	9bfd7b08b8e438b83cc50d5c58191f97
Patch0:		%{name}-dbuspath.patch
Patch1:		%{name}-64bit.patch
URL:		http://www.riverbankcomputing.com/software/pyqt/
# most of BR comes from configure.py
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDeclarative-devel >= %{qt_ver}
BuildRequires:	QtDesigner-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtHelp-devel >= %{qt_ver}
BuildRequires:	QtMultimedia-devel >= %{qt_ver}
BuildRequires:	QtNetwork-devel >= %{qt_ver}
BuildRequires:	QtOpenGL-devel >= %{qt_ver}
BuildRequires:	QtScript-devel >= %{qt_ver}
BuildRequires:	QtScriptTools-devel >= %{qt_ver}
BuildRequires:	QtSql-devel >= %{qt_ver}
BuildRequires:	QtSvg-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	QtWebKit-devel >= %{qt_ver}
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	QtXmlPatterns-devel >= %{qt_ver}
BuildRequires:	phonon-devel
BuildRequires:	pkgconfig
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python-sip-devel >= %{sip_ver}
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-libs
Requires:	python-dbus >= 0.80
Requires:	python-sip >= %{sip_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt4 is a set of Python bindings for the Qt4 toolkit. The bindings
are implemented as a set of Python modules: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns and phonon.

%description -l pl.UTF-8
PyQt4 to zbiór dowiązań do Qt4 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns oraz phonon.

%package devel
Summary:	Files needed to build other bindings based on Qt4
Summary(pl.UTF-8):	Pliki potrzebne do budowania innych dowiązań opartych na Qt4
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt4 classes (e.g. KDE or your own).

%description devel -l pl.UTF-8
Pliki potrzebne do budowania innych dowiązań do klas C++
dziedziczących z dowolnej klasy Qt4 (np. KDE lub własnych).

%package devel-tools
Summary:	PyQt4 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt4
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel-tools
PyQt4 development tools: pylupdate4, pyrcc4, pyuic4.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne PyQt4: pylupdate4, pyrcc4, pyuic4.

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
# small hack to build for shared libs - symbol QT_SHARED not defined anymore?
%{__sed} -i 's/qt_shared = lines\[.*\]/qt_shared = "y"/' configure.py
%{__sed} -i 's/resp = sys.stdin.readline.*/resp = "yes"/' configure.py
%patch0 -p1
%patch1 -p1

%build
%{__python} configure.py \
	--confirm-license \
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

# don't use py_postclean, leave *.py in %{py_sitedir}/PyQt4/uic/widget-plugins
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt4/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt4/uic/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt4/uic/Compiler/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt4/uic/Loader/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt4/uic/port_v2/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt4/uic/port_v3/*.py

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc GPL_EXCEPTION.TXT NEWS OPENSOURCE-NOTICE.TXT README THANKS
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libpythonplugin.so
%dir %{py_sitedir}/PyQt4
%attr(755,root,root) %{py_sitedir}/PyQt4/Qt.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtCore.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtDeclarative.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtDesigner.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtGui.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtHelp.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtMultimedia.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtNetwork.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtOpenGL.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtScript.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtScriptTools.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtSql.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtSvg.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtTest.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtWebKit.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtXml.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtXmlPatterns.so
%attr(755,root,root) %{py_sitedir}/PyQt4/phonon.so
%{py_sitedir}/PyQt4/__init__.py[co]
%{py_sitedir}/PyQt4/pyqtconfig.py[co]
%attr(755,root,root) %{py_sitedir}/dbus/mainloop/qt.so

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pylupdate4
%attr(755,root,root) %{_bindir}/pyrcc4
%attr(755,root,root) %{_bindir}/pyuic4
%{py_sitedir}/PyQt4/uic

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n qscintilla2-%{module}-api
%defattr(644,root,root,755)
%{_datadir}/qt4/qsci/api/python/PyQt4.api
