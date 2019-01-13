%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		ktp-approver
Summary:	ktp-approver
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	60d388bf2019cb83c72d5aa21912cae2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.7.0
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Channel Approver for Telepathy.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ktp_approverrc
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_ktp_approver.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Approver.service
%{_datadir}/kservices5/kded/ktp_approver.desktop
%{_datadir}/kservicetypes5/ktp-approver.desktop
