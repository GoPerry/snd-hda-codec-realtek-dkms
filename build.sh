dkms remove  -m alsa-hda-backport  -v 1.3 --all
dkms add -m alsa-hda-backport  -v 1.3
dkms build -m alsa-hda-backport  -v 1.3
#dkms install -m alsa-hda-backport  -v 1.3
