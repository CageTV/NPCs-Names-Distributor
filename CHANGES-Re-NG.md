# NPCs Name Distribution Re-NG - changes over upstream 2.6.4

Fork of [adya/NPCs-Names-Distributor](https://github.com/adya/NPCs-Names-Distributor) (GPL-3.0). Drop-in replacement: same DLL name
(`NPCsNamesDistributor.dll`), same API, same save record format, same INI and `_DISTR` files.

The FlayaN "NG" fork (2024, conversion to CommonLibSSE-NG) is not merged: upstream has since done its own NG migration and added
Skyrim 1.7.x and VR support, so that fork is behind it.

## Fixes
- **Possible crash on actors without an ActorBase.** `Distributor.cpp` (7 sites) and `Persistency.cpp` dereferenced `GetActorBase()` in log
  arguments, which are evaluated whatever the log level is, on every new actor and on every save load. Replaced with a null-safe `SafeBaseName()`.
  Also guarded `GetRace()` / `GetActorBase()` in the default obscurity name and in the Name Fixer.
- **`NNDNotUnique|Necromancer` false positives** (upstream issue #57). The bare string matched every NPC named "Necromancer" and any NPC
  carrying a keyword of that name. It is now `NNDNotUnique||ccBGSSSE036_Necromancer` (EditorID in the Form filter).
- `vcpkg.json` declared `MIT` while the project is GPL-3.0; corrected to `GPL-3.0-only`.

## Checked, no change needed
- Upstream issue #40 (empty `sFormat`) is already handled in `Options.cpp`.
- All 18 call-site hooks and the 4 in-place patch sites were verified against the Skyrim SE 1.7.104 executable using the 1.7.104 Address
  Library (format 5): every byte signature matches at the computed address, and the patched instructions hold the expected original bytes.
  The two vtable hooks (Character slots 0x41 and 0x6A) were not checked statically.
- Trampoline reservation (14 bytes x 18) matches the 18 call hooks installed.
