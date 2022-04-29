# 0x0F. Load balancer

## Concepts

For this project, students are expected to look at these concepts:

- [Nginx HTTP Proxying, Load Balancing, Buffering, and Caching](https://www.digitalocean.com/community/tutorials/understanding-nginx-http-proxying-load-balancing-buffering-and-caching)
- [Use HAProxy to Set Up HTTP Load Balancing on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-use-haproxy-to-set-up-http-load-balancing-on-an-ubuntu-vps)

## Background Context

You have been given 2 additional servers:

    gc-[STUDENT_ID]-web-02-XXXXXXXXXX
    gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources

**Read or watch**

- [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

