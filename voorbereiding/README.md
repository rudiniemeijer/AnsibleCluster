# Ansible playbooks ClusterHat

## Van schone SD

De inventory heeft het IP van de  controller host

```
ansible-playbook -i inventory pi_controller.yml
```

Als dit klaar is de het vervolg
```
ansible-playbook -i inventory_2 pi_hats.yml
```


# Info

Het script die de netboot images maakt staat alles in:
https://github.com/burtyb/clusterhat-image/blob/master/build/usbboot.sh


De MAC adressen worden bepaald in:
/etc/udev/rules.d/90-clusterhat.rules

/var/lib/clusterhat/nfs/{p1,p2,p3,p4}
mkdir $MNT/var/lib/clusterhat/boot



## switch config

Current Static DHCP Table:
|NO. |IP address| MAC address | hostname |
|--|--|--|--|
|1|192.168.0.100|B8:27:EB:77:F1:7F|controller3|
|2|192.168.0.106|00:22:82:FF:FF:1F|p31|
|3|192.168.0.107|00:22:82:FF:FF:20|p32|
|4|192.168.0.108|00:22:82:FF:FF:21|p33|
|5|192.168.0.109|00:22:82:FF:FF:22|p34|