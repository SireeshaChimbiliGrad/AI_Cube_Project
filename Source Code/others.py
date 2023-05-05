from Puzzle import State, move

def makeNearGoal():
    cube = State()
    cube.set_top([['White','White','White'],['White','White','White'],['White','White','White']])
    cube.set_bottom([['Blue','Blue','Blue'],['Blue','Blue','Blue'],['Blue','Blue','Blue']])
    cube.set_left([['Orange','Orange','Orange'],['Green','Green','Green'],['Green','Green','Green']])
    cube.set_right([['Green','Green','Green'],['Orange','Orange','Orange'],['Orange','Orange','Orange']])
    cube.set_front([['Red','Red','Red'],['Yellow','Yellow','Yellow'],['Yellow','Yellow','Yellow']])
    cube.set_back([['Yellow','Yellow','Yellow'],['Red','Red','Red'],['Red','Red','Red']])
    for action in cube.actions:
        new_s = move(cube, action)
        print(action)
        if new_s.isGoalState():
            print("executing the " + action + " action resulted in the below goal state " + str(new_s))
    # print(cube)    
    # print(move(cube, 'top'))
            

        

makeNearGoal()