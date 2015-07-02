title: Upgrade to 9.04 Ubuntu from 8.10
link: http://satyaakam.net/?p=78
author: satya
description: 
post_id: 78
created: 2009/05/09 16:58:01
created_gmt: 2009/05/09 11:28:01
comment_status: open
post_name: upgrade-to-904-ubuntu-from-810
status: publish
post_type: post

# Upgrade to 9.04 Ubuntu from 8.10

Resisted the upgrade for long since i got reports of network and sound cards not working properly  with Jaunty , i took the alternative cd route to upgrade. As expected my sound card stopped working  added this line to make it work /etc/modprobe.d/alsa-base.conf options snd-hda-intel model=hp-m4 enable_msi=1 other things looks ok so far .