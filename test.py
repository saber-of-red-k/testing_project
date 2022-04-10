import pytest
from calc import *
import web

def test_calc_add_pos():
    x = 2
    y = 4                                   #test sum - OK
    assert calc_add(x,y) == x+y
def test_calc_add_neg():
    x = 5
    y = 2                                   #test sum - not OK
    assert calc_add(x+2,y) == x+y
def test_calc_sub_pos():
    x = 4
    y = 2                                   #test substract OK
    assert calc_substract(x,y) == x-y
def test_calc_sub_neg():
    x = 4
    y = 2                                   #test substract not OK
    assert calc_substract(x+2,y) == x-y
def test_multi_pos():
    x = 5
    y = 5                                   #test multiply OK
    assert calc_multi(x,y) == x*y
def test_multi_neg():
    x = 5
    y = 5                                   #test multiply not OK
    assert calc_multi(x+2,y) == x*y
def test_divide_pos():
    x = 25
    y = 5                                   #test divide OK
    assert calc_divide(x,y) == x/y
def test_divide_neg():
    x = 25
    y = 5                                   #test divide not OK
    assert calc_divide(x+4,y) == x/y
def test_divide_even_pos():
    x = 50
    y = 10                                  #test even divide OK
    assert calc_divide_even(x,y) == x//y
def test_divide_even_neg():
    x = 50
    y = 10                                  #test even divide not OK
    assert calc_divide_even(x+24,y) == x//y
def test_modulus_pos():
    x = 6
    y = 10                                  #test modulus ok
    assert calc_modulus(x,y) == x%y
def test_modulus_neg():
    x = 6
    y = 10                                  #test modulus not ok
    assert calc_modulus(x+4,y) == x%y
def test_root_pos():
    x = 35                                  #test root OK
    assert calc_root(x) == x**0.5
def test_root_neg():
    x = 35                                  #test root not OK
    assert calc_root(x+4) == x**0.5

def test_youtube():                         #test selenium
    assert web.youtube_like() == "LIKE OK"