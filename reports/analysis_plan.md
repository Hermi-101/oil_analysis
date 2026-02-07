

1. Data Analysis Workflow

Our workflow is designed to move from raw, unstructured time-series data to actionable strategic insights using a Bayesian statistical framework.

Data Ingestion & Cleaning:

Load the Brent Oil dataset (1987–2022).

Standardize date formats (handling mixed strings like "20-May-87" and "Apr 22, 2020").

Check for and handle missing price data using forward-filling to maintain time-series continuity.

Exploratory Data Analysis (EDA):

Visualize long-term price movements.

Apply rolling mean (50-day and 200-day) to identify visible market regimes.

Calculate daily log returns to visualize volatility clusters.

Statistical Profiling:

Perform Augmented Dickey-Fuller (ADF) tests to confirm non-stationarity.

Analyze distribution of returns (checking for "fat tails" or kurtosis).

Bayesian Change Point Modeling (PyMC):

Define priors for the switch point (
𝜏
τ
) and market means (
𝜇
1
,
𝜇
2
μ
1
	​

,μ
2
	​

).

Execute MCMC sampling to identify the most probable dates of structural breaks.

Event Attribution:

Cross-reference detected change points with the compiled external_events.csv.

Quantify the percentage change in price and volatility before and after each event.

Insight Generation & Dashboarding:

Summarize the "Sensitivity" of the market to different event categories (War vs. Economic).

Serve results via a Flask API to a React Dashboard.

2. Compiled Event Data (external_events.csv)

Below are the 15 key events researched for the project scope.

Date	Event	Category	Description
1990-08-02	Iraq Invades Kuwait	Geopolitical	Lead to Gulf War; immediate spike in supply-side risk.
1997-07-02	Asian Financial Crisis	Economic	Massive drop in oil demand from emerging Asian economies.
1998-11-01	Low Oil Price Era	Economic	Oil hit ~$10/bbl due to oversupply and Asian crisis lag.
2001-09-11	9/11 Attacks	Geopolitical	Triggered global economic uncertainty and war in Afghanistan.
2003-03-20	Invasion of Iraq	War	Long-term disruption of Iraqi production and regional instability.
2008-07-11	Historical Price Peak	Economic	Brent reached $147.50 due to speculation and peak demand.
2008-09-15	Lehman Brothers Collapse	Economic	Triggered the GFC; price plummeted from $140 to $40.
2011-02-15	Arab Spring (Libya)	Geopolitical	Civil war removed 1.5 million barrels/day from the market.
2014-11-27	OPEC "Market Share" Policy	OPEC Policy	OPEC refused to cut production to fight US Shale; price crash.
2016-11-30	OPEC+ Formation	OPEC Policy	Russia and OPEC agree to joint cuts to end the price slump.
2018-05-08	US exits Iran Nuclear Deal	Sanctions	Renewed sanctions on Iranian oil exports tightened supply.
2020-03-08	Saudi-Russia Price War	Geopolitical	Production surge coincided with the start of global lockdowns.
2020-04-20	Negative WTI / Brent Drop	Economic	Storage crisis; global demand for oil essentially stopped.
2022-02-24	Russia-Ukraine Invasion	War	Sanctions on a global energy giant caused a massive risk premium.
2022-06-01	EU Embargo on Russian Oil	Sanctions	Structural shift in global oil flow from West to East.
3. Assumptions and Limitations
Assumptions:

Information Efficiency: We assume that Brent crude prices are "semi-strong efficient," meaning they reflect all publicly available geopolitical news within 48 hours.

Stationarity of Returns: While raw prices are non-stationary, we assume log returns are stationary and suitable for mean-shift detection.

Proxy Reliability: We assume Brent is a sufficient proxy for the global oil market, even though local benchmarks (WTI, Dubai) may react differently to specific regional events.

Limitations:

Confounding Factors: Multiple events often happen at once. A change point in early 2020 could be attributed to the Saudi-Russia price war or the COVID-19 lockdowns. The model cannot perfectly decouple these.

Anticipatory Pricing: Markets often "price in" an event before it happens (e.g., prices rising before a war starts), which might lead the model to place a change point slightly earlier than the actual event date.

Data Frequency: We are using daily data. Intra-day volatility (which is massive in oil markets) is not captured in this analysis.

Correlation vs. Causal Impact:

It is scientifically critical to distinguish between these two:

Statistical Correlation in Time: Our model identifies that a statistical break occurred "at the same time" as an event.

Causal Impact: To prove causality, we would need to prove that without the event, the price shift would not have happened.

Conclusion: In this analysis, we provide Plausible Attribution. We use the Bayesian model to prove a statistical shift occurred and use qualitative research to argue that the event was the primary catalyst. We do not claim absolute causal proof, as the oil market is a complex system with thousands of moving parts.

4. Communication Channels

To reach our diverse stakeholders at Birhan Energies, we will use the following:

Technical Audience (Data Scientists/Analysts):

Format: GitHub Repository and Jupyter Notebooks.

Channel: Weekly technical syncs and Git Pull Requests.

Executive Audience (Decision Makers/Investors):

Format: Interactive React Dashboard.

Channel: Monthly strategy presentations.

Policy/Government Stakeholders:

Format: White Paper/PDF Report summarizing the "Geopolitical Risk Premiums" found in the data.

Channel: Official email briefings and Birhan Energies' Insights Blog (Medium-style).