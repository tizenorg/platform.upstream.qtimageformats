# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This file is based on qtimageformats.spec from Mer project
# http://merproject.org

%if "%{tizen}" == "2.3"
%define profile wearable
%else
%define _with_tiff 1
%endif

%bcond_with tiff

Name:       qt5-qtimageformats
Summary:    Qt Imageformats
Version:    5.3.1
Release:    0
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source0:    %{name}-%{version}.tar.bz2
Source1001: %{name}.manifest
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
%if %{with tiff}
Buildrequires:  libtiff-devel
%endif

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Image Formats plugin

%package devel
Summary: Qt imageformats = development files
Group:      Base/Libraries

%description devel
This package provides development files for qtimageformats module

%package plugin-mng
Summary:    Qt Imageformats - MNG plugin
Group:      Base/Libraries

%description plugin-mng
This package provides the MNG imageformat plugin


%package plugin-tga
Summary:    Qt Imageformats - TGA plugin
Group:      Base/Libraries

%description plugin-tga
This package provides the TGA imageformat plugin


%package plugin-tiff
Summary:    Qt Imageformats - TIFF plugin
Group:      Base/Libraries

%description plugin-tiff
This package provides the TIFF imageformat plugin


%package plugin-wbmp
Summary:    Qt Imageformats - WBMP plugin
Group:      Base/Libraries

%description plugin-wbmp
This package provides the WBMP imageformat plugin

%package plugin-dds
Summary:    Qt Imageformats - DDS plugin
Group:      Base/Libraries

%description plugin-dds
This package provides the DDS imageformat plugin

%package plugin-icns
Summary:    Qt Imageformats - ICNS plugin
Group:      Base/Libraries

%description plugin-icns
This package provides the ICNS imageformat plugin

%package plugin-jp2
Summary:    Qt Imageformats - JP2 plugin
Group:      Base/Libraries

%description plugin-jp2
This package provides the JP2 imageformat plugin

%package plugin-webp
Summary:    Qt Imageformats - WEBP plugin
Group:      Base/Libraries

%description plugin-webp
This package provides the WEBP imageformat plugin

#### Build section

%prep
%setup -q -n %{name}-%{version}/qtimageformats
cp %{SOURCE1001} .

%build
export QTDIR=/usr/share/qt5
touch .git # Make sure syncqt is run

qmake -qt=5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/cmake

%files plugin-mng
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqmng.so

%files plugin-tga
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqtga.so

%files plugin-tiff
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqtiff.so

%files plugin-wbmp
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqwbmp.so

%files plugin-dds
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqdds.so

%files plugin-icns
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqicns.so

%files plugin-jp2
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqjp2.so

%files plugin-webp
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/imageformats/libqwebp.so

#### No changelog section, separate $pkg.changes contains the history

