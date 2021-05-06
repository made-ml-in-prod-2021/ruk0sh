
# 1. Dataset Description

**Context**
This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to
this date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4.

**Content**
Attribute Information:

- age
- sex
- chest pain type (4 values)
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl
- resting electrocardiographic results (values 0,1,2)
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

One file has been "processed", that one containing the Cleveland database. All four unprocessed files also exist in this directory.

To see Test Costs (donated by Peter Turney), please see the folder "Costs"

**Acknowledgements**
__Creators:__

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
__Donor:__
David W. Aha (aha '@' ics.uci.edu) (714) 856-8779

Inspiration
Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).

See if you can find any other trends in heart data to predict certain cardiovascular events or find any clear indications of heart health.

# 2. Data Overview
|    |   age |   sex |   cp |   trestbps |   chol |   fbs |   restecg |   thalach |   exang |   oldpeak |   slope |   ca |   thal |   target |
|---:|------:|------:|-----:|-----------:|-------:|------:|----------:|----------:|--------:|----------:|--------:|-----:|-------:|---------:|
|  0 |    63 |     1 |    3 |        145 |    233 |     1 |         0 |       150 |       0 |       2.3 |       0 |    0 |      1 |        1 |
|  1 |    37 |     1 |    2 |        130 |    250 |     0 |         1 |       187 |       0 |       3.5 |       0 |    0 |      2 |        1 |
|  2 |    41 |     0 |    1 |        130 |    204 |     0 |         0 |       172 |       0 |       1.4 |       2 |    0 |      2 |        1 |
|  3 |    56 |     1 |    1 |        120 |    236 |     0 |         1 |       178 |       0 |       0.8 |       2 |    0 |      2 |        1 |
|  4 |    57 |     0 |    0 |        120 |    354 |     0 |         1 |       163 |       1 |       0.6 |       2 |    0 |      2 |        1 |
|  5 |    57 |     1 |    0 |        140 |    192 |     0 |         1 |       148 |       0 |       0.4 |       1 |    0 |      1 |        1 |
|  6 |    56 |     0 |    1 |        140 |    294 |     0 |         0 |       153 |       0 |       1.3 |       1 |    0 |      2 |        1 |
|  7 |    44 |     1 |    1 |        120 |    263 |     0 |         1 |       173 |       0 |       0   |       2 |    0 |      3 |        1 |
|  8 |    52 |     1 |    2 |        172 |    199 |     1 |         1 |       162 |       0 |       0.5 |       2 |    0 |      3 |        1 |
|  9 |    57 |     1 |    2 |        150 |    168 |     0 |         1 |       174 |       0 |       1.6 |       2 |    0 |      2 |        1 |
# 3 Real Features EDA
![pairplot](C:\dev\MADE_2_PML\ruk0sh\ml_project\reports\figures\pairplot.png)
# 4. Categorical Features EDA
![bar1](C:\dev\MADE_2_PML\ruk0sh\ml_project\reports\figures\bar1.png)
![heatmap](C:\dev\MADE_2_PML\ruk0sh\ml_project\reports\figures\bar2.png)
# 5.Conclusion
Blah blah blah skewed data, needs preprocessing and so on.
