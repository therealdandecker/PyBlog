Title: Wireguard + Active Directory
Date: 2020-10-25 21:40
Tags: Security, VPN
Category: SSO
Author: Dan

I wanted to start writing a little more again, primarily because there have been a lot of issues I have worked through recently in the HomeLab.

One of the more recent ones that seemed initially very difficult but was a pretty easy resolution came down to using Wireguard with Active Directory.  Full disclosure - this is NOT a write up on using LDAP authentication with Wireguard and AD (I do not think that has been solved yet.)  This is more about the DNS resolution and getting things working together.

If you have not used [Wireguard](https://www.wireguard.com/) you can read up on it here. Wireguard is more performant than any other VPN I have used, including OpenVPN which is probably the next best solution and works much more favorably with AD.

The solution I opted for was a very simple one - Wireguard is configured for a split tunnel with my DNS resolver set to Wireguard + PiHole as the primary with the AD DNS as the secondary.  Setting up the split tunnel in Windows is crazy simple - you just uncheck a box and add your DNS to your config file. 

