import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs import binomial_price
st.set_page_config(page_title='Option Pricer', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('Multi-tool Binomial Option Pricer')
st.sidebar.header('Option Parameters')
S=st.sidebar.number_input('Current Stock Price(S₀)', value=100.0)
K=st.sidebar.number_input('Strike Price(K)', value=100.0)
T=st.sidebar.number_input('Time to Maturity(T) in years', value=1.0)
r=st.sidebar.number_input('Risk-free Rate (r)', value=0.04)
sigma=st.sidebar.number_input('Volatility (σ)', value=0.2)
steps=st.sidebar.slider('Binomial Steps',10,1000,500)
q=st.sidebar.number_input('Dividend Yield (q)', value=0.0)
call=st.sidebar.selectbox('Option Type', options=['Call','Put'])
american=st.sidebar.checkbox('American Option',value=False)
purchase_price=st.sidebar.number_input('Purchase Price', value=10.0)

call_flag=(call=='Call')
price=binomial_price(S,K,T,r,sigma,steps,call=call_flag,american=american,q=q)
st.success(f"The {('American' if american else 'European')} {call} Option Price is: **${price:.2f}**")
S_range=np.linspace(S*0.85,S*1.15,12)
sigma_range=np.linspace(sigma*0.7,sigma*1.3,12)
prices=np.zeros((len(S_range), len(sigma_range)))
pnl=np.zeros_like(prices)
for i, S_i in enumerate(S_range):
    for j, sigma_j in enumerate(sigma_range):
        val=binomial_price(S_i,K,T,r,sigma_j,steps=steps,call=call_flag,american=american, q=q)
        prices[i,j]=val
        pnl[i,j]=val-purchase_price
df_prices=pd.DataFrame(prices, index=[round(s,2)for s in S_range], columns=[round(s,2) for s in sigma_range])
df_pnl=pd.DataFrame(pnl, index=[round(s,2)for s in S_range],columns=[round(s,2)for s in sigma_range])
display_mode=st.sidebar.selectbox('Display Mode',['Heatmap','3D Surface','Data Table'])
col1,col2=st.columns(2)
if display_mode=='Heatmap':
    with col1:
        st.subheader('Option Value Heatmap')
        fig, ax=plt.subplots(figsize=(6,5))
        sns.heatmap(df_prices, cmap='RdYlGn', ax=ax, linewidths=0.5, cbar_kws={'label':'Option Value($)'})
        plt.xlabel('Volatility (σ)')
        plt.ylabel('Stock Price (S)')
        st.pyplot(fig)
    with col2:
        st.subheader('P&L Heatmap ')
        fig, ax=plt.subplots(figsize=(6,5))
        sns.heatmap(df_pnl, cmap='RdYlGn', center=0, ax=ax, linewidths=0.5, cbar_kws={'label':'Profit/Loss ($)'})
        plt.xlabel('Volatility(σ)')
        plt.ylabel('Stock Price(S)')
        st.pyplot(fig)
elif display_mode == '3D Surface':
    from mpl_toolkits.mplot3d import Axes3D
    with col1:
        st.subheader('Option Value 3D Surface')
        X, Y =np.meshgrid(df_prices.columns, df_prices.index)
        fig=plt.figure(figsize=(6,5))
        ax=fig.add_subplot(111, projection='3d')
        surf=ax.plot_surface(X,Y, df_prices.values, cmap='RdYlGn', edgecolor='none')
        ax.set_xlabel('Volatility(σ)')
        ax.set_ylabel('Stock Price (S)')
        ax.set_zlabel('Option Value')
        fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10, label='Option Value in USD$')
        st.pyplot(fig)
    with col2:
        st.subheader('P&L 3D Surface')
        X, Y= np.meshgrid(df_pnl.columns, df_pnl.index)
        fig=plt.figure(figsize=(6,5))
        ax=fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, df_pnl.values, cmap='RdYlGn')
        ax.set_xlabel('Volatility (σ)')
        ax.set_ylabel('Stock Price (S)')
        ax.set_zlabel('P&L')
        st.pyplot(fig)
else:
    with col1:
        st.subheader('Option Value Table')
        st.dataframe(df_prices.style.background_gradient(cmap='RdYlGn', axis=None))
    with col2:
        st.subheader('P&L Table')
        st.dataframe(df_pnl.style.background_gradient(cmap='RdYlGn', axis = None))