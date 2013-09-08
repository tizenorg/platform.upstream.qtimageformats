Name:       qt5-qtimageformats
Summary:    Qt Imageformats
Version:    5.0.2
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  libmng-devel
Buildrequires:  libtiff-devel  

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Image Formats plugin

%package plugin-mng
Summary:    Qt Imageformats - MNG plugin
Group:      Qt/Qt

%description plugin-mng
This package provides the MNG imageformat plugin


%package plugin-tga
Summary:    Qt Imageformats - TGA plugin
Group:      Qt/Qt

%description plugin-tga
This package provides the TGA imageformat plugin


%package plugin-tiff
Summary:    Qt Imageformats - TIFF plugin
Group:      Qt/Qt

%description plugin-tiff
This package provides the TIFF imageformat plugin


%package plugin-wbmp
Summary:    Qt Imageformats - WBMP plugin
Group:      Qt/Qt

%description plugin-wbmp
This package provides the WBMP imageformat plugin

#### Build section

%prep
%setup -q -n %{name}-%{version}/qtimageformats

%build
export QTDIR=/usr/share/qt5
touch .git # Make sure syncqt is run

qmake -qt=5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files plugin-mng
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqmng.so

%files plugin-tga
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqtga.so

%files plugin-tiff
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqtiff.so

%files plugin-wbmp
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqwbmp.so


#### No changelog section, separate $pkg.changes contains the history

