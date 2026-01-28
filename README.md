# Chi-Square Test (KHI²) Using Python

This project implements the **Chi-square (KHI²) goodness-of-fit test** using Python.  
The objective is to determine whether categorical data follows a uniform distribution or if some categories are significantly more important than others.

The project also includes a visualization of the Chi-square distribution and the critical value.

---

## 1. Introduction

The Chi-square (KHI²) test is a statistical method used to compare **observed frequencies** with **expected frequencies** under a given hypothesis.

It is widely used when working with **categorical (qualitative) data**, such as survey results, choices, or classifications.

---

## 2. Problem Description

A training center director wants to know which factor most influences students when choosing a training center.

A group of 100 students were asked to choose one of the following factors:

1. Success rate  
2. Location  
3. Coach  
4. Training schedule  

Observed frequencies:

```
[36, 34, 14, 16]
```

---

## 3. Objective

Determine whether:

- All factors are equally important  
OR  
- One or more factors are more important than the others  

This is done using the Chi-square goodness-of-fit test.

---

## 4. Hypotheses

Null Hypothesis (H0):  
All factors have the same probability of being chosen.

Alternative Hypothesis (H1):  
At least one factor has a different probability.

---

## 5. Theoretical Background

### 5.1 Expected Frequencies

If all factors are equally important:

```
E = Total observations / Number of categories
E = 100 / 4 = 25
```

Each factor is expected to appear 25 times.

---

### 5.2 Chi-square Statistic Formula

```
KHI² = Σ ( (Oi - Ei)² / Ei )
```

Where:

- Oi : Observed frequency  
- Ei : Expected frequency  

---

### 5.3 Degrees of Freedom

```
df = k - 1
df = 4 - 1 = 3
```

Where k is the number of categories.

---

### 5.4 Critical Value

For significance level:

```
α = 0.05
df = 3
```

Critical value from Chi-square table:

```
χ²(0.05, 3) = 7.815
```

---

## 6. Manual Calculation

```
(36 - 25)² / 25 = 4.84
(34 - 25)² / 25 = 3.24
(14 - 25)² / 25 = 4.84
(16 - 25)² / 25 = 3.24

KHI² = 4.84 + 3.24 + 4.84 + 3.24 = 16.16
```

---

## 7. Decision Rule

If:

```
KHI²_calculated > KHI²_critical
```

Then reject H0.

---

## 8. Result

```
KHI²_calculated = 16.16
KHI²_critical = 7.815
```

Since:

```
16.16 > 7.815
```

We reject the null hypothesis.

---

## 9. Conclusion

There is a significant relationship between factors and student choice.  
Some factors influence the selection of the training center more than others.

---

## 10. Python Implementation

The Python program:

- Stores observed data  
- Computes total and expected values  
- Calculates KHI² statistic  
- Computes degrees of freedom  
- Finds critical value  
- Prints the decision  
- Draws the Chi-square distribution curve  

---

## 11. Visualization

### KHI2 – Chi-square Distribution

![KHI2](KHI2.png)

Explanation:

- Blue curve: Chi-square distribution  
- Red dashed line: Critical value (7.815)

---

## 12. Project Structure

```
KHI2-Test/
│
├── KHItesting.py
├── KHI2.png
└── README.md
```

---

## 13. Requirements

```
numpy
scipy
matplotlib
```

---

## 14. Installation

```
pip install numpy scipy matplotlib
```

---

## 15. Run

```
python KHItesting.py
```

---

## 16. Author

Hachim Fernane  
Master Student – Computer Science  
University of Guelma  

---

## 17. License

FEEL FREE TO USE JUST PRAY FOR ME

