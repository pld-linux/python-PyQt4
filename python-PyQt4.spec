#
# Conditional build:
%bcond_without	python2	# CPython 2.x modules
%bcond_without	python3	# CPython 3.x modules

%define		module	PyQt4
# minimal required sip version
%define		sip_ver	2:4.19.12
# last qt version covered by these bindings (minimal required is currently 4.1.0)
%define		qt_ver	4.8.7

Summary:	Python 2 bindings for the Qt4 toolkit
Summary(pl.UTF-8):	Wiązania Pythona 2 do toolkitu Qt4
Name:		python-%{module}
Version:	4.12.3
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyqt/PyQt4_gpl_x11-%{version}.tar.gz
# Source0-md5:	f7b106c39ec16ade9b0f86e570bfe712
Patch0:		%{name}-dbuspath.patch
Patch1:		%{name}-64bit.patch
URL:		https://riverbankcomputing.com/software/pyqt/intro
# most of BR comes from configure.py
BuildRequires:	QtAssistant-compat-devel >= 4.6.3
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
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
%if %{with python2}
BuildRequires:	python-dbus >= 0.80
BuildRequires:	python-sip-devel >= %{sip_ver}
%endif
%if %{with python3}
BuildRequires:	python3-dbus >= 0.80
BuildRequires:	python3-sip-devel >= %{sip_ver}
%endif
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Requires:	python-dbus >= 0.80
Requires:	python-sip >= %{sip_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt4 is a set of Python bindings for the Qt4 toolkit. The bindings
are implemented as a set of Python modules: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns and phonon.

This package contains Python 2 bindings.

%description -l pl.UTF-8
PyQt4 to zbiór wiązań Qt4 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns oraz phonon.

Ten pakiet zawiera wiązania Pythona 2.

%package uic
Summary:	pyuic4 development tool for Python 2
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic4 dla Pythona 2
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description uic
pyuic4 development tool for Python 2.

%description uic -l pl.UTF-8
Narzędzie programistyczne pyuic4 dla Pythona 2.

%package -n python3-PyQt4
Summary:	Python 2 bindings for the Qt4 toolkit
Summary(pl.UTF-8):	Wiązania Pythona 2 do toolkitu Qt4
Group:		Libraries/Python
Requires:	python3-libs
Requires:	python3-dbus >= 0.80
Requires:	python3-sip >= %{sip_ver}

%description -n python3-PyQt4
PyQt4 is a set of Python bindings for the Qt4 toolkit. The bindings
are implemented as a set of Python modules: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns and phonon.

This package contains Python 3 bindings.

%description -n python3-PyQt4 -l pl.UTF-8
PyQt4 to zbiór wiązań Qt4 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns oraz phonon.

Ten pakiet zawiera wiązania Pythona 3.

%package -n python3-PyQt4-uic
Summary:	pyuic4 development tool for Python 3
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic4 dla Pythona 3
Group:		Development/Tools
Requires:	python3-PyQt4 = %{epoch}:%{version}-%{release}

%description -n python3-PyQt4-uic
pyuic4 development tool for Python 3.

%description -n python3-PyQt4-uic -l pl.UTF-8
Narzędzie programistyczne pyuic4 dla Pythona 3.

%package devel-tools
Summary:	PyQt4 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt4
Group:		Development/Tools
Requires:	QtCore >= %{qt_ver}
Requires:	QtXml >= %{qt_ver}

%description devel-tools
PyQt4 development tools: pylupdate4, pyrcc4.

Note: this package doesn't depend on Python version.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne PyQt4: pylupdate4, pyrcc4.

Uwaga: ten pakiet nie jest zależny od wersji Pythona.

%package examples
Summary:	Examples for PyQt4
Summary(pl.UTF-8):	Przykłady do PyQt4
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt4.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt4.

%package -n sip-PyQt4
Summary:	SIP files needed to build other bindings based on Qt4
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania innych wiązań opartych na Qt4
Group:		Development/Languages/Python
Requires:	sip >= %{sip_ver}
Obsoletes:	python-PyQt4-devel < 4.11.3-2

%description -n sip-PyQt4
SIP files needed to build other bindings for C++ classes that inherit
from any of the Qt4 classes (e.g. KDE or your own).

%description -n sip-PyQt4 -l pl.UTF-8
Pliki SIP potrzebne do budowania innych wiązań do klas C++
dziedziczących z dowolnej klasy Qt4 (np. KDE lub własnych).

%package -n QtDesigner-plugin-pyqt4
Summary:	Qt Designer plugin for Python plugins with widgets
Summary(pl.UTF-8):	Wtyczka Qt Designera dla wtyczek Pythona zawierających widgety
# can build only for one python version
%if %{with python2}
Requires:	%{name} = %{epoch}:%{version}-%{release}
%else
Requires:	python3-PyQt4 = %{epoch}:%{version}-%{release}
%endif

%description -n QtDesigner-plugin-pyqt4
This is the Qt Designer plugin that collects all the Python plugins it
can find as a widget collection to Designer.

%description -n QtDesigner-plugin-pyqt4 -l pl.UTF-8
Ten pakiet zawiera wtyczkę Qt Designera zbierającą wszystkie wtyczki
Pythona, które jest w stanie znaleźć, jako zestaw widgetów dla
Designera.

%package -n qscintilla2-%{module}-api
Summary:	PyQt4 API file for QScintilla
Summary(pl.UTF-8):	Plik API PyQt4 dla QScintilli
Group:		Libraries/Python
Requires:	qscintilla2-qt4 >= 2.8.4

%description -n qscintilla2-%{module}-api
PyQt4 API file can be used by the QScintilla editor component to
enable the use of auto-completion and call tips when editing PyQt4
code.

%description -n qscintilla2-%{module}-api -l pl.UTF-8
Plik API PyQt4 może być używany przez komponent edytora QScintilla aby
umożliwić automatyczne dopełnianie i podpowiedzi przy modyfikowaniu
kodu wykorzystującego PyQt4.

%prep
%setup -q -n PyQt4_gpl_x11-%{version}
# small hack to build for shared libs - symbol QT_SHARED not defined anymore?
%{__sed} -i 's/qt_shared = lines\[.*\]/qt_shared = "y"/' configure.py
%{__sed} -i 's/resp = sys.stdin.readline.*/resp = "yes"/' configure.py
%patch0 -p1
%patch1 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' \
      examples/*/*/*/*.py \
      examples/*/*/*.py \
      examples/*/*.py

%build
%if %{with python2}
install -d build-py2
cd build-py2
%{__python} ../configure.py \
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
cd ..
%endif

%if %{with python3}
install -d build-py3
cd build-py3
%{__python3} ../configure.py \
	--confirm-license \
	-c -j 3 \
	-a \
	-b %{_bindir} \
	-d %{py3_sitedir} \
	-q "%{_bindir}/qmake-qt4" \
	-v %{_sipfilesdir}/%{module} \
	--dbus-path="%{py3_sitedir}/dbus/mainloop" \
	LIBDIR_QT="%{_libdir}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with python3}
%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyuic4{,-3}

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%if %{with python2}
%{__make} -C build-py2 install \
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

%{__sed} -i 's,pyuic.py,pyuic.pyc,' $RPM_BUILD_ROOT%{_bindir}/pyuic4
%endif

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README THANKS
%dir %{py_sitedir}/PyQt4
%attr(755,root,root) %{py_sitedir}/PyQt4/Qt.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtAssistant.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtCore.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtDBus.so
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

%files uic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyuic4
%{py_sitedir}/PyQt4/uic
%endif

%if %{with python3}
%files -n python3-PyQt4
%defattr(644,root,root,755)
%doc NEWS README THANKS
%dir %{py3_sitedir}/PyQt4
%attr(755,root,root) %{py3_sitedir}/PyQt4/Qt.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtAssistant.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtCore.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtDBus.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtDeclarative.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtDesigner.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtGui.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtHelp.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtMultimedia.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtNetwork.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtOpenGL.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtScript.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtScriptTools.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtSql.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtSvg.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtTest.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtWebKit.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtXml.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/QtXmlPatterns.so
%attr(755,root,root) %{py3_sitedir}/PyQt4/phonon.so
%{py3_sitedir}/PyQt4/__pycache__
%{py3_sitedir}/PyQt4/__init__.py
%{py3_sitedir}/PyQt4/pyqtconfig.py
%attr(755,root,root) %{py3_sitedir}/dbus/mainloop/qt.so

%files -n python3-PyQt4-uic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyuic4-3
%{py3_sitedir}/PyQt4/uic
%endif

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pylupdate4
%attr(755,root,root) %{_bindir}/pyrcc4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n sip-PyQt4
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files -n QtDesigner-plugin-pyqt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libpyqt4.so

%files -n qscintilla2-%{module}-api
%defattr(644,root,root,755)
%{_datadir}/qt4/qsci/api/python/PyQt4.api
