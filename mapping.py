def mapping(x,in_min,in_max,out_min,out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

'''
mapping(value,fromLow,fromHigh,toLow,toHigh)

value: 変換したい数値
fromLow: 現在の範囲の下限
fromHigh: 現在の範囲の上限
toLow: 変換後の範囲の下限
toHigh: 変換後の範囲の上限
'''