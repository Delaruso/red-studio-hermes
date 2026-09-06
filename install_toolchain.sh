#!/bin/bash
# Red Architecture — Full Professional Toolchain Install
# This script installs everything. It will ask for sudo password interactively.
set -e

echo '=== APT INSTALL ==='
sudo apt-get update -qq
sudo apt-get install -y -qq \
  gimp \
  kdenlive \
  scribus \
  fontforge \
  displaycal \
  argyll \
  ffmpeg \
  imagemagick \
  blender \
  python3-pip \
  python3-dev \
  python3-numpy \
  python3-cairo \
  python3-shapely \
  python3-pillow \
  python3-moviepy \
  python3-moderngl \
  python3-gi \
  gir1.2-gtk-3.0

echo '=== PIP USER INSTALL ==='
pip3 install --user -q \
  py5 \
  generativepy \
  p5 \
  trimesh \
  pycairo \
  shapely \
  pillow \
  moviepy \
  gifsicle \
  moderngl \
  numpy \
  vsketch \
  PyCreative

echo '=== BLENDER ADDONS ==='
BLENDER_ADDONS="$HOME/.config/blender/3.6/scripts/addons"
mkdir -p "$BLENDER_ADDONS"

echo '--- HardOps ---'
if [ ! -d "$BLENDER_ADDONS/HardOps" ]; then
  git clone -q https://github.com/machin3-io/HardOps.git "$BLENDER_ADDONS/HardOps" 2>/dev/null || true
fi

echo '--- BoxCutter ---'
if [ ! -d "$BLENDER_ADDONS/BoxCutter" ]; then
  git clone -q https://github.com/machin3-io/BoxCutter.git "$BLENDER_ADDONS/BoxCutter" 2>/dev/null || true
fi

echo '--- Sverchok ---'
if [ ! -d "$BLENDER_ADDONS/sverchok" ]; then
  git clone -q https://github.com/nortikin/sverchok.git "$BLENDER_ADDONS/sverchok" 2>/dev/null || true
fi

echo '--- Animation Nodes ---'
if [ ! -d "$BLENDER_ADDONS/animation_nodes" ]; then
  git clone -q https://github.com/JacquesLucke/animation_nodes.git "$BLENDER_ADDONS/animation_nodes" 2>/dev/null || true
fi

echo '--- Flip Fluids ---'
if [ ! -d "$BLENDER_ADDONS/flip_fluids" ]; then
  git clone -q https://github.com/rlguy/FlipFluids.git "$BLENDER_ADDONS/flip_fluids" 2>/dev/null || true
fi

echo '=== TYPST ==='
if ! command -v typst >/dev/null 2>&1; then
  curl -fsSL https://typst.app/install.sh | sh || true
fi

echo '=== INKSCAPE EXTENSIONS ==='
mkdir -p "$HOME/.config/inkscape/extensions"
if [ ! -d "$HOME/.config/inkscape/extensions/inkex" ]; then
  git clone -q https://github.com/inkscape/extensions.git "$HOME/.config/inkscape/extensions/inkex" 2>/dev/null || true
fi

echo '=== CLONE DESIGN TOOLING REPOS ==='
mkdir -p "$HOME/red-studio-tools"
cd "$HOME/red-studio-tools"
if [ ! -d beautiful-pdf-mcp ]; then git clone -q https://github.com/Kreminskaya/beautiful-pdf-mcp.git; fi
if [ ! -d koda-stack ]; then git clone -q https://github.com/timkoda/koda-stack.git; fi
if [ ! -d maket ]; then git clone -q https://github.com/ng-galien/maket.git; fi

echo '=== VERIFY ==='
echo '--- Installed binaries ---'
for cmd in gimp kdenlive scribus fontforge displaycal argyll ffmpeg convert typst blender; do
  command -v "$cmd" >/dev/null 2>&1 && echo "OK $cmd" || echo "MISSING $cmd"
done

echo '--- Python packages ---'
python3 -c "import py5, generativepy, trimesh, moderngl, vsketch; print('OK creative stack')" 2>/dev/null || echo 'Some Python packages missing'

echo '--- Blender addons ---'
ls -d "$BLENDER_ADDONS"/* 2>/dev/null | sed 's#.*/##' | grep -E 'HardOps|BoxCutter|sverchok|animation_nodes|flip_fluids' || true

echo '=== DONE ==='
echo 'Next: open Blender > Edit > Preferences > Add-ons > enable HardOps, BoxCutter, Sverchok, Animation Nodes, Flip Fluids'
echo 'Next: run DisplayCAL to profile your monitor'
