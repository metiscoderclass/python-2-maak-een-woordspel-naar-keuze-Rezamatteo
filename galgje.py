import time
import random
looping=True
welke=""
cpkiezen=False
dupes=0
speler1gewonnen=0
speler2gewonnen=0
looped=0
woord=""
lettersright=[]
woordindexdifficulty1=['hallo,','wereld','mens','ei']
woordindexdifficulty2=['limousine','familie','computer']
woordindexdifficulty3=['kippeneieren','computermuis','tafeltennis']


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word





def find_dupes(word,letter):
	dupes=[]
	for letter in word:
		if word.count(letter)>1 and letter not in dupes:
			dupes.append(letter)
	return dupes



speler1=input("speler 1 wat is je naam?")
speler2=input("speler 2 wat is je naam?")
while looping:
	print(woordindexdifficulty1,woordindexdifficulty2,woordindexdifficulty3)
	loaded_data=None
	dupes=0
	lettersright=[]
	looped+=1
	canguess="ja"
	loop=True
	letters=90
	badguess=0
	guessed=[" "]
	guessedright=0
	hoeveelsetguess=1
	previousguessbutguessform=""
	previousguess=" "
	previousindex=""
	difficulty=""
	if looped==0:
		print("welkom bij galgje")
	else:
		print("hallo, welkom alweer bij galgje")
	
	#alles hiervoor zet gewoon de variables. alles in de loop mag steeds gereset worden en alles buiten de loop niet
	
	print("de stand is nu "+str(speler1gewonnen)+"-"+str(speler2gewonnen))
	welke=input("wil je zelf kiezen of wil je dat de computer voor je kiest?")
	if "zelf" in welke:
		if looped%2==0:
			woord=input(f"{speler2} wat moet het woord zijn? ")
		else:
			woord=input(f"{speler1} wat moet het woord zijn? ")
	else:
		cpkiezen=True
	if woord=="qq":
		print("okee...")
		print("de uiteindelijke stand is geworden "+str(speler1gewonnen)+"-"+str(speler2gewonnen))
		loop=False
		canguess="nee"
		looping=False
		#hierstopt hij gewoon het programma als je qq intypt
	else:
		print("\n"*10000)
		difficulty=input("voor we beginnen wat moet de difficulty zijn, makkelijk, normaal of moeilijk? ")
		if difficulty=="makkelijk":
			diff=1
		elif difficulty=="normaal":
			diff=2
		else:
			diff=3
		if cpkiezen==True:
			if diff==1:
				woord=random.choice(woordindexdifficulty1)
			elif diff==2:
				woord=random.choice(woordindexdifficulty2)
			elif diff ==3:
				woord=random.choice(woordindexdifficulty3)
			print(woord)
		start_time = time.time()	
		if looped%2==0:
			print(f"oke {speler2}, het woord dat je moet raden heeft ", len(woord),  " letters")
		else:
			print(f"oke {speler1}, het woord dat je moet raden heeft ", len(woord),  " letters")
		print("_ "*len(woord))
		letters=len(woord)
		#dit gedeelte (was gek genoeg super makkelijk) zorgt er eerst voor dat de tweede speler niet kan spieken bij de eerste speler en typt even veel underscore als er letters zijn in het woord

		while loop==True:
			dupes=0
			print("\n"*100)
			if guessedright==len(woord):
				#dit activeert zodraa je alle letters die in het woord zijn zijn geraden
				cangues="nee"
				if difficulty=="makkelijk":
					guessedwoord=woord
				elif difficulty=="normaal":
					guessedwoord=input(f"Nu je alle letters hebt zal je het woord moeten raden. en nog een keer als reminder, dit zijn je letters: {lettersright}. Dus wat is het woord volgens jou? ")
				else:
					guessedwoord=input("nu je alle letters hebt kan je het woord gaan raden!")
				if guessedwoord==woord:
					end_time = time.time()
					elapsed_time_seconds = end_time - start_time
					elapsed_time_struct = time.gmtime(elapsed_time_seconds)
					elapsed_time_formatted = time.strftime("%H:%M:%S", elapsed_time_struct)
					print("you took",elapsed_time_formatted,"to guess the word")
					win_score=1+diff*1000/elapsed_time_seconds
					
					win_score=round(win_score)
					if win_score<1:
						win_score=1
					elif win_score>9:
						win_score=10
					if looped%2==0:
						speler2gewonnen+=win_score
					else:
						speler1gewonnen+=win_score
					couldofniet=input("wil je dit woord aan de computers lijst toevoegen?")
					if diff==1:
						woordindexdifficulty1.append(woord)
					elif diff==2:
						woordindexdifficulty2.append(woord)
					elif diff==3:
						woordindexdifficulty3.append(woord)
						
							
				else:
					print("__________")
					print("|        |")
					print("|       ( )")
					print("|       -|-")
					print("|       /|")
					print("|")
					print("|")
					print("|_______")
					loop=False
					
					if looped%2==0:
						print(f"aww sorry maar je hebt verloren {speler2}, het woord was: {woord}" )
						speler1gewonnen+=1
					else:
						print(f"aww sorry maar je hebt verloren {speler1}, het woord was: {woord}" )
						speler2gewonnen+=1
				
				loop=False
			
			else:
				canguess="ja"
				if badguess==9:
					print("__________")
					print("|        |")
					print("|       ( )")
					print("|       -|-")
					print("|       /|")
					print("|")
					print("|")
					print("|_______")
					loop=False
					if looped%2==0:
						print(f"aww sorry maar je hebt verloren {speler2}, het woord was: {woord}" )
						speler1gewonnen+=1
					else:
						print(f"aww sorry maar je hebt verloren {speler1}, het woord was: {woord}" )
						speler2gewonnen+=1
			while canguess=="ja":
				if hoeveelsetguess>=1 and hoeveelsetguess!=1:
					print(previousguess)
					if previousguess in woord:
						dupes=find_dupes(woord,guess)
						
						previousindex=woord.index(previousguess)
						previousindex+=1
						# previousindex is de hoeveelste letter in het woord je laatste gok was. ik doe er 1 bij omdat het anders 1 te laag is :)
						if difficulty=="makkelijk":
							pass
						elif difficulty=="normaal":
							print(f"je vorige gok, {previousguess},was de "+str(previousindex)+"e letter van het woord!")
						if previousguess in dupes and difficulty=="normaal":
							print(f"{previousguess} komt meer dan een keer voor in dit woord")
						volledigevorigeguess=f"{previousguess} {previousindex}"
						#volledigevorigeguess is je vorige gok en de hoeveelste letter het was in het woord
						lettersright.append(volledigevorigeguess)
						# .append zorgt ervoor dat die gokken worden toegevoegd aan een lijst
						if difficulty=="normaal":
							print(f"je letters waren: {lettersright}")
						#die lijst wordt hier geprint
						
						print("_ "*len(woord))
					else:
						print("je vorige gok zat helaas niet in het woord")
						print("en even als reminder er zijn "+str(len(woord))+" letters")
				
				if difficulty=="makkelijk":
					print("het woord dat je tot nu toe hebt is:",display_word(woord,guessed))
				elif difficulty=="normaal":
					print(f"je letters waren: {lettersright}")
				
				guess=input("ok, dus wat is je "+str(hoeveelsetguess)+"e gok? ")
				hoeveelsetguess+=1
				if not guess in guessed:
					if len(guess)>=1 and not len(guess)==1:
						print("sorry, je kan maar 1 letter per keer raden")
						#hier check ik of er meer dan een letter in je guess zit
					elif len(guess)==1:
						if guess in woord:
							if guess.isalpha():
								print("goed!")
								guessedright+=woord.count(guess)
								letters-=1
								guessed.append(guess)
								previousguess=guess
								previousguessbutguessform=guess
								canguess="nee"
								#hier zorg ik ervoor dat je eerst krijgt te zien dat je het goed had en welke je goed had en welke je daarvoor al goed had voordat je weer koet raden
							else:
								print("sorry, maar je mag alleen maar letters invoeren")
								#"isalpha" kijkt of de guess in het alphabet zit
						elif not guess in woord:
							if guess.isalpha():
								badguess+=1
							
								print("nee sorry die zit er niet in")
								previousguess="\n"
							else:
								print("sorry je mag alleen maar letters invoeren")
						if badguess==1:
							print("")
							print("")
							print("")
							print("")
							print("")
							print("")
							print("")
							print("|_______")
						elif badguess==2:
							print("_")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|_______")
						elif badguess==3:
							print("__________")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|_______")
						elif badguess==4:
							print("__________")
							print("|        |")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|_______")
						elif badguess==5:
							print("__________")
							print("|        |")
							print("|       ( )")
							print("|")
							print("|")
							print("|")
							print("|")
							print("|_______")
						elif badguess==6:
							print("__________")
							print("|        |")
							print("|       ( )")
							print("|        |")
							print("|")
							print("|")
							print("|")
							print("|_______")
						elif badguess==7:
							print("__________")
							print("|        |")
							print("|       ( )")
							print("|       -|-")
							print("|")
							print("|")
							print("|")
							print("|_______")
						elif badguess==8:
							print("__________")
							print("|        |")
							print("|       ( )")
							print("|       -|-")
							print("|       /")
							print("|")
							print("|")
							print("|_______")
						
						elif badguess==9:
							canguess="ja"
							print("__________")
							print("|        |")
							print("|       ( )")
							print("|       -|-")
							print("|       /|")
							print("|")
							print("|")
							print("|_______")
							loop=False
							if looped%2==0:
								print(f"aww sorry maar je hebt verloren {speler2}, het woord was: {woord}" )
								speler1gewonnen+=1
							else:
								print(f"aww sorry maar je hebt verloren {speler1}, het woord was: {woord}" )
								speler2gewonnen+=1
							canguess=False
							exit
						#al die if badguess id dit dingen kijken gewoon in welke state de strop is
						guessed.append(guess)
						#dit zorgt evoor dat je guess wordt toegevoegd aan een lijst
				else:
					print("sorry, maar die heb je al geraden")
					#als je guess dan in die lijst staat dan krijg je dit te zien
					previousguess="\n"
