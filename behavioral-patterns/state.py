from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, player: 'Player'):
        self.player = player

    @abstractmethod
    def click_play(self): ...


class PlayingState(State):
    def click_play(self):
        print("Stopping music")
        self.player.state = PauseState(self.player)


class PauseState(State):
    def click_play(self):
        print("Starting music")
        self.player.state = PlayingState(self.player)


class Player:
    def __init__(self):
        self.state = PauseState(self)


def main():
    player = Player()
    print(type(player.state))
    player.state.click_play()

    print(type(player.state))
    player.state.click_play()


if __name__ == '__main__':
    main()
    
    """
    <class '__main__.PauseState'>
    Starting music
    <class '__main__.PlayingState'>
    Stopping music
    """