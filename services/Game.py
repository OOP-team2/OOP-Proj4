from ..models import Player, AutoPlayer, Dealer, Money
from ..views import HandView, BackgroundView, BettingView, NumberView, PlayerView, StakeView, WordView
import Round

# 한 게임을 책임지는 클래스입니다.
class Game:
    def __init__(self):
        self.rounds: list = []
        self.winner: Player = None
        self.totalBet: Money = None
        self.dealer: Dealer = None
        # 플레이어들 중 첫번째는 항상 컴퓨터입니다.
        self.computer_player = AutoPlayer()
        self.player = Player()
        # 패를 보여줄 뷰를 가집니다.
        self.hand_view: HandView = None
        self.background_view: BackgroundView = None
        self.betting_view: BettingView = None
        self.number_view: NumberView = None
        self.player_view: PlayerView = None
        self.stake_view: StakeView = None
        self.word_view: WordView = None

    def start_game(self) -> None:
        self.hand_view: HandView = HandView()
        self.background_view: BackgroundView = BackgroundView()
        self.betting_view: BettingView = BettingView()
        self.number_view: NumberView = NumberView()
        self.player_view: PlayerView = PlayerView()
        self.stake_view: StakeView = StakeView()
        self.word_view: WordView = WordView()

        # 딜러를 초기화합니다.
        self.dealer = Dealer()

        # 플레이어와 컴퓨터 플레이어를 생성합니다.
        player: Player = self.create_player(10000)
        computer_player: AutoPlayer = AutoPlayer(10000)
        
        # 게임이 끝나지 않았으면 게임을 계속합니다.
        # 매번 한 라운드를 생성합니다.
        while not self.dealer.check_game_ended(self.players):
            game_round: Round = Round()
            # 라운드가 생성되면 딜러가 패를 분배합니다.
            self.dealer.distrubute_hands(self.players)
            
            # 패가 분배되면 플레이어는 패를 확인합니다.
            # 패는 콘솔창에 출력합니다.
            self.hand_view.display_hand(player, player.get_hands(), front=True)
                
            # 라운드가 시작하기 전에 패를 확인하고 죽을지 안죽을지를 결정합니다.
            players_in: [Player] = [self.players[0]]
            # y/n로 죽을지 안죽을지 입력을 받습니다.
            do_player_fold: str  = input()
            if do_player_fold == "n":
                # 대답이 no 면 이번 판은 넘어갑니다.
                pass

            # 참가가 모두 결정되면 라운드를 시작합니다. => 딜러가 승자를 판별하는게 낫겠습니다.
            round_winner: Player = self.dealer.announce_winner(players_in)

            # 라운드에 승자를 추가합니다.

            # 라운드를 진행된 라운드에 추가하는 것은 라운드가 끝나고 마지막에 합니다.
            self.rounds.append(game_round)
            
        # 게임이 끝나면 승자와 최종 승리 금액을 출력합니다.
        winner: Player = self.dealer.announce_winner(self.players)
        self.player_view.show_player(winner)
        
    def end_game(self) -> None:
        self.is_game_ended = True

    def create_player(self, bet_money: Money) -> Player:
        return Player(bet_money)

    def show_opponent_hands(self) -> None:
        pass

    def display_player(self) -> None:
        pass

    def display_hand(self):
        pass
