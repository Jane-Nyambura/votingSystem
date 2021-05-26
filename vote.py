vote=input("Uhuru or Ruto?")

n_vote=vote.upper()
vote_file=open('vote.txt','a')

if(n_vote=="RUTO"):
    print("Vote has been recoded")
    vote_file.write("RUTO, ")
elif(n_vote=="UHURU"):
    print("vote has been recoded")
    vote_file.write("UHURU, ")
else:
    print("Thats not a valied choice")


vote_file.close()
