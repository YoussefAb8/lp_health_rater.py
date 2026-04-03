# Apex-LP-Health-Rater

An AI-driven regression model developed to analyze and rate the health of Liquidity Pools (LPs) on decentralized exchanges. By leveraging a RandomForestRegressor, this tool processes key protocol and market indicators to generate a health score (0-100).

## Project Status: Testnet

This model is currently deployed and tested on the OpenGradient Testnet.

## How it Works

The model evaluates a Liquidity Pool based on 3 core features:

1.  Volume/TVL: Ratio of daily trading volume to Total Value Locked.
2.  Volatility: Daily price volatility of the pool's assets.
3.  Concentration: Percentage of liquidity held by the top 5 providers.

The output is a single health score from 0 (Very Unhealthy) to 100 (Excellent Health).

## On-chain Validation (Proof of Execution)
<img width="1337" height="588" alt="image" src="https://github.com/user-attachments/assets/cfb07180-5d43-4a1a-8333-6cd8187a4284" />
