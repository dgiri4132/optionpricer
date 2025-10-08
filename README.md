# Option Pricer
This project implements a Binomial Option Pricing Model in Python for both European and American call and put options.
# Overview
The Binomial Option Pricing Model uses a discrete-time algorithm to estimate the fair price of an option.
At each and every step, the stock price can move up or down with probability which is derived from volatility and interst rates.
Backward induction is used to compute the option's value at each node.
# How it works
The main function is :
Python
binomial_price(S,K,T,r,sigma,steps=500,call=True, american=False,q=0.0)
