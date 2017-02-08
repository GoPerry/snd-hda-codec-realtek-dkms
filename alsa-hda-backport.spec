#Perry Yuan 2017.2.6

%{!?kversion: %define kversion %(uname -r)}

#%define kmod_name alsa-hda-backport
%define module snd-hda-codec-realtek
%define module_name snd-hda-codec-realtek
%global dkms_name snd-hda-codec-realtek


Name:		snd-hda-codec-realtek
Version:        1.3
Release:        1%{?dist}
Summary:        Realtek Codec DKMS Driver 

Group:         System Environment/Kernel
License:       GPL
URL:           http://www.dell.com
Source0:       %{name}-%{version}.tar.gz
Source1:       dkms.conf
BuildArch:     x86_64


BuildRequires:  gcc,tar
ExclusiveOS:    linux
Requires:       dkms 
Requires:       gcc, make, perl
Requires:       kernel-devel
Provides:       %{module}-kmod = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}/%{release}-root/

%description
The %{name}  package contains alsa-hda-backport kernel drivers which fix some audio codec bugs.


%prep
rm -rf %{module}-%{version}
#mkdir %{module}-%{version}
%setup -q -n %{module}-%{version}
#cd %{module}-%{version}
#tar xzvf $RPM_SOURCE_DIR/%{module}-%{version}.tar.gz

#mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

#cp -rf %{name}-%{version}  /usr/src/
#cd %{buildroot}/%{_usrsrc}/%{dkms_name}-%{version}/

#%build
#make %{?_smp_mflags}


%install
if [ "$RPM_BUILD_ROOT != /" ];then
	rm -rf $RPM_BUILD_ROOT
fi
#echo "==================\n"
#echo $RPM_BUILD_ROOT
#/root/rpmbuild/BUILDROOT/alsa-hda-backport-1.3-1.el7.x86_64
#echo $RPM_BUILD_DIR

#echo "buildroot --->"
#echo -n %buildroot
#echo "==================\n"

mkdir -p $RPM_BUILD_ROOT/usr/src/%{module}-%{version}/
#install -m 644 $RPM_SOURCE_DIR/%{module}-%{version}/dkms.conf   %{buildroot}/usr/src/%{module}-%{version}/
#install -m 644 $RPM_BUILD_ROOT/%{module}-%{version}/dkms.conf   %{buildroot}/usr/src/%{module}-%{version}/
#install -dm 644 $RPM_BUILD_DIR/%{module}-%{version}/*  %{buildroot}/usr/src/%{module}-%{version}/
cp -rf $RPM_BUILD_DIR/%{module}-%{version}/*  %{buildroot}/usr/src/%{module}-%{version}/
#install -m 644 $RPM_SOURCE_DIR/%{module}-%{version}/alsa-hda-backport_board.bin   %{buildroot}/usr/lib/firmware/alsa-hda-backport/QCA6174/hw3.0/
#cd ${RPM_BUILD_DIR}
#cp -rf %{name}-%{version}/    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
#cp -rf %{name}-%{version}  /usr/src/
#cd %{dkms_name}-%{version}/
#%make_install
#make  DESTDIR=$RPM_BUILD_ROOT install



%clean
#dkms remove  %{dkms_name}/%{version}  --all
if [ "$RPM_BUILD_ROOT != /" ];then
	rm -rf $RPM_BUILD_ROOT
fi

%post
dkms add -m %{module_name} -v %{version}
for kernel in /boot/config-*; do
        KERNEL=${kernel#*-}
        dkms build -m %{module_name} -v %{version} -k ${KERNEL}
        dkms install -m %{module_name} -v %{version} -k ${KERNEL}
        depmod -aq ${KERNEL}
        dracut --host-only --kver $KERNEL -f
done

#dkms build -m %{name} -v %{version}  
echo "installing alsa-hda-backport driver to $KERNEL "
#dkms install -m %{name} -v %{version}

%preun
dkms remove  -m %{name} -v %{version}  --all

%postun 
#rm -rf /usr/src/%{module_name}-%{version}
rm -rf /lib/modules/`uname -r`/extra/$(module).ko
rm -rf /var/lib/dkms/%{module_name}/
rm -rf /usr/src/%{module}-%{version}
depmod -a


%files
%defattr(0755,root,root,-)
%attr(0755,root,root)/usr/src/%{module}-%{version}/*
#%{_usrsrc}/*
#%{_bindir}/*
#%{_libdir}/*

#/usr/src/%{module}-%{version}/

%changelog
* Thu Jan 28 2017 Perry Yuan <perry_yuan@dell.com> [3.10.0-514.el7]
- [alsa-hda-backport] update ALSA AUDIO DKMS driver with BUG Fix [1380571]

