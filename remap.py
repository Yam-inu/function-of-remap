def remap(x,in_min,in_max,out_min,out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

'''
remap(value,currentlyMin,currentlyMax,convertedMin,convertedMax)

value: 変換したい数値(変数)/Value to convert(variable)
currentlyMin: 現在の範囲の下限/minimum of currently range
currentlyMax: 現在の範囲の上限/maximum of currently range
convertedMin: 変換後の範囲の下限/minimum of converted range
convertedMax: 変換後の範囲の上限/maximum of converted range

*example*
import remap
x=50
remap.remap(x,0,100,80,255)
remap.remap(x,1,-1,0,100)
remap.remap(x,0,100,100,0)
'''
