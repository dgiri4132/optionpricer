# Black-Scholes Binomial Option Pricer
![App Demo](demo.gif)

- This project is an interactive Option Pricing Web Appbuilt with Streamlit, implementing a Binomial Model to calcualte option values based on user-specific parameters such as volatility, strike price, time to maturity, and risk-free rate.
- As a add-on it also includes a MySQL integration for structured data collection and analysis of option parameters allowing users to store input-output data from each calculation for further financial modeling.
# Features
- Interactive Mode
  - Dynamically price options using user input.
  - Visualize option values and profit/loss via heatmaps or 3D surfaces.
  - Compare how volatility and stock price impact option value.

- Data Collection Mode
  - Compute option values and store results in a MySQL database.
  - Persist visualization even after saving (via `st.session_state`).
  - Supports exporting results to database for historical tracking.

- Visual Outputs
  - Heatmap of option values and P&L
  - 3D surface plots (option value & P&L)
  - Data tables with color gradients
# Mathematical Model
The app implements a binomial tree approach to the Black Scholes option pricing model
# Setup Instruction
- Clone the repository
```bash
git clone https://github.com/dgiri4132/optionpricer.git
cd optionpricer
```

-Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate        
.venv\Scripts\activate 
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Initialize the MySQL databse
```bash
  mysql -u root -p < database.sql
```
- Run the Streamlit app
```bash
  streamlit run app.py
```

