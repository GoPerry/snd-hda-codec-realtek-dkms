#Perry 2017.2.7

KVERSION:= $(shell uname -r)
CONFIG_SND_HDA_CODEC_REALTEK ?= m
					
######################################
MDIR = kernel/sound/pci/hda/
MOD_NAME = snd-hda-codec-realtek
obj-$(CONFIG_SND_HDA_CODEC_REALTEK) += $(MOD_NAME).o
$(MOD_NAME)-objs += patch_realtek.o


ccflags-y := -I$(src)/include
ccflags-y += -DDBG -DRT3298 -DRTBT_IFACE_PCI -DLINUX

MAKE = make
LINUX_SRC ?= /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(LINUX_SRC) M=$(PWD) modules

clean:
	$(MAKE) -C $(LINUX_SRC) M=$(PWD) clean

install:
	$(MAKE) INSTALL_MOD_PATH=$(DESTDIR) INSTALL_MOD_DIR=$(MDIR) \
		-C $(LINUX_SRC) M=$(PWD) modules_install
	depmod -a
	install -m 0755 -o root -g root  snd-hda-codec-realtek.ko $(DESTDIR)/lib/modules/$(shell uname -r)/kernel/sound/pci/hda/

	
