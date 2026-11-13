# Simulation and decisions

State the model, constraints, units, distributions, and decision objective.
Distinguish supplied assumptions from estimates. For Monte Carlo, preserve a seed,
justify distributions/dependencies, report sampling uncertainty, and check that
increasing sample size stabilizes the relevant result. Validate limiting cases
against simple analytical expectations where possible.

For optimization, check solver status, feasibility, residuals, bounds, and whether
the method finds a local or global optimum. Compare with a simple feasible
baseline. Report sensitivity to material assumptions; an optimum under one set of
inputs is not an unconditional recommendation.

For interactive scenarios, persist verified baseline data and reproduce the same
equations in the browser. Test representative parameter changes and boundaries
against the Python model before claiming the tool supports those scenarios.
