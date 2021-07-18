# Quant

Home project for quantitative financial analysis
- retrieve data from AlphaVantage api for indices and stocks
- retrieve data from quandl api for indices and stocks
- portfolio variance-covariance analysis

### API Key for Alpha Vantage
- [Get an AlphaVantage API key here](https://www.alphavantage.co/)

### Set up your virtual environment and api key
- First, create your environment and activate it:`conda create -n quant`, `conda activate quant`. Here `quant` is the name of your virtual environment
- Install all the required packages: `pip install -r requirements.txt`
- To list any variables you may have, run `conda env config vars list`.
- To set environment variables, run `conda env config vars set ALPHA_VANTAGE_API_KEY='your_api_key_goes_here'`.
[See Conda docs here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#setting-environment-variables)
- If you're using an IDE like pycharm (like me), [See here](https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm)
