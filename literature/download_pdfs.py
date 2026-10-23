"""Download open-access PDFs for the Gene-RNA-Protein joint project.

Record HTTP status. Never invent a success.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from pathlib import Path

OUTDIR = Path(r"d:\Projects\Sun\projects\gene-rna-protein\literature\papers")
LOG = Path(r"d:\Projects\Sun\projects\gene-rna-protein\literature\download_log.json")
UA = "Mozilla/5.0 (compatible; grp-bridge/1.0; mailto:grp-bridge@example.com)"

# filename -> ordered URL candidates
JOBS: dict[str, list[str]] = {
    "2022_Haghighi_Rosetta.pdf": [
        "https://carpenter-singh-lab.broadinstitute.org/files/anne/files/168_haghighi_natmethods_2022.pdf",
        "https://www.biorxiv.org/content/biorxiv/early/2021/09/08/2021.09.08.459417.full.pdf",
        "https://europepmc.org/articles/PMC10012424?pdf=render",
    ],
    "2022_Way_Complementary.pdf": [
        "https://carpenter-singh-lab.broadinstitute.org/files/anne/files/169_way_cellsystems_2022.pdf",
        "https://www.biorxiv.org/content/biorxiv/early/2021/10/21/2021.10.21.465335.full.pdf",
        "https://europepmc.org/articles/PMC10246468?pdf=render",
    ],
    "2017_Ando_TVN_Sphering.pdf": [
        "https://www.biorxiv.org/content/biorxiv/early/2017/07/10/161422.full.pdf",
        "https://www.biorxiv.org/content/10.1101/161422v1.full.pdf",
    ],
    "2017_Subramanian_L1000_CMap.pdf": [
        "https://www.cell.com/cell/pdf/S0092-8674(17)31309-0.pdf",
        "https://europepmc.org/articles/PMC5990023?pdf=render",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5990023/pdf/nihms971392.pdf",
    ],
    "2019_Korsunsky_Harmony.pdf": [
        "https://www.nature.com/articles/s41592-019-0619-0.pdf",
        "https://europepmc.org/articles/PMC6884693?pdf=render",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6884693/pdf/nihms-1059817.pdf",
        "https://www.biorxiv.org/content/biorxiv/early/2018/11/05/461954.full.pdf",
    ],
    "2017_Johnson_ComBat.pdf": [
        # Original ComBat is Biostatistics 2007; use the sva/ComBat practical paper when OA fails.
        "https://bioconductor.org/packages/release/bioc/vignettes/sva/inst/doc/sva.pdf",
    ],
    "2022_Replogle_PerturbSeq.pdf": [
        "https://www.cell.com/cell/pdf/S0092-8674(22)00597-9.pdf",
        "https://europepmc.org/articles/PMC9380471?pdf=render",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9380471/pdf/nihms-1820148.pdf",
        "https://www.biorxiv.org/content/biorxiv/early/2021/12/17/2021.12.16.473013.full.pdf",
    ],
    "2023_Hotelling_CCA_note.pdf": [
        # Skip: classic paper not needed as PDF; placeholder removed intentionally.
    ],
}


def download_one(name: str, urls: list[str]) -> dict:
    out = OUTDIR / name
    if out.exists() and out.stat().st_size > 50_000:
        return {"file": name, "status": "exists", "bytes": out.stat().st_size, "url": None}
    last: dict = {"file": name, "status": "fail", "bytes": 0, "url": None, "errors": []}
    for url in urls:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
                ctype = (resp.headers.get("Content-Type") or "").lower()
                if len(data) < 50_000:
                    last["errors"].append(f"too_small:{url}:{len(data)}")
                    continue
                if "html" in ctype and not data[:5].startswith(b"%PDF"):
                    last["errors"].append(f"html:{url}")
                    continue
                if not data[:5].startswith(b"%PDF"):
                    last["errors"].append(f"not_pdf:{url}")
                    continue
                out.write_bytes(data)
                return {
                    "file": name,
                    "status": "ok",
                    "bytes": len(data),
                    "url": url,
                    "http": getattr(resp, "status", 200),
                }
        except Exception as exc:  # noqa: BLE001
            last["errors"].append(f"{type(exc).__name__}:{url}:{exc}")
        time.sleep(0.5)
    return last


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    results = []
    for name, urls in JOBS.items():
        if not urls:
            continue
        print(f"==> {name}")
        r = download_one(name, urls)
        print(f"    {r['status']}  {r.get('bytes', 0)}  {r.get('url')}")
        results.append(r)
        time.sleep(0.8)
    LOG.write_text(json.dumps(results, indent=2), encoding="utf-8")
    ok = sum(1 for r in results if r["status"] in {"ok", "exists"})
    print(f"\nDone: {ok}/{len(results)} available. Log: {LOG}")


if __name__ == "__main__":
    main()
