#!/usr/bin/env bash
# Create a new regression evidence folder with templates.
# Usage: ./new-evidence-folder.sh MMDDYYYY FeatureName
# Example: ./new-evidence-folder.sh 07242026 UniversalEnrollment

set -euo pipefail

DATE="${1:?Usage: $0 MMDDYYYY FeatureName}"
FEATURE="${2:?Usage: $0 MMDDYYYY FeatureName}"

if ! [[ "$DATE" =~ ^[0-9]{8}$ ]]; then
  echo "Error: Date must be MMDDYYYY (8 digits)" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_ROOT="$(dirname "$SCRIPT_DIR")"
EVIDENCE_ROOT="$MODULE_ROOT/evidence/regression-reports"
TARGET_DIR="$EVIDENCE_ROOT/$DATE"
TEMPLATES_DIR="$MODULE_ROOT/templates"

mkdir -p "$EVIDENCE_ROOT"
mkdir -p "$TARGET_DIR"

copy_if_missing() {
  local src="$1" dest="$TARGET_DIR/$2"
  if [[ ! -f "$dest" ]]; then
    cp "$src" "$dest"
    echo "  + $2"
  fi
}

echo "Target: $TARGET_DIR"

copy_if_missing "$TEMPLATES_DIR/BUG_DOCUMENTATION_TEMPLATE.md" "BUG_DOCUMENTATION_TEMPLATE.md"
copy_if_missing "$TEMPLATES_DIR/TRIAGE_DECISION_WORKSHEET.md" "TRIAGE_DECISION_WORKSHEET.md"

if [[ ! -f "$TARGET_DIR/README.md" ]]; then
  sed -e "s/\[MMDDYYYY\]/$DATE/g" -e "s/\[Feature \/ area\]/$FEATURE/g" \
    "$TEMPLATES_DIR/EVIDENCE_FOLDER_README.md" > "$TARGET_DIR/README.md"
  echo "  + README.md (customized)"
fi

if [[ ! -f "$TARGET_DIR/EVIDENCE_CHECKLIST.md" ]]; then
  cat > "$TARGET_DIR/EVIDENCE_CHECKLIST.md" <<EOF
# Evidence Checklist — $DATE — $FEATURE

- [ ] Screenshot(s) saved to this folder
- [ ] Exception log (.txt) saved
- [ ] Test data reference saved
- [ ] CI console log saved (optional)
- [ ] TestNG report URL recorded in README.md
- [ ] Triage completed (see TRIAGE_DECISION_WORKSHEET.md)
- [ ] Bug doc created: ${DATE}_${FEATURE}_[IssueType].md
EOF
  echo "  + EVIDENCE_CHECKLIST.md"
fi

echo ""
echo "Next: add artifacts, then run prompts from automation-bug-lifecycle/prompts/"
echo "Suggested bug doc: ${DATE}_${FEATURE}_[IssueType].md"
