
def WinRate():
	print("WinRate MLBB Calc by Lorentz 2.0")
	LTR_Match = int(input("Total Match: "))
	LTR_Winrate = float(input("Winrate Now: "))
	LT_Req = float(input("Winrate Goal: "))
	LTR_Win = LTR_Match * (LTR_Winrate / 100)
	LTR_Lose = LTR_Match - LTR_Win
	LTR_sWr = 100 - LT_Req
	LT_Res = 100 / LTR_sWr
	s100 = LTR_Lose * LT_Res
	LTR_pr = s100 - LTR_Match
	print("You Need",int(LTR_pr),"Match Without Losing to get a Winrate rate of:",int(LT_Req))
	
def TotalWin():
	print("Total Win Calc by Lorentz 2.0")
	Match = int(input("Total Match: "))
	Winrate = float(input("Winrate Total: "))
	Win = Match * (Winrate / 100) + 0.1 + 0.1
	Lose = Match - Win + 0.1 + 0.1 + 0.1
	print("Total Win: ",int(Win), "Total Lose: ",int(Lose))
	
start = str(input('''Tool by Lorentz
1. Calc Winrate
2. Calc Total Win/Lose
3. Exit
'''))

if (start == "1"):
	WinRate()
if (start == "2"):
	TotalWin()
if (start == ""):
	exit()
	