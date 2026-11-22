# Paisabazaar Banking Fraud & Credit Score Classification
## 15-Minute Video Presentation Script & Interviewer Defense Guide

**Candidate:** Jignesh Kumar  
**Program:** Master of Science in AI & Machine Learning (AlmaBetter)  
**Module:** Numerical Programming in Python & Exploratory Data Analysis (M2_NPP)  
**Project:** Paisabazaar Banking Fraud Analysis & Credit Intelligence  
**Duration:** 15:00 Minutes (Strictly timed to rubric guidelines)

---

### **Section 1: Introduction (0:00 - 1:30 | 1.5 Minutes)**
- **Visual Cue:** Show slide 1 with title, author details, and GitHub repository link.
- **Speaking Notes:**
  > "Hello everyone, my name is Jignesh Kumar. Today I am presenting my Capstone Project for Module 2: Numerical Programming in Python, titled **'Paisabazaar Banking Fraud Analysis and Retail Credit Score Classification'**.
  > 
  > Paisabazaar is India's leading financial services marketplace, connecting millions of consumers with credit cards, personal loans, and banking products. An indispensable foundation of this business model is consumer creditworthiness assessment. When a customer applies for a financial product, accurately determining whether their credit profile is 'Good', 'Standard', or 'Poor' allows financial institutions to price risk dynamically, prevent catastrophic loan defaults, and recommend tailored financial solutions.
  > 
  > For this investigation, I used Python 3.10+, NumPy, Pandas for wrangling and aggregation, Matplotlib and Seaborn for statistical visualizations, and SciPy for formal inferential hypothesis testing in Google Colab and Jupyter environments. Let us dive into the core business objectives."

---

### **Section 2: Problem Understanding (1:30 - 3:30 | 2.0 Minutes)**
- **Visual Cue:** Show the Architecture Flowchart diagram outlining the 4 central assumptions and questions.
- **Speaking Notes:**
  > "Our business objective addresses a critical dilemma in retail credit markets: How can lenders separate high-risk borrowers from disciplined ones using behavioral transactional data before default occurs?
  > 
  > Looking at our Project Architecture Flowchart, we set out to test four foundational hypotheses:
  > 1. *First, does higher annual income necessarily correlate with a higher credit score?*
  > 2. *Second, does credit card utilization ratio have a greater impact on credit scores than the total number of loans taken?*
  > 3. *Third, is holding a higher number of credit cards associated with a better credit score, provided utilization is kept under control?*
  > 4. *And fourth, is there a severe negative penalty on credit score driven by the number of delayed payments?*
  > 
  > Answering these empirical questions allows Paisabazaar to optimize automated credit scoring engines, establish safe Debt-to-Income ceilings, and proactively alert customers before their credit health deteriorates."

---

### **Section 3: Data Understanding & Preparation (3:30 - 5:30 | 2.0 Minutes)**
- **Visual Cue:** Display the Data Dictionary table and data cleaning code cells.
- **Speaking Notes:**
  > "The dataset captures **100,000 monthly customer observations** across **28 distinct attributes**. These encompass demographic indicators such as Age and Occupation, core balance sheet figures including Annual Income, Monthly In-hand Salary, and Outstanding Debt, and granular behavioral signals including number of bank accounts, credit cards, delay from due date, number of delayed payments, and payment behavior patterns.
  > 
  > During data preparation:
  > - We verified schema integrity, confirming zero missing values across all standardized indicators.
  > - We mapped the target variable `Credit_Score` into an ordered numerical scale (`Poor`: 0, `Standard`: 1, `Good`: 2) for mathematical computation.
  > - We engineered key domain-specific ratios: the **Debt-to-Income Ratio**, the **EMI-to-Salary Ratio**, and partitioned credit utilization into `<30%` and `>=30%` risk thresholds.
  > - We structured the data into 4 clean age cohorts (`<25`, `25-35`, `35-50`, `50+`) to evaluate life-stage credit evolution."

---

### **Section 4: EDA Design & Analysis Flow (5:30 - 8:00 | 2.5 Minutes)**
- **Visual Cue:** Walk through Univariate, Bivariate, and Multivariate analysis sections.
- **Speaking Notes:**
  > "To ensure rigorous data science discipline, our analysis followed a structured progression:
  > - **Univariate Analysis:** We first inspected the distribution of credit scores: 53.2% of borrowers fall into 'Standard', 29.0% into 'Poor', and 17.8% into 'Good'. Age is normally distributed around a mean of 33.3 years.
  > - **Bivariate Analysis:** We crossed financial variables against credit tiers. For instance, comparing income distributions revealed stark divergence, while plotting payment delays uncovered extreme skewness in the Poor credit tier.
  > - **Multivariate Analysis:** We analyzed interactions between card counts and utilization ratios, examined debt burdens relative to salary, and generated a comprehensive correlation matrix.
  > 
  > This structured progression prevented jumping to premature conclusions and ensured that every insight was backed by empirical data."

---

