with open("/home/santhosh/Downloads/Mail+Merge+Project+Completed/Mail Merge Project Completed/Input/Names/invited_names.txt") as namefile:
    names=namefile.readlines()

with open("/home/santhosh/Downloads/Mail+Merge+Project+Completed/Mail Merge Project Completed/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        striped_name= name.strip()
        
        letter1 = letter.replace("[name]",striped_name)
        
        with open(f"/home/santhosh/Downloads/Mail+Merge+Project+Completed/Mail Merge Project Completed/Output/ReadyToSend/letter_for_{striped_name}.txt",mode="r+") as output:
            completed=output.write(letter1)