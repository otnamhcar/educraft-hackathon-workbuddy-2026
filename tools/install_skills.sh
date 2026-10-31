#!/usr/bin/env bash
# Install the four EduCraft skills into the WorkBuddy skills directory.
#
#   ./tools/install_skills.sh
#
# Override the destination if your WorkBuddy version reads skills from elsewhere:
#   WORKBUDDY_SKILLS_DIR=~/.workbuddy/skills ./tools/install_skills.sh
#
# Nothing is compiled. A skill is a folder containing SKILL.md; "installing" it
# means putting that folder where WorkBuddy looks.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/05_Bukti_Proses/skills_package"
if [ -n "${WORKBUDDY_SKILLS_DIR:-}" ]; then
  DEST="$WORKBUDDY_SKILLS_DIR"
elif [ -n "${HOME:-}" ]; then
  DEST="$HOME/.workbuddy-ai/skills"
else
  echo "ERROR: neither WORKBUDDY_SKILLS_DIR nor HOME is set." >&2
  echo "       Set one, e.g. WORKBUDDY_SKILLS_DIR=\$HOME/.workbuddy-ai/skills" >&2
  exit 2
fi

SKILLS=(edu-orchestrator edu-planner edu-writer edu-reviewer)

echo "Source : $SRC"
echo "Target : $DEST"
echo

for s in "${SKILLS[@]}"; do
  if [ ! -f "$SRC/$s/SKILL.md" ]; then
    echo "ERROR: $SRC/$s/SKILL.md not found." >&2
    echo "       Are you running this from a full clone of the repository?" >&2
    exit 2
  fi
done

mkdir -p "$DEST"

for s in "${SKILLS[@]}"; do
  # Only touch a path that is already an edu-* skill folder. On a fresh install
  # this loop deletes nothing at all.
  if [ -d "${DEST:?}/$s" ]; then
    rm -rf -- "${DEST:?}/$s"
  fi
  cp -r "$SRC/$s" "$DEST/$s"
  echo "  installed  $s"
done

echo
count="$(find "$DEST" -maxdepth 1 -type d -name 'edu-*' | wc -l | tr -d ' ')"
echo "Skills now present: $count (expected 4)"

if [ "$count" -ne 4 ]; then
  echo "ERROR: expected 4 edu-* folders, found $count." >&2
  exit 1
fi

cat <<'EOF'

Done. Two things before it works:
  1. RESTART WorkBuddy — the skill list is read when a session opens.
  2. Confirm in a new chat that `edu-orchestrator` is recognised.

Then check the rest of the clone:
  ./tools/doctor.sh
EOF
