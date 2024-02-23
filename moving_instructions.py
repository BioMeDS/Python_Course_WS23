# %%
from pyboy import PyBoy
from pyboy import WindowEvent

def piece_positioning(movement_left, a_rotations, pyboy):
    for rotations in range(a_rotations):
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        for _ in range(3): pyboy.tick()

    if movement_left > 0:
        for fields in range(movement_left):
            pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
            for _ in range(3): pyboy.tick()
    elif movement_left < 0:
        for fields in range(movement_left, 0):
            pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
            for _ in range(3): pyboy.tick()

if __name__ == "__main__":
    pyboy = PyBoy("Tetris.gb", game_wrapper=True)
    pyboy.set_emulation_speed(target_speed=5)
    tetris = pyboy.game_wrapper()
    tetris.start_game()
    # %%
    for _ in range(20):
        tetris.reset_game()
        m_left = int(input("l: "))
        rot = int(input("rot: "))
        piece_positioning(m_left, rot, pyboy)
        for _ in range(700): pyboy.tick()
