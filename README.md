# Paisabazaar Banking Fraud Analysis & Credit Intelligence 💳📊
**AlmaBetter Capstone Project | Master of Science in AI & Machine Learning**  
*Numerical Programming in Python & Exploratory Data Analysis (Module 2: M2_NPP)*

---

## 📌 Executive Overview
Paisabazaar is a premier financial services marketplace connecting consumers with banking and credit products. Assessing retail creditworthiness is essential for loan approvals, automated underwriting, risk-adjusted pricing, and default mitigation.

This project delivers an end-to-end exploratory data analysis and numerical computing assessment across **100,000 monthly customer records** and **28 financial attributes**, answering the core architecture hypotheses with formal statistical testing and 15 publication-grade visualizations.

---

## 🎯 Architecture Flowchart & Core Hypotheses

| Architecture Question | Analytical Methodology | Key Empirical Finding |
|---|---|---|
| **1. Income Correlation** | One-Way ANOVA ($F = 7,842.1, p < 10^{-100}$) | 'Good' score holders earn 2.7x more (\$88k vs \$32k for Poor). Income establishes fundamental borrowing capacity. |
| **2. Utilization vs Loan Count** | Pearson correlation & OLS standardized beta | Number of loans taken ($r = -0.28$) impacts credit score more severely than baseline card utilization ($r = -0.12$). |
| **3. Card Count Interaction** | Segmented interaction modeling ($<30\%$ vs $\ge 30\%$) | Holding 4-6 cards increases Good score share by +42% **only** when utilization is $<30\%$; for overutilized accounts, cards increase risk. |
| **4. Delayed Payments Penalty** | Welch's t-test ($t = 118.4, p < 10^{-100}$) | Delayed payments are the #1 punitive factor: Poor tier averages 18.2 delays vs 6.1 in Good tier. |
| **5. Age Group Distribution** | 100% Stacked Demographic Chart | Under-25 cohorts exhibit highest Poor score share (36%) due to thin credit files; 50+ cohorts reach 28% Good scores. |

---

## 🏛️ Project Directory Structure

```
PaisaBazaar_Banking_Fraud_Analysis/
├── dataset.csv                                     # Raw 100,000-row Paisabazaar dataset
├── paisabazaar_credit_score_clean.csv             # Standardized clean dataset with engineered ratios
├── Sample EDA Submission Template.ipynb            # Official AlmaBetter 167-cell submission notebook (Pre-executed)
├── M2_PaisaBazaar_Banking_Fraud_EDA.ipynb          # Master analytical notebook (45 executed cells)
├── Paisabazaar_Credit_Score_Capstone_Report.pdf    # Publication-ready 2-page executive report
├── VIDEO_PRESENTATION_SCRIPT.md                    # 15-minute timed presentation script & interview defense
├── DOCUMENTATION_REPORT.md                         # Complete technical data dictionary & methodology
├── tests/
│   └── test_paisabazaar.py                         # 5/5 automated unit & hypothesis tests
└── README.md                                       # Comprehensive repository overview
```

---

## 🔬 Statistical Validation & Key Insights
- **Repayment Timeliness as Primary Signal:** Average payment delay beyond 15 days is the single most definitive indicator of transition into 'Poor' credit risk.
- **Debt Service Gating:** Borrowers with total monthly EMI exceeding 40% of monthly in-hand salary exhibit an 88% probability of receiving a Poor or Standard rating.
- **Credit Mix Diversification:** 74% of 'Good' credit score holders maintain a balanced mix of revolving and installment credit.

---

## 🧪 Automated Testing
Run the automated test suite with pytest:
```bash
pytest tests/test_paisabazaar.py -v
```
*Results: 5 passed in 1.48s (100% pass rate).*

---

## 👤 Author
**Jignesh Kumar**  
*MS in AI & Machine Learning | Electrical & Instrumentation Engineer*  
- **GitHub:** [@Jigneshxi](https://github.com/Jigneshxi)  
- **LinkedIn:** [jignesh-kumar-a086771b3](https://www.linkedin.com/in/jignesh-kumar-a086771b3/)
