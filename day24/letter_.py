#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"day24/Input/Letters/starting_letter.txt", mode='r') as starting_letter:
    base_letter = starting_letter.read()

with open(r"day24/Input/Names/invited_names.txt", mode='r') as invited_names:
    invited_people = invited_names.readlines()
    
for name in invited_people:
    name = name.split('\n')[0]
    print(name)
    with open(fr'day24/Output/{name}_invitation.txt', mode='w') as output_invitation:
        output_invitation.write(base_letter.replace('[name]', name))
