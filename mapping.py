def mapping(x,in_min,in_max,out_min,out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

'''
mapping(value,fromLow,fromHigh,toLow,toHigh)

value: 変換したい数値(変数)/Value to convert(variable)
fromLow: 現在の範囲の下限/minimum of currently range
fromHigh: 現在の範囲の上限/maximum of currently range
toLow: 変換後の範囲の下限/minimum of converted range
toHigh: 変換後の範囲の上限/maximum of converted range

*example*
import mapping
x=50
mapping.mapping(x,0,100,80,255)
'''
