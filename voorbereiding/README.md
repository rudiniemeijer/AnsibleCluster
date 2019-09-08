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
|IP address| MAC address | hostname |
|--|--|--|
|ansible-controller|192.168.1.102|B8-27-EB-4A-6C-EF|

|controller1|192.168.1.106|B8-27-EB-62-DA-E9|
|controller3|192.168.1.107|B8-27-EB-33-6C-8D|
|controller2|192.168.1.104|B8-27-EB-42-00-59|
|controller4|192.168.1.105|B8-27-EB-BB-29-78|

|p11|192.168.1.113|00-22-82-FF-FF-11|
|p12|192.168.1.111|00-22-82-FF-FF-12|
|p13|192.168.1.112|00-22-82-FF-FF-13|
|p14|192.168.1.110|00-22-82-FF-FF-14|

|p21|192.168.1.120|00-22-82-ff-ff-21|
|p22|192.168.1.116|00-22-82-ff-ff-22|
|p23|192.168.1.118|00-22-82-ff-ff-23|
|p24|192.168.1.117|00-22-82-FF-FF-24|

|p31|192.168.1.121|00-22-82-FF-FF-31|
|p32|192.168.1.115|00-22-82-FF-FF-32|
|p33|192.168.1.123|00-22-82-FF-FF-33|
|p34|192.168.1.119|00-22-82-FF-FF-34|

|p41|192.168.1.122|00-22-82-FF-FF-41|
|p42|192.168.1.103|00-22-82-FF-FF-42|
|p43|192.168.1.124|00-22-82-FF-FF-43|
|p44|192.168.1.114|00-22-82-FF-FF-44|