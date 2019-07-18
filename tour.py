from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 78
y = 76
z = 45
mc.player.setTilePos(x, y, z)
# Ждём 4 секунды
time.sleep(4)
x = 56
y = 79
z = 45
mc.player.setTilePos(x, y, z)
# ждём ещё 3 секунды
time.sleep(3)
x = 98
y = 79
z = 99
mc.player.setTilePos(x, y, z)
time.sleep(2)
x = 116.909
y = 138.00000
z = -93.359
mc.player.setTilePos(x, y, z)
x = 145.890
y = 220.678
z = 275.898
mc.player.setTilePos(x, y, z)
x = 120.678
y = 230.789
z = 100.456
mc.player.setTilePos(x, y, z)
x = 97.567
y = 43.667
z = 78.456
