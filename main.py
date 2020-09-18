def digit_sum(n):
  if n == 0:
    return n;
  else:
    return (n % 10 + digit_sum(n//10));

def run():
  askInt = int(input("Enter an int: "))
  print(f"sum of digits of {askInt} is {digit_sum(askInt)}.")

if __name__ == "__main__": 
  run()
