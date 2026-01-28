Chi-Square Test (KHI²) Using Python

This project implements the Chi-square (KHI²) goodness-of-fit test using Python to analyze categorical data and determine whether observed frequencies differ significantly from expected frequencies under a specified hypothesis. The project also includes a visualization of the Chi-square distribution and the critical value.

Overview

The Chi-square test is a widely used statistical method for categorical data — data that falls into categories rather than numeric measurements. It helps determine whether patterns in observed data can be explained by chance or whether they indicate a real effect.

The Chi-square test can be used in different ways:

Goodness-of-fit test: Compares observed frequencies to expected frequencies.

Test of independence: Checks if two categorical variables are related.

Test of homogeneity: Tests whether different samples come from the same distribution.

Problem Description

A sports training center wants to know which factor most influences students when choosing a training center.

A group of 100 students were asked to choose the most important factor among:

Success rate

Location

Coach

Training schedule

Observed frequencies:

[36, 34, 14, 16]


The question is whether these differences occur by chance or reflect real preferences.

Objective

The goal is to use the Chi-square goodness-of-fit test to determine whether:

All factors are equally important
OR

At least one factor is significantly different

Hypotheses

Null Hypothesis (H₀):
All categories have the same probability (equal preference).

Alternative Hypothesis (H₁):
At least one category has a different probability.

Statistical Background
Expected Frequencies

If each category is equally likely, the expected frequency for each is:

E = Total observations / Number of categories  
E = 100 / 4 = 25

Chi-Square Statistic

The Chi-square statistic measures the total discrepancy between observed and expected values:

KHI² = ∑ (Oi − Ei)² / Ei


Where:

Oi = Observed frequency

Ei = Expected frequency

Degrees of Freedom

For k categories:

df = k − 1
df = 4 − 1 = 3

Critical Value

For a significance level of α = 0.05 and df = 3, the critical Chi-square value from distribution tables is:

χ²(0.05, 3) = 7.815

Manual Calculation
(36 − 25)² / 25 = 4.84  
(34 − 25)² / 25 = 3.24  
(14 − 25)² / 25 = 4.84  
(16 − 25)² / 25 = 3.24  

KHI² = 4.84 + 3.24 + 4.84 + 3.24 = 16.16

Decision Rule

If:

KHI²_computed > KHI²_critical


Then reject H₀.

Result
KHI²_computed = 16.16  
KHI²_critical = 7.815


Because 16.16 > 7.815, we reject the null hypothesis: the differences in category frequencies are unlikely to be due to chance.

Conclusion

The Chi-square test shows a statistically significant difference between observed and expected frequencies. This indicates that the preference distribution across the four factors is not equal — some factors influence student choice more than others.

Python Implementation

The Python script (code/KHItesting.py) performs the following:

Stores the observed frequencies

Computes the expected frequencies

Calculates the Chi-square statistic

Determines degrees of freedom

Finds the critical value

Outputs results and conclusion

Plots the Chi-square distribution with the critical value

Visualization
KHI² Distribution

This graph shows the Chi-square probability distribution and the critical value used for the test:

The curve shows the theoretical distribution for df = 3 while the vertical line marks the critical value at α = 0.05.

Project Structure
Chi-Square-Test/
│
├── code/
│   └── KHItesting.py         # Python script
├── figures/
│   └── KHI2.png              # Chi-square distribution plot
├── README.md                 # This file
└── requirements.txt

Requirements
numpy
scipy
matplotlib

Installation

Install required libraries:

pip install numpy scipy matplotlib

Run the Program

In the repository folder:

python code/KHItesting.py

Author

Hachim Fernane
Master Student – Computer Science
University of Guelma

License

This project is for educational and academic use only.
