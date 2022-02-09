import game

def test_game_grid_no_input():
    expected_value = [[False, False, False],[ False, False,False],[ False,False,False]]
    assert game.grid_view([]) == expected_value
    
def test_game_grid_input():
    expected_value = [[False, True, True],[ False, True,False],[False, False, False]]
    assert game.grid_view([1,2,4]) == expected_value

def test_game_grid_repeat_input():
    expected_value = [[False, True, True],[ False, True,False],[ False,False, False]]
    assert game.grid_view([1,2,4]) == expected_value

def test_position_of_true_no_value(): 
    assert game.position_true( [[ False, False,False],
                                [ False,False, False],
                                [ False, False, False],
                                ]) == []

def test_position_of_true_multiple(): 
    assert game.position_true( [[ True, False,True],
                                [ False,False, False],
                                [ False, True, False]
                                ]) == [[0,0],[0,2],[2,1]]