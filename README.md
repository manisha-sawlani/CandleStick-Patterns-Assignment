# candlestick-patterns
> Candlestick patterns detector

## Available patterns

* Bearish engulfing
* Bullish engulfing
* BullishRisingThree
* BearishfallingThree




### Dataframe requirements

- Dataframe must contain open, high, low and close prices
- Open, high, low and close prices must be in numeric type.

#### Dataframe Example: 
| Timestamp  |  Open  |  High  |   Low  | Close    | 
| ----------:| ------:| -----: | -----: | -----|:  |                          
| 2023-01-11 | 136.51 | 137.98 | 136.46 | 137.96   |  
| 2023-01-10 | 136.86 | 136.93 | 136.04 | 136.20   |
| 2023-01-09 | 137.13 | 137.38 | 136.40 | 137.03   |
| 2023-01-06 | 136.08 | 137.47 | 135.74 | 137.43   |  
| 2023-01-05 | 136.30 | 136.48 | 135.55 | 135.99   |


### Result
              Open    High     Low   Close   BullishRisingThree
2022-12-21  135.84  136.32  135.60  135.88         True
2022-12-06  141.10  142.27  140.60  141.89         True
2022-04-27  152.61  152.99  151.98  152.62         True
2022-01-13  163.77  164.69  163.55  164.40         True
2021-12-13  167.60  168.39  167.58  168.37         True