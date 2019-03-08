import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
#bai 1
print('bai1 :')
list_1 = [2,6,7,8,8]
print(type(list_1))
np_list1 = np.array(list_1)
print(np_list1.dtype)
np_list2 = np.array(list_1, dtype = np.int16)
print(np_list2.dtype)

#bai2
print('bai2 :')
tuple_ = (1,3,4)
print(type(tuple_))
np_tuple1 = np.array(tuple_)
print(np_tuple1)
print(np_tuple1.dtype)

#bai3
np_3 = np.array([2,3,4,6,8,9,7,3,5,12,6,98])
np_3_reshape = np_3.reshape(4,3)
print('bai3 :')
print(np_3_reshape)
np_3.resize(4,3)
print(np_3)

np_32 = np.arange(18)
print(np_32.reshape(3,6))
print(np_32.reshape(6,3))
# print(np_32.reshape(3,7))

#bai 4
np_4 = np.random.randint(1,100,(3,6))
print('bai4 :')
print(np_4)
print('shape :',np_4.shape)
print('ndim :',np_4.ndim)
print('itemsize :', np_4.itemsize)
print('type :', np_4.dtype)
print('size :', np_4.size)

#bai 5
print('bai5 :')
np_zero_df = np.zeros((3,6))
print(np_zero_df)
np_zero = np.zeros((3,6), dtype = np.int16)
print(np_zero)
np_one_df = np.ones((3,6))
print(np_one_df)
np_one = np.ones((3,6), dtype = np.int16)
print(np_one)
np_empty_df = np.empty((3,6))
print(np_empty_df)
np_empty = np.empty((3,6), dtype = np.int16)
print(np_empty)

#bai 6
list_a = [2,5,8,9,6]
list_b = [3,5,8,7,4]
np_list6 = np.array((list_a, list_b))
print('bai6 :')
print(np_list6)

#bai 7
A = np.array([[2,5], [3,4]])
B = np.array([[9,8], [5,3]])
column_join = np.concatenate((A, B), axis=0)
row_join = np.concatenate((A, B), axis=1)
print('bai7 :')
print(column_join)
print(row_join)

#bai 8
np_7 = 3*np.arange(1,13).reshape(3,4)
print('bai8 :')
print(np_7)

#bai 9
print('bai9 :')
length = np.array([1,4,6,9,11,10])
width = np.array([2,3,7,4,10,12])
areas = length*width
print('areas :', areas)
A = np.array([34,56,32,87,65,29])
B = np.array([26,78,45,38,85,92])
C = A>B
print(C)
radius = np.array([[12,24.5,23.5,26.7,30,19.4,25.6]])
areas_circle = np.pi*radius[radius>25]**2
print('areas circle with radius > 25 :', areas_circle)
#bai 10
np_10 = np.array([[10,3],[5,2],[6,4]])
print('bai10 :')
np_10_assigning = np_10
np_10_copy = np_10.copy()
np_10_view = np_10.view()
print('assigning: np_10_assigning is np_10:', np_10_assigning is np_10)
print('copy: np_10_ass is np_10:', np_10_copy is np_10)
print('view: np_10_ass is np_10:', np_10_view is np_10)
np_10_copy[0,0] = 20
print('modified with copy:', np_10)
np_10_view[0,0] = 20
print('modified with view:', np_10)

#bai 11
np_11 = np.arange(16).reshape(4,-1)
print('bai11 :')
print(np_11)
print('indexing :', np_11[3,-1])
print('slicing :', np_11[1:2,0:2])
a = np.array([2,5,9])
b = np.array([10,4,9])
print('Boolean :', a >= b)


#bai 12
print('bai12 :')
array_a = np.random.randint(1,1001, (100))
print('array_a :', array_a)
rand_a = np.random.choice(array_a, 10)
print('rand_a :', rand_a)
array_b = np.arange(1,51)
print('array_b :', array_b)
for i in range(10):
	np.random.shuffle(array_b)
	print('array_b {}th: {}'.format(i,array_b))
for i in range(5):	
	b_duplicate = np.random.choice(array_b, 10)
	print('b_duplicate {}th: {}'.format(i,b_duplicate))
for i in range(5):	
	b_noduplicate = np.random.choice(array_b, 10, replace = False)
	print('b_noduplicate {}th: {}'.format(i,b_noduplicate))

#bai 13
array_13 = np.random.randint(1,51,(100))
print('bai13 :')
print(array_13)
unique_13, count_13 = np.unique(array_13, return_counts=True)
print('unique_13:', unique_13)
dict_count = dict(zip(unique_13, count_13))
print('dict_count:', dict_count)
dict_count_3 = unique_13[count_13>3]
count_3 = count_13[count_13>3]
print('array have count large 3 is {}'.format(dict(zip(dict_count_3, count_3))))


