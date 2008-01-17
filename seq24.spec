%define name	seq24
%define version 0.8.7
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Minimalistic, loop-based MIDI sequencer
Version: 	%{version}
Release: 	%{release}

Source:		http://www.filter24.org/seq24/%{name}-%{version}.tar.gz
URL:		http://www.filter24.org/seq24/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
#BuildRequires:	libgtkmm-devel 
BuildRequires:  libalsa-devel
BuildRequires:  gtkmm2.4-devel

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

%build
%configure2_5x
perl -pi -e "s#LASH_LIBS = -Wl,--rpath -Wl,/usr/lib#LASH_LIBS = #" src/Makefile

%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Seq24
Comment=Loop-based MIDI sequencer
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;AudioVideo;Audio;X-MandrivaLinux-Multimedia-Sound;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING RTC SEQ24
%{_bindir}/%name
%{_bindir}/dump
%{_datadir}/applications/mandriva-%{name}.desktop
