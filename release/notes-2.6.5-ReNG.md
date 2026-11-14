**NPCs Name Distribution Re-NG 2.6.5** - a maintained fork of NPCs Names Distributor 2.6.4. Drop-in replacement: same DLL name (`NPCsNamesDistributor.dll`), save format, INI, `_DISTR` files, name packs and API. It replaces the original; do not install both.

**FIXED**
- Possible crash on actors that have no ActorBase: the actor's name was read unguarded in log messages on every new NPC and on every save load. Also guarded the race/sex lookup in the default obscurity name and the Name Fixer.
- `NNDNotUnique|Necromancer` matched every NPC named "Necromancer" in any plugin (upstream issue #57). It now targets `ccBGSSSE036_Necromancer` only.
- License metadata (`vcpkg.json` and the copyright field in the DLL) said MIT; the project is GPL-3.0.

**CHECKED**
- All 18 hooked call sites and the 4 in-place patch sites match the Skyrim 1.7.104 executable byte for byte (checked against the 1.7.104 Address Library). Not yet play-tested in game.

Downloads: the main zip is the mod. `NPCsNamesDistributor-2.6.5-pdb.zip` holds debug symbols for crash analysis only.