#bai 14
print('bai14 :')
np_14 = np.random.randint(0,6,(30))
print('np_14 :',np_14)
unique_14, count_14 = np.unique(np_14, return_counts=True)
max_fv = unique_14[count_14 == np.max(count_14)]
max_fv_count = count_14[count_14 == np.max(count_14)]
print('most frequent value: {} with count: {}'.format(max_fv[0], max_fv_count[0]))
np2_14 = np.random.randint(40,101,(20))
print('np2_14 :', np2_14)
np2_14_sort = np.sort(np.unique(np2_14))[::-1]
print('3 max in np2_14 :', np2_14_sort[0:3])
np2_14[np2_14==np.max(np2_14)] = -1
print('array replace max by -1:', np2_14)

#bai 15
print('bai15 :')
array_roll = np.zeros((30,4))
step = 0
while int(np.sum(array_roll)) < 100:
	print('step_', step)
	for player in range(4):
		array_roll[step,player] = np.random.randint(1,7)
		print('player {} roll score {} with sum:{}'.format(player, int(array_roll[step,player]), int(np.sum(array_roll))))
		if int(np.sum(array_roll)) >= 100:
			print('winner {} with step {} have array :\n {}'.format(player, step, array_roll[0:step+1, :]))
			break	
	step += 1

#bai 16
print('bai16 :')
# method 1
with open('song.txt', 'r') as file:
	page = file.read()
	file.close()

soup = BeautifulSoup(page, 'html.parser')
soup_view = soup.find(class_ = 'wikitable').find_next('tbody')
song_l = np.array([i.find('td').text.strip()[1:-1] for i in soup.find('table', class_ = re.compile('wikitable')).find_all('tr')[1:101]])
print(len(song_l))
# method 2	
song_l = []
driver = webdriver.Chrome('C:/Users/Training/Desktop/13.PYTHON/chrome/chromedriver.exe')
link = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2018'
driver.get(link)
content = driver.find_element_by_xpath("//table[contains(@class, 'wikitable')]/descendant::tbody[1]").text
song_l = content.split('\n')
song_l = [i[i.find('"')+1:] for i in song_l]
song_l = np.array([i[:i.find('"')] for i in song_l])


listening = np.random.randint(100,1001,(100))
print('Interested: ', song_l[listening>=800])
print('-----------------------------')
print('Normal: ', song_l[np.logical_and(listening>=500,listening<800)])
print('-----------------------------')
print('Not Interested: ', song_l[listening<500])
print('-----------------------------')

#bai 17
print('bai17 :')
for time in range(10):
	roll = reach = np.zeros(1)
	playerNumber = np.random.randint(2,100, (1))	
	step = player = 0
	while int(np.sum(reach)) < 50:
		player = player%playerNumber
		add = int(np.random.randint(1,7))
		roll = np.insert(roll, roll.shape[0], add)
		if add == 1:
			if int(np.sum(reach)) == 0:
				reach = np.insert(reach, reach.shape[0], 0)
				print('step {} player {} with roll {} at step 0 for sum 0'.format(step, player, add))
			else:
				reach = np.insert(reach, reach.shape[0], -1)
				print('step {} player {} with roll {} then backward -1 for sum {}'.format(step, player[0], add, int(np.sum(reach))))
		elif add in [2,3,4,5]:
			reach = np.insert(reach, reach.shape[0], 1)
			print('step {} player {} with roll {} then forward 1 for sum {}'.format(step, player[0], add, int(np.sum(reach))))
		else:
			reach = np.insert(reach, reach.shape[0], 0)
			print('step {} player {} with roll 6 then roll one again for sum {}'.format(step, player[0], int(np.sum(reach))))
			step += 1
			add_6 = int(np.random.randint(1,7))
			reach = np.insert(reach, reach.shape[0], add_6)
			roll = np.insert(roll, roll.shape[0], add_6)
			print('step {} player {} with roll {} then forward {} for sum {}'.format(step, player[0], add_6, add_6, int(np.sum(reach))))
		player += 1
		step += 1
	print('roll :', roll)
	print('reach :', reach)
	print('Time {} Have {} player in the game and player win is {} with step {}'.format(time, playerNumber[0], step, player[0]))
			
#bai 18
player_number = np.zeros((np.random.randint(2,1000,(1))))
player = 0
turn = 0
print('bai18 :')
while np.max(player_number) < 100:
	if player == len(player_number): player = 0
	hold = np.random.randint(0,10) #if hold != 0 then hold else next player
	if hold != 0:
		roll = np.random.randint(1,7)
		if roll != 1:
			player_number[player] += roll			
			print('Turn {}: player {}th will hold and roll {} have sum is {}'.format(turn, player, roll, int(player_number[player])))
			turn += 1
			time.sleep(np.random.random())
		else:
			player_number[player] = 0						
			print('Turn {}: player {}th will hold and roll 1 have sum is 0'.format(turn, player))
			turn += 1
			player += 1
			time.sleep(np.random.random())
	else:
		print('Turn {}: player {}th will not hold and turn next player'.format(turn, player))
		player += 1
		turn += 1		
		time.sleep(np.random.random())
print('number of player is: ' + str(len(player_number)))	
print('player winner is: ' + str(player) + ' with turn: ' + str(turn))
print('player score is:', player_number)

