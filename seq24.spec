Name:       seq24
Summary:    Minimalistic, loop-based MIDI sequencer
Version:    0.9.2
Release:    3

Source:     http://edge.launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
Patch0:     seq24-fix-jacksession.patch
URL:        https://edge.launchpad.net/%{name}/
License:    GPLv2+
Group:      Sound
BuildRoot:  %{_tmppath}/%{name}-buildroot

BuildRequires:  libalsa-devel
BuildRequires:  gtkmm2.4-devel
BuildRequires:  jackit-devel

%description
Seq24 is a real-time midi sequencer. It was created to provide a very simple
interface for editing and playing midi 'loops'. After searching for a software
based sequencer that would provide the functionality needed for a live techno
performance, such as the Akai MPC line, the Kawai Q80 sequencer, or the
popular Alesis MMT-8, I found nothing similar in the software realm. I set out
to create a very minimal sequencer that excludes the bloated features of the
large software sequencers, and includes a small subset of features that I have
found usable in performing.

%prep
%setup -q
%patch0 -p0

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp src/pixmaps/%{name}.xpm %{buildroot}%{_datadir}/pixmaps
#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Seq24
Comment=Loop-based MIDI sequencer
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;AudioVideo;Audio;X-MandrivaLinux-Multimedia-Sound;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING RTC SEQ24
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
