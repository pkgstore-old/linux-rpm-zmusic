%global app                     ZMusic
%global release_prefix          102

Name:                           zmusic
Version:                        1.1.8
Release:                        %{release_prefix}%{?dist}
Summary:                        ZMusic libraries and headers for GZDoom functionality
License:                        GPLv3
URL:                            https://zdoom.org
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source0:                        https://github.com/coelckers/ZMusic/archive/%{app}-%{version}.tar.gz

BuildRoot:                      %{_tmppath}/%{name}-%{version}-build
BuildRequires:                  gcc-c++
BuildRequires:                  make
BuildRequires:                  cmake
BuildRequires:                  tar
BuildRequires:                  git
BuildRequires:                  nasm
BuildRequires:                  glew-devel

# pkgconfig.
BuildRequires:                  pkgconfig(flac)
BuildRequires:                  pkgconfig(bzip2)
BuildRequires:                  pkgconfig(zlib)
BuildRequires:                  pkgconfig(gl)
BuildRequires:                  pkgconfig(fluidsynth)
BuildRequires:                  pkgconfig(gtk+-3.0)
BuildRequires:                  pkgconfig(sdl)
BuildRequires:                  pkgconfig(sdl2)
BuildRequires:                  pkgconfig(sndfile)
BuildRequires:                  pkgconfig(libgme)
BuildRequires:                  pkgconfig(openal)
BuildRequires:                  pkgconfig(libmpg123)

BuildRequires:                  timidity++
BuildRequires:                  pkgconfig(wildmidi)

%description
ZDoom is a family of enhanced ports (modifications) of the Doom engine for
running on modern operating systems. It runs on Windows, Linux, and OS X, and
adds new features not found in the games as originally published by id Software.

This package provides the necessary zmusic libraries necessary for gzdoom to
function.

# -------------------------------------------------------------------------------------------------------------------- #
# Package: devel
# -------------------------------------------------------------------------------------------------------------------- #

%package devel
Summary:                        ZMusic development headers
Requires:                       zmusic = %{version}-%{release}

%description devel
This package contains the development headers required for building against
zmusic, typically for gzdoom installations.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep
%setup -q -n %{app}-%{version}


%build
# Methodology used from zdoom forums.
%{__mkdir} build
cd build
%cmake  -B builddir \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} ..

%{make_build} %{?_smp_mflags} -C builddir


%install
%{__rm} -rf %{buildroot}

cd build
%{make_install} -C builddir


%files
%defattr(-, root, root, -)
%doc licenses/*
%{_libdir}/*


%files devel
%defattr(-, root, root, -)
%{_includedir}/*


%changelog
* Fri Jun 18 2021 Package Store <kitsune.solar@gmail.com> - 1.1.8-102
- UPD: Add "Vendor" & "Packager" fields.

* Fri Jun 18 2021 Package Store <kitsune.solar@gmail.com> - 1.1.8-101
- UPD: New build for latest changes.

* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.1.8-100
- UPD: License.

* Tue May 25 2021 Louis Abel <tucklesepk@gmail.com> - 1.1.8-1
- Fix requirements to use pkgconfig
- Rebase to 1.1.8

* Tue Mar 30 2021 Louis Abel <tucklesepk@gmail.com> - 1.1.6-3
- Rebase to 1.1.6

* Mon Oct 26 2020 Louis Abel <tucklesepk@gmail.com> - 1.1.3-2
- Build for Fedora 33
- Adapt to Fedora macro changes for out-of-source builds
- Fix provides

* Sun Sep 27 2020 Louis Abel <tucklesepk@gmail.com> - 1.1.3-1
- Rebase to 1.1.3
- lib and lib64 installs fixed

* Sun Jun 14 2020 Louis Abel <tucklesepk@gmail.com> - 1.1.0-1
- Initial zmusic build

