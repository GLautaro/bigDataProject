import twint
import pandas as pd

c = twint.Config()

c.Search = 'virtualidad'
c.Since = '2020-03-15'
c.Until = '2020-06-30'
c.Pandas = True
c.Output = "virtualidad_mar20_jun20.csv"
c.Store_csv = True

twint.run.Search(c)