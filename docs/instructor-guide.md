# Instructor guide

The three labs follow one arc, from a single neuron to behaviour:

1. **Spike Lab**: how a neuron makes a spike.
2. **Relay Lab**: how the spike travels, crosses a synapse and acts on receptors.
3. **Prediction Lab**: what a population of dopamine neurons signals, by replicating a classic
   paper.

They were written for *Introduction to Neuroscience*, a psychology elective at Krea University
(India), taught with Bear, Connors & Paradiso, *Neuroscience: Exploring the Brain*
(Chapters 3–6). They assume no biology beyond school level and no programming.

## Learning objectives

**Spike Lab** (one 90-minute class). Students will be able to:
- explain threshold and the all-or-none spike from their own measurements;
- describe the order of sodium and potassium channel opening, and predict the effect of TTX and TEA;
- explain the absolute and relative refractory periods, and why spikes travel one way;
- explain rate coding: stronger stimuli give more spikes per second, not bigger spikes.

**Relay Lab** (one 90-minute class covering three textbook sessions). Students will be able to:
- explain why myelin, more than thickness, makes conduction fast, and why demyelination slows it;
- put the six steps of chemical transmission in order;
- distinguish spatial and temporal summation, and the role of inhibition;
- contrast ion-channel and G-protein receptors, and classify drugs as agonists, antagonists or
  reuptake blockers.

**Prediction Lab** (a 90-minute open-book assessment). Students will be able to:
- read a raster plot and peri-event histogram;
- state the reward-prediction-error account of dopamine neurons and test it against their own
  replication;
- connect a systems-level finding to spikes, synapses, conduction, receptors and drugs;
- judge what a partial replication failure means for a theory.

## Running a class

**Before class.** Open each lab once on the classroom network. Students need a phone or laptop
with a browser; pairs can share one device. Nothing needs installing, and nothing is recorded,
so there is no student data to manage.

**During class.** The slides mark every lab moment with a coloured *LAB* tag and a QR code.
Students keep the lab open beside the slides and write their numbers in the booklet. In Spike
Lab and Relay Lab each part ends with a short "You are done when…" line, so students know when
to stop; Prediction Lab's question booklet plays that role.

**Pacing passwords.** Relay Lab locks each part until its slide shows a password
(`cheetah`, `chorus`, `keyring`); Prediction Lab has one start password (`juice`), which you can
write on the board when the assessment begins. These stop students racing ahead; they are not
security, since the words are in the page source. Change them in the lab's `index.html`
(`PASSWORDS` or `START_PASSWORD`) and in the matching slide macros. Spike Lab has no passwords.

**Timing.** Each lab part takes about 8 minutes. The slides include planned pauses ("So far"
recaps) and mark optional slides in the speaker notes.

## The assessment format: read, replicate, explain

Prediction Lab and its question booklet show an assessment format that can be reused with other
papers: students **read** a classic paper with a short reading guide, **replicate** its main
findings in a browser lab, then **explain** them, linking the paper back to the course and
judging its limits. The booklet has four sections (A reading, B replicating, C connecting,
D thinking; 40 marks; 90 minutes; open book). Section B numbers vary a little from student to
student because the simulated spikes are random, which discourages copying.

The answer key and marking scheme are not public, so the booklet can be reused. Instructors can
request them from the author (see the contact link in the issue templates).

## Accessibility

The labs and materials were designed to be neurodivergent-friendly:
- one idea per screen, with a bold one-line summary at the top of every slide and lab part;
- numbered steps for every activity, with a "You are done when…" line in Spike Lab and Relay Lab;
- a readable typeface (Atkinson Hyperlegible) and consistent colours for each ion;
- light and dark themes that follow the device; layouts that work at phone width;
- reduced motion respected; sound off by default; keyboard access throughout;
- calm, specific feedback on wrong answers, with a hint rather than a red cross.

## Adapting the labs

- **Your own course.** Session numbers appear in each lab's one-line header (search for
  `class="note"` in its `index.html`) and in the slides and booklets (`materials/`), which are
  LaTeX sources: edit and recompile with `pdflatex` (twice).
- **Links and QR codes.** Each `.tex` file defines `\lablink` near its start; change it and the
  QR codes update themselves.
- **Another textbook.** The labs follow standard content; only the booklet references point to
  Bear et al.
- **Hosting.** The repository is a static website. Fork it and turn on GitHub Pages (Settings →
  Pages → deploy from `main`, root), or copy it to any web server. jsPsych is included in `lib/`,
  so the labs also run offline from a local server; without internet access they fall back to
  system fonts.

## Known limitations

See [`models.md`](models.md) for each simplification. In short: Spike Lab is a cold squid axon;
Relay Lab's EPSPs are larger than real cortical ones and its Part 1 speeds come from rules of
thumb; Prediction Lab's neuron fails to match one result in the original paper, on purpose.
