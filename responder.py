print(
"""I'm Yuhao Zheng
This is my first program -- responder
""")
while True:
 x=raw_input('Please Enter:')
 if x=='end':break
 try:
  y=float(x)
  if y%1>0:
   print ('This is a float')
  else:
   print ('This is an integer')
 except ValueError, e:
  print ("This is a string")
