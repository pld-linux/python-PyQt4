# TODO: package /usr/lib/qt4/plugins/designer/* ?

%define		module	PyQt4
%define		sipver  2:4.7.5

Summary:	Python bindings for the Qt4 toolkit
Summary(pl.UTF-8):	Dowiązania do toolkitu Qt4 dla Pythona
Name:		python-%{module}
Version:	4.4.3
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	89e84c36a8520bf8b3a8a2b20e765154
URL:		http://www.riverbankcomputing.com/software/pyqt/
BuildRequires:	QtAssistant-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtXml-devel
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python-sip-devel >= %{sipver}
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
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

%description -l pl.UTF-8
PyQt4 to zbiór dowiązań do Qt4 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: QtAssistant, QtCore, QtGui,
QtNetwork, QtOpenGL, QtSql, QtSvg i QtXml.

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

%prep
%setup -q -n PyQt-x11-gpl-%{version}
%{__sed} -i 's,pyuic.py,pyuic.pyc,' configure.py

%build
echo 'yes' | python configure.py \
	-c -j 3 \
	-b %{_bindir} \
	-d %{py_sitedir} \
	-q "%{_bindir}/qmake-qt4" \
	-v %{_sipfilesdir}/%{module} \
	LIBDIR_QT="%{_libdir}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{py_sitescriptdir}/dbus/mainloop/qt.so
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libpythonplugin.so
%{py_sitedir}/PyQt4/*.py[co]
%{py_sitedir}/PyQt4/uic
%{_datadir}/qt4/qsci/api/python/PyQt4.api

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
