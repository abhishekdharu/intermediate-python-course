import random
def main():
  dice_rolls = 2
  dice_sum = sum(random.randint(1, 6) for _ in range(dice_rolls))
  print(f'You rolled a {dice_sum}')

if __name__== "__main__":
  main()