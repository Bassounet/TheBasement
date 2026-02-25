# CLAUDE.md - Barney's Basement

## Project Overview

**Barney's Basement** is a professional VR demo built in **Unreal Engine 5.3.2** by Sentient Art Studio. It features 150+ props, 15 materials, Lumen/Nanite rendering, and a full VR grab system. The project is under active development.

- **License:** CC BY 4.0
- **Engine:** Unreal Engine 5.3.2
- **Primary Logic:** Blueprints (`.uasset`)
- **Scripting:** Python (automation in `Content/Python/`)

## How to Run

1. Install **Unreal Engine 5.3.2**
2. Open `TheBasement.uproject`
3. The editor opens to `/Game/Basement/MAP_Basement_NoWP`
4. Use **VR Preview** (requires OpenXR headset) or **Play in Editor** for desktop testing

## Project Structure

```
TheBasement/
├── Config/                  # Engine, game, input, editor settings
├── Content/
│   ├── Basement/            # Main level, environment, meshes, materials
│   ├── SA_1/                # Core systems: animations, hands, physics, enums
│   ├── FPP_BP/GENERAL/      # Player blueprint, game instance, grab system, input
│   ├── Cinematics/          # Sequences and rendering assets
│   ├── FMOD/                # Audio banks, events, buses, VCAs
│   ├── GUNS/                # Weapon systems
│   ├── HUD/                 # UI elements
│   ├── FX/                  # Niagara VFX
│   ├── SND/                 # Sound management
│   ├── Python/              # Automation scripts (AssignCamera.py)
│   └── VRTemplate/          # VR template content
├── Plugins/                 # FMOD, DLSS, FSR2, NIS, Streamline, OpenXR, etc.
└── TheBasement.uproject     # Project file
```

## Key Systems

- **VR Grab System:** `Content/SA_1/Demo/Blueprints/GrabComponent_SA.uasset` — hand tracking, physics-based interaction, multiple grab types
- **VR Player Pawn:** `Content/SA_1/Demo/Blueprints/BP_VRPawn_SA.uasset` — locomotion, teleportation
- **Game Instance:** `Content/FPP_BP/GENERAL/BP_GI.uasset`
- **Game Mode:** `Content/SA_1/VRGameMode.uasset`
- **Main Map:** `Content/Basement/MAP_Basement_NoWP.umap`
- **Audio:** FMOD Studio with spatial audio for VR
- **Cinematics:** MovieRenderPipeline, level sequences in `Content/Cinematics/Sequences/`

## Naming Conventions

| Prefix | Meaning              |
|--------|----------------------|
| `BP_`  | Blueprint            |
| `CO_`  | Component Blueprint  |
| `EN_`  | Enumeration          |
| `BPI_` | Blueprint Interface  |
| `M_`   | Material             |
| `MF_`  | Material Function    |
| `NS_`  | Niagara System (VFX) |
| `SM_`  | Static Mesh          |
| `Anim_`| Animation            |
| `BS_`  | Blend Space          |

## Plugins

- **OpenXR** — VR support (Win64, Linux, Android)
- **FMODStudio** — Audio middleware with Niagara integration
- **DLSS / Streamline / NIS** — NVIDIA upscaling & optimization
- **FSR2** — AMD FidelityFX Super Resolution
- **Niagara** — Visual effects
- **MovieRenderPipeline** — Cinematic rendering
- **ConsoleCommandsHelper** — Custom debug plugin

## Rendering & Graphics

- **Lumen** (ray-traced global illumination)
- **Nanite** (virtualized geometry)
- **Virtual Textures** enabled
- **Ray Tracing** enabled
- **MSAA 4x**
- Physics substepping enabled for VR stability

## Git Conventions

- Commit messages in English or French
- Branch naming: `claude/<worktree-name>` for Claude Code branches
- Main branch: `main`

## Important Notes

- This is a **Blueprint-heavy** project — most game logic is in `.uasset` files (not text-editable)
- Text-editable files: `.ini` configs, `.uproject`, Python scripts, README
- Binary `.uasset`/`.umap` files cannot be diffed or edited as text
- When assisting with this project, focus on: config files, Python scripts, project settings, documentation, and git operations
