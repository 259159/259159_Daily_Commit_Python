
txt = input('Enter a sentence')

txt_list = txt.split(" ")



dictman= {i:len(i) for i in txt_list}

maxman = max(dictman[i] for i in txt_list)

for i in dictman:
  if dictman[i] == maxman:
    print(i)
