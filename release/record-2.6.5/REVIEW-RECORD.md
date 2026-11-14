# Review record - NPCs Name Distribution Re-NG 2.6.5

**Baseline:** upstream NPCs Names Distributor 2.6.4 (adya/NPCs-Names-Distributor main 2986a40), the version players have. The Nexus archive itself could not be downloaded (nxm-only), so the git commit stands in for it. A build of that commit is not byte-identical to the shipped DLL (1,438,208 vs 1,438,720 bytes, different toolchain run).
**Scope:** 393c176 (6 files) plus the 2.6.5 release commit (version, embedded copyright, README, NOTICE, CHANGES, release folder).
**Author-tested set:** none. The DLL has not been run in game. Verified offline only: it builds; all 18 call-hook signatures and 4 patch sites match SkyrimSE.exe 1.7.104 via the 1.7.104 Address Library (format 5).

| # | Kind | Finding | Answer |
|---|---|---|---|
| 1 | DEFINITE | `vcpkg.json` license MIT on a GPL-3.0 project | fixed (GPL-3.0-only), covered by the author's approved license-metadata fix |
| 2 | DEFINITE | DLL resource `LegalCopyright` said "MIT License" | fixed (GPL-3.0), same defect class as #1, shown to the author in the report |
| 3 | DEFINITE | No credit/third-party notice for a fork of GPL work | added NOTICE.txt; shipped beside the DLL as NPCsNamesDistributor-THIRD-PARTY.txt |
| 4 | DEFINITE | Version still 2.6.4 (indistinguishable from upstream) | 2.6.5; a stale CMake cache kept 2.6.4 until reconfigured, verified in the DLL resource |
| 5 | DEFINITE | Same DLL/DISTR names as the original, so both cannot coexist | stated in README, notes and page text |
| 6 | SUSPECTED | Two vtable hooks (Character 0x41, 0x6A) and runtime behavior untested | author chose to release as is ("commit push and release", after being told it is untested); release notes say not yet play-tested |
| 7 | SUSPECTED | VR build untested | page and README say VR is carried over from upstream and untested |
| P | PRE-EXISTING | Shipped _DISTR matches bare name strings across all plugins; only the reported line was fixed | not blocking |
| P | PRE-EXISTING | C4505 warning for a `static` function in Distributor.h | not blocking |
