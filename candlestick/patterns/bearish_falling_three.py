from candlestick.patterns.candlestick_finder import CandlestickFinder


class BearishFallingThree(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 5, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev1_candle = self.data.iloc[idx + 1 * self.multi_coeff]
        prev2_candle = self.data.iloc[idx + 2 * self.multi_coeff]
        prev3_candle = self.data.iloc[idx + 3 * self.multi_coeff]
        prev4_candle = self.data.iloc[idx + 4 * self.multi_coeff]
        

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        prev1_close = prev1_candle[self.close_column]
        prev1_open = prev1_candle[self.open_column]
        prev1_high = prev1_candle[self.high_column]
        prev1_low = prev1_candle[self.low_column]

        prev2_close = prev2_candle[self.close_column]
        prev2_open = prev2_candle[self.open_column]
        prev2_high = prev2_candle[self.high_column]
        prev2_low = prev2_candle[self.low_column]


        prev3_close = prev3_candle[self.close_column]
        prev3_open = prev3_candle[self.open_column]
        prev3_high = prev3_candle[self.high_column]
        prev3_low = prev3_candle[self.low_column]


        prev4_close = prev4_candle[self.close_column]
        prev4_open = prev4_candle[self.open_column]
        prev4_high = prev4_candle[self.high_column]
        prev4_low = prev4_candle[self.low_column]



        
        return (close<open and 
        prev1_close>prev1_open and 
        prev2_close>prev2_open and 
        prev3_close>prev3_open and 
        prev4_close<prev4_open and 
        close<prev3_open )


