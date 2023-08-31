import random
def generate_password(words):
  """Generates a random password based on the user's input.
  Args:
    words: A list of words that the user enters.
  Returns:
    A random password based on the user's input.
  """
  # Create a list of all the characters in the user's input.
  characters = []
  for word in words:
    characters.extend(list(word))
  # Shuffle the characters.
  random.shuffle(characters)
  # Create a password using the first character of each word.
  password = ""
  for word in words:
    password += word[0]
  # Add a random number to the end of the password.
  password += str(random.randint(0, 9))
  # Return the password.
  return password
if __name__ == "__main__":
  # Get the user's input.
  words = input("Enter a few words separated by commas: ").split(",")
  # Generate a random password based on the user's input.
  password = generate_password(words)
  # Print the password.
  print(f"Your password is: {password}")
