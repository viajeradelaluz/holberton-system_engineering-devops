# 0x13. Firewall

![](https://i.ibb.co/VLqDV5s/2-secured-and-monitored-web-infrastructure.jpg)

## Resources

**Read or watch**

- [How To Setup a Firewall with UFW on an Ubuntu and Debian Cloud Server](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)
- [UFW Essentials: Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
- [[Basic] "Forward" a port with UFW](https://help.skysilk.com/support/solutions/articles/9000182486--basic-forward-a-port-with-ufw-in-ubuntu-18-04-linux)
- -[IP Masquerading](https://linuxize.com/post/how-to-setup-a-firewall-with-ufw-on-ubuntu-20-04/)
## Tasks

### **0. Block all incoming traffic but**

Let’s install the `ufw` firewall and setup a few rules on `web-01`.

Requirements:

- The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
- Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    - `22` (SSH)
    - `443` (HTTPS SSL)
    - `80` (HTTP)
- Share the `ufw` commands that you used in your answer file

### **1. Port forwarding**

Firewalls can not only filter requests, they can also forward them.

Requirements

- Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
- Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen
