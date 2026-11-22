# Technical Documentation Report
## Paisabazaar Banking Fraud Analysis & Retail Credit Score Classification

### 1. Executive Summary
This project provides a comprehensive exploratory data analysis (EDA) and numerical computing framework on **100,000 monthly customer observations** from Paisabazaar. The objective is to analyze behavioral financial patterns to classify retail creditworthiness (`Poor`, `Standard`, `Good`) and identify key risk drivers.

### 2. Dataset Architecture & Dictionary
The dataset comprises 28 features detailing customer demographics, balance sheet figures, credit inquiries, debt metrics, and repayment timeliness:
- `Customer_ID`, `Age`, `Occupation`: Demographic segmentation attributes.
- `Annual_Income`, `Monthly_Inhand_Salary`, `Outstanding_Debt`: Balance sheet liquidity and leverage.
- `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`: Product holding metrics.
- `Num_of_Loan`, `Type_of_Loan`: Credit depth and borrowing mix.
- `Delay_from_due_date`, `Num_of_Delayed_Payment`: Repayment timeliness and delinquency.
- `Credit_Mix`, `Credit_Utilization_Ratio`, `Credit_History_Age`: Structural credit score determinants.
- `Total_EMI_per_month`, `Amount_invested_monthly`, `Monthly_Balance`: Cash flow and debt service capacity.
- `Credit_Score` (Target): `Poor` (29.0%), `Standard` (53.2%), `Good` (17.8%).

### 3. Empirical Hypothesis Testing Results
1. **Hypothesis 1 (Annual Income vs Credit Score):**
   - *Test:* One-way ANOVA ($F = 7,842.1, p < 10^{-100}$).
   - *Result:* 'Good' credit score individuals average \$88,240 vs \$32,150 for 'Poor'. Income establishes foundational credit capacity.
2. **Hypothesis 2 (Credit Utilization vs Total Loans Impact):**
   - *Test:* Standardized multivariate regression & Pearson correlation.
   - *Result:* Number of loans taken ($r = -0.28$) impacts creditworthiness more negatively than baseline credit card utilization ($r = -0.12$). Multi-loan proliferation is a primary signal of distress.
3. **Hypothesis 3 (Credit Card Count Interaction):**
   - *Result:* For low-utilization borrowers (<30%), holding 4-6 cards increases 'Good' credit score probability by +42%. Conversely, for overutilized borrowers (>=30%), each additional card increases 'Poor' score risk by +18%.
4. **Hypothesis 4 (Delayed Payment Penalty):**
   - *Test:* Welch's two-sample t-test ($t = 118.4, p < 10^{-100}$).
   - *Result:* Delayed payments are the single most punitive factor. Poor score customers average 18.2 delays vs 6.1 delays in the Good tier.

### 4. Technical Deliverables Summary
- **Official Submission Notebook:** `Sample EDA Submission Template.ipynb` (167 cells, 28/28 executed code cells).
- **Master Analysis Notebook:** `M2_PaisaBazaar_Banking_Fraud_EDA.ipynb` (45 executed cells).
- **Clean Feature Dataset:** `paisabazaar_credit_score_clean.csv` (100,000 rows, engineered ratios).
- **Publication PDF Report:** `Paisabazaar_Credit_Score_Capstone_Report.pdf`.
- **15-Min Video Script:** `VIDEO_PRESENTATION_SCRIPT.md` (8 timed sections + 5 Q&A).
- **Automated Pytest Suite:** `tests/test_paisabazaar.py` (5/5 passing unit tests).
