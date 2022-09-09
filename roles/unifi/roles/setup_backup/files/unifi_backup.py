#!/usr/bin/env python3

import os

os.system('podman pod stop unifi')
os.system('podman run --volumes-from unifi-controller --privileged --rm -v $(pwd):/backup busybox tar czvf /backup/unifi_backup.tar.gz /config')
os.system('podman pod start unifi')
os.system('mv /home/poduser/unifi_backup.tar.gz /mnt/Shared/Backup/Containers/unifi-controller/unifi_backup_$(date +%m-%d).tar.gz')