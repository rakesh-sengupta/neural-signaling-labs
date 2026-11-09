# Relay Lab

Three short browser activities for the combined session on axonal conduction and
synapses (Sessions 10–12) of *Introduction to Neuroscience* (Krea University).
Students use it beside the slides.

1. **The race.** How axon diameter and myelin set conduction speed, and what damaged
   myelin (as in multiple sclerosis) does. Two electrodes 10 cm apart, as in a clinical
   nerve conduction test.
2. **Adding up.** The six steps of a chemical synapse (put in order), then spatial and
   temporal summation and inhibition in a model neuron.
3. **Keys and locks.** Ion-channel versus G-protein receptors, and how agonists,
   antagonists and clearance (reuptake/enzyme) blockers change a synaptic response.

**Pacing:** each part opens only with a password that the teacher shows on that part's
lab slide, so a class moves together. Once a part is unlocked it stays unlocked in that
browser tab (so a reload or "Start again" does not lock it again); the free lab at the end
is never locked. To change the passwords, edit `PASSWORDS` near the middle of the script in
`index.html` (search for `var PASSWORDS`) and the matching `\pwone`, `\pwtwo`,
`\pwthree` in the slides. Letter case and spaces are ignored. This is a pacing aid, not
security: anyone who reads the page source can find the words.

**Privacy:** nothing is saved or sent. Everything runs in the student's browser tab.

## The models

- **Part 1** is not a simulation. Speeds follow rules of thumb fitted to real nerves:
  about 6 m/s per µm of diameter for myelinated mammalian axons (Hursh, 1939), and about
  √(diameter in µm) m/s for bare axons (giving ~1 m/s for a 1 µm pain fibre and ~22 m/s
  for a 500 µm squid giant axon). The damaged-myelin patch covers 3 of the 10 cm and
  conducts like a bare axon of the same diameter.
- **Part 2** is a conductance-based leaky integrate-and-fire neuron (membrane time
  constant 15 ms, rest −65 mV, threshold −50 mV). Each excitatory input gives about 7 mV,
  so three are needed together; one input repeated three times fires the neuron if the
  inputs are at most 7 ms apart. Real CNS EPSPs are usually much smaller.
- **Part 3** is a simplified kinetic model in arbitrary units: transmitter clearance,
  receptor binding, and either a direct (ion channel) or a slow, cascade-driven (G-protein)
  response. Antagonist blocks 85% of receptors; clearance blocker slows clearance 8×;
  agonist produces a tonic response of 70% of the normal peak.

## Running it

Open `index.html` through any web server (for example `python3 -m http.server` from the repository root, then visit `/labs/relay-lab/`), or use the live copy linked from the [main README](../../README.md). It loads jsPsych from `../../lib/`; nothing else is needed.

Teaching materials for this lab are in [`materials/relay-lab/`](../../materials/relay-lab/). Model details and known limitations are in [`docs/models.md`](../../docs/models.md).
