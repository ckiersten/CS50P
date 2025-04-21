import project

def test_initialize_board():
    project.initialize_board()
    for r in range(len(project.board)):
        for c in range(len(project.board[0])):
            assert project.board[r][c] == "[ ]"

def test_place_pieces():
    project.reset()
    project.place_pieces("0,0")
    assert project.board[0][0] == "[X]"
    project.place_pieces("0,0")
    assert project.validMove == False
    project.place_pieces("cat,dog")
    assert project.validMove == False
    for r in range(len(project.board)):
        for c in range(len(project.board[0])):
            if r == 0 and c == 0:
                assert project.board[r][c] == "[X]"
            else:
                assert project.board[r][c] == "[ ]"

def test_reset():
    project.reset()
    for r in range(len(project.board)):
        for c in range(len(project.board[0])):
            project.place_pieces(f"{r},{c}")
            project.check_finished()
            if project.finished:
                break
    assert project.round == 8
    project.reset()
    assert project.round == 1
    assert project.finished == False
    assert project.validMove == False

def test_check_finished():
    project.reset()
    project.check_finished()
    assert project.finished == False
    #when no win
    project.place_pieces("0,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("2,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,2")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,2")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("2,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("2,2")
    project.check_finished()
    assert project.finished == True
    #diagonal win top left to bottom right
    project.reset()
    project.place_pieces("0,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("2,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("2,2")
    project.check_finished()
    assert project.finished == True
    #diagonal win bottom left to top right
    project.reset()
    project.place_pieces("2,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,2")
    project.check_finished()
    assert project.finished == True
    #vertical win
    project.reset()
    project.place_pieces("0,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,2")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("2,0")
    project.check_finished()
    assert project.finished == True
    #horizontal win
    project.reset()
    project.place_pieces("0,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,0")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("1,1")
    project.check_finished()
    assert project.finished == False
    project.place_pieces("0,2")
    project.check_finished()
    assert project.finished == True
