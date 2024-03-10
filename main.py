def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, num_words, chars_sorted_list)

def print_chars(chars_sorted_list):
  s = ""
  for d in chars_sorted_list:
    if not d["char"].isalpha():
      continue
    s += f"The '{d["char"]}' was found {d["num"]} times\n"
  return s[:-2]

def print_report(path, words, chars_sorted_list):
  print(f"--- Begin report of {path} ---")
  print(f"{words} words found in the document\n")
  print(f"{print_chars(chars_sorted_list)}")
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)

def sort_on(dict):
  return dict["num"]

def chars_dict_to_sorted_list(dict):
  sorted_list = []
  for c in dict:
    sorted_list.append({"char": c, "num": dict[c]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def get_book_text(path):
  with open(path) as f:
    return f.read()
  

main()

