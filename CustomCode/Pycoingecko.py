# from pycoingecko import CoinGeckoAPI
# import pandas as pd

# cg=CoinGeckoAPI()

# bitcoin_price_data = cg.get_coin_market_chart_by_id(id = 'bitcoin' , vs_currency='usd', days=30)

# data = pd.DataFrame(bitcoin_price_data,columns = ['prices'])

from nba_api.stats.static import teams
import matplotlib.pyplot as pyplot
import pandas as pd


nba_team = teams.get_teams()

df = pd.DataFrame(nba_team)
print(df)


from nba_api.stats.endpoints import leaguegamefinder

nba_id = leaguegamefinder.LeagueIDNullable
df2 = pd.DataFrame(nba_id)

print(df2)