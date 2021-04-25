import random
from . import *

xd = ["Your message has been read and Ignored successfully ┐(´∀｀)┌","Umm My Ears Were Shut 🙉"]

@ultroid_cmd(pattern="ignore$")
async def oof(ult):
  rd = random.choice(xd)
  await eor(ult, rd)
 
 
@ultroid_cmd(pattern="cantignore$") 
async def oof(ult):
  await eor(ult, "In Mind: **Im Trying To Ignore But I Cant (ｰ ｰ;)**")