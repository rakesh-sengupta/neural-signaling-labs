# Teaching materials

LaTeX sources with compiled PDFs, licensed CC BY 4.0. Each `.tex` file is self-contained:
compile it with `pdflatex` twice (TeX Live with `beamer`, `tcolorbox`, `pgfplots`, `qrcode`).

| Folder | Files | Use |
|---|---|---|
| `spike-lab/` | slide deck (44 slides), activity booklet (10 pages) | one 90-minute class on the action potential |
| `relay-lab/` | slide deck (40 slides), activity booklet (10 pages) | one 90-minute class on conduction, synapses and receptors |
| `prediction-lab/` | question booklet (10 pages) | a 90-minute open-book assessment |

**Design.** Every content slide has a one-line summary at the top and at most three bullet points.
Each class opens and closes with "today on one page", has a short recap after each section,
and marks lab moments with a coloured tag and a QR code. Booklets give each lab part its own
page with numbered steps; the activity booklets add a word list, study cards with short stories from the history
of neuroscience, answers and sources.

**Adapting.** Each file defines `\lablink` near the top; change it and the QR codes follow.
Relay Lab's slides define the pacing passwords (`\pwone`, `\pwtwo`, `\pwthree`); keep them
in step with `PASSWORDS` in `labs/relay-lab/index.html`. Session numbers are set by
`\sessnum`.

**The quiz answer key** and marking scheme are not published, so the question booklet can be
reused; instructors can request them by email (see CONTRIBUTING.md). The paper the quiz
replicates (Schultz, Dayan & Montague, 1997, *Science*) is not included.

The slides and booklets follow Bear, Connors & Paradiso, *Neuroscience: Exploring the Brain*
(4th ed.), Chapters 3–6, but any introductory textbook will do.
