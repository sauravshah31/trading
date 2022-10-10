# Technical Analysis (Notes)
* [Reference](https://zerodha.com/varsity/module/technical-analysis/)
* Analysing pattern (trend), checking for similar pattern in the past
* data
```Python
{
    high
    low
    opening_price
    closing_price
    volume
}
```
### Single Candlestick Patterns
1. Marubozu
* No uppper or lower shadow
* stoploss = low
* trend continues

2. Spinning top,  doji
* Small / no body
* indecision

3. Hammer, Hanging Man
* Small body at top (at least twice)
* downtrend, uptrend reversal
* stoploss = low

4. Shooting Star
* small body at bottom
* uptrend reversal

### Multiple Candlestick Patterns
1. Engulfing Pattern
* t2 englufs t1
* trend reversal
* doji present? indecision but there is a pattern before
* stoploss = min(low1, low2)

2. Piercing Pattern / Dark Cloud Cover
* t2 Englufs 50% of more of t1
* trend reversal
* stoploss = min(low1, low2)

3. Harami Pattern
* t1 = red candle covers t2 = small blue candle body or t1 = blue candle covers t2 = small red candle body
* trend reversal
* stoploss = min(low1, low2)

4. Morning Star / Evening Star
* Bear - doji - Bull / Bull - doji - Bear
* trend reversal

* Support and resistance
* Today's volume > last 10 days average volume
* moving average (simple, exponential)
* combining short term moving average and long term moving average (buy when st > lt and sell when st < lt)