import runHand

# Hand finished after initial deal conditions.
def test_tie():
    assert runHand.baccaratHand(8, 8, 0, 0) == {"Player": 8, "Banker": 8}

def test_player_win():
    assert runHand.baccaratHand(9, 5, 0, 0) == {"Player": 9, "Banker": 5}

def test_player_win_bank_natural():
    assert runHand.baccaratHand(9, 8, 0, 0) == {"Player": 9, "Banker": 8}

def test_bank_win():
    assert runHand.baccaratHand(6, 9, 0, 0) == {"Player": 6, "Banker": 9}

def test_bank_win_player_natural():
    assert runHand.baccaratHand(8, 9, 0, 0) == {"Player": 8, "Banker": 9}

def test_bank_win_7_6():
    assert runHand.baccaratHand(6, 7, 0, 0) == {"Player": 6, "Banker": 7}

def test_player_win_7_6():
    assert runHand.baccaratHand(7, 6, 0, 0) == {"Player": 7, "Banker": 6}

# Player stand
def test_player_stand1():
    assert runHand.baccaratHand(7, 2, 0, 10) == {"Player": 7, "Banker": 2}

def test_player_stand2():
    assert runHand.baccaratHand(7, 2, 0, 5) == {"Player": 7, "Banker": 7}

def test_player_stand3():
    assert runHand.baccaratHand(6, 2, 0, 9) == {"Player": 6, "Banker": 1}

# Banker stand
def test_banker_stand1():
    assert runHand.baccaratHand(3, 7, 1, 0) == {"Player": 4, "Banker": 7}

def test_banker_stand2():
    assert runHand.baccaratHand(0, 7, 10, 0) == {"Player": 0, "Banker": 7}

def test_banker_stand3():
    assert runHand.baccaratHand(4, 7, 6, 0) == {"Player": 0, "Banker": 7}

# Player draw
def test_player_draw1():
    assert runHand.baccaratHand(2, 1, 3, 10) == {"Player": 5, "Banker": 1}

def test_player_draw2():
    assert runHand.baccaratHand(5, 0, 7, 5) == {"Player": 2, "Banker": 5}

def test_player_draw3():
    assert runHand.baccaratHand(2, 2, 3, 4) == {"Player": 5, "Banker": 6}

def test_player_draw4():
    assert runHand.baccaratHand(0, 0, 10, 10) == {"Player": 0, "Banker": 0}

def test_player_draw5():
    assert runHand.baccaratHand(3, 0, 3, 10) == {"Player": 6, "Banker": 0}

# Banker draw
def test_banker_draw3():
    assert runHand.baccaratHand(2, 3, 3, 10) == {"Player": 5, "Banker": 3}

def test_banker_draw3_stand():
    assert runHand.baccaratHand(0, 3, 8, 6) == {"Player": 8, "Banker": 3}

def test_banker_draw4():
    assert runHand.baccaratHand(4, 4, 4, 5) == {"Player": 8, "Banker": 9}

def test_banker_draw5():
    assert runHand.baccaratHand(5, 5, 6, 10) == {"Player": 1, "Banker": 5}

def test_banker_draw6():
    assert runHand.baccaratHand(1, 6, 7, 10) == {"Player": 8, "Banker": 6}


