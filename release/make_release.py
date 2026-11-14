"""Builds the NPCs Name Distribution Re-NG release package + release record.
Usage: python release/make_release.py <version>   (run after a Release build; reads build/Release/NPCsNamesDistributor.dll)
Outputs (release/): '<Title> <version>.zip' (main file), '<dll name>-<version>-pdb.zip' (debug symbols, separate), record-<version>/.
"""
import hashlib, json, os, shutil, sys, zipfile

VER = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "release")
TITLE = "NPCs Name Distribution Re-NG"
DLL = "NPCsNamesDistributor.dll"
build = os.path.join(ROOT, "build", "Release")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


readme = f"""{TITLE} {VER}

A maintained fork of NPCs Names Distributor by sasnikol (adya). Drop-in replacement: same DLL name, same save format, same INI options,
same _DISTR files, same name packs, same API. IT REPLACES THE ORIGINAL - do not install both.

Requirements: SKSE64, Address Library for SKSE Plugins, Spell Perk Item Distributor (SPID) 6+, a names pack.
Optional: SKSE Menu Framework (in-game menu).
Built for Skyrim SE, AE and 1.7.x (one DLL). VR support is carried over from upstream and has not been tested here.

Install with your mod manager and let it overwrite NPCs Names Distributor. Existing saves keep their generated names.

What changed: see CHANGES.txt. Credits and third-party notices: SKSE/Plugins/NPCsNamesDistributor-THIRD-PARTY.txt
Source code: https://github.com/CageTV/NPCs-Names-Distributor
Original mod: https://www.nexusmods.com/skyrimspecialedition/mods/73081
"""

files = {
    "README.txt": readme.replace("\n", "\r\n").encode(),
    "CHANGES.txt": open(os.path.join(ROOT, "CHANGES-Re-NG.md"), "rb").read(),
    "NPCs Names Distributor_DISTR.ini": open(os.path.join(ROOT, "Required Files", "NPCs Names Distributor_DISTR.ini"), "rb").read(),
    "SKSE/Plugins/" + DLL: open(os.path.join(build, DLL), "rb").read(),
    "SKSE/Plugins/NPCsNamesDistributor-LICENSE.txt": open(os.path.join(ROOT, "LICENSE"), "rb").read(),
    "SKSE/Plugins/NPCsNamesDistributor-THIRD-PARTY.txt": open(os.path.join(ROOT, "NOTICE.txt"), "rb").read(),
}
main_zip = os.path.join(OUT, f"{TITLE} {VER}.zip")
if os.path.exists(main_zip):
    os.remove(main_zip)
with zipfile.ZipFile(main_zip, "w", zipfile.ZIP_DEFLATED) as z:
    for name, data in files.items():
        z.writestr(name, data)

pdb_zip = os.path.join(OUT, f"NPCsNamesDistributor-{VER}-pdb.zip")
if os.path.exists(pdb_zip):
    os.remove(pdb_zip)
with zipfile.ZipFile(pdb_zip, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(build, "NPCsNamesDistributor.pdb"), "NPCsNamesDistributor.pdb")

rec = os.path.join(OUT, f"record-{VER}")
shutil.rmtree(rec, ignore_errors=True)
os.makedirs(os.path.join(rec, "sources"))
manifest = [{"path": n, "sha256": hashlib.sha256(d).hexdigest(), "size": len(d), "status": "shipped"} for n, d in files.items()]
json.dump({"version": VER, "package": os.path.basename(main_zip), "package_sha256": sha(main_zip), "files": manifest}, open(os.path.join(rec, "SHIPPED-MANIFEST.json"), "w"), indent=2)
shutil.copyfile(os.path.join(ROOT, "Required Files", "NPCs Names Distributor_DISTR.ini"), os.path.join(rec, "sources", "NPCs Names Distributor_DISTR.ini"))
print(main_zip, os.path.getsize(main_zip), "bytes;", len(files), "files")
print(pdb_zip, os.path.getsize(pdb_zip), "bytes")
