#!/usr/bin/env bash
# Is this clone healthy enough to run?
#
#   ./tools/doctor.sh
#
# Six checks. Exit 0 only if all pass. Every check states what it looked at,
# so a failure tells you where to look rather than just that something is wrong.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ -n "${WORKBUDDY_SKILLS_DIR:-}" ]; then
  DEST="$WORKBUDDY_SKILLS_DIR"
elif [ -n "${HOME:-}" ]; then
  DEST="$HOME/.workbuddy-ai/skills"
else
  echo "ERROR: neither WORKBUDDY_SKILLS_DIR nor HOME is set." >&2
  echo "       Set one, e.g. WORKBUDDY_SKILLS_DIR=\$HOME/.workbuddy-ai/skills" >&2
  exit 2
fi
cd "$REPO_ROOT"

pass=0
fail=0
warn=0

ok()   { printf '  \033[32mPASS\033[0m  %s\n' "$1"; pass=$((pass+1)); }
no()   { printf '  \033[31mFAIL\033[0m  %s\n' "$1"; fail=$((fail+1)); }
meh()  { printf '  \033[33mWARN\033[0m  %s\n' "$1"; warn=$((warn+1)); }
head_() { printf '\n%s\n' "$1"; }

head_ "1. Python"
if command -v python3 >/dev/null 2>&1; then
  ok "python3 $(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])')"
else
  no "python3 not found — tools/check_grounding.py needs it"
fi

head_ "2. Skill contracts present in the clone"
missing=0
for s in edu-orchestrator edu-planner edu-writer edu-reviewer; do
  [ -f "05_Bukti_Proses/skills_package/$s/SKILL.md" ] || { no "missing 05_Bukti_Proses/skills_package/$s/SKILL.md"; missing=1; }
done
[ "$missing" -eq 0 ] && ok "4 of 4 contracts found"

head_ "3. Skills installed for WorkBuddy"
if [ -d "$DEST" ]; then
  n="$(find "$DEST" -maxdepth 1 -type d -name 'edu-*' | wc -l | tr -d ' ')"
  if [ "$n" -eq 4 ]; then
    ok "4 edu-* skills installed in $DEST"
  else
    no "$n of 4 installed in $DEST — run ./tools/install_skills.sh, then restart WorkBuddy"
  fi
else
  no "$DEST does not exist — run ./tools/install_skills.sh"
fi

head_ "4. Knowledge layer"
kmiss=0
for f in 03_Hasil/referensi/rulebook_ipas.md \
         03_Hasil/referensi/cp_ipas.md \
         03_Hasil/referensi/konteks_aktual.md \
         03_Hasil/referensi/source_material_energi.md \
         03_Hasil/referensi/source_material_wujud_zat.md; do
  [ -f "$f" ] || { no "missing $f"; kmiss=1; }
done
[ "$kmiss" -eq 0 ] && ok "rulebook, CP, actual-context register and both source sheets found"

head_ "5. Rulebook copies identical"
if command -v sha256sum >/dev/null 2>&1; then
  sums="$(sha256sum 03_Hasil/referensi/rulebook_ipas.md \
      05_Bukti_Proses/skills_package/edu-orchestrator/assets/rulebook_ipas.md \
      05_Bukti_Proses/skills_package/edu-reviewer/assets/rulebook_ipas.md 2>/dev/null \
      | awk '{print $1}' | sort -u | wc -l | tr -d ' ')"
  if [ "$sums" = "1" ]; then
    ok "3 copies, one checksum ($(sha256sum 03_Hasil/referensi/rulebook_ipas.md | cut -c1-16))"
  else
    no "$sums distinct checksums — the copies have drifted"
  fi
else
  meh "sha256sum not available, skipped"
fi

head_ "6. Grounding check (R001)"
if command -v python3 >/dev/null 2>&1; then
  for run in 03_Hasil/materi_ajar 03_Hasil/edu_output_wujud_zat; do
    out="$(python3 tools/check_grounding.py --run "$run" --knowledge 03_Hasil/referensi --out /tmp/doctor_$$.md 2>&1)"
    if [ $? -eq 0 ]; then
      ok "$run — ${out%%$'\n'*}"
    else
      no "$run — ${out%%$'\n'*}"
    fi
  done
  rm -f "/tmp/doctor_$$.md"
else
  no "skipped, no python3"
fi

printf '\n────────────────────────────────\n'
printf '  %d passed · %d failed · %d warning\n' "$pass" "$fail" "$warn"
printf '────────────────────────────────\n'

if [ "$fail" -gt 0 ]; then
  echo "  Not ready. Fix the FAIL lines above."
  exit 1
fi
echo "  Ready. Start with: README.md → \"Run it yourself\""
exit 0
