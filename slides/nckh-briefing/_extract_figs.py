"""Extract cited figure pages from local PDFs as PNG for slides."""
from pathlib import Path
import pymupdf

PAPERS = Path(r"d:\Projects\Sun\projects\gene-rna-protein\literature\papers")
OUT = Path(r"d:\Projects\Sun\projects\gene-rna-protein\slides\nckh-briefing\figures")
OUT.mkdir(parents=True, exist_ok=True)

# (pdf, 0-based page, out_stem, cite_caption)
JOBS = [
    ("2022_Haghighi_Rosetta.pdf", None, "haghighi_fig2", "Haghighi et al. 2022, Fig. 2"),
    ("2022_Haghighi_Rosetta.pdf", None, "haghighi_fig4", "Haghighi et al. 2022, Fig. 4"),
    ("2022_Way_Complementary.pdf", None, "way_fig1", "Way et al. 2022, Fig. 1"),
    ("2017_Ando_TVN_Sphering.pdf", None, "ando_fig1", "Ando et al. 2017, Fig. 1"),
    ("2017_Ando_TVN_Sphering.pdf", None, "ando_fig3", "Ando et al. 2017, Fig. 3"),
    ("2024_Arevalo_BatchCorrection.pdf", None, "arevalo_fig1", "Arevalo et al. 2024, Fig. 1"),
]

FIND = {
    "haghighi_fig2": ("2022_Haghighi_Rosetta.pdf", ["Figure 2", "Fig. 2."]),
    "haghighi_fig4": ("2022_Haghighi_Rosetta.pdf", ["Figure 4", "Fig. 4."]),
    "way_fig1": ("2022_Way_Complementary.pdf", ["Figure 1", "Fig. 1."]),
    "ando_fig1": ("2017_Ando_TVN_Sphering.pdf", ["Figure 1", "Fig. 1"]),
    "ando_fig3": ("2017_Ando_TVN_Sphering.pdf", ["Figure 3", "Fig. 3"]),
    "arevalo_fig1": ("2024_Arevalo_BatchCorrection.pdf", ["Figure 1", "Fig. 1"]),
}


def find_page(doc, keys):
    for i, page in enumerate(doc):
        t = page.get_text() or ""
        for k in keys:
            if k in t:
                return i
    return None


def main():
    captions = []
    for stem, (fn, keys) in FIND.items():
        path = PAPERS / fn
        if not path.exists():
            print("MISSING", path)
            continue
        doc = pymupdf.open(path)
        pi = find_page(doc, keys)
        if pi is None:
            print("NOT FOUND", stem, keys)
            continue
        # Prefer page that looks like figure panel (often same page as caption)
        page = doc[pi]
        # High-res render
        mat = pymupdf.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out = OUT / f"{stem}.png"
        pix.save(str(out))
        print(f"OK {stem} <- {fn} p{pi+1} -> {out.name} ({pix.width}x{pix.height})")
        captions.append(f"{stem}: {fn} page {pi+1}")
    (OUT / "CITATIONS.txt").write_text("\n".join(captions), encoding="utf-8")


if __name__ == "__main__":
    main()
