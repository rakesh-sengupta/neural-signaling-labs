# Neural Signalling Labs

[![tests](https://github.com/rakesh-sengupta/neural-signalling-labs/actions/workflows/tests.yml/badge.svg)](https://github.com/rakesh-sengupta/neural-signalling-labs/actions/workflows/tests.yml)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

Three browser labs, with student booklets and slides, for teaching how neurons signal to
psychology students. Students change a model neuron, measure what happens and replicate
classic findings, on a phone or laptop, with nothing to install and nothing saved.

**Try them:** https://rakesh-sengupta.github.io/neural-signalling-labs/

| Lab | Topic | Parts | Materials |
|---|---|---|---|
| [**Spike Lab**](https://rakesh-sengupta.github.io/neural-signalling-labs/labs/spike-lab/) | The action potential (Hodgkin–Huxley model) | threshold and all-or-none · sodium and potassium channels, TTX and TEA · refractory period · rate coding | [slides](materials/spike-lab/session09-action-potential-slides.pdf), [booklet](materials/spike-lab/session09-activity-booklet.pdf) |
| [**Relay Lab**](https://rakesh-sengupta.github.io/neural-signalling-labs/labs/relay-lab/) | Conduction, synapses, receptors | myelin and conduction speed, multiple sclerosis · the steps of a chemical synapse, summation and inhibition · agonists, antagonists, reuptake blockers | [slides](materials/relay-lab/sessions10-12-relay-slides.pdf), [booklet](materials/relay-lab/sessions10-12-activity-booklet.pdf) |
| [**Prediction Lab**](https://rakesh-sengupta.github.io/neural-signalling-labs/labs/prediction-lab/) | Replicating Schultz, Dayan & Montague (1997) | be the monkey · record a dopamine neuron (Fig. 1) · watch prediction errors move (Fig. 3) · test the theory | [question booklet](materials/prediction-lab/quiz2-question-booklet.pdf) |

## Why these labs

- **For psychology students.** Each lab starts from a question a psychologist would ask
  (how does a neuron say "stronger"? why do some messages arrive late? what does dopamine
  report?) and keeps the biology to what answers it.
- **Measure, don't watch.** Every part asks students to predict, measure and record, with
  instant feedback in the two teaching labs.
- **Honest models.** Each lab says where it simplifies; Prediction Lab even keeps a result
  where the 1997 model does not match the data, for students to find. See
  [docs/models.md](docs/models.md).
- **Neurodivergent-friendly.** One idea per screen, numbered steps, a readable typeface,
  light and dark themes, reduced motion, sound off by default.
- **Assessment by replication.** Prediction Lab and its booklet form an open-book exam:
  read a paper, replicate it, explain it.

## For instructors

Start with the [instructor guide](docs/instructor-guide.md): learning objectives, timings,
pacing passwords, the assessment format and how to adapt everything to your course. The
slides and booklets are LaTeX sources in [`materials/`](materials/) with compiled PDFs
alongside.

## Running locally

The repository is a static website; there is nothing to build.

```bash
git clone https://github.com/rakesh-sengupta/neural-signalling-labs.git
cd neural-signalling-labs
python3 -m http.server 8000
# open http://localhost:8000/
```

Dependencies: [jsPsych](https://www.jspsych.org/) 7.3.4 and its html-button-response plugin
1.2.0 are included in [`lib/`](lib/) (MIT licence), so the labs run offline. Fonts load from
Google Fonts when online and fall back to system fonts otherwise. Any current browser works,
including on phones.

To rebuild a booklet or slide deck: `pdflatex file.tex` twice (TeX Live with `beamer`,
`tcolorbox`, `pgfplots` and `qrcode`).

## Tests

[`tests/run_all.py`](tests/run_all.py) serves the site, opens each lab in headless Chromium
at laptop and phone sizes, works through every part as a student would, and checks the
numbers the teaching materials depend on (thresholds, conduction speeds, summation, drug
effects, learning curves). It runs on every push via GitHub Actions.

```bash
pip install -r tests/requirements.txt
python -m playwright install chromium
python tests/run_all.py          # about 4 minutes
python tests/run_all.py --quick  # skips one 90-second real-time task
```

## Contributing and support

Bug reports, teaching reports and suggestions are welcome; see
[CONTRIBUTING.md](CONTRIBUTING.md). Please follow the [code of conduct](CODE_OF_CONDUCT.md).

## Paper

A description of the module, its design, models and validation is in
[`paper/preprint/`](paper/preprint/) (preprint on EdArXiv: link to follow).

## Licence and citation

Code is under the [MIT licence](LICENSE); booklets, slides, documentation and figures are
under [CC BY 4.0](LICENSE-CONTENT.md). If you use the labs, please cite them using
[CITATION.cff](CITATION.cff).

Rakesh Sengupta, School of Interwoven Arts and Sciences, Krea University, India.
