# RED ARCHITECTURE — WORKFLOW & COOPERATION PROTOCOL
## Maximum Effectiveness for Empire Mode

---

## 1. COOPERATION MODEL

### WHAT I DO AUTONOMOUSLY
- Write all copy, code, SVG, scripts, specs
- Generate Blender files, audio drones, PDF templates
- Search web for references and best practices
- Create business artifacts, scripts, templates
- Maintain file structure and naming conventions
- Update Obsidian vault with project state

### WHAT REQUIRES YOUR APPROVAL
- Business strategy pivots
- Pricing changes
- Public-facing copy that will be sent to clients
- Final color/material choices for physical artifacts
- Anything involving money or legal exposure

### WHAT WE REVIEW TOGETHER
- Visual direction after first draft
- Story copy after chapter 1 is written
- Physical artifact prototypes before mass production

---

## 2. ASSET PIPELINE (STAGES)

### STAGE 1: BRIEF
You give me a one-line direction. I ask zero questions unless it’s a decision point.

### STAGE 2: GENERATION
I produce the artifact:
- Web: single HTML file with all effects embedded
- 3D: .blend + export script
- Print: SVG template + assembly spec
- Audio: .wav generated from Python
- PDF: HTML template ready for print/PDF conversion
- Business: markdown doc, ready to copy-paste

### STAGE 3: VERIFICATION
I verify:
- File wrote clean
- No broken references
- All dependencies present
- Size/line count reasonable

### STAGE 4: DELIVERY
I give you:
- Exact file path
- What changed
- What’s verified
- What’s left
- One clear next action

### STAGE 5: ITERATION
You say “refine X” or “next Y.” No need to re-explain context unless it changed.

---

## 3. FILE STRUCTURE

```
/home/sky/red studio hermes/
├── AGENTS.md                    # Project rules
├── index.html                   # Live website
├── analytics/
│   ├── docker-compose.yml       # Umami stack
│   └── SETUP.md
├── artifacts/
│   ├── cipher_envelope/
│   │   ├── template.svg
│   │   ├── professional.svg
│   │   ├── design_brief.md
│   │   └── assembly_instructions.md
│   ├── sigils/
│   │   ├── sigil_01_the_signal.svg
│   │   └── ... (12 total)
│   ├── 3d_models/
│   │   ├── generate_relics.py
│   │   └── sovereign_relics.blend
│   ├── fragments/
│   │   ├── fragment_template.html
│   │   └── fragment_01.md
│   ├── relic_packaging/
│   │   ├── relic_box_sigil.svg
│   │   └── relic_box_assembly.md
│   └── audio/
│       ├── generate_drone.py
│       └── 40hz_drone.wav
├── docs/
│   ├── Blueprint.md
│   ├── Upgrade_Plan.md
│   ├── Business_Artifacts.md
│   ├── Story_Art_System.md
│   ├── Toolchain_Upgrade_Plan.md
│   └── Workflow_Protocol.md (this file)
├── outbound/
│   ├── script_email.md
│   ├── cipher_envelope_copy.md
│   └── sovereign_audit_template.md
└── targets/
    └── target_brands.csv
```

---

## 4. NAMING CONVENTIONS

**Files:** `snake_case` for code/scripts, `Title_Case.md` for docs, `kebab-case.html` for web
**Versions:** Never version files with _v2, _final, _new. Overwrite or use dates: `fragment_2026-09-03.md`
**Sigils:** `sigil_NN_name.svg` where NN is zero-padded
**Relics:** `relic_NN_name.blend` where NN is zero-padded
**Fragments:** `fragment_NN_topic.html`

---

## 5. AUTOMATION RULES

### WHAT TO AUTOMATE
- Audio drone generation → `python generate_drone.py`
- Blender relic generation → `blender --background --python generate_relics.py`
- Sigil generation → Python script generating all 12 SVGs
- PDF rendering → `python -m http.server` + headless Chromium print
- Analytics → Umami Docker container
- File verification → checksums after each generation

### WHAT NOT TO AUTOMATE
- Business copy that goes to clients
- Visual design choices
- Pricing or strategy
- Anything requiring human judgment

---

## 6. DAILY CADENCE

### MORNING (YOU)
1. Check `/home/sky/red studio hermes/outbound/` for today’s outreach
2. Review any new artifacts in `/artifacts/`
3. Send one cipher envelope or one email

### DURING DAY (ME WHEN CALLED)
1. Generate next artifact in pipeline
2. Update project docs if strategy changed
3. Research next reference or technique

### EVENING (YOU)
1. Open latest artifact, take screenshot, send me feedback
2. I refine overnight
3. You wake up to upgraded version

---

## 7. COMMUNICATION PROTOCOL

### SHORT INPUTS → FAST OUTPUT
- “next” → produce next artifact in queue
- “refine X” → edit X, no re-explanation
- “open” → open latest files on your PC
- “verify” → run verification checks

### LONG INPUTS → STRUCTURED OUTPUT
If you type more than 2 sentences, I’ll respond with a structured plan before executing.

### ESCALATION
If something is blocked, I say exactly what’s blocked and what I need from you. No guessing, no filler.

---

## 8. QUALITY GATES

### BEFORE ANY ARTIFACT IS SHIPPED
- [ ] File size > 0 bytes
- [ ] No broken internal references
- [ ] Matches naming convention
- [ ] Uses correct palette (#FF0001, #C9A84C, #000)
- [ ] No forbidden words (“secret society”, “subliminal”, etc.)
- [ ] Verified by automated check or manual inspection

### BEFORE CLIENT-FACING COPY IS SENT
- [ ] Read aloud — does it sound like a person or marketing?
- [ ] Forbidden-word check
- [ ] No prices, no URLs, no branding on envelope exterior
- [ ] Reviewed by you

---

## 9. TOOLCHAIN STATUS

### INSTALLED
- Blender 5.2.1 ✓
- Inkscape 1.4.4 ✓
- ImageMagick 7.1.2 ✓
- FFmpeg 8.0.1 ✓
- Node v26.7.0 ✓
- Python 3.14.4 ✓
- Git 2.53.0 ✓

### PENDING
- GIMP, Kdenlive, Scribus, FontForge, DisplayCAL, ArgyllCMS
- Typst
- Python packages: py5, generativepy, p5, trimesh, moderngl, vsketch, PyCreative
- Blender addons: HardOps, BoxCutter, Sverchok, Animation Nodes, Flip Fluids

### ONCE INSTALLED, WE AUTOMATE
- Sigil batch generation
- Blender relic batch rendering
- Audio drone variation generation
- PDF batch compilation from fragments
- Analytics dashboard for site

---

## 10. NEXT ACTIONS (QUEUE)

1. You finish the apt install in your terminal
2. You run the pip + Blender addon + Typst steps
3. You tell me “done”
4. I verify the full toolchain
5. I generate the first upgraded artifact using the new stack
6. You review, say “next” or “refine X”
7. We repeat

---

*This protocol is the operating system for Red Architecture. Every output follows this. No exceptions.*
