Upgrade to 9.04 Ubuntu from 8.10
################################
:date: 2009-05-09 16:58
:author: satya
:category: Ubuntu
:tags: Ubuntu
:slug: upgrade-to-904-ubuntu-from-810
:status: published

Resisted the upgrade for long since i got reports of network and sound
cards not working properly  with Jaunty , i took the alternative cd
route to upgrade. As expected my sound card stopped working  added this
line to make it work

/etc/modprobe.d/alsa-base.conf

options snd-hda-intel model=hp-m4 enable\_msi=1

other things looks ok so far .
