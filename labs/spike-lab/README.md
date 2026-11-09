# Spike Lab

A model neuron students can "poke", for Session 9 (*Neural signalling III: the action potential*) of
*Introduction to Neuroscience* (Krea University). Students use it beside the slides, in any web browser.

1. **Find the threshold.** One short push; find the weakest push that fires. Spikes are all-or-none.
2. **Watch the doors, then block them.** Sodium and potassium channels, a sodium blocker (like TTX) and a potassium blocker (like TEA).
3. **Can it fire again straight away?** Two pushes; the refractory period.
4. **Stronger means faster.** A steady push; firing rate rises with stimulus strength (rate coding).

Then a results page (with a line to copy into the booklet) and a free lab.

**Privacy:** nothing is saved or sent. Everything runs in the student's browser tab.

**The model:** Hodgkin & Huxley (1952), squid giant axon at 6.3 °C, resting near −65 mV.
The "potassium blocker" removes 90% of the voltage-opened part of the K⁺ conductance and keeps
the small resting part, so the cell still rests at −65 mV. Because this is a cold squid axon,
refractory periods are longer than in a warm mammalian neuron.

## Running it

Open `index.html` through any web server (for example `python3 -m http.server` from the repository root, then visit `/labs/spike-lab/`), or use the live copy linked from the [main README](../../README.md). It loads jsPsych from `../../lib/`; nothing else is needed.

Teaching materials for this lab are in [`materials/spike-lab/`](../../materials/spike-lab/). Model details and known limitations are in [`docs/models.md`](../../docs/models.md).
