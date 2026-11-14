<h1 align="center">
NPCs Name Distribution Re-NG
</h1>

![Splash](https://github.com/adya/NPCs-Names-Distributor/blob/main/images/Splash.png)

A framework that generates and distributes names to any NPCs using SPID. Highly customizable through configuration files. Supports any NPCs from any mods.

**NPCs Name Distribution Re-NG** is a maintained fork of [NPCs Names Distributor](https://github.com/adya/NPCs-Names-Distributor) by sasnikol (adya),
kept up to date for current Skyrim versions (SE, AE and 1.7.x; VR support is carried over from upstream and untested here). It is a drop-in replacement: the DLL is still `NPCsNamesDistributor.dll`,
the save format, INI options, `_DISTR` files, name packs and API are unchanged. **It replaces the original: do not install both.**

See [CHANGES-Re-NG.md](CHANGES-Re-NG.md) for what differs from upstream and the [original Nexus page](https://www.nexusmods.com/skyrimspecialedition/mods/73081)
for the full documentation of name definitions and options.

## Requirements
- SKSE64 and Address Library for SKSE Plugins
- Spell Perk Item Distributor (SPID) 6 or newer
- A names pack (name definition files)
- SKSE Menu Framework (optional, for the in-game menu)

## License
GPL-3.0, see [LICENSE](LICENSE). Credits and third-party notices: [NOTICE.txt](NOTICE.txt).
