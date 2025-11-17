# students in Clubs
from pyscript import display # pyright: ignore[reportMissingImports]

# Working with Sets
from pyscript import display, document


Math_Club = {'Leona', 'Phoebe', 'Sang', 'Sean'}
Debate_Club = {'Bea', 'Allen', 'Khloe', 'Aj'}



display(Math_Club | Debate_Club, target='one') 
display(Math_Club & Debate_Club, target='both') 
display(Math_Club - Debate_Club, target='first') 
display(Debate_Club -  Math_Club, target='second')
display(Math_Club ^ Debate_Club, target='onlyone') 

