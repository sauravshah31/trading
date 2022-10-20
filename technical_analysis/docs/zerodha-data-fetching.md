# Technical Analysis
## Zerodha Data Fetching

* kite.zerodha.com
* cookies, local storage
* GET : https://kite.zerodha.com/oms/user/profile/full -> JSON response containing user profile data
* GET : https://kite.zerodha.com/api/marketwatch -> JSON response containing data for watchlist (1-7)
* GET : https://kite.zerodha.com/oms/portfolio/holdings -> JSON response containing data for current holdings
* GET : https://kite.zerodha.com/static/js/chunk-2d22c101.4f927a35.js -> lising in js data structure
    * ["instruments"]["NSE"]
    * ["instruments"]["BSE"]