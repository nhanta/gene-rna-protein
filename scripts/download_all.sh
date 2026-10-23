#!/bin/bash
# Run on HUS: /work/users/minhnth/projects/gene-rna-protein/scripts/download_all.sh
set -uo pipefail

BASE=/work/users/minhnth/projects/gene-rna-protein
LOGDIR="$BASE/logs"
mkdir -p "$LOGDIR" \
  "$BASE/data/raw/rosetta_curated" \
  "$BASE/data/raw/rosetta_preprocessed" \
  "$BASE/data/raw/jump/orf_interpretable" \
  "$BASE/data/raw/jump/crispr_interpretable" \
  "$BASE/data/raw/jump/compound_interpretable" \
  "$BASE/data/raw/arevalo_zenodo" \
  "$BASE/data/processed"

ts() { date -Is; }

run_sync() {
  local name="$1"
  shift
  local logfile="$LOGDIR/${name}.log"
  echo "[$(ts)] START $name" | tee -a "$LOGDIR/download_all.log"
  if "$@" >>"$logfile" 2>&1; then
    echo "[$(ts)] OK $name" | tee -a "$LOGDIR/download_all.log"
    return 0
  else
    local rc=$?
    echo "[$(ts)] FAIL $name (exit $rc) — see $logfile" | tee -a "$LOGDIR/download_all.log"
    return "$rc"
  fi
}

echo "[$(ts)] download_all begin" | tee -a "$LOGDIR/download_all.log"
df -h /work | tee -a "$LOGDIR/download_all.log"

# 1) Rosetta curated (required — DATA.md §1.1)
run_sync rosetta_curated aws s3 sync --no-sign-request \
  s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data \
  "$BASE/data/raw/rosetta_curated"

# 2) Rosetta preprocessed (DATA.md §1.2)
run_sync rosetta_preprocessed aws s3 sync --no-sign-request \
  s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/preprocessed_data \
  "$BASE/data/raw/rosetta_preprocessed"

# 3) JUMP interpretable profiles (no sphering yet — for SV A)
run_sync jump_orf aws s3 cp --no-sign-request \
  s3://cellpainting-gallery/cpg0016-jump-assembled/source_all/workspace/profiles_assembled/ORF/v1.0a/profiles_wellpos_cc_var_mad_outlier.parquet \
  "$BASE/data/raw/jump/orf_interpretable/"

run_sync jump_crispr aws s3 cp --no-sign-request \
  s3://cellpainting-gallery/cpg0016-jump-assembled/source_all/workspace/profiles_assembled/CRISPR/v1.0a/profiles_wellpos_cc_var_mad_outlier.parquet \
  "$BASE/data/raw/jump/crispr_interpretable/"

run_sync jump_compound aws s3 cp --no-sign-request \
  s3://cellpainting-gallery/cpg0016-jump-assembled/source_all/workspace/profiles_assembled/COMPOUND/v1.0/profiles_var_mad_int.parquet \
  "$BASE/data/raw/jump/compound_interpretable/"

# 4) Arevalo Zenodo metadata (best-effort; large files listed in JSON)
{
  cd "$BASE/data/raw/arevalo_zenodo" || exit 1
  curl -fsSL -o zenodo_11644046.json "https://zenodo.org/api/records/11644046" || true
  curl -fsSL -o README.md "https://zenodo.org/records/11644046/files/README.md?download=1" || true
} >>"$LOGDIR/arevalo_zenodo.log" 2>&1
echo "[$(ts)] DONE arevalo_zenodo (metadata)" | tee -a "$LOGDIR/download_all.log"

{
  echo "# inventory — generated $(ts)"
  echo
  echo "## Disk"
  df -h /work | tail -1
  echo
  echo "## Sizes"
  du -sh "$BASE/data/raw"/* 2>/dev/null
  du -sh "$BASE/data/raw/jump"/* 2>/dev/null
  echo
  echo "## Files (sample)"
  find "$BASE/data/raw" -type f | head -200
} > "$BASE/data/inventory.md"

echo "[$(ts)] ALL JOBS FINISHED" | tee -a "$LOGDIR/download_all.log"
