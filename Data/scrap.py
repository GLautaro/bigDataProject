import twint
import pandas as pd

c = twint.Config()

#c.Search = 'virtualidad'
c.Username = "LAVOZcomar"
c.Since = '2020-07-01'
c.Until = '2020-12-31'
c.Pandas = True
c.Output = "noticias_lavoz_jul_dic_2020.csv"
c.Store_csv = True

twint.run.Search(c)