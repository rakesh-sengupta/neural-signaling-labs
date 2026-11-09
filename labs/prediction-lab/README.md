# Prediction Lab

A browser lab for replicating the main findings of Schultz, Dayan & Montague (1997),
"A neural substrate of prediction and reward", *Science* 275, 1593–1599. It was written
for Quiz 2 of *Introduction to Neuroscience* (Krea University): students read the paper,
replicate it here, then answer questions in a booklet.

1. **Be the monkey.** A light, then a star one second later. The student presses when the
   star appears. Probe trials withhold the star (trials 14, 19, 23) or show it 0.5 s early
   (16, 21), so students can see their own prediction of *when*.
2. **Record a dopamine neuron.** Rasters and histograms like the paper's Fig. 1: before
   learning, after learning, reward withheld, and reward without the light.
3. **Watch it learn.** Prediction error for each of 80 trials, like Fig. 3, with a withheld
   reward on trial 50, an optional second light, and an optional "receptor blocker".
4. **Test the theory.** A fully trained neuron, with late, early, double and half rewards,
   and a two-light sequence with light 2 left out (the paper's own prediction).

**Privacy:** nothing is saved or sent. Students write their numbers in the booklet.

**Start password:** the lab opens only with a word the teacher announces (for example, written
on the board) when the assessment begins, so nobody starts early. The default is `juice`; change
`START_PASSWORD` near the top of the script in `index.html`. Letter case and spaces are ignored. This is a pacing aid, not security:
anyone who reads the page source can find the word. Once unlocked, the lab stays open in
that browser tab.

## The model (stated in the lab too)

- **Learning:** the temporal-difference (TD) rule of the paper (Eqs. 3–5): each light is
  represented as a chain of signals, one for each 100 ms step after it came on, each with its
  own weight (a "complete serial compound"). Discount factor γ = 0.98 per step; learning
  rate α = 0.3; one weight update per trial. The "receptor blocker" halves the learning rate,
  following the paper's point that animals given dopamine receptor blockers learn more slowly.
- **Spikes:** the prediction error is turned into Poisson spikes. Resting rate 5 spikes/s
  (real dopamine neurons: about 0.5–7 spikes/s). A positive error adds 30 spikes/s per unit
  for 100 ms; a negative error lowers the rate for 200 ms; both start 50 ms after the event.
  These spike settings are choices for display, not fitted to data.
- **Known mismatch:** with this representation, a reward that arrives 0.5 s *early* produces a
  burst *and* a dip at the usual time. The paper's note 18 reports no dip after an early
  reward. This is left in on purpose: the quiz asks students to notice and discuss it.
- Recording (Parts 2 and 4) does not change the weights.

## Running it

Open `index.html` through any web server (for example `python3 -m http.server` from the repository root, then visit `/labs/prediction-lab/`), or use the live copy linked from the [main README](../../README.md). It loads jsPsych from `../../lib/`; nothing else is needed.

Teaching materials for this lab are in [`materials/prediction-lab/`](../../materials/prediction-lab/). Model details and known limitations are in [`docs/models.md`](../../docs/models.md).
