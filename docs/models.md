# What the labs simulate

Each lab is a single HTML file that runs entirely in the browser. This page says what each
model is, where it comes from, how it was simplified for teaching, and which values the
teaching materials rely on. Every value in the "Checked values" tables is confirmed by the
automated tests in [`tests/run_all.py`](../tests/run_all.py).

The guiding rule: **simplify, and say so.** Wherever a lab simplifies, the lab page, its
booklet or its slide notes tell students.

---

## Spike Lab: the action potential

**Model.** The Hodgkin–Huxley (1952) equations for the squid giant axon at 6.3 °C, resting
near −65 mV (rate functions shifted to that rest; gNa = 120, gK = 36, gL = 0.3 mS/cm²;
ENa = +50, EK = −77, EL = −54.4 mV). Forward Euler integration, step 0.01 ms.

**Stimuli.** Strength is a 0–10 classroom scale. Parts 1–3 use 1 ms current pulses
(1.6 µA/cm² per unit); Part 4 uses a 200 ms step (4 + 4.6 × (strength − 1) µA/cm²).

**Blockers.** The sodium blocker (like TTX) removes the sodium conductance. The potassium
blocker (like TEA) removes 90 % of the *voltage-opened* part of the potassium conductance but
keeps its small resting part, so the cell still rests at −65 mV. (Blocking all of it makes the
model fire on its own, which would confuse the lesson.)

**Simplifications to tell students.** A cold squid axon is slower than a warm mammalian
neuron, so its refractory periods are longer; the slides and booklet say so.

| Checked value | Lab value |
|---|---|
| Weakest strength that fires (Part 1) | 4.5 (strength 4 does not) |
| Peak at threshold / at strength 10 | about +37 mV / +41 mV |
| Time above 0 mV, no blocker / potassium blocker | about 1.2 ms / 2.6 ms |
| Sodium blocker | no spike |
| Shortest gap for two spikes, strength 8 / 10 | 13 ms / 12 ms |
| Firing rate at strengths 1, 3, 5, 7, 10 | 5, 80, 90, 105, 115 spikes/s |

---

## Relay Lab: conduction, synapses and receptors

**Part 1, the race, is not a simulation.** Conduction speeds follow rules of thumb fitted to
real nerves: about 6 m/s per µm of diameter for myelinated mammalian axons (Hursh, 1939),
and about √(diameter in µm) m/s for bare axons. Electrodes are 10 cm apart, as in a clinical
nerve-conduction test. The "damaged myelin" patch (as in multiple sclerosis) covers 3 of the
10 cm and conducts like a bare axon of the same diameter. The drawing is not to scale.

**Part 2, adding up,** uses a leaky integrate-and-fire neuron with conductance-based synapses
(membrane time constant 15 ms; rest −65 mV; threshold −50 mV; reset −70 mV; refractory
2 ms; excitatory synapses: weight 0.9, time constant 3 ms, reversal 0 mV; inhibitory:
weight 2.5, 6 ms, −72 mV). The Hodgkin–Huxley neuron of Spike Lab was tried first, but its
summation window was only 2–3 ms, too short to show temporal summation in the 1–15 ms range
the textbook describes. Each excitatory input here gives about 7 mV, much larger than a
typical cortical EPSP; the lab and the slide notes say so.

**Part 3, keys and locks,** is a simplified kinetic model in arbitrary units, scaled so that
"no drug" peaks at 100: transmitter in the cleft decays (clearance), binds receptors, and
drives either a direct ion-channel response or a slow cascade (G-protein) response. The
antagonist blocks 85 % of receptors; the clearance blocker slows clearance eightfold; the
agonist gives a steady response of 70 % of the normal peak. Only the directions of the
effects are meant to be taken literally.

| Checked value | Lab value |
|---|---|
| Speeds: 1 µm bare / 12 µm myelinated / squid 500 µm / 12 µm damaged | 1 / 72 / 22 / 10 m/s |
| Rise from one excitatory input | about 7.2 mV (threshold is 15 mV above rest) |
| Inputs needed together to fire | 3 (A + B + C); adding inhibitory D blocks the spike |
| One input repeated three times | fires at 7 ms gaps, not at 8 ms |
| Ion-channel synapse: none / antagonist / clearance blocker | 100 / 15 / about 210 |
| G-protein synapse (serotonin): none / antagonist / clearance blocker | 100 / 15 / about 290 |

---

## Prediction Lab: replicating Schultz, Dayan & Montague (1997)

**Learning model.** The temporal-difference (TD) rule of the paper (its Eqs. 3–5). Each light
is represented as a chain of signals, one for each 100 ms step after it came on, each with its
own weight (a "complete serial compound"). Prediction V(t) is the weighted sum; the prediction
error is δ(t) = r(t) + γV(t+1) − V(t); weights change by α Σ x(t) δ(t) once per trial.
γ = 0.98 per step, α = 0.3. A trial runs from −1 s to +2 s; the light comes on at 0 s and the
juice at 1.0 s. The "dopamine receptor blocker" halves the learning rate, following the paper's
point that animals given dopamine receptor blockers learn more slowly.

**From prediction error to spikes.** The neuron fires at random (Poisson) at 5 spikes/s at rest,
within the 0.5–7 spikes/s reported for monkey dopamine neurons (Ljungberg, Apicella & Schultz,
1992). A positive error adds 30 spikes/s per unit for 100 ms; a negative error lowers the rate
for 200 ms; both start 50 ms after the event, close to the reported burst latency (Schultz &
Romo, 1990). These display settings are choices, not fits to data. Recordings (Parts 2 and 4)
do not change the weights.

**A deliberate mismatch.** With this representation of time, juice that arrives 0.5 s *early*
produces a burst *and* a pause at the usual time. The paper's note 18 reports that real neurons
showed a pause at the usual time only when the reward was *late*. The mismatch is kept on
purpose: the question booklet asks students to find it and judge what it means for the theory.

| Checked value | Lab value |
|---|---|
| Juice response falls below half (one light) | trial 3 |
| Response moves to the light (biggest response at 0 s) | trial 26 |
| Same, with receptor blocker | trials 6 and 49 |
| Two lights: response ends up at | light 1 (trial 21); light 2 response 0 |
| Rates after training (spikes/s): light / juice / withheld juice | about 17 / 5 / 0 |
| Late juice: at 1.0 s / at 1.5 s | pause (0) / burst (about 20) |
| Early juice: at 0.5 s / at 1.0 s | burst (about 20) / pause (0) |
| Light 2 left out: at 0.5 s / at 1.0 s | dip (about 2.7) / smaller burst (about 12.5) |

Spike counts are random, so recorded rates vary a little from run to run; the trial numbers in
Part 3 are exact.

---

## References

- Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and
  its application to conduction and excitation in nerve. *Journal of Physiology*, 117, 500–544.
- Hursh, J. B. (1939). Conduction velocity and diameter of nerve fibers. *American Journal of
  Physiology*, 127, 131–139.
- Ljungberg, T., Apicella, P., & Schultz, W. (1992). Responses of monkey dopamine neurons
  during learning of behavioral reactions. *Journal of Neurophysiology*, 67, 145–163.
- Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and
  reward. *Science*, 275, 1593–1599.
- Schultz, W., & Romo, R. (1990). Dopamine neurons of the monkey midbrain: contingencies of
  responses to stimuli eliciting immediate behavioral reactions. *Journal of Neurophysiology*,
  63, 607–624.