#bai 19
# player random interger from 1 to 20 number, have 7 prize:
# special prize(1 number have 5 digits)
# first prize(1 number have 5 digits)
# second prize(2 number have 5 digits)
# third prize(6 number have 5 digits)
# four prize(4 number have 4 last digits)
# five prize(6 number have 4 last digits)
# six(prize(3 number have 3 last digits)
#seven(prize(7 number have 2 last digits)
import numpy as np
specialToThird = np.random.choice(np.arange(10000, 100000), 10, replace=False)
fourFive = np.random.choice(np.arange(1000, 10000), 10, replace=False)
specialPrize = specialToThird[0]
FirstPrize = specialToThird[1]
secondPrize = specialToThird[2:4]
thirdPrize = specialToThird[4:]
fourPrize = fourFive[:4]
fivePrize = fourFive[4:]
sixPrize = np.random.choice(np.arange(100, 1000), 3, replace=False)
sevenPrize = np.random.choice(np.arange(10, 100), 4, replace=False)



userSelection = 0
numberSelection = np.zeros(np.random.randint(1,21,(1)), dtype = int)
print('thirdPrizei19 :')
print('Number of selection: ', str(len(numberSelection)))
for numberOfSelection in range(len(numberSelection)):
	while True:
		userSelection = input('fill number have 5 digits: ')
		try:
			userSelection = int(userSelection)
			if len(str(userSelection)) != 5:
				continue
			else:
				print('valid number!')
				numberSelection[numberOfSelection] = int(userSelection)
				break
		except ValueError:
			print('')
	
print('num of selection: ', numberSelection)
print('specialPrize: ', specialPrize)
print('FirstPrize: ', FirstPrize)
print('secondPrize: ', secondPrize)
print('thirdPrize: ', thirdPrize)
print('fourPrize: ', fourPrize)
print('fivePrize: ', fivePrize)
print('sixPrize: ', sixPrize)
print('sevenPrize: ', sevenPrize)
for selection in numberSelection:
	print('Number: ', str(selection))
	if int(selection) == specialPrize:
		print('get special Prize!')
		continue
	elif int(selection) == FirstPrize:
		print('get First Prize!')
		continue
	elif int(selection) in secondPrize:
		print('get second Prize!')
		continue
	elif int(selection) in thirdPrize:
		print('get third Prize!')
		continue
	elif int(str(selection)[1:]) in fourPrize:
		print('get four Prize!')
		continue
	elif int(str(selection)[1:]) in fivePrize:
		print('get five Prize!')
		continue
	elif int(str(selection)[2:]) in sixPrize:
		print('get six Prize!')
		continue
	elif int(str(selection)[3:]) in sevenPrize:
		print('get seven Prize!')
		continue
	else:
		print('No prize!')
#bai 20
#random from 2 to 500 player to draw a box have ticket from 1 to 10000 to get random from 1 to
#5 prize. player can reject our draw. the game end when nobody play or player get all prize.
playerPrize = {}
numberRand = np.random.randint(1,1001,(np.random.randint(1,6)))
nr = numberRand.tolist()
print(numberRand.tolist())
playerNumber = np.zeros(np.random.randint(2,500,(1)), dtype=int)
indexPlayer = np.arange(len(playerNumber))
listTick = np.arange(1,10001)
print('bai20 :')
print('prize list:', numberRand)
print('number of player: ', len(playerNumber))
turn = 0
while len(numberRand) != 0 and len(listTick) != 0 and len(indexPlayer) != 0:
	playerDraw = np.random.choice(listTick, indexPlayer.shape[0], replace = False)
	dictPlayer = dict(zip(indexPlayer, playerDraw))
	print('turn: {}, ticket of player draw: {}'.format(turn, dictPlayer))
	for ticket in playerDraw:
		if ticket in numberRand:
			playerPrize[int(indexPlayer[playerDraw==ticket][0])] = ticket
			print('--------------------------------------------')
			print('player {}th get prize {} with number {}'.format(indexPlayer[playerDraw==ticket][0], nr.index(int(ticket)), ticket))
			print('--------------------------------------------')
			indexPlayer = indexPlayer[playerDraw!=ticket]
			playerDraw = playerDraw[playerDraw!=ticket]
			numberRand = numberRand[numberRand != ticket]
		listTick = listTick[listTick != ticket]

	holdOrRemove = np.random.randint(0,100,(playerDraw.shape[0])) #if 0 is remove and other is hold
	playerDraw = playerDraw[holdOrRemove!=0]
	indexPlayer = indexPlayer[holdOrRemove!=0]
	holdOrRemove = holdOrRemove[holdOrRemove!=0]
	turn += 1
	time.sleep(np.random.random())
	print('.')
	time.sleep(np.random.random())
	print('..')
	time.sleep(np.random.random())
	print('...')

print(playerPrize)
if playerPrize == {}:
	print('nobody get prize!')
else:
	for key, value in playerPrize.items():
		print('play {}th get prize {} with ticket is {}'.format(key, nr.index(int(value)), value))