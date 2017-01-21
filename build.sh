 dkms remove -m snd-hda-codec-realtek -v 1.1 --all
dkms add -m snd-hda-codec-realtek -v 1.1
dkms build -m snd-hda-codec-realtek -v 1.1
dkms install  -m snd-hda-codec-realtek -v 1.1
