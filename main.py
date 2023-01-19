import random
import numpy as np

class Color:
  purple = '\033[35;1m'
  green = '\033[32;1m'
  block_blue = '\033[1;34;7m'
  blue = '\033[34;1m'
  red = '\033[31;1m'
  yellow = '\033[0;33;1m'
  end = '\033[m'

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

positive_words = np.loadtxt("Positive Words List.txt", dtype = "str")
negative_words = np.loadtxt("Negative Words List.txt", dtype = "str")
profession_words = np.loadtxt("Professions List.txt", dtype = "str")
plural_nouns = np.loadtxt("plural nouns.txt", dtype = "str")

print()
print(Color.purple +
      r"  ////^\\\\\\\\")
print("    | ^   ^ |")
print("   @(o) (o) @")
print("   /  <     |")
print("   | \___/  |")
print("    \______/" +
      Color.end)
print()
print(Color.block_blue + "\n Welcome to Chadbot! \n\n" + Color.end)
def random_career():
  return random.choice(profession_words)
def feeling_response():
  random_response_A = random.randint(1, 3)
  random_response_B = random.randint(1, 3)

  while True:
    feeling = str.lower(input("\t"))
    if feeling in positive_words:
      if random_response_A == 1:
        print(Color.yellow + f"\nI'm glad to hear that, {name}!" + Color.end)
      elif random_response_A == 2:
        print(Color.yellow + "\nThat sounds spectacular!" + Color.end)
      elif random_response_A == 3:
        print(Color.yellow + "\nI can tell, it's rubbing off on me!" + Color.end)
      break
    elif feeling in negative_words:
      if random_response_B == 1:
        print(Color.yellow + f"\nI'm sorry to hear that, {name}!" + Color.end)
      elif random_response_B == 2:
        print(Color.yellow + "\nBummer, I hope you feel better soon!" + Color.end)
      elif random_response_B == 3:
        print(Color.yellow + "\nThat's a real shame, my condolences!" + Color.end)
      break
    else:
      print(Color.yellow + "\nSorry I didn't quite catch that! Could you say that again?\n" + Color.end)
def likes():
  random_noun = random.choice(plural_nouns)
  return Color.yellow + f"\nI like {random_noun}!\n" + Color.end

def age_response():
  while True:
    age = input("\n\t")
    if str.isnumeric(age):
      age = int(age)
      print()
      if age < 18: 
        print(Color.yellow + "Glad to see someone so young talking to this rusty old bucket!" + Color.end)
      elif age >= 18: 
        print(Color.yellow + "That's pretty interesting! Glad I got to know more about you!" + Color.end)
      break
    else:
      print(Color.yellow + "\nSorry I didn't quite catch that! Could you say that again?\n" + Color.end)

name = Color.green + input(Color.yellow + "Hello there, good sir! " +
              "\nMy name is Chadbot, I'm glad to see that you've chosen to run my program." +
              "\nIf you don't mind, could I please get your name? \n\n\t" + Color.end) + Color.end
print(Color.yellow + f"\nIt is quite the delight to meet you, {name}" + Color.yellow + "! " +
      Color.yellow + f"\nI've heard about a famous {random_career()} that has the same name as you, haha!")

print(Color.yellow + f"How are you feeling today, {name}" + Color.yellow + "?" + Color.red +
       get_super("\n*Chadbot will only accept one word responses\n") + Color.end)
feeling_response()

print(Color.yellow + f"How old are you, {name}" + Color.yellow + "? If you don't mind me asking.\n" + Color.end)
age_response()

print(Color.yellow + "\nI will now proceed to list a bunch of things that I like until you stop me! " + 
      "\nFeel free to join me! Type stop to exit." + Color.end)

while True:
  print(likes())
  answer = str.lower(input("\t"))
  if answer == "stop":
    print(Color.yellow + f"\nIt was nice to have your company, {name}!" + Color.end)
    break