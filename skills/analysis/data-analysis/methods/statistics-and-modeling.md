# Statistics and modeling

Define the estimand, population, denominator, sampling process, units, and time
window. Inspect missingness, dependence, outliers, and selection bias. Choose
tests and confidence intervals from their assumptions; account for multiple
comparisons when relevant. Distinguish practical effects from statistical
significance and association from causation. Do not universally label values
beyond two standard deviations as errors.

For prediction, compare with a simple baseline. Separate training and evaluation,
fit preprocessing on training data, and prevent future or target leakage. Use
chronological splits/backtests for forecasts and metrics that match the intended
decision. Report uncertainty, calibration where relevant, and limitations outside
the observed range. Preserve seeds, features, splits, and parameters for follow-up.

NumPy/SciPy provide numerical methods; statsmodels provides statistical models;
scikit-learn provides predictive models, clustering, and text features; SymPy
provides symbolic work. Select the library from the task rather than inventing a
fixed analysis pipeline. Validate symbolic solutions against constraints and
numerical solutions against residuals and boundary cases.
