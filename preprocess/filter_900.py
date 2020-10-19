import chess.pgn
import bz2

pgn_file = bz2.open("Raw/lichess_db_standard_rated_2020-09.pgn.bz2", mode="rt")
out_pgn_file = bz2.open("Filter_900/lichess_db_standard_rated_2020-09.pgn.bz2", mode="wt")

while True:
    game = chess.pgn.read_game(pgn_file)
    if game is None:
        break
    whiteElo = int(game.headers["WhiteElo"])
    blackElo = int(game.headers["BlackElo"])
    if whiteElo<900 or whiteElo>=1000 or blackElo<900 or blackElo>=1000:
        continue
    if "Bullet" in game.headers["Event"]:
        continue # Skip bullet games
    if "Blitz" not in game.headers["Event"]:
        continue # Only blitz games
    if "Normal" != game.headers["Termination"]:
        continue # Skip time expired games
    print(whiteElo)
    print(blackElo)
    print(game.headers)
    out_pgn_file.write(str(game))

out_pgn_file.close()