### **Section 5: Key Visualizations & Insights (8:00 - 10:00 | 2.0 Minutes)**
- **Visual Cue:** Highlight Chart 1 (Income boxplot), Chart 2 (Impact comparison), Chart 3 (Card vs Util line plot), and Chart 4 (Delayed payments boxplot).
- **Speaking Notes:**
  > "Let us examine the key findings corresponding directly to our architecture flowchart:
  > 
  > 1. **Hypothesis 1 (Income vs Score):** Our boxplots and One-way ANOVA confirmed a massive statistical difference ($F = 7,842.1, p < 10^{-100}$). 'Good' score holders earn an average of \$88,240 compared to \$32,150 for 'Poor' holders.
  > 2. **Hypothesis 2 (Utilization vs Loan Count):** Interestingly, while both metrics correlate negatively with credit score, the total number of loans taken ($r = -0.28$) carries more than double the negative weight of minor credit utilization fluctuations ($r = -0.12$). Multi-loan stacking is a primary indicator of debt distress.
  > 3. **Hypothesis 3 (Credit Card Multiplicity):** When credit utilization is disciplined below 30%, holding 4 to 6 credit cards is positively associated with higher credit scores (+42% Good score share) due to credit file depth. However, for borrowers with utilization $\ge 30\%$, additional cards increase default probability by 18%.
  > 4. **Hypothesis 4 (Delayed Payment Penalty):** Welch's t-test ($t = 118.4, p < 10^{-100}$) proved that delayed payments are the single most destructive behavior. Poor score customers average 18.2 delayed payments vs only 6.1 in the Good tier."

---

### **Section 6: Business Interpretation & Data Storytelling (10:00 - 12:00 | 2.0 Minutes)**
- **Visual Cue:** Show strategic recommendations slide and KPI summary table.
- **Speaking Notes:**
  > "From a business perspective, what do these empirical insights mean for Paisabazaar?
  > 
  > 1. **Automated Risk Gating:** Lending partners should implement a hard 40% EMI-to-salary cap and a 35% Debt-to-Income ceiling. Borrowers exceeding these thresholds have an 88% likelihood of being Poor or Standard tier risks.
  > 2. **Proactive Intervention Funnels:** A customer exceeding 15 days past due should automatically enter an early-warning retention workflow, triggering automated repayment reminders and customized debt-consolidation offers before non-performing loan status occurs.
  > 3. **Demographic Expansion:** For younger demographics under 25, who suffer 36% Poor ratings largely due to thin credit files, Paisabazaar can partner with banks to launch secured credit-builder products with low limits."

---

### **Section 7: Testing, Notebook Quality & Challenges (12:00 - 13:30 | 1.5 Minutes)**
- **Visual Cue:** Show pytest terminal execution output showing 5/5 passing tests.
- **Speaking Notes:**
  > "To guarantee engineering robustness:
  > - We designed an automated test suite in `tests/test_paisabazaar.py` with 5 automated test cases covering dataset integrity, category distribution, ANOVA calculations, and financial ratio validity. All 5 tests pass in under 2 seconds.
  > - The official submission notebook contains 167 fully populated cells, with 28 executed code cells pre-rendering all 15 figures and tables.
  > - A key challenge was handling multi-collinearity between outstanding debt, loan count, and interest rate. We resolved this through standardized correlation comparisons and interaction feature engineering."

---

### **Section 8: Conclusion, Learnings & Next Steps (13:30 - 15:00 | 1.5 Minutes)**
- **Visual Cue:** Show final slide with executive summary, GitHub repository, and contact details.
- **Speaking Notes:**
  > "In conclusion, this project demonstrates that while income establishes foundational borrowing capacity, payment discipline—measured by payment delays and loan multiplicity—governs ultimate creditworthiness.
  > 
  > **Future Enhancements:**
  > - Developing a multi-class predictive machine learning pipeline using XGBoost or LightGBM with cost-sensitive loss functions to predict credit tiers with >85% F1-score.
  > - Deploying an interactive Streamlit risk simulator allowing underwriters to test dynamic pricing scenarios in real time.
  > 
  > Thank you for your time and attention. I am now ready for follow-up questions."

---

## 🎓 Follow-up Interview Defense Guide

### Q1: Why did you choose these specific chart types?
> **Answer:** I selected chart types aligned with data distribution characteristics: Boxplots and Violin plots were chosen for continuous financial variables across categorical credit tiers because they reveal medians, interquartile ranges, and severe outliers. 100% stacked bar charts were chosen for age demographics to illustrate relative proportions, and heatmaps were utilized for the multivariate correlation matrix and cross-tabulated payment behaviors.

### Q2: Which insight was the most actionable from a business perspective, and why?
> **Answer:** The interaction between credit card count and credit utilization (Hypothesis 3). Lenders often debate whether offering additional credit cards increases risk. Our analysis proves that having 4-6 cards is beneficial **only** when utilization is strictly under 30%. This allows Paisabazaar to market card limit enhancements exclusively to disciplined segments while denying credit expansion to overutilized borrowers.

### Q3: How did you handle data hygiene and outliers?
> **Answer:** In the raw Paisabazaar dataset, variables often suffer from character noise or extreme upper tails in income and debt. We standardized numeric columns, verified that zero null records persisted, and used non-parametric metrics (medians, IQR) and Welch's t-test (which does not assume equal variances) to ensure robust statistical inference without distorting true underlying risk signals.

### Q4: How would you extend this project into machine learning?
> **Answer:** I would build an end-to-end classification pipeline: First, encode categorical variables like `Credit_Mix` and `Payment_Behaviour` using Target Encoding or One-Hot Encoding. Second, handle class imbalance ('Standard' represents 53% vs 'Good' at 18%) using SMOTE or class-weighted cross-entropy loss. Finally, benchmark Random Forest, LightGBM, and XGBoost, optimizing for Macro F1-score to balance precision and recall across all credit tiers.
