import random

print "Welcome to WH game!"
print "It's so simple, you're gonna answer my questions and at the end get silly sentences."
print "First, tell me how many people are playing this game?"

player_count = 0

while player_count == 0:
	next = raw_input("> ")
	if next.isdigit():
		player_count = int(next)
	else:
		print "Type a valid number:"

print "Now introduce me the players:"

players = []
for i in range(1, player_count + 1):
	print "Player %d is: " % i
	player = raw_input("> ")
	players.append(player)
	i += 1

print "Good job! Now let's ask players about time."


whenlist = []
for player in players:
	print " %r  tell me when?" % player
	when = raw_input("> ")
	whenlist.append(when)

print "Alright, Now let's ask players about location."

wherelist = []
for player in players:
	print " %r , tell me where?" % player
	where = raw_input("> ")
	wherelist.append(where)

print "Partners!"

wholist = []
for player in players:
	print " %r , tell me with who?" % player
	who = raw_input("> ")
	wholist.append(who)

whatlist = []
print "And finaly, What was happening?"
for player in players:
	print " %r, tell me what were you doing?" % player
	what = raw_input("> ")
	whatlist.append(what)

print "Ok , now let's see the resaults:"

for player in players:
	when = random.choice(whenlist)
	who = random.choice(wholist)
	what = random.choice(whatlist)
	where = random.choice(wherelist)
	sentece = "%s, %s and %s were %s %s " % (when, who, player, what, where)
	print sentece
	whenlist.remove(when)
	wholist.remove(who)
	whatlist.remove(what)
	wherelist.remove(where)


