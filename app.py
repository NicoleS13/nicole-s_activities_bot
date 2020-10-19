print("Title of program: Activities bot")
print()
while True:
  description = input("Could you describe what you feel like doing in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  activities_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "fun":
      feelings_list.append("fun")
      activities_list.append("playing some sports or some computer games")
      counter += 1
    if each_word == "chill":
      feelings_list.append("chill")
      activities_list.append("listening to music or watch a movie")
      counter += 1
    if each_word == "with others":
      feelings_list.append("with others")
      activities_list.append("going out and have fun with them, watch a movie or go skating")
      counter += 1
    if each_word == "entertaining":
      feelings_list.append("entertaining")
      activities_list.append("watching youtube")
      counter += 1
    if each_word == "enlightening":
      feelings_list.append("enlightening")
      activities_list.append("reading a book or learning something new")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you feel like doing something " + feelings_list[0] + ". Try "+ activities_list[0] + "! Hope these activites are good :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
