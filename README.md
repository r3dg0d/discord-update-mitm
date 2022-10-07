<h1 align="center">
    discord-update-mitm
</h1><h3 align="center">
    A simple Discord MitM attack (proof of concept)
    <br></br>
    Developed by
    <a href="https://github.com/rodriguez-moon">
        Rodriguez Moon
    </a>
    <br/>
    Version 1.0.0
</h2>

### Disclaimer ⚠️
> This project was made for education purposes only and just serves as a proof of concept. I am not responsible for any consequences that may come from use of this program.

Please follow Discord's [Terms of Service](https://dis.gd/tos) and [Community Guidelines](https://dis.gd/guidelines). 
<br/>
Don't run this program on another person's PC without express permission beforehand.

### About ⭐
> As this is only a proof of concept, the implementation is quite simplistic. Serious attackers would likely implement similar concepts in a more complex manner.

Discord is mainly ran through it's `Update.exe` executable (see [Squirrel](https://github.com/Squirrel/Squirrel.Windows)). Located at `%localappdata%\Discord\Update.exe`, it manages opening Discord, as well as updating and uninstalling the client.

An attacker can exploit this fact by replacing the legitimate `Update.exe` file with  a [specially crafted one](./payload/). 

This imposter updater can then run it's own malicious code before sending the commands to the real updater (renamed `Update.bak.exe`).

To add to the facade, I gave the malicious payload identical version information and signed it with a similar certificate to the real one. It's not perfect, but may look legitimate to an unexperienced user.

---

Malicious practices may include:
- Implementing a token grabber to consistently recieve the victim's auth token.
  - Other kinds of credential/data exfiltration are also viable.
- Intercepting `--uninstall` commands to prevent the victim from easily removing the compromised `Update.exe` file.


---
<h5 align="center">
Last updated 2022/10/07

---
