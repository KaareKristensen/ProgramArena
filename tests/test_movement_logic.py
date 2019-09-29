from programarena.game import game

import pytest
import uuid


@pytest.fixture
def game_setup():
    # 10, 10 board for this specific game
    return game.Game(uuid.uuid4(), 10, 10)


def test_all_board_positions_should_contain_zeroes_at_startup(game_setup):
    game = game_setup
    assert game is not None
    board = game.get_board()
    for i in range(len(board)):
        for j in range(len(board[i])):
            assert board[i][j] == 0
