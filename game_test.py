import game

def testgame_grid_no_input():
    expected_value = [[False, False, False,False],[ False, False,False, False],[ False,False, False, False],[False, False, False,False]]
    assert game.grid_view([]) == expected_value
    
def testgame_grid_input():
    expected_value = [[False, True, False,True],[ False, True,False, False],[ False,False, False, False],[False, False, False,False]]
    assert game.grid_view([1,3,5]) == expected_value

def testgame_grid_repeat_input():
    expected_value = [[False, True, False,True],[ False, True,False, False],[ False,False, False, False],[False, False, False,False]]
    assert game.grid_view([1,3,5,1]) == expected_value


def testposition_of_true_no_value(): 
    assert game.position_true( [[ False, False,False, False],
                                [ False,False, False, False],
                                [ False, False, False, False],
                                [False, False, False,False]]) == []

def testposition_of_true_multiple(): 
    assert game.position_true( [[ True, False,True, False],
                                [ False,False, False, False],
                                [ False, True, False, False],
                                [False, False, False,False]]) == [[0,0],[0,2],[2,1]]


def test_no_neighbour():
    def test_no_neighbour():

        nb_num, false_nb = game.neighbours( [[ True, False,True, False],
                                         [ False,False, False, False],
                                         [ False, True, False, False],
                                         [False, False, False,False]], [0,0])
        assert nb_num == 0
        assert  false_nb == [[0,1],[1,0],[1,1]]

def test_3_neighbours():
   nb_num, false_nb = game.neighbours( [[ True, False,True, False],
                                        [ False,True, False, False],
                                        [ False, True, False, False],
                                        [False, False, False,False]], [1,1])
   assert nb_num == 3
   assert  false_nb == [[0,1],[1,0],[1,2],[2,0],[2,2]]

def test_no_status_change():
   assert game.change_status( [[ True, True, False, False],
                               [ True,True, False, False],
                               [ False, False, False, False],
                               [False, False, False,False]]) == [[ True, True, False, False],
                               [ True,True, False, False],
                               [ False, False, False, False],
                               [False, False, False,False]]
   
def test_status_change():
    assert game.change_status( [[ False, False, False, False],
                               [ True,True, True, False],
                               [ False, False, False, False],
                               [False, False, False,False]]) == [[  False, True, False, False],
                               [ False,True, False, False],
                               [ False, True, False, False],
                               [False, False, False,False]]

