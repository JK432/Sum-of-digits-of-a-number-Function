# Write a Python function to find sum of digits of a number
def sum(n):
  s=0
  for i in n:
    s=s+int(i)
  print(s)

x=input()
sum(x)