---
title: 'Neural Signalling Labs: browser simulations and replication-based assessment for teaching neural signalling to psychology students'
tags:
  - neuroscience education
  - action potential
  - synaptic transmission
  - reward prediction error
  - jsPsych
  - JavaScript
authors:
  - name: Rakesh Sengupta
    orcid: 0000-0003-1768-0551
    affiliation: 1
affiliations:
  - name: School of Interwoven Arts and Sciences, Krea University, Sri City, Andhra Pradesh, India
    index: 1
date: 9 November 2026
bibliography: paper.bib
---

# Summary

*Neural Signalling Labs* is a learning module of three browser labs, with student booklets
and slide decks, for the part of an introductory neuroscience course that runs from the
action potential to neurotransmitters. Students change a model neuron, measure what happens
and write their numbers in a booklet, on a phone or laptop, with nothing to install and nothing
recorded.

- **Spike Lab** runs the Hodgkin–Huxley model of the squid giant axon [@hodgkin1952].
  Students find the threshold, block sodium and potassium channels, measure the refractory
  period and discover rate coding.
- **Relay Lab** races spikes along bare and myelinated axons using measured rules of thumb
  [@hursh1939], asks students to assemble the steps of a chemical synapse and add up
  inputs in an integrate-and-fire neuron, and lets them apply agonists, antagonists and
  reuptake blockers to ion-channel and G-protein synapses.
- **Prediction Lab** asks students to replicate a classic paper, @schultz1997, on dopamine
  neurons and reward prediction error. Students first do a cue–reward timing task
  themselves, then record a model dopamine neuron driven by the paper's temporal-difference
  rule [@sutton1981] before and after learning, regenerate its two main figures, and test
  the theory's predictions, including one where the 1997 model disagrees with the data
  reported in the paper.

The labs are single HTML files built on jsPsych [@deleeuw2015; @deleeuw2023] and served as a
static website (\autoref{fig:labs}). Code is MIT-licensed; booklets, slides and documentation
are CC BY 4.0 LaTeX sources with compiled PDFs.

![Four views from the labs. (A) Spike Lab: voltage, and sodium and potassium channel opening during a spike. (B) Relay Lab: one excitatory input stays below threshold; three together fire the cell (grey). (C) Prediction Lab: a trained model dopamine neuron bursts after the light and pauses when the expected juice is withheld, as in Fig. 1 of @schultz1997. (D) Prediction error over 80 training trials moves from the juice back to the light, as in their Fig. 3.\label{fig:labs}](figure.png)

# Statement of need

Psychology students usually meet neural signalling in an introductory neuroscience course
[@bear2016], where it is the most physiological part of the syllabus. Excellent simulators
exist for teaching electrophysiology [@stuart2009; @heitler2022], and simulation exercises
work best with a structured-inquiry design [@crisp2012]. These labs serve a different
situation: a lecture class of psychology students, using whatever devices they carry, with no
computer lab and no time to learn a simulator's interface.

They address that situation in four ways. They start from questions a psychologist would ask
(how does a neuron signal "stronger"? what does dopamine report?) and expose only the
controls that answer them. They run in any browser, including on phones and offline from a
local copy. They were designed to be neurodivergent-friendly: one idea per screen, numbered
steps, a readable typeface, both colour themes, reduced motion and no sound by default. And Prediction Lab packages a reusable assessment format, read a
paper, replicate it, explain it, that brings the argument for teaching through replication
[@frank2012] into a lecture course without collecting or storing any student data.

# Learning objectives and content

Each lab supports one 90-minute class; full objectives are in `docs/instructor-guide.md`.
After Spike Lab, students can explain threshold, the all-or-none spike, the order of channel
opening, refractoriness and rate coding from their own measurements. After Relay Lab, they
can explain why myelin speeds conduction and demyelination slows it, order the steps of
chemical transmission, distinguish spatial and temporal summation, and classify drugs by
their action at receptors. Prediction Lab is a 90-minute open-book assessment: students read
a raster plot, state and test the prediction-error account, connect it to spikes, synapses,
conduction, receptors and drugs, and judge what a partial replication failure means for a
theory.

The module contains the three labs; two slide decks (44 and 40 slides); two ten-page activity
booklets with step-by-step lab pages, word lists, study cards, answers and sources; a ten-page
question booklet with a reading guide; an instructor guide; model notes stating every simplification and the values the materials rely
on; and end-to-end tests that drive every lab part in a headless browser at laptop and phone
sizes and check those values on each commit.

# Instructional design

Every activity follows the same cycle: predict, measure, record, check. In the two teaching
labs, each part ends with a "you are done when…" line, and numeric answers get immediate, specific feedback ("a little low; check the readout")
rather than a red cross. Slides carry a one-line summary at the top, at most three points,
and a coloured *LAB* tag with a QR code wherever students switch to the lab. Relay Lab locks
each part until its slide shows a password, so a class moves together.

The models are simplified, and say so. Relay Lab's conduction speeds come from empirical rules
rather than simulation, and its integrate-and-fire neuron has larger EPSPs than real cortical
neurons. Prediction Lab keeps a deliberate mismatch: with the paper's representation of time,
a reward delivered early produces a pause at the usual time, which the paper's note 18 reports
real neurons did not show. Finding this, and deciding whether it falsifies the theory or only
one assumption, is a question in the assessment.

# Experience of use

[AUTHOR TO COMPLETE: when each lab was first used, the course, cohort size and level, and what
you observed. For example: "Spike Lab and Relay Lab were used in *Introduction to Neuroscience*
at Krea University in November 2026 with N psychology undergraduates and PhD students;
Prediction Lab and its booklet formed the second in-class quiz." Add one or two concrete
observations, such as where students struggled or what the teaching assistant reported.]

# Story of the project

The labs grew out of a teaching assistant's feedback after a class on membrane potentials:
the slides were hard to follow at a glance, and students struggled to keep up. Rewriting the
decks in an "at a glance" format raised a further question: could students *do* each idea
beside the slide, rather than only watch it? Spike Lab came first, then Relay Lab, which
compressed three textbook sessions into one class when the syllabus had to be cut. Prediction
Lab began as a quiz and became a rehearsal for the course's end-term format, in which students
read, replicate and explain a classic study.

# Acknowledgements

I thank the students and the teaching assistant of *Introduction to Neuroscience* at Krea
University for their feedback. The lab code, booklets, slides, tests and a draft of this paper
were developed with the assistance of Claude (Anthropic), a generative AI model, working to the
author's specifications. The author designed the pedagogy, chose and checked the models
against the cited sources, reviewed all materials and takes responsibility for them.

# References
