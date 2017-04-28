'''
Created on Nov 3, 2016

@author: branaugh
total playtime = 3+ hrs.
'''

import libtcodpy as libtcod
import textwrap
import time
import math
import shelve
import pygame.mixer
from libtcodpy import Mouse
from random import randint

#pygame.init()
pygame.mixer.init()

# window size
screenWidth = 80
screenHeight = 43

# camera size
cameraWidth = 80
cameraHeight = 30

# dungeon size
dungeonWidth = 150
dungeonHeight = 150

# bottom panel size
barWidth = 20
panelHeight = 13
panelY = screenHeight - panelHeight

# message size
messageX = barWidth + 3
messageWidth = screenWidth - barWidth - 17
messageHeight = panelHeight - 7

inventoryWidth = 20
equipmentWidth = 20

healAmount = 30

# fog of war
fovAlg = 0
fovLightWalls = True
torchRadius = 10

# room parameters
roomMaxSize = 15
roomMinSize = 10
maxRooms = 20

limitFPS = 17

charRight = 256 
charGrassRight = 257
charPathRight = 258
charDesertRight = 259
charBridgeRight = 260
charSnowRight = 261
charDungeonRight = 262
charMineRight = 263
charHouseRight = 264

charLeft = 288 
charGrassLeft = 289
charPathLeft = 290
charDesertLeft = 291
charBridgeLeft = 292
charSnowLeft = 293
charDungeonLeft = 294
charMineLeft = 295
charHouseLeft = 296

charTowards = 320 
charGrassTowards = 321
charPathTowards = 322
charDesertTowards = 323
charBridgeTowards = 324
charSnowTowards = 325
charDungeonTowards = 326
charMineTowards = 327
charHouseTowards = 328

charAway = 352
charGrassAway = 353
charPathAway = 354
charDesertAway = 355
charBridgeAway = 356
charSnowAway = 357
charDungeonAway = 358
charMineAway = 359
charHouseAway = 360

waterTile = 384
grassTile = 385
darkGrassTile = 395
flowersTile1 = 386
flowersTile2 = 387
flowersTile3 = 388
pathTile = 389
desertTile = 390
bridgeTile = 391
snowTile = 392
darkSnowTile = 394
dungeonTile = 393
darkDungeonTile = 396
mineFloor = 397
darkMineFloor = 398

dungeonWall = 415
darkDungeonWall = 447
iceWall = 474
darkIceWall = 475
volcanoWall = 479
darkVolcanoWall = 511
mineWall = 504
darkMineWall = 505

treeTopLeft = 399
treeTopMiddle = 400
treeTopRight = 401
treeMiddleLeft = 402
treeMiddleMiddle = 403
treeMiddleRight = 404
treeBottomLeft = 405
treeBottomMiddle = 406
treeBottomRight = 407
treeBottomCornerLeft = 408
treeBottomCornerRight = 409
treeTopCornerLeft = 410
treeTopCornerRight = 411

darkTreeTopLeft = 412
darkTreeTopMiddle = 413
darkTreeTopRight = 414
darkTreeMiddleLeft = 444
darkTreeMiddleMiddle = 445
darkTreeMiddleRight = 446
darkTreeBottomLeft = 476
darkTreeBottomMiddle = 477
darkTreeBottomRight = 478
darkTreeBottomCornerLeft = 440
darkTreeBottomCornerRight = 441
darkTreeTopCornerLeft = 442
darkTreeTopCornerRight = 443

waterGrassTopRight = 416
waterGrassTopLeft = 417
waterGrassBottomRight = 418
waterGrassBottomLeft = 419

grassWaterBottomRight = 420
grassWaterBottomLeft = 421
grassWaterTopRight = 422
grassWaterTopLeft = 423

grassWaterStraightLeft = 424
grassWaterStraightRight = 425
grassWaterStraightTop = 426
grassWaterStraightBottom = 427

bridgeTopLeft = 428
bridgeTopMiddle = 429
bridgeTopRight = 430
bridgeBottomLeft = 431
bridgeBottomMiddle = 432
bridgeBottomRight = 433

houseRoofLeft = 544
houseRoofMiddle = 545
houseRoofRight = 546
houseTopLeft = 547
houseTopMiddle = 548
houseTopRight = 549
houseMiddleLeft = 550
houseMiddleMiddle = 551
houseMiddleRight = 552
houseBottomLeft = 553
houseBottomMiddle = 554
houseBottomRight = 555

houseWall = 556
houseBackWall = 557
houseWindowWall = 558
houseFloor = 559
houseWindowFloor = 560
bedTop = 561
bedBottom = 562
tableLeft = 563
tableRight = 564

mayorTile = 565
maybellTile = 566
louisTile = 567
ariannaTile = 568

volcanoLight = 576
volcanoDark = 577
blackTile = 578
lavaTile = 579
lightBottomLeft = 580
lightBottomRight = 581
lavaBottomRight = 582
lavaBottomLeft = 583
lavaTopRight = 584
lavaTopLeft = 585
darkBottomRight = 586
darkBottomLeft = 587
blackBottomRight = 588
blackBottomLeft = 589
grassBottomRight = 590
grassBottomLeft = 591
grassTopRight = 592
grassTopLeft = 593

zombieRight = 267
zombieLeft = 299
zombieTowards = 331
zombieAway = 363
zombieTiles = [zombieRight, zombieLeft, zombieTowards, zombieAway]

skeletonRight = 266
skeletonLeft = 298
skeletonTowards = 330
skeletonAway = 362
skeletonTiles = [skeletonRight, skeletonLeft, skeletonTowards, skeletonAway]

skullRight = 268
skullLeft = 300
skullTowards = 332
skullAway = 364
skullTiles = [skullRight, skullLeft, skullTowards, skullAway]

spriteRight = 269
spriteLeft = 301
spriteTowards = 333
spriteAway = 365
spriteTiles = [spriteRight, spriteLeft, spriteTowards, spriteAway]

guardianRight = 270
guardianLeft = 302
guardianTowards = 334
guardianAway = 366
guardianTiles = [guardianRight, guardianLeft, guardianTowards, guardianAway]

glacierRight = 271
glacierLeft = 303
glacierTowards = 335
glacierAway = 367
glacierTiles = [glacierRight, glacierLeft, glacierTowards, glacierAway]

sirenRight = 272
sirenLeft = 304
sirenTowards = 336
sirenAway = 368
sirenTiles = [sirenRight, sirenLeft, sirenTowards, sirenAway]

dragonRight = 273
dragonLeft = 305
dragonTowards = 337
dragonAway = 369
dragonTiles = [dragonRight, dragonLeft, dragonTowards, dragonAway]

lavaElemRight = 274
lavaElemLeft = 306
lavaElemTowards = 338
lavaElemAway = 370
lavaElemTiles = [lavaElemRight, lavaElemLeft, lavaElemTowards, lavaElemAway]

demonRight = 275
demonLeft = 307
demonTowards = 339
demonAway = 371
demonTiles = [demonRight, demonLeft, demonTowards, demonAway]

demonessRight = 276
demonessLeft = 308
demonessTowards = 340
demonessAway = 372
demonessTiles = [demonessRight, demonessLeft, demonessTowards, demonessAway]

azadloneaRight = 277
azadloneaLeft = 309
azadloneaTowards = 341
azadloneaAway = 373
azadloneaTiles = [azadloneaRight, azadloneaLeft, azadloneaTowards, azadloneaAway]

orcRight = 278
orcLeft = 310
orcTowards = 342
orcAway = 374
orcTiles = [orcRight, orcLeft, orcTowards, orcAway]

trollRight = 279
trollLeft = 311
trollTowards = 343
trollAway = 375
trollTiles = [trollRight, trollLeft, trollTowards, trollAway]

ogreRight = 280
ogreLeft = 312
ogreTowards = 344
ogreAway = 376
ogreTiles = [ogreRight, ogreLeft, ogreTowards, ogreAway]

elementalRight = 281
elementalLeft = 313
elementalTowards = 345
elementalAway = 377
elementalTiles = [elementalRight, elementalLeft, elementalTowards, elementalAway]

zombieCompRight = 282
zombieCompLeft = 314
zombieCompTowards = 346
zombieCompAway = 378
zombieCompTiles = [zombieCompRight, zombieCompLeft, zombieCompTowards, zombieCompAway]

angelRight = 283
angelLeft = 315
angelTowards = 347
angelAway = 379
angelTiles = [angelRight, angelLeft, angelTowards, angelAway]

boarRight = 284
boarLeft = 316
boarTowards = 348
boarAway = 380
boarTiles = [boarRight, boarLeft, boarTowards, boarAway]

snakeRight = 285
snakeLeft = 317
snakeTowards = 349
snakeAway = 381
snakeTiles = [snakeRight, snakeLeft, snakeTowards, snakeAway]

lynxRight = 286
lynxLeft = 318
lynxTowards = 350
lynxAway = 382
lynxTiles = [lynxRight, lynxLeft, lynxTowards, lynxAway]

stairsUp = 472
stairsDown = 473
chestTile = 512
chestOpenTile = 513
potionTile = 514
swordTile = 515
bowTile = 516
helmSteel = 517
chestSteel = 518
greavesSteel = 519
gauntletsSteel = 520
sabatonsSteel = 521
helmLeather = 522
chestLeather = 523
greavesLeather = 524
gauntletsLeather = 525
sabatonsLeather = 526

tombLeft = 527
tombRight = 528
skullFloorTile = 529
skullInvTile = 530
orangeGemFloorTile = 531
orangeGemInvTile = 532
purpleGemFloorTile = 533
purpleGemInvTile = 534

fire1 = 535
fire2 = 536
fire3 = 537
fire4 = 538
fire5 = 539

ice1 = 540
ice2 = 541
ice3 = 542
ice4 = 543
ice5 = 569

necro1 = 570
necro2 = 571
necro3 = 572
necro4 = 573
necro5 = 574

psyc1 = 575
psyc2 = 598
psyc3 = 599
psyc4 = 600
psyc5 = 601

heal1 = 602
heal2 = 603
heal3 = 604
heal4 = 605
heal5 = 606

invIcon = 287
spellsIcon = 319
equipIcon = 351
storyIcon = 383

introSong = 'Opening Music.mp3'
houseSong = 'House Music.mp3'
townSong = 'Outside Music.mp3'
catacombsSong = 'Catacombs Music.mp3'
forestSong = 'Forest Music.mp3'
tundraSong = 'Tundra Music.mp3'
volcanoSong = 'Volcano Music.mp3'
minesSong = 'Mines Music.mp3'
combatSong = 'Combat Music.mp3'

allMaps = {}

allMaps['Town', 0] = ['                                                                                                                   ',
                         '   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF12DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE    ',
                         '   EEEEEEEEEEEEEEEEEEEEEEMHHHHHHHHHHHHHHHHHIssGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHLEEEEEEEEEEEEEEEEEEEEEE    ',
                         '   EEEEEEEEEEEEEEEEEEEMHHIggggggggggggggggggssggggggggggggggggggggggggggggggggggggggggggGLEEEEEEEEEEEEEEEEEEEEE    ',
                         '   EEEEEEEMHHHHHHHHHHHIgggssssssssssssssssssssgggggggg!ggggggggggggggABBBBBBBBCggggggggggGHHHHHHHHHLEEEEEEEEEEE    ',
                         '   EEEEEEEFgggggggggggggggssssssssssssssssssssgggggggggggggggggggggggGLEEEEEEEKCgggggggggggggggggggGHHHHHLEEEEE    ',
                         '   EMHHHHHIggggggg@gggggggssggggggggggXYZgggggggggggggggggggggggggggggGLEEEEEEEKCggggggggggg#ggggggggggggGHHHLE    ',
                         '   EFgggggggggggggggggggggssggggggggggNOPggggggggggggglffffffffffkgggggGLEEEEEEEKCgggggggggggggggggggggggggggGH    ',
                         '   EFgggggggggggggggssssssssggggggggggQRTgggggggglffffmwwwwwwwwwwqkgggggDEEEEEEEEFggggggggggggggggggggggssssss6    ',
                         '   EFgggXYZgggggggggssssssssggggggggggUVWgggggglfmwwwwwwwwwwwwwwwwqfkgggGHHHHHHHHIggggggggggggggggggggggssssss7    ',
                         '   EFgggNOPgggggggggssggggggggggggggggggggglfffmwwwwwwwwwwwwwwwwwwwwqffkggggggggggggggggggggggggggggggggssgggAB    ',
                         '   EFgggQRTgggggggggssgggggggggggggggggglffmwwwwwwwwwwwwuyyyytwwwwwwwwwzgggggggggg!ggggggggggsssssssssssssgggDE    ',
                         '   EFgggUVWggggsssssssgggggggggggglfffffmwwwwwwwwwwwwuyyvggggptwwwwwwwwqfkgggggggggggggXYZgggsssssssssssssgggDE    ',
                         '   EFggggggggggsssssssgggggggggglfmwwwwwwwwwwwwwwuyyyvggggggggpyytwwwwwwwqkggggggggggggNOPgggssggggggggggggggDE    ',
                         '   EFggggggssssssgggggggggggggggxwwwwwwwwwwwwwwuyvgggABBBBBBBBCggpyytwwwwwqkgggggggggggQRTgggssggggggggggggggDE    ',
                         '   EFggggggssssssgggggggggggggggxwwwwwwwwuyyyyyvggggAJEEEEEEEEKCggggxwwwwwwqfkgggggggggUVWgggssggggggggggggggDE    ',
                         '   EFggggggssgggggggggggggggggglmwwwwuyyyvggggggggggDEEEEEEEEEEFggggptwwwwwwwqfffffkgggggggggssggggggggggggggDE    ',
                         '   EFggggggssggggggggggggggggggxwwwwuvggggggggggggggDEEEEEEEEEEFgggggpyyyytwwwwwwwwqffkggggggssggggggggggggggDE    ',
                         '   EFggggggssgggggggggggggggglfmwwwwzgggggggggggggggGHHHHHHHHHHIggggggggggxwwwwwwwwwwwqkgggggssggggggggggggggDE    ',
                         '   EFgg!gssssggggggggggggglffmwwwwwwzgggggggggggggggggggggggggggggggggggggxwwwwwwwwwwwwzgggggssssssssssggggggDE    ',
                         '   EFggggssssgggggggggggglmwwwwwwwwwzggggggggggggggggggggggggggggABBBBCgggpyyytwwwwwwwwzgggggssssssssssggggggDE    ',
                         '   EFggggssggggggggggggglmwwwwwwwwuyvggggggggggggg)````````(gggggGLEEEKCggggggpytwwwwwwzgggggggg#ggggssgABCggDE    ',
                         '   EFggggssgggggggggggggxwwwwwwwuyvgggggggggggg)```_%%%%%%-```(gggGLEEEKCgggggggpyytwwwzgggggggggggggssgDEFggDE    ',
                         '   EFggggssgggABCgggggggxwwwwuyyvggggggggggggg)`_%%%%%%%%%%%%-`(gggGLEEEKCgggggggggxwwwqfkgggggggggggssgDEFggDE    ',
                         '   EFggggssgggDEFgggggggnoooorggggggggggggggg;}`+%%%%%%%%%%%%=`{:gggGLEEEFgggggggggxwwwwwzgggggggggggssgDEFggDE    ',
                         '   EFggggssgggGHIgggssssjjjjjjggggABBBCggggg;>>}```+%%%%%%=```{>>:gggGHLEFgggggggggxwwwwwzgggggggggggssgDEFggDE    ',
                         '   EFggggssgggggggggssssjjjjjjggggDEEEFgggg;>>>>>>}````````{>>>>>>:ggggDEFgggggggggpytwwwzgggggggggggssgDEFggDE    ',
                         '   EFggggssgggggggggssggehhhhiggggDEEEFggg;>>>>>>>>>>>>>>>>>>>>>>>>:gggGHIgggggggggggxwwwzgggggggggggssgGHIggDE    ',
                         '   EFggggsssssssggggssggxwwwwzggggGHHHIgg;>>>>>>>>>>>>>>>>>>>>>>>>>>:ggggggggggggggggxwwwzgggggggggggssggggggDE    ',
                         '   EFggggsssssssggggssggxwwwwzgggggggggg;>>>>>>>>>>>>>>>>>>>>>>>>>>>>:gggggggggggggggxwwwzgggggggggggssggggggDE    ',
                         '   EFgggggggggssssssssggxwwwwqkgggggggg;>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:ggggggggggggggxwwwzggggggsssssssggggggDE    ',
                         '   EFgggggggggssssssssggxwwwwwzgggggggg>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ggggggggggggggxwwwzggggggsssssssggggggDE    ',
                         '   EFgggggggggggggggggggptwwwwzgggggggg<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|gggggggggggglfmwwwzggggggssgggggggggggDE    ',
                         '   EFggggggggggggggggggggxwwwwzggggggggg<>>>>>>>>>>>>>>>>>>>>>>>>>>>>|gggggggggglffmwwwwwzggggggssgggggggggggDE    ',
                         '   EFggggggggggggggggggggxwwwwzggggggggggg<>>>>>>>>>>[$$]>>>>>>>>>>|ggggggggggggxwwwwwwwwzggggggssgggggggg!ggDE    ',
                         '   EFggggggggggggggggggggxwwwwzgggggggggggggg<>>>>>>>$$$$>>>>>>>|gggggggggggggglmwwwwwwuyvggggggssgggggggggggDE    ',
                         '   EFggggggggggggggggggggxwwwwzgggggggggggggggggg<>>>$$$$>>>|ggggggggggggggggggxwwwwwwwzggggggggssgggggggggggDE    ',
                         '   EFggggggggggggggggggggxwwwwzggABBBBBCgggggggggggggggggggggggggggggggggggggggxwwwwuyyvggggggggssgggggggggggDE    ',
                         '   EFggggggggggggggggggggxwwwwzggDEEEEEKCggggggggggggggggggggggggggggggggggggggxwwwuvgggggggggggssgggggggggggDE    ',
                         '   EFggggggggggggg!ggggggxwwwwzggDEEEEEEKCgggggggggggggggggggggggggggggggggggggnooorggggggggggggssgggggggggggDE    ',
                         '   EFggggggggggggggggggggxwwwwzggDEEEEEEEKCgggggggggggggggggABBBBBBBBCgggggggggjjjjjssssssssssssssgggggggggggDE    ',
                         '   EFggggggggggggggggggggptwwwzggDEEMHHHHHIggggggggggggggggAJEEEEEEEMIgggggggggjjjjjssssssssssssssgggggggggggDE    ',
                         '   EFgggggggggggggggggggggxwwwzggDEEFgggggggggggggggggggggAJEEEEEEEMIggggggggggehhhiggggggggggggssgggggggggggDE    ',
                         '   EFgggABBBCgggggggggggggxwwwzggGHHIggggggggggggggggggggAJEEEEMHHHIgggggggglffmwwwzggggggggggggssgggggggggggDE    ',
                         '   EFgggDEEEKCggggggggggggxwwwqfffffkgggggggggggggggggggDEEEEEEFgggggglfffffmwwwwwwzggggggggggggsssssggggggggDE    ',
                         '   EFgggDEEEEKCgggggggggggxwwwwwwwwwqfffkgggggggggggggggGHHHHHHIggggglmwwwwwwwwwwwwzgggXYZggggggsssssggggggggDE    ',
                         '   EFgggDEEEEEKCggggggggggptwwwwwwwwwwwwqffkggggggggggggggggggggglfffmwwwwwwwwwwuyyvgggNOPgggggggggssggggggggDE    ',
                         '   EFgggDEEEEEEKCggggggggggpytwwwwwwwwwwwwwqffkggggggggggggggglffmwwwwwwwwwwwwuyvggggggQRTgggggggggssggggggggDE    ',
                         '   EFgggGHHHHHHHIggggggggggggpyyytwwwwwwwwwwwwqfffkggggggglfffmwwwwwwwwwwwwwuyvggggggggUVWgggggggggssggggggggDE    ',
                         '   EFgggg#gggggggggggggggggggggggpytwwwwwwwwwwwwwwqfffffffmwwwwwwwwwwwwwwuyyvgggggggggggSggggssssssssggggggggDE    ',
                         '   EKCgggggggXYZgggggggggggggggggggpyyyyytwwwwwwwwwwwwwwwwwwwwwwwwwwwuyyyvgggggggggggggggggggssssssssggggggggDE    ',
                         '   EEKCggggggNOPgggggggggggggggggggggggggpyyyytwwwwwwwwwwwwwwwwwwuyyyvgABBBBBBBBBCgggggggggggssggggggggggggggDE    ',
                         '   EEEKBCggggQRTggggggggggggABBBCgggggggggggggpytwwwwwwwwwwwwwwwwzggggAJEEEEEEEEEFgggggggggggssgggg@gggggggggDE    ',
                         '   EEEEEKCgggUVWggggggggggggDEEEFgggggggggggggggpyyyytwwwwuyyyyyyvgggAJEEEEEEEEMHIsssssssssssssggggggggggggggDE    ',
                         '   EEEEEEKCgggggggggggggggggDEEEFggggggggggggggggggggxwwwwzgggggggggAJEEEEEMHHHIggsssssssssssssggggggggggggggDE    ',
                         '   EEEEEEEKCggggggggggggggggDEEEFggggggggggggggggggggxwwwwzgggggggggDEEEEEEFggggggssgggggggggggggggggggggggggDE    ',
                         '   EEEEEEEEKC!ggggggggggggggGHHHIggggggggggggggggggggxwwwwqkggggggggGHHHHHHIggggggssgggg#ggggggggABBBBBBBBBBBJE    ',
                         '   EEEEEEEEEKCgggggggggggggggggggggggggggggggggggggggxwwwwwqkgggggggggggggssssssssssggggggggABBBBJEEEEEEEEEEEEE    ',
                         '   EEEEEEEEEEKCggggggABBBBBBBBBBBBBBBBBBBCgggg@ggggggptwwwwwzgggggggggggggssssssssssgggggABBJEEEEEEEEEEEEEEEEEE    ',
                         '   EEEEEEEEEEEKCgggggDEEEEEEEEEEEEEEEEEEEKBBBBBBBBBBBCptwwwwzgABBBBBBBBBBCssABBBBBBBBBBBBJEEEEEEEEEEEEEEEEEEEEE    ',
                         '   EEEEEEEEEEEEKC345BJEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFgxwwwwzgDEEEEEEEEEEF~0DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE    ',
                         '                                                                                                                   ',
                         '                                                                                                                   ']

allMaps['Home', 0] = ['                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                              XWYBYWX                                     ',
                      '                              Xl-E-lX                                     ',
                      '                              X-----X                                     ',
                      '                              X-----X                                     ',
                      '                              X-----X                                     ',
                      '                              XTA---X                                     ',
                      '                              X-----X                                     ',
                      '                              XXXSXXX                                     ',
                      '                                XXX                                       ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ',
                      '                                                                          ']

allMaps['Mayor', 0] = ['                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                       XBWYYYYYYYYYWYYYX                                 ',
                       '                       XEl---------l---X                                 ',
                       '                       X---XXXX--------X                                 ',
                       '                       X---X  X-----a--X                                 ',
                       '                       X---X  XTA------X                                 ',
                       '                       X---X  X--------X                                 ',
                       '                       XXXXX  XXXXSXXXXX                                 ',
                       '                                 XXX                                     ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ',
                       '                                                                         ']

allMaps['Louis', 0] = ['                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                           XBYYYYYYWYYYX                                  ',
                       '                           XE------l---X                                  ',
                       '                           X-----------X                                  ',
                       '                           X-----------X                                  ',
                       '                           X-b---------X                                  ',
                       '                           X---------TAX                                  ',
                       '                           XXXXSXXXXXXXX                                  ',
                       '                              XXX                                         ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ',
                       '                                                                          ']
 
allMaps['Arianna', 0] = ['                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                               XYWYYYBYX                                  ',
                         '                               X-l---E-X                                  ',
                         '                               X-------X                                  ',
                         '                               X-------X                                  ',
                         '                               X-------X                                  ',
                         '                               XXXXXX--X                                  ',
                         '                                    X--X                                  ',
                         '                              XYWYYYX--X                                  ',
                         '                              X-l------X                                  ',
                         '                              X-----c--X                                  ',
                         '                              X--------X                                  ',
                         '                              XTA------X                                  ',
                         '                              X--------X                                  ',
                         '                              XXXXSXXXXX                                  ',
                         '                                 XXX                                      ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ',
                         '                                                                          ']
 
allMaps['Maybell', 0] = ['                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                              XYWYYBYYWYX                                  ',
                          '                              X-l--E--l-X                                  ',
                          '                              X---------X                                  ',
                          '                              X---------X                                  ',
                          '                              X---------X                                  ',
                          '                              X------d--X                                  ',
                          '                              X---------X                                  ',
                          '                              XTA-------X                                  ',
                          '                              X---------X                                  ',
                          '                              XXXXSXXXXXX                                  ',
                          '                                 XXX                                       ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ',
                          '                                                                           ']

allMaps['Catacombs', 0] = ['                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ',
                           '                               X--lr--X-------------D--X--lr--X                           ',
                           '                               X------X----------------X------X                           ',
                           '                               X--lr--X----XXXXXXXX----X--lr--X                           ',
                           '                               X-----------X--lr--X-----------X                           ',
                           '                               X--lr--X----X------X----X--lr--X                           ',
                           '                               X------X----X------X----X------X                           ',
                           '                               X--lr--X----------------X--lr--X                           ',
                           '                               XXXXXXXX----------------XXXXXXXX                           ',
                           '                                      X-S--------------X                                  ',
                           '                                      XXXXXXXXXXXXXXXXXX                                  ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ',
                           '                                                                                          ']

allMaps['Catacombs', 1] = ['                                                                                                       ',
                          '                                                                                                       ',
                          '                                        XXXXXXXXXXXXXXXXX   XXXXXXXX              XXXXXXXXXXX          ',
                          '                                        X---------------X   X------X              X---------X          ',
                          '                                        X--Z------------X   X------X              X------D--X          ',
                          '                                        X---------------X   X----P-X              X---------X          ',
                          '                                        X---------------X   X------X              X---------X          ',
                          '                                        X---------------X   XXX--XXX              X---------X          ',
                          '                                        X---------------X     X--X                X---------X          ',
                          '                                        XXXXXXXXXXXXXX--XXXXXXX--XXXXXXXXXX       X----Z----X          ',
                          '                                                     X--------------------X       X---------X          ',
                          '                                                     X--------------------X       XXXXX--XXXX          ',
                          '                                                     X--XXXXXXXXXXXXXXXX--X           X--X             ',
                          '                                                     X--X              X--X           X--X             ',
                          '                                                     X--X              X--X           X--X             ',
                          '                                                   XXX--XXX  XXXXXXXXXXX--X           X--X             ',
                          '                                                   X------X  X------------X           X--X             ',
                          '                                                   X------X  X------------X           X--X             ',
                          '                                                   X------X  X------------XXXXXXX     X--X             ',
                          '                                                   X------X  X-----Z------------X     X--X             ',
                          '                                                   X------X  X------------------X  XXXX--XXXX          ',
                          '                                                   XXX--XXX  X------------XXXX--X  X--------X          ',
                          '                                                     X--X    X------------X  X--XXXX--------X          ',
                          '                                                     X--X    XXXXXXXXXXXXXX  X--------------X          ',
                          '                                                     X--X                    X------------P-X          ',
                          '                                                   XXX--XXXXX                XXXXXXXX--XXXXXX          ',
                          '                                                   X--------X                       X--X               ',
                          '                                                   X--------X                  XXXXXX--XXXXXXXXXXX     ',
                          '                                                   X--------X                  X-----------------X     ',
                          '                                                   X--Z-----XXXXXXXXXXXXX      X-----------------X     ',
                          '                                                   X--------------------X      X-------------Z---X     ',
                          '                                                   X--------------------X      X-----------------X     ',
                          '                                                   XXXXXXXXXXXXXXXXXXX--X      X-----------------X     ',
                          '                                                                     X--X      X-----------------X     ',
                          '                                                                     X--X      X-----------------X     ',
                          '                                                               XXXXXXX--X      X-Z---------------X     ',
                          '                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  X--------X      X-----------------X     ',
                          '                   X--------------------Z-------------------X  X--------X      XXXXXXXXXXXXXXXXXXX     ',
                          '                   X----------------------------------------X  X--XXXXXXX                              ',
                          '                   X--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------X  X--X                                    ',
                          '                   X--X                              X------X  X--X                                    ',
                          '                   X--X            XXXXXXXXXXXXXX    X------XXXX--X XXXXXXXXX  XXXXXXXXX               ',
                          '        XXXXXXXXXXXX--XXXXXXXXXXXX X---------Z--X    X------------X X-------X  X-----P-X               ',
                          '        XX---------X--X----------X X------------X    X------------X X-------X  X-------X               ',
                          '        XX-----Z---X--X---Z------X X------------X    X------XXXX--X X-Z-----X  X-------X               ',
                          '        XX-----------------------X X--Z---------X    XXXXXXXXXXX--X X-------X  X-------X               ',
                          '        XX-----------------------X X------------X              X--X X-------X  X-------X               ',
                          '        XXXXXXXXXXXX--XXXXXXXXXXXX XXXXXXXXXXX--X   XXXXXXXX   X--X XXXX--XXXXXXXX--XXXX               ',
                          '                   X--X                      X--X   X---P--X   X--X    X--X      X--X                  ',
                          '                   X--X   XXXXXXXX           X--X   X------X   X--XXXXXX--XXXXXXXX--XXXXXXXXX          ',
                          '                   X--X   X------XXXXXXXX    X--X   X------X   X----------------------------X          ',
                          '                  XX--XX  X-Z-----------X    X--X   X------X   X----------------------------X          ',
                          '        XXXXXXXXXXX----X  X-------------X    X--X   XXXX--XX   XXXXXXXXXXXXXXXXXXXXXXXXXXX--X          ',
                          '        X--------------X  X------XXXXX--X    X--X      X--X                              X--X          ',
                          '        X--------------X  XXX--XXX   X--X    X--X      X--X  XXXXXXXXXXXXXXXXX  XXXXXXXXXX--X          ',
                          '        X--XXXXXXXX----X    X--X     X--XXXXXX--XXXXXXXX--X  X---------------X  X-----------X          ',
                          '        X--X      X----X    X--X     X--------------Z-----X  X---------------X  X--Z--------X          ',
                          '        X--X      X----X    X--X     X--------------------X  X------XXXX--X--XXXX-----------X          ',
                          '        X--XXXX   X----X    X--X     X--XXXXXXXXXXXXXXXX--X  X------X  X--X-----------------X          ',
                          '        X-----X   XX--XX  XXX--XXXX  X--X              X--X  XXX--XXX  X--X-----------------X          ',
                          '        X-----X    X--X   X-------X XX--XXXX           X--X    X--X    X--XXXXXXX-----------X          ',
                          '        X-----X    X--X   X-----Z-X X------X      XXXXXX--X    X--X    X--X     X-----------X          ',
                          '        X-----X    X--XXXXX-------X X------X      X-------XXXXXX--X  XXX--XXX   X--------Z--X          ',
                          '        X-----X    X--------------X X------X      X---------------X  X------X   X-----------X          ',
                          '        X-S---X    X--------------X X------X      X---------------X  X-Z----X   XXXXXXXXXXXXX          ',
                          '        X-----X    XXXXXXXX-------X XXXXXXXX      X--------XXXXXXXX  X----P-X                          ',
                          '        XXXXXXX           X-------X               X--------X         XXXXXXXX                          ',
                          '                          XXXXXXXXX               XXXXXXXXXX                                           ',
                          '                                                                                                       ',
                          '                                                                                                       ']

allMaps['Catacombs', 2] = ['                                                                                                                                                                      ',
                          '              XXXXXXXXX                                                                                                                                               ',
                          '              X-------X                                                                                                                                               ',
                          '              X-S-----X                                XXXXXXXXXXXXXXX                                                                                                ',
                          '              X-------X                                X-------------X                                                                                                ',
                          '              X-------XXXXXXXXXXXXXXXXXX               X--P----------X                                                                                                ',
                          '              X------------------------X               X-------------X                                                  XXXXXXXXXXXXXXXXXXXXXX                        ',
                          '              X------------------------X               X-------------X                                                  X--------------------X                        ',
                          '              XXXXXXXXXXXXXXXXXXXXXXX--X               XXXXXXXXXXXX--X                                                  X--------------Z-----X                        ',
                          '                                    X--X                          X--X                                                  X--------------------X                        ',
                          '                                    X--X                          X--X                                                  X--------------------X                        ',
                          '                     XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------X         XXXXXXXX       ',
                          '                     X-----------------------------------------------------------------------------------------------------------------------X         X------X       ',
                          '                     X-----------------------------------------------------------------------------------------------------------------------X         X------X       ',
                          '                     X---Z-----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X         X--Z---X       ',
                          '                     X---------------------------------X                                 X--X                                             X--X         X------X       ',
                          '                     X---------------------------------X  XXXXXXXXXXXXXXXXXXXXXXXXX      X--X                                             X--X         X------X       ',
                          '                     X---------------------------------X  X-----------------------X      X--X                        XXXXXXXXXXXXXXXXXXXXXX--X         X------X       ',
                          '                     X---------------------------------X  X-----------------------X      X--X                        X-----------------------XXXXXXXXXXX------X       ',
                          '                     X---------------------------------X  X-----------------------X      X--X                        X----------------------------------------X       ',
                          '                     X---------------------------Z-----X  X-----------------------X      X--X                        X----------------------------------------X       ',
                          '                     X---------------------------------X  X-----------------------XXXXXXXX--X                        X----Z------------------XXXXXXXXXXX------X       ',
                          '                     X---------------------------------X  X-----Z---------------------------X                        X-----------------------X         X------X       ',
                          '                     X---------------------------------X  X---------------------------------X                        XXXXXXXXXX--XXXXXXXXXXXXX         X------X       ',
                          '                     X---------------------------------X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                 X--X                     X------X       ',
                          '                     X------Z--------------------------X                                                           XXXXXXXXXXXX--X                     X------X       ',
                          '                     X---------------------------------XXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXX     X-------------X                     X------X       ',
                          '                     X-------------------------------------------------------X    X--Z-----------------------X     X-------------X                     X------X       ',
                          '                     X-------------------P-----------------------------------X    X--------------------------X     X--XXXXXXXXXXXX                     X------X       ',
                          '                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X    X-----------------------X--XXXXXXX--X                    XXXXXXXXXXXXX------X       ',
                          '                                                                          X--X    X----------P------------X-----------X    XXXXXXXXXXX     X------------------X       ',
                          '                                      XXXXXXXXXXXXX                       X--X    XXXXXXXXXXXXXXXXXXXXXXXXX-----------X    X---------X     X------------------X       ',
                          '                                      X-----------X                       X--X                            X-----------X    X---------XXXXXXX------------------X       ',
                          '                                      X-----Z-----X                       X--X                            X-----------X    X---P------------------------------X       ',
                          '                                      X-----------XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------X    X----------------------------------X       ',
                          '                                      X------------------------------------------------Z------------------------------X    X---------XXXXXXXXXXXXXXXXXXXXXXXXXX       ',
                          '                                      X-------------------------------------------------------------------------------X    X---------X                                ',
                          '                                      X-----------XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXX      ',
                          '                                      X-----------X                       X--X                                                             X---------------Z---X      ',
                          '                                      X-----------X                       X--X          XXXXXXXXXX                                         X-------------------X      ',
                          '                                      XXXXXXXXXXXXX                       X--X          X---P----X                                         X-------------------X      ',
                          '                                                                          X--XXXXXXXXXXXX--------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------X      ',
                          '                                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X------------------------------------------------------------------------------------X      ',
                          '                                     X--------------------------------X   X-------------------------------------Z----------------------------------------------X      ',
                          '                                     X------Z-------------------------X   XXXXXXXXXXXXXXX--------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      ',
                          '                                     X--------------------------------X                 X--------X                     X--X                                           ',
                          '                                     X--------------------------------X                 XXXX--XXXX                     X--X              XXXXXXXXXXXXXXXXXX           ',
                          '                                     X--------------------------------X                    X--X                        X--X              X----------------X           ',
                          '                                     X--------------------------------X                    X--X                        X--X              X--P-------------X           ',
                          '                                     X--------------------------------X                    X--X                        X--X              X----------------X           ',
                          '                                     XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX                    X--X                        X--X              XXXXXXXX--XXXXXXXX           ',
                          '                                                    X--X                                   X--X                        X--X                     X--X                  ',
                          '                                                    X--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X             XXXXXXXXXXXX--XXXXXXXXXXXXXX        X--X                  ',
                          '                                                    X-----------------------------Z-----------X             X--------------------------X        X--X                  ',
                          '                                                    X-----------------------------------------X             X--------------------------XXXXXXXXXX--X                  ',
                          '                                                    XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX             X--------------------------------------X                  ',
                          '                                                                        X--X                                X-------------Z------------------------X                  ',
                          '                                                                        X--X                                X--------------------------XXXXXXXXXXXXX                  ',
                          '                                                                        X--X                                X--------------------------X                              ',
                          '                                                                        X--X                                XXXXXXXXXXXXXXXXXXXXXXXXXXXX                              ',
                          '                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X                                                                                          ',
                          '                       X----------------------------X----------------------X            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                            ',
                          '                       X----------------K-----------X----------------------X            X--------------------------------X                                            ',
                          '                       X--XXXXXX--------------------X----------------------X            X--------------------------------X                                            ',
                          '                       X--X    X--------------------X----------------------X            X--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--X                                            ',
                          '                       X--X    X--------------------X----------------------X            X--X                          X--X                                            ',
                          '                       X--X    X--------------------X----------------------X            X--X                          X--X                                            ',
                          '                       X--X    X--------------------X----------------------X            X--X              XXXXXXXXXXXXX--XXXXXXXXXXXXX                                ',
                          '                       X--X    X--------------------X----------------------X      XXXXXXX--X              X--------------------------X                                ',
                          '                       X--X    X--------------------X----------------------X      X--------X              X---B----------------------X                                ',
                          '                       X--X    X-------------------------------------------X      X--------X              X--------------------------X                                ',
                          '                       X--X    X-------------------------------------------X      X--------X              X--------------------------X                                ',
                          '                       X--X    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      X--------X              XXXXXXXXXXXXXX--XXXXXXXXXXXX                                ',
                          '                       X--X                                                       XXX--XXXXX      XXXXXXXXX--------------------------XXXXXXXXX                        ',
                          '                       X--X                                                         X--X          X------------------------------------------X                        ',
                          '                       X--X                                                         X--X          X------------------------------------------X                        ',
                          '                       X--X                                                         X--X          X----------K-------------------------------X                        ',
                          '                       X--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X          X------------------------------------------X                        ',
                          '                       X---------------------------------------------------------------X          X------------------------------------------X                        ',
                          '                       X---------------------------------------------------------------X          X---------------------------------K--------X                        ',
                          '                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------X          X----D-------------------------------------X                        ',
                          '                                                             X------------K------------X          X------------------------------------------X                        ',
                          '                                                             X-------------------------X          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
                          '                                                             X-------------------------X                                                                              ',
                          '                                                             X---P---------------------X                                                                              ',
                          '                                                             X-------------------------X                                                                              ',
                          '                                                             XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ',
                          '                                                                                                                                                                      ',
                          '                                                                                                                                                                      ',
                          '                                                                                                                                                                      ',
                          '                                                                                                                                                                      ',
                          '                                                                                                                                                                      '] 

allMaps['Catacombs', 3] = ['                                                                                                                                                                                    ',
                          '                                                                                                                                                                                    ',
                          '                             XXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXX           XXXXXXXXXXXXXXXXX                                                                                 ',
                          '                             X-P-------X         X--------------------X           X---------------X      XXXXXXXXXXXXXXXXXXXXXX                                                     ',
                          '                             X---------X         X--------------------X           X-------Z-------X      X-------X------------X                                                     ',
                          '                             X---------XXXXXXXXXXX--XXXXXXXXXXXXXXXX--X           X---------------X      X-------X-------K----X                                                     ',
                          '                             X------------------------X      XXXXXXX--XXXXXXXX    XXXXXXXX--XXXXXXX      X-------X------------X                                                     ',
                          '                             X-------Z----------------X      X---------------X           X--X            X-------XXXXXXX------X                             XXXXXXXXXXXXXXXXXXXXX   ',
                          '                             XXXXXXXXXXXXXXXXXXXXXXXXXX      X---------------XXXXXXXXXXXXX--XXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX     X--P----------------X   ',
                          '                                                             X-------K--------------------------------------------------------------------------------X     X-------------------X   ',
                          '                                XXXXXXXXXXXXXXXXXXXXXX       X----------------------------------------------------------------------------------------X     X-------------------X   ',
                          '                                XP--------K----------X       X----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXX------XXXXXXXXXXXXXXX---------X     X-------------------X   ',
                          '                                X--------------------X       X--XXXXXXXXXXXXXXX                          X-------X------------X             X---------X     XXXXXXXXX--XXXXXXXXXX   ',
                          '                                X--XXX---------------X       X--X                                        X-------X--P----K----X             X---------X             X--X            ',
                          '                                X--X XXXXXXX--XXXXXXXX       X--X                                        X-------X------------X             XXXXXXXX--X     XXXXXXXXX--XXXXXXXXXX   ',
                          '                                X--X       X--X              X--X                                        XXXXXXXXXXXXXXXXXXXXXX                    X--X     X-------------------X   ',
                          '                                X--X       X--X              X--X                                                                                  X--X     X----------Z--------X   ',
                          '                                X--X       X--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           X--X     X-------------------X   ',
                          '                                X--X       X-------------------------------------------------------------------------------------------X           X--X     X-------------------X   ',
                          '                                X--X       X--------------------------------------------------------------------------------------P----X           X--XXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '                                X--X       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX----------X           X-----------X                    ',
                          '                                X--X                                                      X-------K---------------X         X----------X           X-----------X                    ',
                          '                                X--X                            XXXXXXXXXXXXXXX           X-----------------------X         X----------X           X--XXXXXXXXXX                    ',
                          '                                X--X XXXXXXXXXXXXXX             X-------------X           X-----------------------X         XXXXXXXXXXXX           X--X                             ',
                          '                                X--X X-P----------X             X-------------X           X-----------------------X                                X--X                             ',
                          '                              XXX--X X------------X             X--XXXXXXXXX--X           X-----------------------X                                X--X                             ',
                          '                              X----X X------------X             X--X       X--X           X-----------------------X                                X--X                             ',
                          '                              X-K--X XXXXXX--XXXXXX             X--X       X--X           X-----------------------X                                X--X                             ',
                          '                              X--XXX      X--XXXXXXXXXXXXXXXXXXXX--X       X--X           XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX            ',
                          '                              X--X        X------------------------X       X--X                                X-------------------------------------------------------X            ',
                          '                              X--X        X------------------------X       X--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX    X----------------K--------------------------------------X            ',
                          '                              X--X        X--XXXXXXXXXXXXXXXXXXXX--X       X------------------------Z-----X    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--X            ',
                          '                              X--X  XXXXXXX--XXXXXX             X--X       X------------------------------X                                        X--X             X--X            ',
                          '                              X--X  X-------------X             X--X       XXXXXXXXXX---------------------X                                        X--X             X--X            ',
                          '                              X--X  X------K------X             X--X                X---------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X             X--X            ',
                          '                              X--X  X-------------X             X--X          XXXXXXX--------------------------------------------------------------X--X             X--X            ',
                          '                              X--X  XXXXXXXXXXXXXXX             X--X          X--------------------------------------------------------------------X--X             X--X            ',
                          '                              X--X                              X--X          X---------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXX-----K------X--X             X--X            ',
                          '                              X--XXXXXXX                        X--X          X----Z----------------------X            X--X           X------------X--X         XXXXX--XXXXX        ',
                          '                              X--------X                        X--X          X---------------------------X            X--X           X---------------X         X----------X        ',
                          '                              X-----D--X   XXXXXXXXXXXXXXXXXXXXXX--X          XXXXXXXXXXXXXXXXXXXXXXXXXXXXX            X--X           X---------------X         X----------X        ',
                          '                              X--------X   X-------------K----P-X--X                                                   X--X           XXXXXXXXXXXXXXXXX         X----------X        ',
                          '                              X--------X   X--------------------X--X                                                   X--X                                     X-Z--------X        ',
                          '                              X--H-----X   X--------------------X--X                                          XXXXXXXXXX--XXXXXXXXXX                            X----------X        ',
                          '                              X--------X   X-----------------------X            XXXXXXXXXXXXX                 X--------------------X                            XXXXXXXXXXXX        ',
                          '                              XXXXXXXXXX   X-----------------------X            X-----------X                 X--------------Z-----X                                                ',
                          '                                           X--XXXXXXXXXXXXXXXXXXXXXX            X-----------XXXXXXXXXXXXXXXXXXX--------------------X              XXXXXXXXXXXXXXXXXXXXXXXXXXXX      ',
                          '                                           X--X                                 X--K-----------------------------------------------X              X---------------------S----X      ',
                          '                                           X--X                 XXXXXXXXXXXXXXXXX--------------------------------------------------X              X--------------------------X      ',
                          '                                           X--X                 X---------------------------XXXXXXXX--XXXXXXXXX--P-----------------X              X--------------------------X      ',
                          '                                           X--X                 X---------------------------X      X--X       XXXXXXXXXXXXXXXXXXXXXX              XXXXXXXXXXXX--XXXXXXXXXXXXXX      ',
                          '                                           X--X                 X--XXXXXXXXXXXXXXXXXXXXXXXXXX      X--X                                                      X--X                   ',
                          '                                           X--XXXXXXXXXXXXXXXXXXX--X                               X--X                                                      X--X                   ',
                          '                                           X---------Z-------------X                               X--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X                   ',
                          '                                           X-----------------------X                               X------------------------------------------------K-----------X                   ',
                          '                                           XXXXXXXXXXXXXXXXXXXXXXXXX                               X-------K----------------------------------------------------X                   ',
                          '                                                                                                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                   ',
                          '                                                                                                                                                                                    ',
                          '                                                                                                                                                                                    ']

allMaps['Catacombs', 4] = ['                                                                         ',
                           '                                                                         ',
                           '                         XXXXXXXXXXXXXXXXXXXXX                           ',
                           '                         X-P--------------S--X                           ',
                           '                         X-------------------X                           ',
                           '                         X----XXXXXXXXXXXXXXXX                           ',
                           '               XXXXXXXXXXX----X                                          ',
                           '               X--------------X                                          ',
                           '               X--------------X                                          ',
                           '               X--XXXXXXXXXXXXX                                          ',
                           '               X--X                                                      ',
                           '               X--X       XXXXXXXXXXXXXXXXXXXXX                          ',
                           '               X--X       X-----------------U-X                          ',
                           '               X--X       X-------------------X                          ',
                           '               X--X       X--XXXXXX-----------X                          ',
                           '               X--XXXXXXXXX--X    X-----------X                          ',
                           '               X-------------X    X-----*-----X                          ',
                           '               X-------------X    X-----------X                          ',
                           '               XXXXXXXXXXXXXXX    XXXXXXXXXXXXX                          ',
                           '                                                                         ',
                           '                                                                         ',
                           '                                                                         ',
                           '                                                                         ',
                           '                                                                         ',
                           '                                                                         ',
                           '                                                                         ',
                           '                                                                         ']

allMaps['Forest', 0] = ['  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXjgggggggggggggggggggggggggggggggggggggggggiXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXjggh----------------------------------D------fggiXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXjggh-------abbbbbbc--------------------------------fggiXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXjggh---------akXXXXXXlc----------------------------------fggiXXXXXXXXXXX   ',
                          '  XXXXXXXXjggh------------dXXXXXXXXe------------n----------abbc----------fggiXXXXXXXX   ',
                          '  XXXXXjggh---------------fggggggggh-----------------------dXXe-------------fggiXXXXX   ',
                          '  XXjggh---------------------------------------------------dXXe----------------fggiXX   ',
                          '  XXe-----abbbbbbbbbc--------------------------------------dXXe-------------------dXX   ',
                          '  XXe-----dXXXXXXXXXe--------------------------------------dXXe-------------------dXX   ',
                          '  XXe-----dXXXXXjgggh----------------abbbbbbbbbc-----------fggh-------------------dXX   ',
                          '  XXe--o--dXXXXXe--------------------dXXXXXXXXXe----------------------------------dXX   ',
                          '  XXe-----fgggggh--------------------dXXXXXXXXXe---------------------------m------dXX   ',
                          '  XXe------------------------n-------dXXXXXXXXXe----------------------------------dXX   ',
                          '  XXe--------------------------------dXXXXXXXXXe----------------------------------dXX   ',
                          '  XXe--------------------------------fgggggggggh----------------------------------dXX   ',
                          '  XXe----------------------------------------------------------abbbbc-------------dXX   ',
                          '  XXe--------------m------------------------------------o------dXXXXe-------------dXX   ',
                          '  XXlbbc----------------------------------S--------------------dXXXXe----------abbkXX   ',
                          '  XXXXXlbbc----------------abbbc-------------------------------fiXXjh-------abbkXXXXX   ',
                          '  XXXXXXXXlbbc------------akXXXlc------------------abbbbbc------fggh-----abbkXXXXXXXX   ',
                          '  XXXXXXXXXXXlbbc---------fgggggh------------------dXXXXXe------------abbkXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXlbbc--------------------------n----fgggggh---------abbkXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXlbbc----------------------------------------abbbkXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXXXXXXXXX   ',
                          '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']

allMaps['Forest', 1] =   ['   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXjggiX   ',
                          '   XXjggggggggggggggggggggggggggiXXXXXXXXXXXXXjgggggggggggggggiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXeD-dX   ',
                          '   XXe--------------------------dXXXXXXXXXXXXXe---------------fgggggiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dX   ',
                          '   XXe----abbbc-----------------fgggggggggggggh-----n----F----------fggggiXXXXjgggggggggiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dX   ',
                          '   XXe----dXXXe----------------------------------------------------------dXXXXe---------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dX   ',
                          '   XXe----fgggh-C-----------F--------------------------------------------dXXXXe---P-----dXjgggggggggggggggggggggggggggiXXe--dX   ',
                          '   XXe-------------m------------abbbbbbbbbbbbbc----abbbbbc-------m-------dXXXXe---------dXe---------------m-----------dXXe--dX   ',
                          '   XXlbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXlbbbbkXXXXXlbbbbbbbbbbbbc--dXXXXlbbbbbbc--dXe----abbbc----------F-------dXXen-dX   ',
                          '   XXXXXjgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggh--dXXXXXXXXXXXe--dXe----fgggh----------abbbbc--dXXe--dX   ',
                          '   XXXjgh-------m----------------------F---------------------------------dXXXXXXXXXXXe--dXe------o------------fggggh--dXXe--dX   ',
                          '   jggh---------------------------------------------n--------------------fgggggggggggh--dXlbbbbbbbbbbbbc--------------dXXe--dX   ',
                          '   e----------------abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc--------o--------fggggggggggggggh--abbbbbbbbbbbkXXe--dX   ',
                          '   e----------abbc--dXjgggggggggggggggggggggggggggggggggggiXXXXXXXXXXXe-----------------------------------dXXXXXXXXXXXXXXe--dX   ',
                          '   e--o-------dXXe--dXe-------------o---------------------fgggggggiXXXe--abbbbbbbbbbbc------n-------------dXXXXXXXXXXXXXXe--dX   ',
                          '   e----------dXXe--dXe------abbbbbbbbc---------------------------dXXXe--dXXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXXe--dX   ',
                          '   e--abbbbbbbkXXe--dXe-----akXXXXXXXXlc----------------F---------dXXXe--dXXXXXXXXXXXXggggggjggggggggggggggggggggggggggggh--dX   ',
                          '   e--dXXXXXXXXXXe--dXe----akXXXXXXXXXXlc-------------------------dXXXem-dXXXXXXXXXXXXXXXXXXe-m-----------------------------dX   ',
                          '   e--dXXXXXXXXXXe--dXe----fggggggggggggh--------m----------------dXXXe--dXXXXXXXXXXXXXXXXXXe-----------------o---------F---dX   ',
                          '   e--dXXXXXXXXXXe--dXe------------------------------abbbbbbc-----dXXXe--dXXXXXXXXXXXXXXXXXXe--abbbbbbbbbbbbbbbbbbbbbbbbbbbbkX   ',
                          '   e--dXXXXXXXXXXe--dXe------------------------------dXXXXXXe-----dXXXe--fgggggggggggggggiXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '   e--dXXXXXXXXXXe--dXe------F-----------------------fggggggh-----dXXXe-------n----------dXXe--fgggggggggggggggggiXXXXXXXXXXXX   ',
                          '   e--fgggggggggie--dXe---------n---------------------------------dXXXe------------------dXXe--------------------dXXXXXXXXXXXX   ',
                          '   e------------de--dXe---------------------------------------o---dXXXlbbbbbbbbbbbbbbbcF-dXXe--------------------dXXXXXXXXXXXX   ',
                          '   e------------de--dXlbbbbbbbbbbbbbbbbbbbbc--abbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXXXXXXXe--dXXlbbbbbbbbbbbbbbbbbc--dXXXXXXXXXXXX   ',
                          '   e-n----abbc--de--fggggggggggggggggggggggh--fggggggggggggggggggggggggiXXXXXXXXXXXXXXe--fggggggggggggggggggggh--dXXXXXXXXXXXX   ',
                          '   e------fggh--de-------m---------------------------------------------dXXXXXXXXXXXXXXe--------------------------dXXXXXXXXXXXX   ',
                          '   e------------de--------------------------------------------n--------dXXXXXXXXXXXXXXe-------------n------------dXXXXXXXXXXXX   ',
                          '   e---F--------dlbbbbbbbbbbbbbbbbbbbbbbbbbc--abbbbbbbbbbbbbbbbbbbbbc--dXXXXXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXX   ',
                          '   e------------fgggggiXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXe--fgggggggggggggggggggggggggggggggggggggggggggggggiXXXXXX   ',
                          '   lbc----------------dXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXe--------------------------------------------------dXXXXXX   ',
                          '   XXe-------o---P----dXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXe---------------------------------m----------------dXXXXXX   ',
                          '   XXlbbbbbbbbbbbbbbbbkXXXXXXXXXXjgggggggggh--fgggggggggggggggggggiXlbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc--dXXXXXX   ',
                          '   XXXXXXXXjgggggggggggggggggggggh---n----------------------------fgggggggggggggggggggggggggggggggiXXXXXXXXXXXXXXXXXe--dXXXXXX   ',
                          '   XXXXXXXXe--------------------------------F---abbbbbbbbbbbc--------------o----------------------dXXXXXXXXXXXXXXXXXe--dXXXXXX   ',
                          '   XXXXXXXXe------------------------------------fgggggggggggh-------------------------------------dXXXXXXXXXXXXXXXXXe--dXXXXXX   ',
                          '   XXXXXXXXe----------------------------------------------------------------------abbbbbbbbbbbbc--fgggggggggggggiXXXe--dXXXXXX   ',
                          '   XXXXXXXXe---------m----------abc-------------------------------------n---------dXXXXXXXXXXXXe----------------dXXXe--dXXXXXX   ',
                          '   XXXXXXXXlbbbbbbbbbbbbbbbc----fgh----F-------abbbbc--------------------abbbbbc--dXXXXXXXXXXXXe-----------m----dXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe------------------akXXXXlc-----------abbc----dXXXXXe--dXXXXXXXXXXXXe--abc-----------dXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe------------------fggggggh--o--------dXXe----dXXXXXe--dXXXXXXXXXXXXe--fgh-----------dXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe------abbbbbc------------------------fggh----dXXXXXe--dXXXXXXXXXXXXe---------F------dXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe--abbbkXXXXXe----------------------F---------dXXXXXe--dXXXXXXXXXXXXe--n---------abbbkXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe--fgggggggggh--------------------------------dXXXXXe--dXXXXXXXXXXXXe----------abkXXXXXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe--------------------------------------abbbbbbkXXXXXe--dXXXXXXXXXXXXlbbbbbbbbbbkXXXXXXXXXe--dXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXe----------n----------------------abbbbkXXXXXXXXXXXXe--dXjggggggggggggggggggggggggiXXXXXXe-FdXXXXXX   ',
                          '   XjgggggggggggggggggggiXXlbbbbbbbbbbbbbbbbbbbc--abbbbbbbbbbkXXXXXXXXXXXXXXXXXem-dXe-------m----------------fggggiXe--dXXXXXX   ',
                          '   Xe----------------F--dXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXlbbbc---------F---------------dXe--dXXXXXX   ',
                          '   Xe-n-----------------dXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXjgggh-----------n---------P---dXe--dXXXXXX   ',
                          '   Xe----XXXXXXXXXX-----dXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXe-----------------------abbbbbkXe--dXXXXXX   ',
                          '   Xe----XXXXXXXXXX--m--fggggiXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXlbbc--abbbbbbbbbbbbbbbbbkXXXXXXXe--dXXXXXX   ',
                          '   Xe----XXXXXXXXXX----------dXXXXXXXXXXXXXXXXXem-dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXe--dXXXXXXXjgggggggggggggggggh--dXXXXXX   ',
                          '   Xe------------------------dXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXe--dXXXXXXXe------------o-------dXXXXXX   ',
                          '   Xe-----o------------------dXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXe--dXXXXXXXe--------------------dXXXXXX   ',
                          '   Xe--abbbbbbbbbbbbbbbbbbc--fgggggggggggggggggh--fggggggggggggggggggiXXXXXXXXXe--dXXXXe--dXXXXXXXe--abbbbbbbbbbbbbbbbbkXXXXXX   ',
                          '   Xe--dXXXXXXXXXXXXXXXXXXe----------------------------------o-------dXXXXXXXXXe--dXXXXe-ndXXXXXXXe--fggggggggggggggggggggiXXX   ',
                          '   Xe--dXXXXXXXXXXXXXXXXXXe------------n---------F-------------------dXXXXXXXXXe-odXXXXe--dXXXXXXXe-----------------------dXXX   ',
                          '   Xe--fgggggggiXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbbc--abbbbbbbbbbbbbbbc--dXXXXXXXXXe--dXXXXe--dXXXXXXXe------n----------------dXXX   ',
                          '   Xe---F------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXe--dXXXXXXXXXe--dXXXXe--dXXXXXXXlbbbbbbbbbbbbbbbbbbbbc--dXXX   ',
                          '   Xe----------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXe--dXXXXXXXXXe--dXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXX   ',
                          '   Xlbbbbbbbc--dXXXXXXXXXXXXXXXXXjgggggggggggggh--dXXXXXXXXXXXXXXXe--dXXXXXXXXXe--fggggh--fgggggggggggggggggggggiXXXXXXe--dXXX   ',
                          '   XXXXXXXXXe--fgggggggggggggggggh--------m-------dXXXXXXXXXXXXXXXe--dXXXXXXXXXe--------------------------------dXXXXXXe--dXXX   ',
                          '   XXXXXXXXXe----------F--------------------------dXXXXXXXXXXXXXXXe--dXXXXXXXXXe-------m------------------------djgggggh--dXXX   ',
                          '   XXXXXXXXXe-------------------------------------djggggggggggggggh--fgggggggggh----------abbbbbbbbbbbbbbbbbbc--de--------dXXX   ',
                          '   XXXXXXXXXe-nabbbbbbbbbbbbbbbbbc-n--------------de---F---------------------------n------dXXXXXXXXXXXXXXXXXXe--de--------dXXX   ',
                          '   XXXXXXXXXe--dXXjgggiXXjgggggiXe----------------de------------m-----------------ac------dXXXXXXXXXXXXXXXXXXe--de---F----dXXX   ',
                          '   XXXXXXXXXe--dXXe---fggh-----dXlbbbbbbbbbbbbbc--de---abbbc---------abbbbbbbbc---de---F--dXXXXXXXXXXXXXXXXXXe--fh--------dXXX   ',
                          '   Xjgggggggh--dXXe---P--------fgggggggggggggggh--de---fgggh---------dXXXXXXXXe---fh------dXXXXXXXXXXXXXXXXXXe------------dXXX   ',
                          '   Xe----------dXXe----o----------------m---------de--n--------------dXXXXXXXXe-----------dXXXXXXXXXXXXXXXXXXe---------o--dXXX   ',
                          '   Xe-m--------dXXe-------------------------------dlbbbbbbbbbbbbbbbbbkXXXXXXXXe---------abkXXXXXXXXXXXXXXXXXXlbbbbbbbbbbbbkXXX   ',
                          '   Xe--abbbbbbbkXXlbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXXXXXXXXXXXXXXXe---o-----dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '   XeS-dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbbbbbbbbbkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '   XlbbkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']

allMaps['Forest', 2] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXjgggggggggggggggggggggggiXXXXjggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggiXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXe-----------------------fggggh-----------------------n------------------------------------dXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXe-----------m----------------------------------F-----------abbbbbbc-----------------------dXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXe--abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXlbbbbbbbbbc------m------dXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXjgggggggggggggggiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe-------------dXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXjgggggggh--fgggggggiXXXXXXXXXXXXXXXXXe---------------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe-------------dXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXe------------------dXXXXXXXXXXXXXXXXXe---------------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe-------------dXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXe----F--------n----dXXXXXXXXXXXXXXXXXe------abc---n--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--abbbbbbbbbbkXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXe-------abbc-------dXXXXXXXXXXXXXXXXXe-----akXlc-----dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXjggggiXXjggggiXXXXXXXX   ',
                          '    XXXXXXXXXe-------dXXe-------fgggggggggiXXXXXXXe-P---fgggh-----fggggggggggggggggggggggggggggggh--dXXXXe----dXXe----dXXXXXXXX   ',
                          '    XXXXXXXXXe---o---fggh-----------------dXXXXXXXe---m---------------------------------------------dXXXXe-P--fggh----dXXXXXXXX   ',
                          '    XXXXXXXXXe----------------------------dXXXXXXXe-----------------------m-----------------F-------dXXXXe-----n------fgiXXXXXX   ',
                          '    XXXXXXXXXe--abbbbbbbbbbbbbbbbbbbbbbc--dXXXXXXXlbbbbbbbc--abbbc----------------------------o-----dXXXXlbbbc-----F----dXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXe-odXXXXXXXXXXXXXXXe--dXXXe---------abbbbbbbbc---------------dXXXXXXXXe----------dXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXe--dXXXe---------dXXXXXXXXe---------------dXXXXXXXXe----------dXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXjgggggggggggh--fggggiXXXXXXXXXXe--dXXXe-F-------fggggggggh---------------dXXXXXXXXe----------dXXXXXX   ',
                          '    XXXXXXXXXem-dXXXXXXXXXXe-------------------fgiXXXXXXXXe--dXXXe----------------------------------dXXXXXXXXe-----o----dXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXe---------------------fggggiXXXe--dXXXe--------------n-------------------dXXXXXXXXe----------dXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXe--------------------------dXXXe--dXXXe----------------------------------dXXXXXXXXe--abbbbbbbkXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXe-----n--------F-----ac----dXXXe--dXXXlbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXe--dXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXe--dXXXXXXXXXXe--------------------de----dXXXe--dXXXXXXXXXjgggggggggggggggggggggggggggggggggggggh--fggggggiXXXXXXX   ',
                          '    XXXXXXjggh--fgggiXXXXXXe--------------------de----dXXXe--dXXXXXXXXXe-----------------------------------------------dXXXXXXX   ',
                          '    XXXjggh---------dXXXXXXe--------------------fh----dXXXe--dXXXXXXXXXe----m------abbbbbc----------------F--------o---dXXXXXXX   ',
                          '    jggh------------dXXXXXXe-------abbbc--------------dXXXe--dXXXXXXXXXe-----------fgggggh--------n------abbbc---------dXXXXXXX   ',
                          '    e-----------m---dXXXXXXe---F--akXXXlc-----o-------dXXXe--dXXXXXXXXXe------F-------------------------akXXXlc--------dXXXXXXX   ',
                          '    e-L-abbbbc------dXXXXXXe-----akXXXXXlc------------dXXXe--dXXXXXXXXXe--------------------------------fgggggh--------dXXXXXXX   ',
                          '    e---fggggh---F--dXXXXXXe-----fgggggggh-----abbc---dXXXe--dXXXXXXXXXe-----------------------------------------------dXXXXXXX   ',
                          '    e---------------dXXXXXXe-------------------fggh---dXXXe--dXXXXXXXXXlbbc--abbbbbbbbbbbbbbbbbbbbbbbbbbbbc------------dXXXXXXX   ',
                          '    e--o------------dXXXXXXe----------n---------------dXXXe--dXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe-----m------dXXXXXXX   ',
                          '    e---------------fggggiXlbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXe--dXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXe------------dXXXXXXX   ',
                          '    lbbbbbbbbbc-----n----dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--fggggggggggggh--fgggggggggggggiXXXXXXXXXXXXXXe------------dXXXXXXX   ',
                          '    XXXXXXXXXXe----------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--------------------------------dXXXXXXXXXXXXXXe------------dXXXXXXX   ',
                          '    XXXXXXXXXXlbbbbbbbc--dXXXXjgggggggggggiXXXXXXXXXXXXXXXe---abbbbbbbc-----------n--------dXXXXXXXXXXXXXXe--abbbbbbbbbkXXXXXXX   ',
                          '    jgggggggggggggggggh--dXjggh-----------dXXXXXXXXXXXXXXXe---fgggggggh--------------------dXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXX   ',
                          '    eD-------o-----------dXe-------P-o----dXXXXXXXXXXXXXXXe---o-----------------abc--------dXXXXXXXXXXXXXXen-dXXXXXXXXXXXXXXXXX   ',
                          '    e--------------------dXe--------------dXXXXXXXXXXXXXXXe-----------F---------fgh--------dXXXXXXXXXXXXXXe--dXXXXXjggggggggiXX   ',
                          '    lbbbbbbbbbbbbbbbbbbbbkXe--------------dXXXXXXXXXXXXXXXe--------------------------------dXXXXXXXXXXXXXXe--fgggggh--------dXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXe--m-----------dXXXXXXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXXe-------------F---dXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXlbbbbbbbbbbbc--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe------------abc--dXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--abbbbbc---fgh--dXX   ',
                          '    XXjggggggggggggggggggggggggggggggggh--fgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggh--dXXXXXe--------dXX   ',
                          '    XXe------------------------------------------n-----------------------------------------------------------dXXXXXe-----m--dXX   ',
                          '    XXe-----------------------------------------------------------------------------------------o------------dXXXXXlbbbbbbbbkXX   ',
                          '    XXe----m-abbbc---------F---------abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXXXXXXX   ',
                          '    XXe-----akXXXlc--------------o---dXXXXXXXXXjgggggggggggggggggggggggggggggggggiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXe-----fgggggh------------------dXXXXXXXXXe--------n-------------------m----dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXe-----------------abbbbbbbc----dXXXXXXXXXe----------------------------m----dXXXXXXXXXXXXXXXXXXXXXjggggggggggggggiXXXXXXXX   ',
                          '    XXe------F------n---fgggggggh----dXXXjgggggh--abbbbbbbbbbbbbbbbbbbbbbbbbbbc--dXXXXXXXXXXXXXXXXXXXXXe-----------m--dXXXXXXXX   ',
                          '    XXe------------------------------dXXXe--m-----fgggggiXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXe---abbbbc-----dXXXXXXXX   ',
                          '    XXlbbbbc--abbbbbbbbbbbbbbbbbbbbbbkXXXe--------------dXXXXXXXXXXXXXXXXXXXXXe--fgggggggggggggggggggggh---dXXXXe-----dXXXXXXXX   ',
                          '    XXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXe---------F----dXXXXXXXXXXXXXXXXXXXXXe---------n------------------fggggh-----dXXXXXXXX   ',
                          '    XXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXe----------n---dXXXXXXXXXXXXXXXXXXXXXe---------------------------o-------F---dXXXXXXXX   ',
                          '    XXXXXXXe--fgggggggiXXXXXXXXXXXXXXXXXXe--------------dXXXXXXXXXXXXXXXXXXXXXe--abbbbbbbbbbbbbbbbbbbbbc--------------dXXXXXXXX   ',
                          '    XXXXXXXe-o--------fggggggggggggggggggh--------------fgggggggiXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXe---abc--------dXXXXXXXX   ',
                          '    XXXXXXXe----------------------------------o-----------------fgiXXXXXXXXXXXeo-dXXXXXXXXXXXXXXXXXXXXXlbbbkblbbbbbcn-dXXXXXXXX   ',
                          '    XXXXXXXe-abbc--m----------n-----------------------------------dXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXX   ',
                          '    XXXXXXXe-fggh-----abbbbbbbbbbbbc-------------------------abbbbkXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXX   ',
                          '    XXXXXXXe----------dXXXXXXXXXXXXe---abbbbbbbbbbbc--m------fggiXXXXXXXXXXXXXe--dXXXXXXXXjgggggggggggggggggggiXXXXe--dXXXXXXXX   ',
                          '    XXXXXXXen--abbbc--dXXXXXXXXXXXXe---dXXXXXXXXXXXe------------dXXXXXXXXXXXXXe--fggggggggh-------------o-----dXXXXe--fggggggiX   ',
                          '    XXXXXXXe---dXXXe--dXXXXXXXXXXXXe---fgggggggggggh-F----------dXXXXXXXXXXXXXe----------------m----------P---dXXXXe---o-----dX   ',
                          '    XXXXXXXe---fgggh--dXXXXXXXXXXXXe------n---------------abbc--dXXXXXXXXXXXXXe-------------------------------dXXXXe---------dX   ',
                          '    XXXXXXXe----------dXXXXXXXXXXXXe----------------------dXXe--dXXXXXXXXXXXXXlbbbbbbbbbbbc-------------------dXXXXlbbbbbbc-mdX   ',
                          '    XXXXXXXe---o--F---dXXXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbbbbkXXlbbkXXXXXXXXXXXXXXXXXXXXXXXXXe----F------n-------dXXXXXXXXXXXe--dX   ',
                          '    XXXXXXXe----------dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe-------------------dXXXXXXXXXXXe--dX   ',
                          '    XXXXXXXlbbbbbbbbbbkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbbbbbbbbbbbbbbbbbbbkXXXXXXXXXXXeS-dX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbbkX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Forest', 3] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXjggggggggggiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXjgh----------fgiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXjgh-----U-n------fgiXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXe------------------dXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbc---m----------abkXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbc----------abkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbbbc--abbbkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXjggggggggh--fggggggggggiXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXjgh----------------------fgiXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXjgh------m-----*-o-----------fgiXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXjgh------------------------------fgiXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXe----------------------------------dXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXe----------------------------------dXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXe--------------n-------------------dXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXlbc-----o------------------------abkXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXlbbbc----------------m-----abbbkXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXlbbbc--------------abbbkXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlc------------akXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXjgh--------n---fgiXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXjgh----------------fgiXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXe--P------S----------dXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbc----------------abkXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbc------------abkXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXlbbbbbbbbbbbbkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Tundra', 0] = ['                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                              XXXXXX                         ',
                          '                                          XXXXX----XXXX                      ',
                          '                                       XXXX------D----XXXXX                  ',
                          '                                     XXX------------------XX                 ',
                          '                                     X---------------------XX                ',
                          '                                     X----------------------X                ',
                          '                                     X----------------------X                ',
                          '                                    XX---------------------XX                ',
                          '                                  XXX--------------------XXX                 ',
                          '                       XXXXXXXXXXXX---------------------XX                   ',
                          '                     XXX-------------------------------XX                    ',
                          '                 XXXXX---------------------------XXXXXXX                     ',
                          '              XXXX------------------XXXXXXXXXXXXXX                           ',
                          '           XXXX--------------------XX                                        ',
                          '           X-----------------------X                                         ',
                          '           X-----------------------X                                         ',
                          '           X-----------------------X                                         ',
                          '           XXXX-----------S-------XX                                         ',
                          '              XXXX-------------XXXX                                          ',
                          '                 XXXXXXXXXXXXXXX                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ',
                          '                                                                             ']

allMaps['Tundra', 1] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX----------------------I-------XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXX   ',
                          '    XXX---------------------------------------------------------------------E------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXX   ',
                          '    XXX----------------------------------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXXXXXXXXXXX   ',
                          '    XXX------------------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------E----XXXXXXXXXXXXXX   ',
                          '    XXX-----I------------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXX   ',
                          '    XXX------------------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXX   ',
                          '    XXX------------------------------XXXXXXXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------------------------------E-------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXX   ',
                          '    XXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXX-----------------------------------------I----------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------------------P--XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX-----E----XXXXXXXXXXXXXXXXXX------------I-------XXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX-P--------XXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXX--------D---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------E-----------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--------P--------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX----------------------------I------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--I--------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---I---XXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------------------------------XXXXXXXXXXXXXXXXXXXXXX------------I-----XXX   ',
                          '    XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXX------------------------------------------XXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXXXXXXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXX---------------------------I--------------------------------------XXXXXXXXXXXXXXXXXXXX----------------------------------------------------XXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--------------------------------------------XXXXXXXXXXXXXXXXXXXX----------------------------------------------------XXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------P--XXX   ',
                          '    XXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------I-----------XXX   ',
                          '    XXXXXX--S---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Tundra', 2] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX-------------------------------------I--------------------------------------------------------------------------------------------------XXXXXXXXXXX   ',
                          '    XXX--------------------------------------------------------------------------------------------------------I-------------------------------XXXXXXXXXXX   ',
                          '    XXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXX--XXXXXXX---------------------------------------------------------------------------XXXXXXXXXXX--------------I------------------XXXXXXXX   ',
                          '    XXX---------XX--XXXXXXX-------E-------------------------------------------------------------E-----XXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX---------XX--XXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX---I-----XX--XXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX---------XX--XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXX------------------------E--------XXXXXXXX   ',
                          '    XXX--XXXXXXXXX--XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXX---------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXX----------------------------------------------------------XXXXXXXX------------------XXXXXXX--------E----------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXX----------------------------------------------------------XXXXXXXX--I---------------XXXXXXX-------------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXX------------------XXXXXXX--XX---------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXX------------------XXXXXXX--XX---------------------------------XXXXXXXX   ',
                          '    XXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXX----------------XXXXX------------------------------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXX-----E----------XXXXX--------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXX--XXXXXXX----------------XXXXXXX--XXXXXXXXXXX   ',
                          '    XXX----------------XXXXX-------------------------E------XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXX--XXXXXXX----------------XXXXXXX--XXXXXXXXXXX   ',
                          '    XXX----------------XXXXX-------E------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-----I-----XXXXXXXXXXX--XXXXXXX----------------XXXXXXX--XXXXXXXXXXX   ',
                          '    XXX------------P---XXXXX--------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXX--XXXXXXX----------------XXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX------------P---XXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX----------------XXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XX--------------------XXXXXXXXXXXXXXXX--XXXXX--------------------XXXXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XX----------------I---XXXXXXXXXXXXXXXX--XXXXX--------------------XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XX--------------------XXXXXXXXXXXXXXXX--XXXXX--------------------XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX---------------I----XXXXXXX   ',
                          '    XX---I----------------XXXXXXXXXXXXXXXX--XXXXX--------XXXXXXXXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XX--------------------------------------XXXXX--------XXXXXXXXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XX--------------------------------------XXXXX--------XXXXX--------------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--------XXXXX--------------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX----P---XXXXX--------------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX---I----------------XXXXXXX   ',
                          '    XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--------XXXXX--------------E-----------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------XXXXXXX   ',
                          '    XXXXX-----------------------------XXXX--XXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXX-----------------------------XXXX--XXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXX------------------------P----XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXX------E----------------------XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXX-----------------------------XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXX-----------------------------XXXX-------------------I-----------------------------------------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXX------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------------------------------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------XXX   ',
                          '    XXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXX------XXX   ',
                          '    XXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXX-----------------I------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXX-----E------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------I-------------XXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXX--XXXXXX-----I---------------XXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXX-----------XXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXX-----------XXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXX-----------XXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXX----E------XXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXX---------------------XXXXXXXXX-----------XXXX   ',
                          '    XXXXXXXXXXXXXX----------------------------------------------------------------------------------------------------------------XXXXXXXXX-----------XXXX   ',
                          '    XXXXXXXXXXXXXX---------------------------------------------------------------------------------------------------------I------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XXXXXX---------------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XXXXXX---------------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX---------XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XXXXXX---------------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX---------XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXX--XXXXXX---------------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX-----------------------------------------------------------------------XXXXXXXX----------XXXXXX--XXXXXX----I----------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX---I---------------------------------------------------------E---------XXXXXXXX----------XXXXXX--XXXXXX---------------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX---------XXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXX----------XXXXXX--XXXXXX---------------------XXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX---------XXXXXXXXXXXXXXXXXXXXXX---------E------------------------------XXXXXXXX----------XXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XX---------XXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXX--E-------XXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXX------XXXX--XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXX----------XXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXX---P--------XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXX------------XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXX------XXXX--XXXXXXXX   ',
                          '    XXX----------P---XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--------------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------I----------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX----E---------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------XXXXXXXXXXXXXXXX------------XXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--------------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----E------XXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX-----XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX-----XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX-----------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX-----------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXX-------------------P-----XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----XXXXXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX------------E------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----XXXXXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----XXXXXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----XXXXXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----XXXXXXXX   ',
                          '    XXX-----------XXXXXXXXXXXXXXXXXXX--------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXXXXX-----XXXXXXXX   ',
                          '    XXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXXXXX-----XXXXXXXX   ',
                          '    XXX-S---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------I--------XXXXXX--------I--------XXXXXXXXXXXXXXXXXXXXXXXXXXX-B-----------------XXXXXXXX-D---XXXXXXXX   ',
                          '    XXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXXXXX-----XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Tundra', 3] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------XXXXXXXXXXXXXXXXXXX---------------------S----XXXXXXX   ',
                          '    XXXXX----------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------XXXXXXXXXXXXXXXXXXX--------------------------XXXXXXX   ',
                          '    XXXXX----------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--------------------------XXXXXXX   ',
                          '    XXXXX--XXXXXXXXXXXXXXXXXXXX------------------I-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--------------------------XXXXXXX   ',
                          '    XXXXX--XXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXX--XXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXX-------------XXXXXXXXX------E-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--------XXXXX   ',
                          '    XXXXX-------------XXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXI-XXXXXXXXXXXXXXXXXXXXX-----------------------P--XXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXI-------------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX-----------------------------E-----XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-------XXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX---------E-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-------XXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX-----------------------------------XXXXXX------------XXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX------------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX-----------------------------------XXXXXX---------P--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX------------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------------XXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX-------E----------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------------XXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX------------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX------------------XXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXX----------------XXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXX----------------XXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----I-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------------------------I---------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------XXX-------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------XXX-----------------E-------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------XXX---------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------XXXXXXXXX-------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------------P---------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------XXXXX-------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------XXXXX-------------I-----------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------XXXXX-------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------I---------------------------------------XXXXX-------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------XXXXX-------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX------------------------------------------------------------------------------------------------------------E----------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--------------------------------------------------------------------------------------------------------------------------------XXXX-----------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--------------------------------------------------------------------------------------------------------------------------------XXXX-----------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--------------------------------------------------------------------------------------------------------------------------------XXXX-----------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--------------------------------------------------------------------------------------------------------------------------------XXXX-----------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--------------------------------------------E--------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX------------------------------------------------------------------------------XXX--------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX------------------------------------------------------------------------------XXX--------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX------------------------------------------------------------------------------XXX--------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--------P--------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------XXXXXX----------------------------------------------------------------------------------------------------------------------------I-----------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------XXXXXX----------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------XXXXXX----------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-------XXXXXX----------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXXX------------E-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXX----------------------E---------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXX--XXXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------XXXXXXXXXX--XXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX----------------I---------------XXXXXXXXX------------XXXXXXXXXX-----------XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--------------------------------XXXXXXXXX-----E------XXXXXXXXXX------I----XXXXXXXX   ',
                          '    XXX----------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXX--XXXXXXX--XXXXXXXX   ',
                          '    XXX---P------------XXXXXXX-------------------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXX--XXXXXXX--XXXXXXXX   ',
                          '    XXXXX--------E-----XXXXXXX----------------------I--------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX--XXXXXXXX   ',
                          '    XXXXX--------------XXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXX--------------------------XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--------XXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXX---------------------I----XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--------XXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXX--------------------------XXXXXXXXXXXXXXX-----------------------------------XXXXX--------XXXX   ',
                          '    XXX--------------XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------------------------XXXXXXXXXXXXXXX-----------------------------------XXXXX----P---XXXX   ',
                          '    XXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------I-------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--------XXXX   ',
                          '    XXX-D-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--------XXXX   ',
                          '    XXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Tundra', 4] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX--------XXXXXXXXXXXXXX-------------------I--------------------------------------XXXXXXXXXXXXXX---------------P---XXXXX   ',
                          '    XX------------XXXXXXXXXX-------O----------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX--XXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX------------XXXXXXXXXX------------------XXXXXXXXXXXXXXXX--------------XXXXXXXX--XXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX---I----XX--XXXXXXXXXX------------------XXXXXXXXXXXXXXXX--------E-----XXXXXXXX--XXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX--------XX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXX--XXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX--------XX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXX---------XXXXXXXXXX-------E-----------XXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXX---------XXXXXXXXXX-------------------XXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX-----E-------------------------XXXXX---------XXXXXXXXXX-------------------XXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXX----D----XXXXXXXXXX-------------------XXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXX---------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXX--------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXX--------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXX--------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXX--------E-----------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXX--------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXX--------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------------------------------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------------------------------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------E-----XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXX--------------XXXXXXXX   ',
                          '    XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX-------I------XXXXXXXX   ',
                          '    XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX--------------XXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--------------------------------------------------------------------------------------------------XXXXXXX   ',
                          '    XXXXXX--XXXXXXX--------------------------------------------------------------------------------------------------XXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------------------I---------------------------------XXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------------------------------XXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX----------I--------------------------------------------------XXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX------------------------------------------------------I------XXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------------------------------XXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXX--------------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXX--------------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXX--------------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXX------E-------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXX----------------P---XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXX--------------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------XXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------I-------XXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX-------------XXXXXXXXXXXX----------------------XXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------XXXXXXXXXXXX----------------------XXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------XXXXXXXXXXXX----------------------XXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX------E------XXXXXXXXXXXX----I-----------------XXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXXXXXXX------------------------------------XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXXXXXXX------------------------------------XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX------------------E---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXXXX-------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXX----E-----------------XXXXXXXXXXXXXXXX-------------------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXX-------------------------------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXX-------------------------------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX----------E---XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX---------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX----P---------XXX-----------------------------XXXXX   ',
                          '    XXXX----P----XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX--------------XXX-----------------------------XXXXX   ',
                          '    XXXX---------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------E---------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX-----------------------------XXXXX   ',
                          '    XXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXX-----------------------XXXXXXXX---------XXXXXXXXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXX---------XXXXXXXXX------------E----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXX---------XXXXXXXXX------------------------------------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXX--------------I----XXXXXXXXX------------------------------------------------------------XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXX-------------------XXXXXXXXX------I----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------XXXXXXXXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX---------------------I----XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXX------------------------E------------XXXXXX--XXXXXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX-E-----------------------------------------------------XXXXXX--XXXXXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX-----------------------E-------------------------------XXXXXX--XXXXXXXXX-----------------E--------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXX-------------------------------------XXXXXX--XXXXXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXX----I---------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXX-----------XXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXX-----------XXXXXX--------------------------XXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXX-----------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXX--P--------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX-----------XXXXXXXX   ',
                          '    XXX--XXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX-----E-----XXXXXXXX   ',
                          '    XXX------------XXXXXXXXX---------------XXXXXXXXXXX--------------------------------------XXXXXXXXXXXXX-----------XXXXXXXX   ',
                          '    XXX------------XXXXXXXXX---------------XXXXXXXXXXX--------------------------------------XXXXXXXXXXXXX-----------XXXXXXXX   ',
                          '    XXX------------XXXXXXXXX-------I-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXX-----S------XXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX   ',
                          '    XXX------------XXXXXXXXX-----------------------------------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXX------------XXXXXXXXX-----------------------------------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Tundra', 5] = ['                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                             XXXXXXX                           ',
                          '                                             X-----X                           ',
                          '                                             X--U--X                           ',
                          '                                             X-----X                           ',
                          '                                             X-----X                           ',
                          '                                             X-----X                           ',
                          '                                             X-----X                           ',
                          '                                             X-----X                           ',
                          '                                             X-----X                           ',
                          '                                XXXXXXXXXXXXXX-----X                           ',
                          '                          XXXXXXX---------------XXXXXXX                        ',
                          '                        XXX---------------------------XXX                      ',
                          '                        X-------------------------------X                      ',
                          '                        X-------------------------------X                      ',
                          '                        X--------------*----------------X                      ',
                          '                        X-------------------------------X                      ',
                          '                        X-------------------------------X                      ',
                          '                        XXX---------------------------XXX                      ',
                          '                          XXXXXXX---------------XXXXXXX                        ',
                          '                             X-----XXXXXXXXXXXXXX                              ',
                          '                             X-----X                                           ',
                          '                             X-----X                                           ',
                          '                             X-----X                                           ',
                          '                             X---P-X                                           ',
                          '                             X-----X                                           ',
                          '                             X-----X                                           ',
                          '                             X-S---X                                           ',
                          '                             X-----X                                           ',
                          '                             XXXXXXX                                           ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ',
                          '                                                                               ']

allMaps['Volcano', 0] = ['                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                           XXXXXXXXXXXXXXXXXX                             ',
                          '                         XXX----------------X                             ',
                          '                         XXX----------------XX                            ',
                          '                       XXX-------------------X                            ',
                          '                    XXXX---------------------X                            ',
                          '                   XX------------------------X                            ',
                          '                  XX------------XXXXX--------X                            ',
                          '                  X-------------X  XXX--D--XXX                            ',
                          '                  X-------------X    XXXXXXX                              ',
                          '                  X-------------X                                         ',
                          '                  X-------------XX                                        ',
                          '                  X--------------XXXX                                     ',
                          '                  X-----------------XXXXXXXXXXX                           ',
                          '                  X---------------------------XX                          ',
                          '                  X----------------------------X                          ',
                          '                  X--------------------------S-X                          ',
                          '                  X----------------------------X                          ',
                          '                  XXXXXX----------------------XX                          ',
                          '                       XXXXXXXXXXXXXXXXXXXXXXXX                           ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ',
                          '                                                                          ']

allMaps['Volcano', 1] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX---------------------------------------------------------------------------------------A--------------------XXXXXXXXX---------P--XXXXXXX   ',
                          '    XXX--------------------------------------------A---------------------------------------------------------------XXXXXXXXX------------XXXXXXX   ',
                          '    XXX----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX------------XXXXXXX   ',
                          '    XXX----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXX----------------------XXXXXXXXX--------------------------------------------------------------XXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXXXXXXX   ',
                          '    XXX----------------------XXXXXXXXX--------------------------------------------------------------XXXXXXXXXXXXX--------------------XXXXXXXXXX   ',
                          '    XXX-S--------------------XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX--------------------XXXXXXXXXX   ',
                          '    XXX----------------------XXXXXXXXX--XXXXXXXXXX--------------------------------------XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX------A------------------A------------XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX--------------------------------------XXXXXXXXXX-------A-----------------XXXXXXXX--XXXXXXXXXX   ',
                          '    XXXXXXXXX---------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXX--XXXXXXXXXX   ',
                          '    XXXXXXXXX---------------------------XXXXXXXXXXXXX------------A-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XX------XX   ',
                          '    XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XX------XX   ',
                          '    XXXXXXXXX--XXX-------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXX--XX------XX   ',
                          '    XXXXXXXXX--XXX-------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXX--XXXXXXXX--XX--A---XX   ',
                          '    XXX--------XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXX--XXXXXXXX--XX------XX   ',
                          '    XXX--------XXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXX--XX------XX   ',
                          '    XXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX-------XXXX--XXXXXXXXA-XX------XX   ',
                          '    XXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX----------A------------XXXXXXXXXXXXXXXXX------------XXX--XXXXX-------XXXX--XXXXXXXX--XX------XX   ',
                          '    XXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-----------------XXXXX-------------XXXXXXXX--XX------XX   ',
                          '    XXXX--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX------A----------XXXXX---A---------XXXXXXXX--XXXX--XXXX   ',
                          '    XXXX--XX----XX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX------------XXX--XXXXX-------XXXX--XXXXXXXX--XXXX--XXXX   ',
                          '    XXXX----A---XX--XXXXX--P----------XXXX--------XXXXXXXXXXXX-----------------XXXXXXXXX------------XXX--XXXXX-------XXXX--XXXXXXXX--XXXX--XXXX   ',
                          '    XXXX--------XX--XXXXX-------------XXXX--------XXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXX--XXXX--XXXX   ',
                          '    XXXX--XX----XX--XXXXX-------------XXXX--XXXXXXXXXXXXXXXXXX--------D--------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXX--------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXX-------------XXXX--XXXXXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXX--------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXX-------------XXXX--XXXXXXXXXXXXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXX-------------XXXXXXXX--XXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXXX--------A----XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX-------------XXXXXXXX--XXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXX   ',
                          '    XXXX--XX----XX--XXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXX   ',
                          '    XXXX--------XX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX--XXX-------------XXX--XXXXXXXXXX   ',
                          '    XXXX--------XX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------A--------------------------------XXXXX-------A----------XXX--XXXXXXXXXX   ',
                          '    XXXX--XX----XXA-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------------------------------------XXXXX------------------XXX--XXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXX----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXX-------------XXX--XXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXX---P------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXX-----------P-XXX--XXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXX--------------------A-------XXXX--------------------------------------------------------XXX-------------XXX--XXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXX----------------------------XXXX--------------------------------------------------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXX   ',
                          '    XXXX--XX----XX--XXXX----------------------------XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX   ',
                          '    XXXX-----P--XX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX---------------------------------------XXXXXXXXXXX-----------------XXXXXXXXXX   ',
                          '    XXXX--------XX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX---------------------------------------XXXXXXXXXXX-----------------XXXXXXXXXX   ',
                          '    XXXX--XX----XX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX----------A------------------------A---XXXXXXXXXXXA-XXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXX---------------------------------------XXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXXX---------------------------------------XXXXXXXXXXX--XXXXX----------------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXXX--A--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX----------------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX-----A----------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXXX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX----------------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX----------------XXXX   ',
                          '    XXXX--XXXXXXXX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX--XX----XX--XXXXXXX-------A-----------XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX--------XX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXX-----------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX-----A--XX--XXXXXXX-------------------XXXXXXXXXX--XXXXXXX-----------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX--XX----XX--XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXX-------A---------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX----------------------------------------XXXXXXX-----------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXX----------------------------------------XXXXXXX-----------------XXXXXXXXXXXXX--XXXX------------------------------XXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXX------------------------------XXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--XXXX--------------------A---------XXXXXXXXXXXX   ',
                          '    XXXX----------------------------------A------------------------------------------------------XXXX-C----------------------------XXXXXXXXXXXX   ',
                          '    XXXX-----------------------------------------------------------------------------------------XXXX------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Volcano', 2] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------P--XXXXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXX   ',
                          '    XXXX-----A-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------XXXXXXXXX-----------XXXXX   ',
                          '    XXXX-----------------------------------------------------------------------------------XXXXXXXXX--A--------XXXXX   ',
                          '    XXXX----------------------------------------------------------------------------A------XXXXXXXXXXX--XXXXXXXXXXXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX------------------------------------------XXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX---A-------------------------XXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX-----------------------------XXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------A-----XXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXX   ',
                          '    XXXXXXXXXXX---------------------XXXXXXXXXXX--XXXXXXXXXXXXXXXX--------------------------------------------XXXXXXX   ',
                          '    XXXXXXXXXXX-----------------S---XXXXXXXXXXX--XXXXXXXXXXXXXXXX---------------A----------------------------XXXXXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXX-----XXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXX   ',
                          '    XXXXXXXXXXXXXX--XXXXXXXXXXX-----XXXXXXXXXXX-----XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----A-------XXXXXXX   ',
                          '    XX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXX   ',
                          '    XX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXX-P---XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XX--A---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XX------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XX------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX---------------XXXXXXXXXXXXX----------XX   ',
                          '    XX------XXXXX-------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXX----------XX   ',
                          '    XXXX--XXXXXXX-------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------A---------XXXXXXXXXXXXX----------XX   ',
                          '    XXXX--XXXXXXX-------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXX-----A----XX   ',
                          '    XXXX--XXXXXXX------------------------------------XXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXX----------XX   ',
                          '    XXXX--XXXXXXX------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX----------XX   ',
                          '    XXXX--XXXXXXX-------------------XXXXXXXXXXXXXXX--XXXXXXXXX------XXXXXXXXXXXXXXX-------------------------------XX   ',
                          '    XXXX--XXXXXXX-------------------XXXXXXXXXXXXXXX--XXXXXXXXX------XXXXXXXXXXXXXXX-------------------------------XX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--A---XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX------XXXXXXXXXXXXXXX-------------------------XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX------XXXXXXXXXXXXXXX-------------------------XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------------XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------A--------------------------------------XXXXXXXX   ',
                          '    XXXX--XXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXX--XXXXXXXXX--XXXXXXXXXXXXX--XXXXXXXXXXXXX----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX---------XXX--XXXXXXXXXXXXX--XXXXXXXXXXXXX----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX----A----XXX--XXXXXXXXXXXXX--XXXXXXXXXXXXX-----A----------------------XXXXXXX------------XXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX--------------XXXXXXXXXXXXX--XXXXXXXXXXXXX----------------------------XXXXXXX------------XXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX--------------XXXXXXXXXXXXX--XXXXXXXXXXXXX----------------------------XXXXXXX------------XXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX---------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX----------------------------XXXXXXX------A-----XXXXXXXXXXXXXXXXXXXX   ',
                          '    XXX----P----XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX------------XXXXXX------XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX------------XXXXXX--A---XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX------------XXXXXX------XXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX------------XX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX------------XX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----P-----XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX------XXXX--XX   ',
                          '    XXXXXXXXXXXXXXXXX---------------------------XXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XXXXXX--XX   ',
                          '    X-------XXXXXXXXX---------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXX--XXXXXXXXX--XXXXXX--XX   ',
                          '    X-------XXXXXXXXX-------------------------------------------------------------------------------------XXXXXX--XX   ',
                          '    X-P-----XXXXXXXXX-------------A-----------------------------------------------------------------------XXXXXX--XX   ',
                          '    X-------XXXXXXXXX---------------------------XXXXXXX--XXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XX   ',
                          '    X-------XXXXXXXXX---------------------------XXXXXXX--XXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XX   ',
                          '    X-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XX   ',
                          '    X----A--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--A---XXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XX   ',
                          '    X--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXX--XXXXXXX----XX   ',
                          '    X--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXX--XXXXXXX-A--XX   ',
                          '    XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX--XXXX   ',
                          '    XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX----------A----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX--XXXX   ',
                          '    XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX--XXXX   ',
                          '    XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX--XXXX   ',
                          '    XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX--XXXX   ',
                          '    XXXXXXXX-------------------------XXXXXX---A-----------XXXX-----------------------------------------XXXXXXX--XXXX   ',
                          '    XXXXXXXX-------------------------XXXXXX---------------XXXX-----------------------A-----------------XXXXXXX--XXXX   ',
                          '    XXXXXXXX-------------------------XXXXXX---------------XXXX-----------------------------XXXXXXXXXXXXXXXXXXX--XXXX   ',
                          '    XXXXXXXX--------A----------------XXXXXXX--XXXXXXXXXXXXXXXX-----------------------------XXXXXXXXXXXXXXXX-------XX   ',
                          '    XXXXXXXX-------------------------XXXXXXX--XXXXXXXXXXXXXXXX-----------------------------XXXXXXXXXXXXXXXX-------XX   ',
                          '    XXXXXXXX-------------------------XXXXXXX--XXXXXXXXXXXXXXXX---A--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XX   ',
                          '    XXXXXXXX-------------------------XXXXXXX--XXXXXXXXXXXXXXXX------XXXXXXXX--------------------------------------XX   ',
                          '    XXXXXXXX-------------------------XXXXXXX--XXXXXXXXXXXXXXXX------XXXXXXXX--------------------------------------XX   ',
                          '    XXXXXXXX------------------A-------------------------------------XXXXXXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX------A-------------------------------------------------XXXXXXXX-------------XXXXXXXX----XXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX-------------------------XXXXXXXXXXXXXXXXX--XXXXXX------XXXXXXXX-------Y-----XXXXXXXX----XXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX-------------------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX------------------XXXXXXXX--D-XXXXXXXXXXXXXXX   ',
                          '    XXXXXXXX-------------------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX------------------XXXXXXXX----XXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXX--XXX-------------XXXXXXXXX--XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----A-----XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX   ',
                          '    XXXX-----A--XXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------------------XXXXXXXXXXX----------------XXXXXXXXXXXXXXXX--XXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXX---------------------------------------------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXX---------------------------------------------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXX------Y---------XXXXXXXXX--XXXXXXXXXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXX--XXXXXXXXXXX---------------M---------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXX--XXXXXXXXXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--A---------------------------------XXXXXXXXXXX-----------XXXXXXXXXXX-------------------------------XXXXXXXX   ',
                          '    XXXX------------------------------------XXXXXXXXXXX-----------XXXXXXXXXXX-------------------------------XXXXXXXX   ',
                          '    XXXX--------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----P------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Volcano', 3] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX-------------------------------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------Y--------XXXXXXXXXXXXXXXXXXXX----------------------M--------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXX-------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXX----Y--------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXX------M------------------------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXX---------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXX---------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--P-------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXX   ',
                          '    XX--------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXX   ',
                          '    XX--------XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXX   ',
                          '    XX--Y-----XXXXXXXXXXXXXX---------------------------------------------XXXXXXXXXXXXXXXXXXXXXX-------Y--------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---Y-------XXXXX   ',
                          '    XX--------XXXXXXXXXXXXXX---------------------------------------------XXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX--------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XX--------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------Y-----------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX---------------------------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---Y----------------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--------------Y------------------------XXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------Y---XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX----XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------XXXXXXXXXXXXXXXXX--------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------XXXXXXXXXXXXXXXXX--------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-P------------------XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX----XXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX-----------------Y----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-Y--XXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXX   ',
                          '    XXXXXXXX---------------------------------XXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXX   ',
                          '    XXXXXXXX---------------------------------XXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXX------------------------M--------XXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXX------M--------------------------XXXXXXXXXXX------XXXXXXXXXXXXXXXX------------P-XXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXX---------------------------------XXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXX--M---XXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXX-----------M---------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-D--XXXXXXXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------XXXXXXXXXXX   ',
                          '    XX-----------XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--M------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XX-----Y-----XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XX-----------XXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XX-----------XXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------------------------------------------------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX---------P--XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--Y--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---Y---XXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX-------L-------XXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXX-----XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXX---------------XXXXXXXXXXXXXXXX---------M-----------XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXX------------------XXX--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX------M----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------Y--------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------------------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX--------------------M--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------Y----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX----Y--------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----M-----------------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------P--XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXX-----------------------------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX------Y-------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXX--XXXXX----------XXXX   ',
                          '    XXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--Y--------------------------------------------------------------------------------------XXXX   ',
                          '    XXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------------------------------------------XXXX   ',
                          '    XXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----Y----XXXX   ',
                          '    XXXXXX-S--------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXX   ',
                          '    XXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Volcano', 4] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXX------------S--XXX   ',
                          '    XXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXX---------------XXX   ',
                          '    XXXXX-----------M------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------M---------XXXXXXXXXXX---------------XXX   ',
                          '    XXXXX----------------------------------------------------------------------------------XXXXXXXXXXX---------------XXX   ',
                          '    XXXXX----------------------------------------------------------------------------------XXXXXXXXXXX---------------XXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------XXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------XXXXXXXXX   ',
                          '    XXXXXX--XXXX------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXX------------XXXXXXXX-----------X---------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX----------Y-------XXXXXXXX-----------X---------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX------------------XXXXXXXX--XXXXXXX--X--XXXXXXX--XXXX--XXXXXXX--X--XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXX------------XXXXXXXX--X-----X--X--------X--X-----------X--X--X---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXX---------P--XXXXXXXX--X--Y--X--X--------X--X-----------X--X--X---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX--------X--X---M----X--X-------Y---X--X--X--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX--------X--X--------X--X-----------X--X--X--X------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXX--XXXXXXXXXXXXX--X--X--X------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX----------------------------------------------------X--X--X--X---------------------XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX----------------------------------------------------X--X--X--X---------------------XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X--X--X--XXXXX--XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX-------------X---------------------X--X--X---------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX-------------X---------------------X--X--X------M--XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXXXXXXXXXX--X--X--XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX-------------X--X------------------X--X------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX-------M-----X--X------------------X--X------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX-------------X--X---Y--------------X--X--XXXXXXXX--XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXX--X--X---------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXX--XXXXXXX--XXXXXXXXXXXXXXX--------------------------------------X--X-----Y---XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXX--------------------------------------X--X---------XXXXXXXXXXXXX--XXXX-----------XXX   ',
                          '    XXXX---------Y---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-------Y---XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-----------XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-----------XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX---Y-------XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-----------XXX   ',
                          '    XXXX--M----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX-----------XXX   ',
                          '    XXXX-------------XXXXXXXXXXXXXXX-----------------------X--X------------------------XXXXXXXXXXXXX--XXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------------------X--X---------Y--------------XXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXX--XXXXXXX-----X--XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--X--------X-----X-----X---------------------------XXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--X--------X-----X-----X--XXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--X----M---X-----X----------------X--X---------M---XXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--X--------X-----X----------------X--X-------------XXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXX-----X-----------Y----X--X------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX----------------------------X-----X----------------X---------X---------------------XXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXX----------------------------X-----XXXXXXXXXXXXXXXXXX---------X---------------------XXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X--------X-------------------------X------X------XXXXXXXXXXXXXXXXXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X--------X-------------------------X---Y--X------XXXXXXXXXXXXXXXXXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X----Y---XXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXX-----P-----XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X--------XXXXXXXX--X---------------M------X------XXXXXXXXXXXXXXXXXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX--X----------------------X------XXXXXXXXXXXXXXXXXXX-----------XXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------X--XXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--X--------------------------------Y-----XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------M-----X-----------X--------Y-----------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------X-----------X--------------------------XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XX-------------------------------------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XX--------------------------------------------Y----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XX-----------------XXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XX-----------------XXXXXXXXXXXXXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXX   ',
                          '    XX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXXXX   ',
                          '    XX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------XXXXXXX   ',
                          '    XX-D---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------M--------XXXXXXXXXXXXXXXX   ',
                          '    XX-----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']


allMaps['Volcano', 5] = ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXX-----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXX--------------Y----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXXXXXXXXX    ',
                          '    XXXX-------------------------------------------------XXXXXXXXXXXXXXX---------------------Y-------------XXXXXXXXXXX    ',
                          '    XXXX-----------------------------XXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-----------------------------------XXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX--XXXXXXXXXXXXXX-------------------XXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXX--------XXXXXXXXXXX-------------------XXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXX--XXXXXXXXXXXX--------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX--------------XXXXXXXXXXX------XXXXXXXXXX---M----XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX---M----------XXXXXXXXXXX------XXXXXXXXXX--------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXX--------------XXXXXXXXXXX--M---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX    ',
                          '    XX--------------XXXXXXXX--------------XXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX    ',
                          '    XX-----Y--------XXXXXXXX--------------XXXXXXXXXXX------------------------------------------------XXXXXXXXXXXXXXXXX    ',
                          '    XX--------------XXXXXXXX--------------XXXXXXXXXXX-------------------------------------------Y----XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXX--P-------Y---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----M------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXX--------------------------------------------------------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXX--------------------------------------------------------------------XXXXX---------XXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXX-----Y---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX---------XXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXX---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXX----P----XXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXX---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------------XXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------------XXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX---------------------------------------------------------------------XXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXX-----------------------------------------Y---------------------------XXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------------XXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----Y-------------------------------------------Y---XXXXXXXXXXXX    ',
                          '    XXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------------XXXXXXXXXXXX    ',
                          '    XXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX    ',
                          '    XXXX----------M----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX    ',
                          '    XXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX    ',
                          '    XXXX---------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX    ',
                          '    XXXX---M----------------------------------------XXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX    ',
                          '    XXXX--------------------------------------------XXXXXXXXXX--------M-------XXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX--XXXXXXXXXX---------------------------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-------XXXXXXXX---------------------------------------XXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXX-------XXXXXXXX----------------XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXX-------------XXXXXXXXXX-------XXXXXXXX--P-------------XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXX------P------XXXXXXXXXXXXX--XXXXXXXXXX----------------XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXX-------------XXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------M--------------XXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXXXXXXX    ',
                          '    XXXXXX----------------H------------XXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXX-----------------------------XXXXXXXXXXX--XXXX----------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXX--------------XXXX--XXXXXXXXXXX--XXXX----------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX--------------XXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX--------------XXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXX----------XXXXXXXXXXX--------------XXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXX-S--------XXXXXXXXXXX--------------XXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXX----------XXXXXXXXXXX--------------XXXXX    ',
                          '    XXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX-----Y----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX    ',
                          '    XXXX-------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX    ',
                          '    XXXX-------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX    ',
                          '    XXXX-D-----XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXX    ',
                          '    XXXX-------XXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXX----------XXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXX----------------------------------------M---------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXX-------M------XXXXXXXXXXX--------------------------------------------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------Y------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXX----Y-------------Y-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------XXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXX------------------------XXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------M--------------------------XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXXXXX---------------------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXXXXX---------------------------XXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX-----------Y---------------------XXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXX-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX-------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXX    ',
                          '    XXXXX---------------------------------------------P---XXXXXXXXXXXXXXXXXXXX-----------------------------------XXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXX-------XXXXXXXXXXXXXXXXXXXX---------------------------M-------XXXXX    ',
                          '    XXXXX----Y----------------------------XXXXXXXXX-------XXXXXXXXXXXXXXXXXXXX------M----------------------------XXXXX    ',
                          '    XXXXX---------------------------Y-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------XXXXX    ',
                          '    XXXXX---------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ']

allMaps['Volcano', 6] =  ['    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----D----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX----------------------------------------------------XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------*-----------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXX----------------------------------------------------------XXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXX----------------------------------------------------XXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXX----------------------------------------------XXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXX----------------------------------------XXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----S--P--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
                          '    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ']

class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        self.explored = False
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight
    
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
    
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
    
    def intersect(self, other):
        return(self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1)
        
class Object:
    def __init__(self, x, y, char, name, color, timerStart, speed, moveSpeed, stairType='D', attacking=False, blocks=False, fighter=None, ai=None, companion=False, questNPC=None, item=None, equipment=None, buff=None, buffStart=None, description="None yet!", tiles=None, contains=None):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.timerStart = timerStart
        self.speed = speed
        self.moveSpeed = moveSpeed
        self.wait = 0
        self.stairType = stairType
        self.attacking = attacking
        self.blocks = blocks
        self.fighter = fighter
        self.companion = companion
        self.buff = buff
        self.buffStart = buffStart
        self.description = description
        self.tiles = tiles
        self.contains = contains
        if self.fighter:
            self.fighter.owner = self
            
        self.ai = ai
        if self.ai:
            self.ai.owner = self
            
        self.questNPC = questNPC
        if self.questNPC:
            self.questNPC.owner = self
            
        self.item = item
        if self.item:
            self.item.owner = self
            
        self.equipment = equipment
        if self.equipment:
            self.equipment.owner = self
            self.item = Item()
            self.item.owner = self
        
    def move(self, dx, dy):
        if not is_blocked(self.x + dx, self.y + dy):
            self.x = self.x + dx
            self.y = self.y + dy
            self.wait = self.moveSpeed
            
    def move_towards(self, targetX, targetY):
        dx = targetX - self.x
        dy = targetY - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy)
        
    def pathing(self, target):
        fov = libtcod.map_new(len(dungeon), len(dungeon[0]))
        for height in range(len(dungeon[0])):
            for width in range(len(dungeon)):
                libtcod.map_set_properties(fov, width, height, not dungeon[width][height].block_sight, not dungeon[width][height].blocked)
                
        for object in objects:
            if object.blocks and object != self and object != target:
                libtcod.map_set_properties(fov, object.x, object.y, True, False)
                
        path = libtcod.path_new_using_map(fov, 1.41)
        libtcod.path_compute(path, self.x, self.y, target.x, target.y)
        
        if not libtcod.path_is_empty(path) and libtcod.path_size(path) < 25:
            x, y = libtcod.path_walk(path, True)
            if x or y:
                # for selecting directional tile for monster
                if self.x < x:
                    self.char = self.tiles[0]  # going right
                elif self.x > x:
                    self.char = self.tiles[1]  # going left
                elif self.y < y:
                    self.char = self.tiles[2]  # going down
                elif self.y > y:
                    self.char = self.tiles[3]  # going up
                self.x = x
                self.y = y
                self.wait = self.moveSpeed

        else:
            self.move_towards(target.x, target.y)
        
        libtcod.path_delete(path)
        
    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
    
    def distance_to_tile(self, x, y, other):
        dx = other.x - x
        dy = other.y - y
        return math.sqrt(dx ** 2 + dy ** 2)
    
    def send_to_back(self):
        global objects
        objects.remove(self)
        objects.insert(0, self)
           
    def draw(self):
        global currentMap, dungeonLevel
        if currentMap != 'Town' and dungeonLevel != 0 and not (currentMap == 'Catacombs' and dungeonLevel == 4) and not (currentMap == 'Forest' and dungeonLevel == 3) and not (currentMap == 'Tundra' and dungeonLevel == 5) and not (currentMap == 'Volcano' and dungeonLevel == 6):
            if libtcod.map_is_in_fov(fovMap, self.x, self.y):
                (x, y) = to_camera_coordinates(self.x, self.y)
                if x is not None:
                    libtcod.console_set_default_foreground(con, self.color)
                    libtcod.console_put_char(con, x, y, self.char, libtcod.BKGND_NONE)
        else:
            (x, y) = to_camera_coordinates(self.x, self.y)
            if x is not None:
                libtcod.console_set_default_foreground(con, self.color)
                libtcod.console_put_char(con, x, y, self.char, libtcod.BKGND_NONE) 
        
    def clear(self):
        (x, y) = to_camera_coordinates(self.x, self.y)
        if x is not None:
            libtcod.console_put_char(con, x, y, ' ', libtcod.BKGND_NONE)
    
class Fighter:
    def __init__(self, hp, defense, power, mana=0, experienceWorth=0, death_function=None):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.base_max_mana = mana
        self.mana = mana
        self.experienceWorth = experienceWorth
        self.death_function = death_function
     
    @property   
    def power(self):
        global equipped_list
        if self.owner.name == 'Reinald':
            bonus = sum(equipment.equipment.power_bonus for equipment in equipped_list)
        else:
            bonus = 0
        return self.base_power + bonus
    
    @property   
    def defense(self):
        global equipped_list
        if self.owner.name == 'Reinald':
            bonus = sum(equipment.equipment.defense_bonus for equipment in equipped_list)
        else:
            bonus = 0
        return self.base_defense + bonus
    
    @property   
    def max_hp(self):
        global equipped_list
        if self.owner.name == 'Reinald':
            bonus = sum(equipment.equipment.max_hp_bonus for equipment in equipped_list)
        else:
            bonus = 0
        return self.base_max_hp + bonus
    
    @property   
    def max_mana(self):
        global equipped_list
        if self.owner.name == 'Reinald':
            bonus = sum(equipment.equipment.max_mana_bonus for equipment in equipped_list)
        else:
            bonus = 0
        return self.base_max_mana + bonus
    
    def attack(self, target):
        damage = self.power - target.fighter.defense
        
        if damage > 0:
            if self.owner.name == 'Reinald' or self.owner.name == 'Flame Elemental Companion' or self.owner.name == 'Zombie Companion' or self.owner.name == 'Angel Companion':
                message(self.owner.name + ' attacks ' + target.name + ' for ' + str(damage) + ' damage.', libtcod.green)
            else:
                message(self.owner.name + ' attacks ' + target.name + ' for ' + str(damage) + ' damage.', libtcod.red)
            target.fighter.take_damage(damage)
        else:
            message(self.owner.name + ' attacks ' + target.name + ', but it has no effect!', libtcod.orange)
        
    def take_damage(self, damage):
        if damage > 0:
            self.hp = self.hp - damage
            if self.hp <= 0:
                function = self.death_function
                if function is not None:
                    function(self.owner)
                    
    def heal(self, amount):
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
class BasicMonster:
    def __init__(self, burning=False, unstable=False, stun=False, confuse=False, polymorph=False):
        self.burning = burning
        self.unstable = unstable
        self.stun = stun
        self.confuse = confuse
        self.polymorph = polymorph
    def take_turn(self):
        global player
        timer = int(time.time())
        monster = self.owner
        companion = None
        if libtcod.map_is_in_fov(fovMap, monster.x, monster.y):
            for obj in objects:
                if obj.ai:
                    if obj.companion:
                        companion = obj  
            if companion is not None:  
                if monster.distance_to(companion) >= 2:
                    monster.pathing(companion)
                elif companion.fighter.hp > 0:
                    if monster.attacking == False:
                        monster.timerStart = timer
                        monster.fighter.attack(companion)                
                        monster.attacking = True
                        if monster.ai.burning == True:
                            message(monster.name + " takes 1 point of continual damage.", libtcod.green)
                            monster.fighter.take_damage(1)
                    else:
                        if timer == monster.timerStart + monster.speed:
                            monster.timerStart = timer
                            monster.fighter.attack(companion)
                            if monster.ai.burning == True:
                                message(monster.name + " takes 1 point of continual damage.", libtcod.green)
                                monster.fighter.take_damage(1)          
            elif monster.distance_to(player) >= 2:
                monster.pathing(player)
            elif player.fighter.hp > 0:
                if monster.attacking == False:
                    monster.timerStart = timer
                    monster.fighter.attack(player)                
                    monster.attacking = True
                    if monster.ai.burning == True:
                        message(monster.name + " takes 1 point of continual damage.", libtcod.green)                    
                        monster.fighter.take_damage(1)
                else:
                    if timer == monster.timerStart + monster.speed:
                        monster.timerStart = timer
                        monster.fighter.attack(player)
                        if monster.ai.burning == True:
                            message(monster.name + " takes 1 point of continual damage.", libtcod.green)                    
                            monster.fighter.take_damage(1)
            else:
                if monster.attacking == True:
                    monster.attacking = False

class Companion:
    def __init__(self, creationTime=None, duration=None):
        self.creationTime = creationTime
        self.duration = duration
    def take_turn(self):
        timer = int(time.time())
        comp = self.owner
        if (timer >= int(comp.ai.creationTime) + int(comp.ai.duration)):
            message("The " + self.owner.name + " disappears.", libtcod.red)
            objects.remove(self.owner)
        else:
            inFOV = False
            for obj in objects:
                if obj.fighter:
                    if obj.fighter.death_function == monster_death:
                        if libtcod.map_is_in_fov(fovMap, obj.x, obj.y):
                            inFOV = True
                            if comp.distance_to(obj) >= 2:
                                comp.pathing(obj)
                            elif obj.fighter.hp > 0:
                                if comp.attacking == False:
                                    comp.timerStart = timer
                                    comp.fighter.attack(obj)                
                                    comp.attacking = True
                                    break
                                else:
                                    if timer == comp.timerStart + comp.speed:
                                        comp.timerStart = timer
                                        comp.fighter.attack(obj)
                                        break                   
                        else:
                            if comp.distance_to(player) >= 2:
                                comp.pathing(player)
            if not inFOV:
                if comp.attacking == True:
                    comp.attacking = False

class ConfusedMonster:
    def __init__(self, creationTime=None, duration=None, old_ai=None, confuse=True):
        self.creationTime = creationTime
        self.duration = duration
        self.old_ai = old_ai
        self.confuse = confuse
    
    def take_turn(self):  
        timer = int(time.time())
        comp = self
        if (timer >= int(comp.creationTime) + int(comp.duration)):
            self.owner.ai = self.old_ai
            message("The " + self.owner.name + " is no longer confused.", libtcod.red)
        else: 
            self.owner.move(libtcod.random_get_int(0, -1, 1), libtcod.random_get_int(0, -1, 1))
            
class StunnedMonster:
    def __init__(self, creationTime=None, duration=None, old_ai=None, stun=True):
        self.creationTime = creationTime
        self.duration = duration
        self.old_ai = old_ai
        self.stun = stun
    
    def take_turn(self):  
        timer = int(time.time())
        comp = self
        if (timer >= int(comp.creationTime) + int(comp.duration)):
            self.owner.ai = self.old_ai
            message("The " + self.owner.name + " is no longer stunned.", libtcod.red)        

class QuestNPC:
    def __init__(self, reward=None):
        self.reward = reward
                    
class Item:
    def __init__(self, use_function=None):
        self.use_function = use_function
        
    def pick_up(self):
        global inventory
        if len(inventory) >= 40:
            message('Your inventory is too full to pick up that ' + self.owner.name + '.', libtcod.orange)
        else:
            if self.owner in objects:
                objects.remove(self.owner)
            if self.owner.name == "Skull":
                self.owner.char = skullInvTile
            if self.owner.name == "Orange Gem":
                self.owner.char = orangeGemInvTile
            if self.owner.name == "Purple Gem":
                self.owner.char = purpleGemInvTile
            inventory.append(self.owner)
            message('You picked up a ' + self.owner.name + '.', libtcod.green)          
            equipment = self.owner.equipment
            if equipment and get_equipped_in_slot(equipment.slot) is None:
                equipment.equip()   
            
    def use(self):
        global inventory
        if self.use_function is None:
            message('The ' + self.owner.name + ' cannot be used.', libtcod.orange)     
        else:
            if self.use_function() != 'cancelled':
                inventory.remove(self.owner)    
                
    def drop(self): 
        global player, inventory
        if self.owner.name != "Skull" and self.owner.name != "Orange Gem" and self.owner.name != "Purple Gem":
            inventory.remove(self.owner)  
            message("You dropped the " + self.owner.name + ".", libtcod.orange)
        else:
            message("You cannot drop that item!", libtcod.orange)

class Equipment:
    def __init__ (self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0, max_mana_bonus=0, ranged=False):
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.max_mana_bonus = max_mana_bonus
        self.ranged = ranged
        
        self.slot = slot
        self.is_equipped = False
            
    def equip(self):
        global equipped_list, inventory
        oldEquipment = get_equipped_in_slot(self.slot)
        if oldEquipment is not None:
            oldEquipment.dequip()
        self.is_equipped = True
        equipped_list.append(self.owner)
        if self.owner in inventory:
            inventory.remove(self.owner)
        message('Equipped ' + self.owner.name + ' on ' + self.slot + '.', libtcod.green)
        
    def dequip(self):
        global equipped_list, inventory
        if self.is_equipped == True:
            self.is_equipped = False
            equipped_list.remove(self.owner)
            inventory.append(self.owner)
            message('Dequipped ' + self.owner.name + ' from ' + self.slot + '.', libtcod.green)
            
    def drop(self): 
        global player, inventory
        inventory.remove(self.owner)  
        message("You dropped the " + self.owner.name + ".", libtcod.orange)

class Spell:
    def __init__ (self, name, icon, type, range, manaRequired, damage=0, learned=False, description="None yet."):
        self.name = name
        self.icon = icon
        self.type = type
        self.range = range
        self.manaRequired = manaRequired
        self.damage = damage
        self.learned = learned
        self.description = description
    
    def cast(self):
        global player, playerLevel
        if self.manaRequired <= player.fighter.mana:
            if self.type == 'single-target':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        message(player.name + ' casts ' + self.name + ' at ' + target.name + ' for ' + str(self.damage + playerLevel) + ' damage.', libtcod.green)
                        target.fighter.take_damage(self.damage + playerLevel)
                        player.fighter.mana = player.fighter.mana - self.manaRequired
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                    
            if self.type == 'multiple-target':
                message("Casting a spell...please select a target.", libtcod.orange)
                x, y = target_tile()
                if x is not None:
                    message(player.name + ' casts ' + self.name + '.' , libtcod.green)
                    for obj in objects:
                        if player.distance_to_tile(x, y, obj) <= self.range and obj.fighter and obj != player:
                            message('The ' + obj.name + ' takes ' + str(self.damage + playerLevel) + ' damage.', libtcod.green)
                            obj.fighter.take_damage(self.damage + playerLevel)
                            if obj.fighter.hp <= 0:
                                for objs in objects:
                                    if player.distance_to_tile(x, y, objs) <= self.range and objs.fighter and objs != player:
                                        message('The ' + objs.name + ' takes ' + str(self.damage + playerLevel) + ' damage.', libtcod.green)
                                        objs.fighter.take_damage(self.damage + playerLevel)
                    player.fighter.mana = player.fighter.mana - self.manaRequired
                else:
                    message("You are too far away from that tile.", libtcod.orange)
                    
            if self.type == 'burn':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        if (target.ai.burning):
                            message("The target is already under a similar spell effect.", libtcod.orange)
                        else:
                            message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It begins taking continual damage!', libtcod.green)
                            target.ai.burning = True
                            player.fighter.mana = player.fighter.mana - self.manaRequired
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                    
            if self.type == 'heal':
                message(player.name + ' casts ' + self.name + '.', libtcod.green)
                cast_heal()
                player.fighter.mana = player.fighter.mana - self.manaRequired
            
            if self.type == 'companion-elemental':
                message(player.name + ' casts ' + self.name + '.', libtcod.green)
                fighter_component = Fighter(hp=15, defense=0, power=15, experienceWorth=0, death_function=companion_death)
                ai_component = Companion(int(time.time()), 60)
                elem = Object(player.x, player.y + 1, elementalTowards, 'Flame Elemental Companion', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, companion=True, tiles=elementalTiles)
                objects.append(elem)
                player.fighter.mana = player.fighter.mana - self.manaRequired
                
            if self.type == 'companion-undead':
                message(player.name + ' casts ' + self.name + '.', libtcod.green)
                fighter_component = Fighter(hp=15, defense=0, power=10, experienceWorth=0, death_function=companion_death)
                ai_component = Companion(int(time.time()), 60)
                und = Object(player.x, player.y + 1, zombieCompTowards, 'Zombie Companion', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, companion=True, tiles=zombieCompTiles)
                objects.append(und)
                player.fighter.mana = player.fighter.mana - self.manaRequired
                
            if self.type == 'companion-angel':
                message(player.name + ' casts ' + self.name + '.', libtcod.green)
                fighter_component = Fighter(hp=15, defense=0, power=20, experienceWorth=0, death_function=companion_death)
                ai_component = Companion(int(time.time()), 60)
                ang = Object(player.x, player.y, angelTowards, 'Angel Companion', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, companion=True, tiles=angelTiles)
                objects.append(ang)
                player.fighter.mana = player.fighter.mana - self.manaRequired
            
            if self.type == 'confuse':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        if (target.ai.confuse):
                            message("The target is already under a similar spell effect.", libtcod.orange)
                        else:
                            message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It begins wandering, confused!', libtcod.green)
                            ai_component = ConfusedMonster(int(time.time()), 5, target.ai)
                            target.ai = ai_component
                            target.ai.owner = target
                            player.fighter.mana = player.fighter.mana - self.manaRequired
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                    
            if self.type == 'stun':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        if (target.ai.stun):
                            message("The target is already under a similar spell effect.", libtcod.orange)
                        else:
                            message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It stares off into space!', libtcod.green)
                            ai_component = StunnedMonster(int(time.time()), 5, target.ai)
                            target.ai = ai_component
                            target.ai.owner = target
                            player.fighter.mana = player.fighter.mana - self.manaRequired
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                    
            if self.type == 'unstable':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        if (target.ai.unstable):
                            message("The target is already under a similar spell effect.", libtcod.orange)
                        else:
                            message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It becomes unstable!', libtcod.green)
                            target.ai.unstable = True
                            player.fighter.mana = player.fighter.mana - self.manaRequired
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                    
            if self.type == 'defense-buff':
                if player.buff:
                    message('You can\'t have more than one buff!', libtcod.orange)
                else:
                    message(player.name + ' casts ' + self.name + '.', libtcod.green)
                    player.buffStart = int(time.time())
                    player.buff = "defense"
                    player.fighter.defense = player.fighter.defense + 5
                    player.fighter.mana = player.fighter.mana - self.manaRequired
                    
            if self.type == 'power-buff':
                if player.buff:
                    message('You can\'t have more than one buff!', libtcod.orange)
                else:
                    message(player.name + ' casts ' + self.name + '.', libtcod.green)
                    player.buffStart = int(time.time())
                    player.buff = "power"
                    player.fighter.power = player.fighter.power + 5
                    player.fighter.mana = player.fighter.mana - self.manaRequired
            
            if self.type == 'slip':
                message(player.name + ' casts ' + self.name + '.' , libtcod.green)
                for obj in objects:
                    if (libtcod.map_is_in_fov(fovMap, obj.x, obj.y)):
                        message('The ' + obj.name + ' has reduced speed!', libtcod.green)
                        obj.moveSpeed = obj.moveSpeed * 2
                player.fighter.mana = player.fighter.mana - self.manaRequired 
                
            if self.type == 'wail':
                message(player.name + ' casts ' + self.name + '.' , libtcod.green)
                for obj in objects:
                    if (libtcod.map_is_in_fov(fovMap, obj.x, obj.y)):
                        if obj.ai:
                            if obj.ai.confuse:
                                message("The target is already under a similar spell effect.", libtcod.orange)
                            else:
                                message(obj.name + ' is frozen in fear!', libtcod.green)
                                ai_component = StunnedMonster(int(time.time()), 5, obj.ai)
                                obj.ai = ai_component
                                obj.ai.owner = obj
                player.fighter.mana = player.fighter.mana - self.manaRequired
                    
            if self.type == 'slow':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        message(player.name + ' casts ' + self.name + ' at ' + target.name + '. Its speed is reduced by half.', libtcod.green)
                        target.moveSpeed = target.moveSpeed * 2
                        player.fighter.mana = player.fighter.mana - self.manaRequired
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                        
            if self.type == 'polymorph':
                message("Casting a spell...please select a target.", libtcod.orange)
                target = target_monster()
                if target is not None:
                    if (target.x <= self.range + player.x) and (target.y <= self.range + player.y):
                        if (target.ai.polymorph):
                            message("The target is already under a similar spell effect.", libtcod.orange)
                        elif (target.name == "Flaming Skull" or target.name == "Forest Guardian" or target.name == "Hybernating Dragon" or target.name == "Lady Azadlonea"):
                            message("This spell has no effect on that target!", libtcod.orange)
                        else:
                            monsterType = randint(0, 2)
                            if monsterType == 0:
                                message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It turns into a boar!', libtcod.green)
                                fighter_component = Fighter(hp=15, defense=0, power=3, experienceWorth=40, death_function=monster_death)
                                target.tiles = boarTiles
                            elif monsterType == 1:
                                message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It turns into a snake!', libtcod.green)
                                fighter_component = Fighter(hp=12, defense=0, power=4, experienceWorth=40, death_function=monster_death)
                                target.tiles = snakeTiles
                            else:
                                message(player.name + ' casts ' + self.name + ' at ' + target.name + '. It turns into a lynx!', libtcod.green)
                                fighter_component = Fighter(hp=13, defense=0, power=4, experienceWorth=40, death_function=monster_death)
                                target.tiles = lynxTiles
                            target.fighter = fighter_component
                            target.fighter.owner = target
                            target.ai.polymorph = True
                            player.fighter.mana = player.fighter.mana - self.manaRequired                                
                    else:
                        message("You are too far away from that target.", libtcod.orange)
                else:
                    message("No target selected, please try again.", libtcod.orange)
                    
            if self.type == 'teleport':
                message("Casting a spell...please select a target.", libtcod.orange)
                x, y = target_tile()
                if x is not None:
                    for obj in objects:
                        if obj.x == x and obj.y == y:
                            message("That tile is full.", libtcod.orange)
                        else:
                            message(player.name + ' casts ' + self.name + '.' , libtcod.green)
                            player.x = x
                            player.y = y
                            player.fighter.mana = player.fighter.mana - self.manaRequired
                            break
                else:
                    message("You are too far away from that tile.", libtcod.orange)
        else:
            message("Not enough mana!", libtcod.orange)
                    
def load_customfont():
    a = 256
    for y in range(5, 18):
        libtcod.console_map_ascii_codes_to_font(a, 32, 0, y)
        a = a + 32
        
def get_equipped_in_slot(slot):
    for obj in equipped_list:
        if obj.equipment.slot == slot: 
            return obj.equipment
    return None
        
def is_blocked(x, y):
    if dungeon[x][y].blocked:
        return True
    for object in objects:
        if object.blocks and object.x == x and object.y == y:
            return True
    return False   
        
def createRoom(room):
    global dungeon
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            dungeon[x][y].blocked = False
            dungeon[x][y].block_sight = False
        
def createHorizontalTunnel(x1, x2, y):
    global dungeon
    for x in range(min(x1, x2), max(x1, x2) + 1):
        dungeon[x][y].blocked = False
        dungeon[x][y].block_sight = False
        dungeon[x + 1][y + 1].blocked = False
        dungeon[x + 1][y + 1].block_sight = False
        
def createVerticalTunnel(y1, y2, x):
    global dungeon
    for y in range(min(y1, y2), max(y1, y2) + 1):
        dungeon[x][y].blocked = False
        dungeon[x][y].block_sight = False
        dungeon[x + 1][y + 1].blocked = False
        dungeon[x + 1][y + 1].block_sight = False
        
def makeRandomMap():
    global dungeon, objects, player, stairs, dungeonLevel
    player.char = charMineTowards
    pygame.mixer.music.stop()
    pygame.mixer.music.load(minesSong)
    pygame.mixer.music.play(-1)
    
    objects = [player]
    dungeon = [[Tile(True) for y in range (dungeonHeight)] for x in range(dungeonWidth)]
    
    # dungeon generation algorithm
    rooms = []
    num_rooms = 0
    
    for r in range(maxRooms):
        w = libtcod.random_get_int(0, roomMinSize, roomMaxSize)
        h = libtcod.random_get_int(0, roomMinSize, roomMaxSize)
        x = libtcod.random_get_int(0, 0, dungeonWidth - w - 1)
        y = libtcod.random_get_int(0, 0, dungeonHeight - h - 1)
        
        new_room = Rect(x, y, w, h)
        
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break
        if not failed:
            createRoom(new_room)
            (new_x, new_y) = new_room.center()
            
            if num_rooms == 0:
                player.x = new_x
                player.y = new_y
            else:
                (prev_x, prev_y) = rooms[num_rooms - 1].center()
                if libtcod.random_get_int(0, 0, 1) == 1:
                    createHorizontalTunnel(prev_x, new_x, prev_y)
                    createVerticalTunnel(prev_y, new_y, new_x)
                else:
                    createVerticalTunnel(prev_y, new_y, prev_x)
                    createHorizontalTunnel(prev_x, new_x, new_y)
            place_objects(new_room)
            for obj in objects:
                if obj.name == 'Treasure Chest':
                    dungeon[obj.x][obj.y].blocked = True
            rooms.append(new_room)
            num_rooms = num_rooms + 1
    if dungeonLevel < 100:
        stairs = Object(new_x, new_y, stairsDown, 'stairs', libtcod.white, 0, 0, 0)
        objects.append(stairs)
        stairs.send_to_back()
    
def makeMap(importMap):
    global dungeon, objects, player, stairs, currentMap
    global stairsToCatacombs1, stairsToCatacombs2, stairsToForest1, stairsToForest2, stairsToForest3, stairsToTundra1, stairsToTundra2, stairsToMines1, stairsToMines2
    dungeon = [[Tile(True) for x in range (len(importMap))] for y in range(len(importMap[0]))]
    objects = [player]
    
    if currentMap == 'Town':
        player.char = charGrassTowards
        pygame.mixer.music.stop()
        pygame.mixer.music.load(townSong)
        pygame.mixer.music.play(-1)
    elif currentMap == 'Catacombs':
        player.char = charDungeonTowards
        pygame.mixer.music.stop()
        pygame.mixer.music.load(catacombsSong)
        pygame.mixer.music.play(-1)
    elif currentMap == 'Forest':
        player.char = charGrassTowards 
        pygame.mixer.music.stop()
        pygame.mixer.music.load(forestSong)
        pygame.mixer.music.play(-1)
    elif currentMap == 'Tundra':
        player.char = charSnowTowards
        pygame.mixer.music.stop()
        pygame.mixer.music.load(tundraSong)
        pygame.mixer.music.play(-1) 
    elif currentMap == 'Volcano':
        player.char = charDungeonTowards
        pygame.mixer.music.stop()
        pygame.mixer.music.load(volcanoSong)
        pygame.mixer.music.play(-1)
    elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == 'Maybell' or currentMap == 'Home'):
        player.char = charHouseAway
        pygame.mixer.music.stop()
        pygame.mixer.music.load(houseSong)
        pygame.mixer.music.play(-1)
        
    for x in range(len(importMap)):
        for y in range(len(importMap[0])):
            if currentMap == 'Town':
                if importMap[x][y] == 'S':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    player.x = y
                    player.y = x
                if importMap[x][y] == 'g':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 's':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'j':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == '!':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == '@':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == '#':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == '1':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToCatacombs1 = Object(y, x, pathTile, 'To Catacombs', libtcod.white, 0, 0, 0, stairType='1')
                    objects.append(stairsToCatacombs1)
                    stairsToCatacombs1.send_to_back()
                if importMap[x][y] == '2':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToCatacombs2 = Object(y, x, pathTile, 'To Catacombs', libtcod.white, 0, 0, 0, stairType='1')
                    objects.append(stairsToCatacombs2)
                    stairsToCatacombs2.send_to_back()
                if importMap[x][y] == '3':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToForest1 = Object(y, x, grassTile, 'To Forest', libtcod.white, 0, 0, 0, stairType='2')
                    objects.append(stairsToForest1)
                    stairsToForest1.send_to_back()
                if importMap[x][y] == '4':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToForest2 = Object(y, x, grassTile, 'To Forest', libtcod.white, 0, 0, 0, stairType='2')
                    objects.append(stairsToForest2)
                    stairsToForest2.send_to_back()
                if importMap[x][y] == '5':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToForest3 = Object(y, x, grassTile, 'To Forest', libtcod.white, 0, 0, 0, stairType='2')
                    objects.append(stairsToForest3)
                    stairsToForest3.send_to_back()
                if importMap[x][y] == '6':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToTundra1 = Object(y, x, pathTile, 'To Tundra', libtcod.white, 0, 0, 0, stairType='3')
                    objects.append(stairsToTundra1)
                    stairsToTundra1.send_to_back()
                if importMap[x][y] == '7':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToTundra2 = Object(y, x, pathTile, 'To Tundra', libtcod.white, 0, 0, 0, stairType='3')
                    objects.append(stairsToTundra2)
                    stairsToTundra2.send_to_back()
                if importMap[x][y] == '8':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToVolcano1 = Object(y, x, pathTile, 'To Volcano', libtcod.white, 0, 0, 0, stairType='4')
                    objects.append(stairsToVolcano1)
                    stairsToVolcano1.send_to_back()
                if importMap[x][y] == '9':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToVolcano2 = Object(y, x, pathTile, 'To Volcano', libtcod.white, 0, 0, 0, stairType='4')
                    objects.append(stairsToVolcano2)
                    stairsToVolcano2.send_to_back()
                if importMap[x][y] == '~':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToMines1 = Object(y, x, pathTile, 'To Mines', libtcod.white, 0, 0, 0, stairType='5')
                    objects.append(stairsToMines1)
                    stairsToMines1.send_to_back()
                if importMap[x][y] == '0':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairsToMines2 = Object(y, x, pathTile, 'To Mines', libtcod.white, 0, 0, 0, stairType='5')
                    objects.append(stairsToMines2)
                    stairsToMines2.send_to_back()
                    
            elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == 'Maybell' or currentMap == 'Home'):
                if importMap[x][y] == '-':                     
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'l':                     
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'S':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    player.x = y
                    player.y = x
                if importMap[x][y] == 'a':
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False  
                    equipment_component = Equipment(slot='weapon', power_bonus=4)
                    quest_reward = Object(x, y, swordTile, 'Iron Sword', libtcod.white, 0, 0, 0, equipment=equipment_component, description="Basic iron sword. Increases power by 4.")
                    npc = QuestNPC(reward=quest_reward)
                    NPC = Object(y, x, mayorTile, 'Mayor', libtcod.white, 0, 0, 0, questNPC=npc)
                    objects.append(NPC)
                if importMap[x][y] == 'b':
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False        
                    equipment_component = Equipment(slot='feet', defense_bonus=6)
                    quest_reward = Object(x, y, sabatonsSteel, 'Iron Sabatons', libtcod.white, 0, 0, 0, equipment=equipment_component, description="Basic iron sabatons. Increases defense by 6.")  
                    npc = QuestNPC(reward=quest_reward)
                    NPC = Object(y, x, louisTile, 'Louis', libtcod.white, 0, 0, 0, questNPC=npc)
                    objects.append(NPC)
                if importMap[x][y] == 'c': 
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False  
                    npc = QuestNPC()
                    NPC = Object(y, x, ariannaTile, 'Arianna', libtcod.white, 0, 0, 0, questNPC=npc)
                    objects.append(NPC)
                if importMap[x][y] == 'd':
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False  
                    equipment_component = Equipment(slot='hands', defense_bonus=9)
                    quest_reward = Object(x, y, gauntletsSteel, 'Lambent Gloves', libtcod.white, 0, 0, 0, equipment=equipment_component, description="High quality gauntlets. Increases defense by 9.")
                    npc = QuestNPC(reward=quest_reward)
                    NPC = Object(y, x, maybellTile, 'Maybell', libtcod.white, 0, 0, 0, questNPC=npc)
                    objects.append(NPC)
                    
            else:
                if importMap[x][y] == '-':                     
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'm':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'n':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'o':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                if importMap[x][y] == 'D':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairs = Object(y, x, stairsDown, 'Stairs', libtcod.white, 0, 0, 0, stairType='D')
                    objects.append(stairs)
                    stairs.send_to_back()
                if importMap[x][y] == 'U':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    stairs = Object(y, x, stairsUp, 'Stairs', libtcod.white, 0, 0, 0, stairType='U')
                    objects.append(stairs)
                    stairs.send_to_back()
                if importMap[x][y] == 'S':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    player.x = y
                    player.y = x
                if importMap[x][y] == 'Z':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=20, defense=0, power=4, experienceWorth=40, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, zombieTowards, 'Zombie', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=zombieTiles)
                    objects.append(monster)
                if importMap[x][y] == 'K':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=30, defense=2, power=8, experienceWorth=80, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, skeletonTowards, 'Skeleton', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=skeletonTiles)
                    objects.append(monster)
                if importMap[x][y] == 'F':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=30, defense=3, power=15, experienceWorth=100, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, spriteTowards, 'Forest Sprite', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=spriteTiles)
                    objects.append(monster)
                if importMap[x][y] == 'E':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=50, defense=5, power=19, experienceWorth=200, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, glacierTowards, 'Living Glacier', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=glacierTiles)
                    objects.append(monster)
                if importMap[x][y] == 'I':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=45, defense=3, power=20, experienceWorth=250, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, sirenTowards, 'Ice Siren', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=sirenTiles)
                    objects.append(monster)
                if importMap[x][y] == 'A':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=50, defense=3, power=32, experienceWorth=300, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, lavaElemTowards, 'Lava Elemental', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=lavaElemTiles)
                    objects.append(monster)
                if importMap[x][y] == 'M':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=70, defense=5, power=32, experienceWorth=450, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, demonTowards, 'Demon Lord', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=demonTiles)
                    objects.append(monster)
                if importMap[x][y] == 'Y':
                    dungeon[y][x].blocked = False
                    dungeon[y][x].block_sight = False
                    fighter_component = Fighter(hp=60, defense=6, power=37, experienceWorth=450, death_function=monster_death)
                    ai_component = BasicMonster()
                    monster = Object(y, x, demonessTowards, 'Demoness', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=demonessTiles)
                    objects.append(monster)
                if importMap[x][y] == '*':
                    if (currentMap == "Catacombs"):
                        dungeon[y][x].blocked = False
                        dungeon[y][x].block_sight = False
                        fighter_component = Fighter(hp=50, defense=3, power=10, experienceWorth=150, death_function=monster_death)
                        ai_component = BasicMonster()
                        monster = Object(y, x, skullTowards, 'Flaming Skull', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=skullTiles)
                        objects.append(monster)
                    if (currentMap == "Forest"):
                        dungeon[y][x].blocked = False
                        dungeon[y][x].block_sight = False
                        fighter_component = Fighter(hp=75, defense=5, power=20, experienceWorth=300, death_function=monster_death)
                        ai_component = BasicMonster()
                        monster = Object(y, x, guardianTowards, 'Forest Guardian', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=guardianTiles)
                        objects.append(monster)
                    if (currentMap == "Tundra"):
                        dungeon[y][x].blocked = False
                        dungeon[y][x].block_sight = False
                        fighter_component = Fighter(hp=125, defense=7, power=30, experienceWorth=500, death_function=monster_death)
                        ai_component = BasicMonster()
                        monster = Object(y, x, dragonTowards, 'Hybernating Dragon', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=dragonTiles)
                        objects.append(monster)
                    if (currentMap == "Volcano"):
                        dungeon[y][x].blocked = False
                        dungeon[y][x].block_sight = False
                        fighter_component = Fighter(hp=200, defense=7, power=42, experienceWorth=1000, death_function=monster_death)
                        ai_component = BasicMonster()
                        monster = Object(y, x, azadloneaTowards, 'Lady Azadlonea', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=azadloneaTiles)
                        objects.append(monster)
                if importMap[x][y] == 'P':
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False
                    item_component = Item(use_function=cast_heal)
                    potion = Object(y, x, potionTile, 'Potion', libtcod.white, 0, 0, 0, item=item_component, description="A healing potion. Heals 30 hit points.")
                    chest1 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[potion])
                    objects.append(chest1)          
                if importMap[x][y] == 'B':
                    if (currentMap == "Catacombs"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='weapon', power_bonus=5, ranged=True)
                        item = Object(y, x, bowTile, 'Worn Bow', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic, worn ranged bow. Increases power by 5.")
                        chest2 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest2) 
                    if (currentMap == "Tundra"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='weapon', power_bonus=10, ranged=True)
                        item = Object(y, x, bowTile, 'Ice Bow', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A bow that shoots arrows of ice. Increases power by 10.")
                        chest2 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest2) 
                if importMap[x][y] == 'H':
                    if (currentMap == "Catacombs"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='head', defense_bonus=3)
                        item = Object(y, x, helmSteel, 'Iron Helm', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A lightly rusted iron helm. Increases defense by 3.")
                        chest3 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest3)   
                    if (currentMap == "Volcano"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='feet', defense_bonus=8)
                        item = Object(y, x, sabatonsSteel, 'Champion Boots', libtcod.white, 0, 0, 0, equipment=equipment_component, description="Glorious, winged boots. Increases defense by 8.")
                        chest3 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest3) 
                if importMap[x][y] == 'C':
                    if (currentMap == "Forest"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='chest', defense_bonus=5)
                        item = Object(y, x, chestSteel, 'Steel Hauberk', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A sturdy breastplate. Increases defense by 5.")
                        chest4 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest4) 
                    if (currentMap == "Volcano"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='chest', defense_bonus=10)
                        item = Object(y, x, chestSteel, 'Bright Hauberk', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A magnificently crafted breastplate. Increases defense by 10.")
                        chest4 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest4) 
                if importMap[x][y] == 'L':
                    if (currentMap == "Forest"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='legs', defense_bonus=5)
                        item = Object(y, x, greavesSteel, 'Steel Greaves', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A sturdy set of greaves. Increases defense by 5.")
                        chest5 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest5) 
                    if (currentMap == "Volcano"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='legs', defense_bonus=8)
                        item = Object(y, x, greavesSteel, 'Bright Greaves', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A magnificently crafted set of greaves. Increases defense by 8.")
                        chest5 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest5)
                if importMap[x][y] == 'O':
                    if (currentMap == "Tundra"):
                        dungeon[y][x].blocked = True
                        dungeon[y][x].block_sight = False   
                        equipment_component = Equipment(slot='head', defense_bonus=7)
                        item = Object(y, x, helmSteel, 'Icy Helm', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A powerful helm that is always cold to the touch. Increases defense by 7.")
                        chest6 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                        objects.append(chest6)
            if currentMap == 'Catacombs':
                if importMap[x][y] == 'l': 
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False  
                    npc = QuestNPC()
                    NPC = Object(y, x, tombLeft, 'Ancient Tomb', libtcod.white, 0, 0, 0, questNPC=npc)
                    objects.append(NPC)
                if importMap[x][y] == 'r': 
                    dungeon[y][x].blocked = True
                    dungeon[y][x].block_sight = False  
                    npc = QuestNPC()
                    NPC = Object(y, x, tombRight, 'Ancient Tomb', libtcod.white, 0, 0, 0, questNPC=npc)
                    objects.append(NPC) 
                        
def random_choice_index(chances):
    dice = libtcod.random_get_int(0, 1, sum(chances))
    total = 0
    choice = 0
    
    for w in chances:
        total = total + w
        if dice <= total:
            return choice
        choice = choice + 1
        
def random_choice(chances_dict):
    chances = chances_dict.values()
    strings = chances_dict.keys()
    return strings[random_choice_index(chances)]

def from_dungeon_level(table):
    for (value, level) in reversed(table):
        if dungeonLevel >= level:
            return value
    return 0
 
def place_objects(room):
    maxMonsters = from_dungeon_level([[2, 1], [3, 33], [4, 66]])
    monsterChances = {}
    monsterChances['orc'] = 80
    monsterChances['troll'] = from_dungeon_level([[15, 20], [30, 40], [60, 60]])
    monsterChances['ogre'] = from_dungeon_level([[15, 50], [30, 70], [60, 90]])
    
    maxItems = from_dungeon_level([[1, 1], [2, 50]])
    itemChances = {}
    itemChances['heal'] = 70
    itemChances['sword1'] = from_dungeon_level([[15, 33]])
    itemChances['sword2'] = from_dungeon_level([[10, 66]])
    itemChances['sword3'] = from_dungeon_level([[1, 90]])
    itemChances['bow1'] = from_dungeon_level([[15, 25]])
    itemChances['bow2'] = from_dungeon_level([[10, 50]])
    itemChances['helm1'] = from_dungeon_level([[15, 30]])
    itemChances['helm2'] = from_dungeon_level([[10, 70]])
    itemChances['chest1'] = from_dungeon_level([[15, 20]])
    itemChances['chest2'] = from_dungeon_level([[10, 60]])
    itemChances['legs1'] = from_dungeon_level([[15, 35]])
    itemChances['legs2'] = from_dungeon_level([[10, 75]])
    itemChances['feet1'] = from_dungeon_level([[15, 10]])
    itemChances['feet2'] = from_dungeon_level([[10, 40]])
    itemChances['hands1'] = from_dungeon_level([[15, 40]])
    itemChances['hands2'] = from_dungeon_level([[10, 80]])
    
    numMonsters = libtcod.random_get_int(0, 0, maxMonsters)
    
    for i in range(numMonsters):
        x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
        
        if not is_blocked(x, y):
            choice = random_choice(monsterChances)
            if choice == 'orc':
                fighter_component = Fighter(hp=20, defense=1, power=5, experienceWorth=40, death_function=monster_death)
                ai_component = BasicMonster()
                monster = Object(x, y, orcTowards, 'orc', libtcod.white, 0, 3, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=orcTiles)
            elif choice == 'troll':
                fighter_component = Fighter(hp=40, defense=3, power=10, experienceWorth=100, death_function=monster_death)
                ai_component = BasicMonster()
                monster = Object(x, y, trollTowards, 'troll', libtcod.white, 0, 5, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=trollTiles)
            elif choice == 'ogre':
                fighter_component = Fighter(hp=55, defense=6, power=18, experienceWorth=220, death_function=monster_death)
                ai_component = BasicMonster()
                monster = Object(x, y, ogreAway, 'troll', libtcod.white, 0, 5, 5, False, blocks=True, fighter=fighter_component, ai=ai_component, tiles=ogreTiles)
            objects.append(monster)
            
    numItems = libtcod.random_get_int(0, 0, maxItems)
    for i in range(numItems):
        x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
        if not is_blocked(x, y):
            choice = random_choice(itemChances)
            if choice == 'heal':
                item_component = Item(use_function=cast_heal)
                potion = Object(y, x, potionTile, 'Potion', libtcod.white, 0, 0, 0, item=item_component, description="A healing potion. Heals 20 hit points.")
                chest1 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[potion])
                objects.append(chest1)  
            if choice == 'sword1':   
                equipment_component = Equipment(slot='weapon', power_bonus=2)
                item = Object(x, y, swordTile, 'Sword', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic sword. Increases power by 2.")
                chest2 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest2) 
            if choice == 'sword2':   
                equipment_component = Equipment(slot='weapon', power_bonus=6)
                item = Object(x, y, swordTile, 'Powerful Sword', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A powerful sword. Increases power by 6.")
                chest3 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest3) 
            if choice == 'sword3':   
                equipment_component = Equipment(slot='weapon', power_bonus=12)
                item = Object(x, y, swordTile, 'Lustrous Sword', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A sparkling sword. Increases power by 12.")
                chest4 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest4) 
            if choice == 'bow1':
                equipment_component = Equipment(slot='weapon', power_bonus=4, ranged=True)
                item = Object(y, x, bowTile, 'Bow', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic ranged bow. Increases power by 4.")
                chest5 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest5)
            if choice == 'bow2':
                equipment_component = Equipment(slot='weapon', power_bonus=8, ranged=True)
                item = Object(y, x, bowTile, 'Powerful Bow', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A powerful ranged bow. Increases power by 8.")
                chest6 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest6)  
            if choice == 'helm1':
                equipment_component = Equipment(slot='head', defense_bonus=3)
                item = Object(y, x, helmSteel, 'Helm', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic helm. Increases defense by 3.")
                chest7 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest7)  
            if choice == 'helm2':
                equipment_component = Equipment(slot='head', defense_bonus=7)
                item = Object(y, x, helmSteel, 'Strong Helm', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A strong helm. Increases defense by 7.")
                chest8 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest8)                
            if choice == 'chest1':
                equipment_component = Equipment(slot='chest', defense_bonus=4)
                item = Object(y, x, chestSteel, 'Cuirass', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic breastplate. Increases defense by 4.")
                chest9 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest9)
            if choice == 'chest2':
                equipment_component = Equipment(slot='chest', defense_bonus=9)
                item = Object(y, x, chestSteel, 'Strong Cuirass', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A strong breastplate. Increases defense by 9.")
                chest10 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest10)  
            if choice == 'legs1':
                equipment_component = Equipment(slot='legs', defense_bonus=4)
                item = Object(y, x, greavesSteel, 'Greaves', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic set of greaves. Increases defense by 4.")
                chest11 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest11)
            if choice == 'legs2':
                equipment_component = Equipment(slot='legs', defense_bonus=8)
                item = Object(y, x, greavesSteel, 'Strong Greaves', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A strong set of greaves. Increases defense by 8.")
                chest12 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest12)  
            if choice == 'feet1':         
                equipment_component = Equipment(slot='feet', defense_bonus=5)
                item = Object(y, x, sabatonsSteel, 'Boots', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic pair of sabatons. Increases defense by 5.")
                chest13 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest13)
            if choice == 'feet2':          
                equipment_component = Equipment(slot='feet', defense_bonus=8)
                item = Object(y, x, sabatonsSteel, 'Strong Boots', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A strong pair of sabatons. Increases defense by 8.")
                chest14 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest14)
            if choice == 'hands1':          
                equipment_component = Equipment(slot='hands', defense_bonus=4)
                item = Object(x, y, gauntletsSteel, 'Grips', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A basic pair of gauntlets. Increases defense by 4.")
                chest15 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest15)
            if choice == 'hands2':          
                equipment_component = Equipment(slot='hands', defense_bonus=7)
                item = Object(x, y, gauntletsSteel, 'Strong Grips', libtcod.white, 0, 0, 0, equipment=equipment_component, description="A strong pair of gauntlets. Increases defense by 7.")
                chest16 = Object(y, x, chestTile, 'Treasure Chest', libtcod.white, 0, 0, 0, contains=[item])
                objects.append(chest16)
                            
def render_bar(x, y, totalWidth, name, value, maximum, barColor, backColor):
    barWidth = int(float(value) / maximum * totalWidth)
    
    libtcod.console_set_default_background(panel, backColor)
    libtcod.console_rect(panel, x, y, totalWidth, 1, False, libtcod.BKGND_SET)
    
    libtcod.console_set_default_background(panel, barColor)
    if barWidth > 0:
        libtcod.console_rect(panel, x, y, barWidth, 1, False, libtcod.BKGND_SET)
        
    libtcod.console_set_default_foreground(panel, libtcod.white)
    libtcod.console_print_ex(panel, x + totalWidth / 2, y, libtcod.BKGND_NONE, libtcod.CENTER, name + ': ' + str(int(value)) + '/' + str(int(maximum)))
  
def get_names_under_mouse():
    global mouse, camera_x, camera_y, currentMap
    (x, y) = (mouse.cx, mouse.cy)
    (x, y) = (camera_x + x, camera_y + y)
    
    if currentMap == 'Town':
        names = [object.name for object in objects if object.x == x and object.y == y]
    else:
        names = [object.name for object in objects if object.x == x and object.y == y and libtcod.map_is_in_fov(fovMap, object.x, object.y)]
    names = ' , '.join(names)
    return names 

def move_camera(target_x, target_y):
    global camera_x, camera_y, fovRecompute, dungeon
 
    x = target_x - cameraWidth / 2  
    y = target_y - cameraHeight / 2
 
    if x < 0: 
        x = 0
    if y < 0: 
        y = 0
    if x > len(dungeon) - cameraWidth - 1: 
        x = len(dungeon) - cameraWidth - 1
    if y > len(dungeon[0]) - cameraHeight - 1: 
        y = len(dungeon[0]) - cameraHeight - 1
         
    if x != camera_x or y != camera_y: 
        fovRecompute = True
    (camera_x, camera_y) = (x, y)
 
def to_camera_coordinates(x, y):
    global camera_x, camera_y
    (x, y) = (x - camera_x, y - camera_y)
    if (x < 0 or y < 0 or x >= cameraWidth or y >= cameraHeight):
        return (None, None)
    return (x, y)
 
def renderAll():
    global dungeon
    global fovRecompute, fovMap
    global prevTime
    global camera_x, camera_y
    global playerLevel
    global playerExperiencePoints, experienceMax
    global hotbarAbilities
    global dungeonLevel, currentMap
    
    if currentMap != 'Mines':
        dungeonMap = allMaps[currentMap, dungeonLevel]
    
    move_camera(player.x, player.y)
    
    if fovRecompute:
        fovRecompute = False
        libtcod.map_compute_fov(fovMap, player.x, player.y, torchRadius, fovLightWalls, fovAlg)
        libtcod.console_clear(con)
    
    for x in range(cameraWidth):
        for y in range(cameraHeight):                
            (map_x, map_y) = (camera_x + x, camera_y + y)
            if currentMap == 'Town':
                if dungeonMap[map_y][map_x] == 'g':
                    libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'w':
                    libtcod.console_put_char_ex(con, x, y, waterTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 's':
                    libtcod.console_put_char_ex(con, x, y, pathTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '!':
                    libtcod.console_put_char_ex(con, x, y, flowersTile1, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '@':
                    libtcod.console_put_char_ex(con, x, y, flowersTile2, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '#':
                    libtcod.console_put_char_ex(con, x, y, flowersTile3, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == '1':
                    libtcod.console_put_char_ex(con, x, y, pathTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '2':
                    libtcod.console_put_char_ex(con, x, y, pathTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '3':
                    libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '4':
                    libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '5':
                    libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '6':
                    libtcod.console_put_char_ex(con, x, y, pathTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '7':
                    libtcod.console_put_char_ex(con, x, y, pathTile, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == 'x':                 
                    libtcod.console_put_char_ex(con, x, y, grassWaterStraightLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'z':
                    libtcod.console_put_char_ex(con, x, y, grassWaterStraightRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'y':
                    libtcod.console_put_char_ex(con, x, y, grassWaterStraightBottom, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'f':
                    libtcod.console_put_char_ex(con, x, y, grassWaterStraightTop, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == 'u':
                    libtcod.console_put_char_ex(con, x, y, waterGrassBottomRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 't':
                    libtcod.console_put_char_ex(con, x, y, waterGrassBottomLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'q':
                    libtcod.console_put_char_ex(con, x, y, waterGrassTopRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'm':
                    libtcod.console_put_char_ex(con, x, y, waterGrassTopLeft, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == 'v':
                    libtcod.console_put_char_ex(con, x, y, grassWaterTopLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'p':
                    libtcod.console_put_char_ex(con, x, y, grassWaterTopRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'k':
                    libtcod.console_put_char_ex(con, x, y, grassWaterBottomLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'l':
                    libtcod.console_put_char_ex(con, x, y, grassWaterBottomRight, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == 'j':
                    libtcod.console_put_char_ex(con, x, y, bridgeTile, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'n':
                    libtcod.console_put_char_ex(con, x, y, bridgeTopLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'o':
                    libtcod.console_put_char_ex(con, x, y, bridgeTopMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'r':
                    libtcod.console_put_char_ex(con, x, y, bridgeTopRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'e':
                    libtcod.console_put_char_ex(con, x, y, bridgeBottomLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'h':
                    libtcod.console_put_char_ex(con, x, y, bridgeBottomMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'i':
                    libtcod.console_put_char_ex(con, x, y, bridgeBottomRight, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == 'A':
                    libtcod.console_put_char_ex(con, x, y, treeTopLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'B':
                    libtcod.console_put_char_ex(con, x, y, treeTopMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'C':
                    libtcod.console_put_char_ex(con, x, y, treeTopRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'D':
                    libtcod.console_put_char_ex(con, x, y, treeMiddleLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'E':
                    libtcod.console_put_char_ex(con, x, y, treeMiddleMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'F':
                    libtcod.console_put_char_ex(con, x, y, treeMiddleRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'G':
                    libtcod.console_put_char_ex(con, x, y, treeBottomLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'H':
                    libtcod.console_put_char_ex(con, x, y, treeBottomMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'I':
                    libtcod.console_put_char_ex(con, x, y, treeBottomRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'J':
                    libtcod.console_put_char_ex(con, x, y, treeBottomCornerLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'K':
                    libtcod.console_put_char_ex(con, x, y, treeBottomCornerRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'L':
                    libtcod.console_put_char_ex(con, x, y, treeTopCornerLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'M':
                    libtcod.console_put_char_ex(con, x, y, treeTopCornerRight, libtcod.white, libtcod.black)
                    
                if dungeonMap[map_y][map_x] == '`':
                    libtcod.console_put_char_ex(con, x, y, volcanoLight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '>':
                    libtcod.console_put_char_ex(con, x, y, volcanoDark, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == '$':
                    libtcod.console_put_char_ex(con, x, y, blackTile, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '%':
                    libtcod.console_put_char_ex(con, x, y, lavaTile, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '(':
                    libtcod.console_put_char_ex(con, x, y, lightBottomLeft, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == ')':
                    libtcod.console_put_char_ex(con, x, y, lightBottomRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '-':
                    libtcod.console_put_char_ex(con, x, y, lavaBottomLeft, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '_':
                    libtcod.console_put_char_ex(con, x, y, lavaBottomRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '+':
                    libtcod.console_put_char_ex(con, x, y, lavaTopRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '=':
                    libtcod.console_put_char_ex(con, x, y, lavaTopLeft, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '{':
                    libtcod.console_put_char_ex(con, x, y, darkBottomRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '}':
                    libtcod.console_put_char_ex(con, x, y, darkBottomLeft, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '[':
                    libtcod.console_put_char_ex(con, x, y, blackBottomRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == ']':
                    libtcod.console_put_char_ex(con, x, y, blackBottomLeft, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '|':
                    libtcod.console_put_char_ex(con, x, y, grassBottomRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == '<':
                    libtcod.console_put_char_ex(con, x, y, grassBottomLeft, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == ':':
                    libtcod.console_put_char_ex(con, x, y, grassTopRight, libtcod.white, libtcod.black) 
                if dungeonMap[map_y][map_x] == ';':
                    libtcod.console_put_char_ex(con, x, y, grassTopLeft, libtcod.white, libtcod.black)                 
                
                if dungeonMap[map_y][map_x] == 'X':
                    libtcod.console_put_char_ex(con, x, y, houseRoofLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'Y':
                    libtcod.console_put_char_ex(con, x, y, houseRoofMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'Z':
                    libtcod.console_put_char_ex(con, x, y, houseRoofRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'N':
                    libtcod.console_put_char_ex(con, x, y, houseTopLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'O':
                    libtcod.console_put_char_ex(con, x, y, houseTopMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'P':
                    libtcod.console_put_char_ex(con, x, y, houseTopRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'Q':
                    libtcod.console_put_char_ex(con, x, y, houseMiddleLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'R':
                    libtcod.console_put_char_ex(con, x, y, houseMiddleMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'T':
                    libtcod.console_put_char_ex(con, x, y, houseMiddleRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'U':
                    libtcod.console_put_char_ex(con, x, y, houseBottomLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'V':
                    libtcod.console_put_char_ex(con, x, y, houseBottomMiddle, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'W':
                    libtcod.console_put_char_ex(con, x, y, houseBottomRight, libtcod.white, libtcod.black)
                                       
                if dungeonMap[map_y][map_x] == 'S':
                    libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
            
            elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == 'Maybell' or currentMap == 'Home'):
                if dungeonMap[map_y][map_x] == '-':
                    libtcod.console_put_char_ex(con, x, y, houseFloor, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'X':
                    libtcod.console_put_char_ex(con, x, y, houseWall, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'Y':
                    libtcod.console_put_char_ex(con, x, y, houseBackWall, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'W':
                    libtcod.console_put_char_ex(con, x, y, houseWindowWall, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'l':
                    libtcod.console_put_char_ex(con, x, y, houseWindowFloor, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'B':
                    libtcod.console_put_char_ex(con, x, y, bedTop, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'E':
                    libtcod.console_put_char_ex(con, x, y, bedBottom, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'T':
                    libtcod.console_put_char_ex(con, x, y, tableLeft, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'A':
                    libtcod.console_put_char_ex(con, x, y, tableRight, libtcod.white, libtcod.black)
                if dungeonMap[map_y][map_x] == 'S':
                    libtcod.console_put_char_ex(con, x, y, houseFloor, libtcod.white, libtcod.black)
                    
            elif currentMap == 'Catacombs':
                if dungeonLevel == 0 or dungeonLevel == 4:
                    if dungeonMap[map_y][map_x] == 'X':
                        libtcod.console_put_char_ex(con, x, y, dungeonWall, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '-':
                        libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'S':
                        libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '*':
                        libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'D':
                        libtcod.console_put_char_ex(con, x, y, stairsDown, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'U':
                        libtcod.console_put_char_ex(con, x, y, stairsUp, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'l':
                        libtcod.console_put_char_ex(con, x, y, tombLeft, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'r':
                        libtcod.console_put_char_ex(con, x, y, tombRight, libtcod.white, libtcod.black)
                else:
                    visible = libtcod.map_is_in_fov(fovMap, map_x, map_y)        
                    if not visible:
                        if dungeon[map_x][map_y].explored:
                            if dungeon[map_x][map_y].blocked and dungeonMap[map_y][map_x] != 'P' and dungeonMap[map_y][map_x] != 'B' and dungeonMap[map_y][map_x] != 'H' and dungeonMap[map_y][map_x] != 'C' and dungeonMap[map_y][map_x] != 'L' and dungeonMap[map_y][map_x] != 'O':
                                libtcod.console_put_char_ex(con, x, y, darkDungeonWall, libtcod.white, libtcod.black)
                            else:
                                libtcod.console_put_char_ex(con, x, y, darkDungeonTile, libtcod.white, libtcod.black)
                    else:
                        if dungeon[map_x][map_y].blocked:
                                libtcod.console_put_char_ex(con, x, y, dungeonWall, libtcod.white, libtcod.black)
                        else:
                            libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                        dungeon[map_x][map_y].explored = True
                    
            elif currentMap == 'Forest':
                if dungeonLevel == 0 or dungeonLevel == 3:
                    if dungeonMap[map_y][map_x] == 'X':
                            libtcod.console_put_char_ex(con, x, y, treeMiddleMiddle, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'a':
                            libtcod.console_put_char_ex(con, x, y, treeTopLeft, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'b':
                            libtcod.console_put_char_ex(con, x, y, treeTopMiddle, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'c':
                            libtcod.console_put_char_ex(con, x, y, treeTopRight, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'd':
                            libtcod.console_put_char_ex(con, x, y, treeMiddleLeft, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'e':
                            libtcod.console_put_char_ex(con, x, y, treeMiddleRight, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'f':
                            libtcod.console_put_char_ex(con, x, y, treeBottomLeft, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'g':
                            libtcod.console_put_char_ex(con, x, y, treeBottomMiddle, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'h':
                            libtcod.console_put_char_ex(con, x, y, treeBottomRight, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'i':
                            libtcod.console_put_char_ex(con, x, y, treeTopCornerLeft, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'j':
                            libtcod.console_put_char_ex(con, x, y, treeTopCornerRight, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'k':
                            libtcod.console_put_char_ex(con, x, y, treeBottomCornerLeft, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'l':
                            libtcod.console_put_char_ex(con, x, y, treeBottomCornerRight, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '-':
                            libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'S':
                            libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '*':
                            libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'D':
                            libtcod.console_put_char_ex(con, x, y, stairsDown, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'U':
                        libtcod.console_put_char_ex(con, x, y, stairsUp, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'm':
                            libtcod.console_put_char_ex(con, x, y, flowersTile1, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'n':
                            libtcod.console_put_char_ex(con, x, y, flowersTile2, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'o':
                            libtcod.console_put_char_ex(con, x, y, flowersTile3, libtcod.white, libtcod.black)
                            
                else:
                    visible = libtcod.map_is_in_fov(fovMap, map_x, map_y)        
                    if not visible:
                        if dungeon[map_x][map_y].explored:
                            if dungeon[map_x][map_y].blocked and dungeonMap[map_y][map_x] != 'P' and dungeonMap[map_y][map_x] != 'B' and dungeonMap[map_y][map_x] != 'H' and dungeonMap[map_y][map_x] != 'C' and dungeonMap[map_y][map_x] != 'L' and dungeonMap[map_y][map_x] != 'O':
                                if dungeonMap[map_y][map_x] == 'X':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeMiddleMiddle, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'a':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeTopLeft, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'b':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeTopMiddle, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'c':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeTopRight, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'd':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeMiddleLeft, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'e':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeMiddleRight, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'f':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeBottomLeft, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'g':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeBottomMiddle, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'h':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeBottomRight, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'i':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeTopCornerLeft, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'j':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeTopCornerRight, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'k':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeBottomCornerLeft, libtcod.white, libtcod.black)
                                if dungeonMap[map_y][map_x] == 'l':
                                    libtcod.console_put_char_ex(con, x, y, darkTreeBottomCornerRight, libtcod.white, libtcod.black) 
                            else:
                                libtcod.console_put_char_ex(con, x, y, darkGrassTile, libtcod.white, libtcod.black)
                    else:
                        if dungeon[map_x][map_y].blocked:
                            if dungeonMap[map_y][map_x] == 'X':
                                libtcod.console_put_char_ex(con, x, y, treeMiddleMiddle, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'a':
                                libtcod.console_put_char_ex(con, x, y, treeTopLeft, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'b':
                                libtcod.console_put_char_ex(con, x, y, treeTopMiddle, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'c':
                                libtcod.console_put_char_ex(con, x, y, treeTopRight, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'd':
                                libtcod.console_put_char_ex(con, x, y, treeMiddleLeft, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'e':
                                libtcod.console_put_char_ex(con, x, y, treeMiddleRight, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'f':
                                libtcod.console_put_char_ex(con, x, y, treeBottomLeft, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'g':
                                libtcod.console_put_char_ex(con, x, y, treeBottomMiddle, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'h':
                                libtcod.console_put_char_ex(con, x, y, treeBottomRight, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'i':
                                libtcod.console_put_char_ex(con, x, y, treeTopCornerLeft, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'j':
                                libtcod.console_put_char_ex(con, x, y, treeTopCornerRight, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'k':
                                libtcod.console_put_char_ex(con, x, y, treeBottomCornerLeft, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'l':
                                libtcod.console_put_char_ex(con, x, y, treeBottomCornerRight, libtcod.white, libtcod.black)
                        else:
                            if dungeonMap[map_y][map_x] == '-':
                                libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'S':
                                libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'm':
                                libtcod.console_put_char_ex(con, x, y, flowersTile1, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'n':
                                libtcod.console_put_char_ex(con, x, y, flowersTile2, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'o':
                                libtcod.console_put_char_ex(con, x, y, flowersTile3, libtcod.white, libtcod.black)
                            if dungeonMap[map_y][map_x] == 'F':
                                libtcod.console_put_char_ex(con, x, y, grassTile, libtcod.white, libtcod.black)
                        dungeon[map_x][map_y].explored = True
                    
            elif currentMap == 'Tundra':
                if dungeonLevel == 0 or dungeonLevel == 5:
                    if dungeonMap[map_y][map_x] == 'X':
                        libtcod.console_put_char_ex(con, x, y, iceWall, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '-':
                        libtcod.console_put_char_ex(con, x, y, snowTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'S':
                        libtcod.console_put_char_ex(con, x, y, snowTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '*':
                        libtcod.console_put_char_ex(con, x, y, snowTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'D':
                        libtcod.console_put_char_ex(con, x, y, stairsDown, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'U':
                        libtcod.console_put_char_ex(con, x, y, stairsUp, libtcod.white, libtcod.black)
                else:
                    visible = libtcod.map_is_in_fov(fovMap, map_x, map_y)        
                    if not visible:
                        if dungeon[map_x][map_y].explored:
                            if dungeon[map_x][map_y].blocked and dungeonMap[map_y][map_x] != 'P' and dungeonMap[map_y][map_x] != 'B' and dungeonMap[map_y][map_x] != 'H' and dungeonMap[map_y][map_x] != 'C' and dungeonMap[map_y][map_x] != 'L' and dungeonMap[map_y][map_x] != 'O':
                                libtcod.console_put_char_ex(con, x, y, darkIceWall, libtcod.white, libtcod.black)
                            else:
                                libtcod.console_put_char_ex(con, x, y, darkSnowTile, libtcod.white, libtcod.black)
                    else:
                        if dungeon[map_x][map_y].blocked:
                            libtcod.console_put_char_ex(con, x, y, iceWall, libtcod.white, libtcod.black)
                        else:
                            libtcod.console_put_char_ex(con, x, y, snowTile, libtcod.white, libtcod.black)
                        dungeon[map_x][map_y].explored = True
                    
            elif currentMap == 'Volcano':
                if dungeonLevel == 0 or dungeonLevel == 6:
                    if dungeonMap[map_y][map_x] == 'X':
                        libtcod.console_put_char_ex(con, x, y, volcanoWall, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '-':
                        libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'S':
                        libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == '*':
                        libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'D':
                        libtcod.console_put_char_ex(con, x, y, stairsDown, libtcod.white, libtcod.black)
                    if dungeonMap[map_y][map_x] == 'U':
                        libtcod.console_put_char_ex(con, x, y, stairsUp, libtcod.white, libtcod.black)
                else:
                    visible = libtcod.map_is_in_fov(fovMap, map_x, map_y)        
                    if not visible:
                        if dungeon[map_x][map_y].explored:
                            if dungeon[map_x][map_y].blocked and dungeonMap[map_y][map_x] != 'P' and dungeonMap[map_y][map_x] != 'B' and dungeonMap[map_y][map_x] != 'H' and dungeonMap[map_y][map_x] != 'C' and dungeonMap[map_y][map_x] != 'L' and dungeonMap[map_y][map_x] != 'O':
                                libtcod.console_put_char_ex(con, x, y, darkVolcanoWall, libtcod.white, libtcod.black)
                            else:
                                libtcod.console_put_char_ex(con, x, y, darkDungeonTile, libtcod.white, libtcod.black)
                    else:
                        if dungeon[map_x][map_y].blocked:
                            libtcod.console_put_char_ex(con, x, y, volcanoWall, libtcod.white, libtcod.black)
                        else:
                            libtcod.console_put_char_ex(con, x, y, dungeonTile, libtcod.white, libtcod.black)
                        dungeon[map_x][map_y].explored = True
                    
            else:
                visible = libtcod.map_is_in_fov(fovMap, map_x, map_y)        
                if not visible:
                    if dungeon[map_x][map_y].explored:
                        if dungeon[map_x][map_y].blocked:
                            for chests in objects:
                                if chests.fighter == None:
                                    if x == chests.x and y == chests.y:
                                        libtcod.console_put_char_ex(con, x, y, darkMineFloor, libtcod.white, libtcod.black)
                                    else:
                                        libtcod.console_put_char_ex(con, x, y, darkMineWall, libtcod.white, libtcod.black)
                                else:
                                    libtcod.console_put_char_ex(con, x, y, darkMineWall, libtcod.white, libtcod.black)
                        else:
                            libtcod.console_put_char_ex(con, x, y, darkMineFloor, libtcod.white, libtcod.black)
                else:
                    if dungeon[map_x][map_y].blocked:
                        libtcod.console_put_char_ex(con, x, y, mineWall, libtcod.white, libtcod.black)
                    else:
                        libtcod.console_put_char_ex(con, x, y, mineFloor, libtcod.white, libtcod.black)
                    dungeon[map_x][map_y].explored = True
          
    for object in objects:
        object.draw()
        
    libtcod.console_blit(con, 0, 0, screenWidth, screenHeight, 0, 0, 0)
    
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_clear(panel)
    
    img = libtcod.image_load('panel.png')
    libtcod.image_blit_rect(img, panel, 0, 0, -1, -1, libtcod.BKGND_SET) 
    
    # message menu
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_rect(panel, (messageX - 1), 6, (screenWidth / 2 + 5), 6, False, libtcod.BKGND_SET)
    libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
    
    # ability menu
    libtcod.console_set_default_background(panel, libtcod.dark_gray)
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_rect(panel, 27, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 31, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 35, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 39, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 43, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 47, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 51, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 55, 2, 3, 3, False, libtcod.BKGND_SET)
    libtcod.console_rect(panel, 59, 2, 3, 3, False, libtcod.BKGND_SET)
    
    x = 28
    y = 3
    for ability in hotbarAbilities:
        image = ability.icon
        libtcod.console_put_char(panel, x, y, image, libtcod.BKGND_NONE)
        x = x + 4
    
    # return home button
    if (currentMap == 'Mines' or dungeonLevel == 0) and currentMap != 'Town' and currentMap != 'Home' and currentMap != 'Mayor' and currentMap != 'Louis' and currentMap != 'Arianna' and currentMap != 'Maybell':
        libtcod.console_set_default_background(panel, libtcod.black)
        libtcod.console_rect(panel, (screenWidth - 10), 2, (screenWidth / 2 - 33), 2, False, libtcod.BKGND_SET)
        libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
        libtcod.console_set_default_foreground(panel, libtcod.white)
        libtcod.console_print_ex(panel, (screenWidth - 7), 2, libtcod.BKGND_NONE, libtcod.CENTER, 'Return')
        libtcod.console_print_ex(panel, (screenWidth - 5), 3, libtcod.BKGND_NONE, libtcod.CENTER, 'Home')
    
    # inventory button
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_rect(panel, (screenWidth - 12), 5, (screenWidth / 2 - 35), 1, False, libtcod.BKGND_SET)
    libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
    
    # equipment button
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_rect(panel, (screenWidth - 12), 7, (screenWidth / 2 - 35), 1, False, libtcod.BKGND_SET)
    libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
    
    # abilities button
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_rect(panel, (screenWidth - 6), 5, (screenWidth / 2 - 35), 1, False, libtcod.BKGND_SET)
    libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
    
    # log button
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_rect(panel, (screenWidth - 6), 7, (screenWidth / 2 - 35), 1, False, libtcod.BKGND_SET)
    libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
    
    libtcod.console_put_char(panel, (screenWidth - 10), 5, invIcon, libtcod.BKGND_NONE)
    libtcod.console_put_char(panel, (screenWidth - 10), 7, equipIcon, libtcod.BKGND_NONE)
    libtcod.console_put_char(panel, (screenWidth - 4), 5, spellsIcon, libtcod.BKGND_NONE)
    libtcod.console_put_char(panel, (screenWidth - 4), 7, storyIcon, libtcod.BKGND_NONE)

    y = 6
    for (line, color) in allMessages:
        libtcod.console_set_default_foreground(panel, color)
        libtcod.console_print_ex(panel, messageX, y, libtcod.BKGND_NONE, libtcod.LEFT, line)
        y = y + 1
    
    # status bars
    render_bar(1, 3, barWidth, 'HP', player.fighter.hp, player.fighter.max_hp, libtcod.light_red, libtcod.darker_red)
    render_bar(1, 7, barWidth, 'Mana', player.fighter.mana, player.fighter.max_mana, libtcod.light_blue, libtcod.darker_blue)
    render_bar(1, 9, barWidth, 'Exp', playerExperiencePoints, experienceMax, libtcod.light_green, libtcod.darker_green)
    
    currentTime = abs(int(prevTime + 1 - time.time()))
    if currentTime > 1:
        currentTime = 1 
    render_bar(1, 5, barWidth, 'Stamina', currentTime, 1, libtcod.light_fuchsia, libtcod.darker_fuchsia)
    
    libtcod.console_print_ex(panel, 1, 1, libtcod.BKGND_NONE, libtcod.LEFT, 'Level: ' + str(playerLevel))
    libtcod.console_print_ex(panel, screenWidth - 12, 9, libtcod.BKGND_NONE, libtcod.LEFT, currentMap)
    libtcod.console_print_ex(panel, screenWidth - 12, 11, libtcod.BKGND_NONE, libtcod.LEFT, 'Floor: B' + str(dungeonLevel))

    libtcod.console_print_ex(panel, 1, 11, libtcod.BKGND_NONE, libtcod.LEFT, get_names_under_mouse())

    libtcod.console_blit(panel, 0, 0, screenWidth, panelHeight, 0, 0, panelY)
   
def message(newMessage, color=libtcod.white):
    global allMessages
    newMessageLines = textwrap.wrap(newMessage, messageWidth)  
    
    for line in newMessageLines:
        if len(allMessages) == messageHeight:
            del allMessages[0]
        allMessages.append((line, color))
        
def story(newStory, color=libtcod.white):
    global allStory
    newStoryLines = textwrap.wrap(newStory, 40)  
    
    for line in newStoryLines:
        if len(allStory) == 38:
            del allStory[0]
        allStory.append((line, color))
        
def mayorText(number):
    global mayor1, mayor2
    if number == 1:
        questMenu(""" The mayor appears deep in thought, brow furrowed with concern, as you approach. Hearing your footfall, he looks up to meet your gaze. """, [], 20)
        questMenu(""" "Oh! Reinald...good morning. I assume you heard the explosion..." """, [], 20)
        questMenu(""" "It came from the mountain in the center of town. You have heard the story of the mountain, right...? No?" """, [], 20)
        questMenu(""" "Many, many years ago, a powerful demon named Lady Azadlonea threatened the safety of our town. However, a hero rose to fight the demon and sealed her away in the town's mountain." """, [], 20)
        questMenu(""" "However...it would appear as though she is now escaping, and if we don't stop her the volcano will erupt and bury the town!" """, [], 20)
        questMenu(""" "Maybe there are clues to resealing the demon where the hero was laid to rest. Please, go to the town's catacombs and find the hero! And take this...it should be helpful in your quest." """, [], 20)
        for obj in objects:
            if obj.name == "Mayor":
                inventory.append(obj.questNPC.reward)
                message("You got an " + obj.questNPC.reward.name + ".", libtcod.green)
                break
        mayor1 = True
    elif number == 2:
        questMenu(""" "Please...go into the catacombs and find the body of the old hero." """, [], 20)
    elif number == 3:
        questMenu("""  The mayor, who had been pacing furiously, pauses as you approach. """, [], 20)
        questMenu("""  "Did you find the body...?!" he exclaims. You explain your adventures in the catacombs. """, [], 20)
        questMenu("""  "I see...so we need to find two gems? Well...I believe the best place to start would be the woodsman." """, [], 20)
        questMenu("""  "Head south from here, and ask the woodsman in his home if he has seen any orange gems within the forest. And Reinald..." """, [], 20)
        questMenu("""  "Thank you for taking on this dangerous task...the survival of the town is in your hands." """, [], 20)
        mayor2 = True
    else:
        questMenu(""" "Thank you for taking on this tremendous task...please save our town!" """, [], 20)

def heroText(number):
    global hero1, hero2, inventory
    if number == 1:
        questMenu(""" Approaching the marbled tomb, you realize that the room is incredibly quiet, even for catacombs. """, [], 20)
        questMenu(""" You carefully remove the lid from the old hero's tomb and peer within... """, [], 20)
        questMenu(""" ...only to find that the skeleton of the hero is missing its skull. """, [], 20)
        questMenu(""" You cannot commune with the spirit if part of its body is missing...it seems you'll have to search the catacombs for the skull. """, [], 20)
        hero1 = True
    elif number == 2:
        questMenu(""" The skull of the old hero is missing. You won't be able to speak to him until you find his skull. """, [], 20)
    elif number == 3:
        questMenu(""" You place the skull back in the tomb where it belongs, and almost immediately your mind if filled with a strong voice: """, [], 20)
        questMenu(""" "Aaah...that's so much better! Thank you for returning my skull to me, young man." """, [], 20)
        questMenu(""" "I know what you are here for. I can feel that Azadlonea is escaping from her prison in the mountain..." """, [], 20)
        questMenu(""" "Ages ago, I used two gems to seal away the demon - one orange, and one purple. After sealing her, I tossed the gems away so that even I would not know exactly where they were." """, [], 20)
        questMenu(""" "But it would seem as though the gems are needed again, so I will help you as best I can." """, [], 20)
        questMenu(""" "The orange gem I tossed away in the forest, and the purple gem I discarded in the tundra. You will have to search those places to find the gems you seek." """, [], 20)
        questMenu(""" "Please, take this information and do what you must to save the town. Become the new hero." """, [], 20)
        hero2 = True
        for item in inventory:
            if item.owner.name == 'Skull':
                inventory.remove(item.owner)
                break
    else:
        questMenu(""" "Hello, Reinald. Thank you for helping me...but you must hurry and find the gems to seal away the demon!" """, [], 20)

def louisText(number):
    global louis1, louis2
    if number == 1:
        questMenu(""" "Hey Reinald, nice to see you." """, [], 20)
    elif number == 2:
        questMenu(""" "Hello Reinald, did you need something? ... Oh, the mayor sent you here?" """, [], 20)
        questMenu(""" Louis listens patiently as you explain your encounter with the old hero. "Two gems, eh?" """, [], 20)
        questMenu(""" "Well...I spend the majority of my time in the forest, so I should be able to help you." """, [], 20)
        questMenu(""" "A few days I saw something orange and sparkling in the grass of the deep woods south of here, but I did not go any closer for fear of the forest guardian that watches the area." """, [], 20)
        questMenu(""" "You, however, should have nothing to fear from the guardian. Perhaps if you can defeat it, you'll be able to find the gem..." """, [], 20)
        louis1 = True
    elif number == 3:
        questMenu(""" "Please bring that gem back to me when you think you've found it." """, [], 20)
    elif number == 4:
        questMenu(""" "Ah, I see you have the gem! Yes, that looks quite like what I saw days ago." """, [], 20)
        questMenu(""" "Now for the second gem...if the hero said it could be found in the tundra, you will probably want to speak to Maybell." """, [], 20)
        questMenu(""" "She lives closest to the tundra, and I know she will occasionally venture within to look for snow flowers." """, [], 20)
        questMenu(""" "Go and speak with her, and hopefully she can help you. Oh! And take these - I don't need them anymore, and they should be of use to you." """, [], 20)
        for obj in objects:
            if obj.name == "Louis":
                inventory.append(obj.questNPC.reward)
                message("You got " + obj.questNPC.reward.name + ".", libtcod.green)
                break
        louis2 = True
    else:
        questMenu(""" "Hello Reinald, have you gone to visit Maybell yet?" """, [], 20)
    
def ariannaText():
    questMenu(""" "Hi Reinald, how are you doing?" """, [], 20)
    
def maybellText(number):
    global maybell1, maybell2
    if number == 1:
        questMenu(""" "Good morning, Reinald." """, [], 20)
    elif number == 2:
        questMenu(""" Maybell freezes as you enter, and watches closely while you approach. "Reinald, you're tracking dirt into my beautiful home...!" """, [], 20)
        questMenu(""" Regardless, you continue and begin to explain your quest. Maybell's expression softens somewhat as she senses your resolve. """, [], 20)
        questMenu(""" "I'm sorry, I didn't mean to be rude. You know how I like to keep everything gorgeous! But...I suppose this isn't the time for that, especially since it seems my home is about to be swallowed by lava anyway. """, [], 20)
        questMenu(""" "Yes, I saw a purple gem when I was in the tundra yesterday. However, I saw it in the clutches of a sleeping red dragon... """, [], 20)
        questMenu(""" "I hope you can defeat the dragon and take the gem, Reinald...it sounds like its the town's only hope! """, [], 20)
        maybell1 = True
    elif number == 3:
        questMenu(""" "Do you have the gem yet? No? Well...please return once the gem is in your possession." """, [], 20)
    elif number == 4:
        questMenu(""" "Ah, I see you have the gem! Bring it here, let me take a look..." """, [], 20)
        questMenu(""" Maybell turns the gem over in her hands as she examines it, then nods before handing it back. "Yes, this seems to be the one I saw." """, [], 20)
        questMenu(""" "That means you have both gems, right Reinald?" """, [], 20)
        questMenu(""" "Then please, take them to the volcano and put an end to all of this madness!" """, [], 20)
        questMenu(""" "Oh, and by the way, I found these weeks ago in the tundra, and I have absolutely no use for them! Do you want them?" """, [], 20)
        for obj in objects:
            if obj.name == "Maybell":
                inventory.append(obj.questNPC.reward)
                message("You got " + obj.questNPC.reward.name + ".", libtcod.green)
                break
        maybell2 = True
    else:
        questMenu(""" "Please hurry Reinald...I'm not sure how much longer the town has!" """, [], 20)
        
def updateLog():
    global allStory, logUpdate1, logUpdate2, logUpdate3, logUpdate4, logUpdate5, logUpdate6, logUpdate7, logUpdate8, logUpdate9, logUpdate10, logUpdate11
    global mayor1, mayor2, hero1, hero2, louis1, louis2, maybell1, maybell2
    
    if mayor1 and logUpdate1 == False:
        story("The mayor has asked me to go to the town's catacombs and check on the body of the hero who once sealed the demon away. I can reach the catacombs if I follow the path north from the mayor's house.", libtcod.red)
        logUpdate1 = True
        
    if hero1 and logUpdate2 == False:
        story("I found the tomb of the old hero, but discovered his body to be missing its skull. I won't be able to contact the hero until I find his skull, deeper in the catacombs.", libtcod.light_green)
        logUpdate2 = True
        
    skullInInventory = False
    for item in inventory:
        if item.name == "Skull":
            skullInInventory = True
            
    if skullInInventory and logUpdate3 == False:
        story("I found the skull of the hero after destroying its animated form. I should take the skull back to the tomb of the hero.", libtcod.red)
        logUpdate3 = True
        
    if hero2 and logUpdate4 == False:
        story("I managed to contact the spirit of the ancient hero. He told me that I need to find two gems to seal away the demon. I should tell this to the mayor.", libtcod.light_green)
        logUpdate4 = True
        
    if mayor2 and logUpdate5 == False:
        story("The mayor told me that the woodsman should be able to help me find the orange gem. I can find his house, just above the entrance to the forst, if I travel south from the mayor's house.", libtcod.red)
        logUpdate5 = True
        
    if louis1 and logUpdate6 == False:
        story("Louis, the woodsman, informed me that I can find the orange gem the ancient hero spoke of if I travel deep into the forest, which is just south of Louis' home.", libtcod.light_green)
        logUpdate6 = True
        
    orangeGemInInventory = False
    for item in inventory:
        if item.name == "Orange Gem":
            orangeGemInInventory = True 
            
    if orangeGemInInventory and logUpdate7 == False:
        story("I found the orange gem in the possession of a forest guardian, who had to be defeated. I should take the gem back to Louis.", libtcod.red)
        logUpdate7 = True
    
    if louis2 and logUpdate8 == False:
        story("According to Louis, Maybell, who lives near the entrance to the tundra, may be able to help me find the remaining gem. I should travel to her house east of the mayor's.", libtcod.light_green)
        logUpdate8 = True
        
    if maybell1 and logUpdate9 == False:
        story("Maybell told me that she saw a purple gem like the one I described when she encountered a hybernating dragon in the tundra. I should travel east from Maybell's house to the tundra and check there.", libtcod.red)
        logUpdate9 = True
        
    purpleGemInInventory = False
    for item in inventory:
        if item.name == "Purple Gem":
            purpleGemInInventory = True  
            
    if purpleGemInInventory and logUpdate10 == False:
        story("I found the purple gem within the possessions of the red dragon. I should return to Maybell and let her know.", libtcod.light_green)
        logUpdate10 = True
    
    if maybell2 and logUpdate11 == False:
        story("Now that I have both gems, I must journey into the volcano and put a stop to Lady Azadlonea!", libtcod.red)
        logUpdate11 = True
    
     
def player_select_or_attack(mousex, mousey, lastTime):
    global mouse
    global cantAttack
    global hotbarAbilities
    global allAbilities
    global inventory
    global allMaps, currentMap, dungeonLevel
    global mayor1, mayor2
    global hero1, hero2
    global louis1, louis2
    global maybell1, maybell2
    timer = int(time.time())
    
    x = mousex
    y = mousey
        
    # spell buttons
    if (x >= 27 and x <= 29) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 0:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[0].cast()
        return
            
    elif (x >= 31 and x <= 33) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 1:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[1].cast()
        return
        
    elif (x >= 35 and x <= 37) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 2:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[2].cast()
        return 
                   
    elif (x >= 39 and x <= 41) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 3:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[3].cast()
        return
                    
    elif (x >= 43 and x <= 45) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 4:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[4].cast()
        return
                    
    elif (x >= 47 and x <= 49) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 5:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[5].cast()
        return
                    
    elif (x >= 51 and x <= 53) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 6:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[6].cast()
        return
                    
    elif (x >= 55 and x <= 57) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 7:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[7].cast() 
        return
                   
    elif (x >= 59 and x <= 61) and (y >= 32 and y <= 35):
        if len(hotbarAbilities) <= 8:
            message("No spell loaded.", libtcod.orange)
        else:
            hotbarAbilities[8].cast()
        return
                
    # inventory menu
    elif (x >= 68 and x <= 72) and y == 35:
        chosenItem = inventory_menu('Left click to use, right click to drop permanently, or enter to cancel.\n')
        if drop == False:
            if chosenItem is not None:
                if chosenItem.equipment:
                    chosenItem.equipment.equip()
                else:
                    chosenItem.item.use()
        else:
            if chosenItem is not None:
                if chosenItem.item:
                    chosenItem.item.drop()
                elif chosenItem.equipment:
                    chosenItem.equipment.drop()
        return
    
    # equipment menu
    elif (x >= 74 and x <= 78) and y == 35:
        chosenItem = equipment_menu('Click the item you would like to dequip, or press enter to cancel.\n')
        if chosenItem is not None:
            chosenItem.equipment.dequip()
        return
    
    # abilities menu
    elif (x >= 68 and x <= 72) and y == 37:
        chosenAbility = abilities_menu('Select an ability to add it to your hotbar, or press enter to cancel.\n')
        if chosenAbility is not None:
            if chosenAbility not in hotbarAbilities and chosenAbility.learned == True:
                hotbarAbilities.append(chosenAbility)
                message(chosenAbility.name + " added to hotbar.", libtcod.green)
            elif chosenAbility not in hotbarAbilities and chosenAbility.learned == False:
                if playerSkillPoints > 0:
                    message("You have not yet learned that ability. However, you have enough skill points to learn it. Right click the spell to learn it.", libtcod.orange)
                else:
                    message("You have not yet learned that ability!", libtcod.orange)
            elif chosenAbility in hotbarAbilities:
                hotbarAbilities.remove(chosenAbility)
                message(chosenAbility.name + " removed from hotbar.")
            return
    
    # story log
    elif (x >= 74 and x <= 78) and y == 37:
        storyMenu("Story", [], 24)
      
    elif (x >= 70 and x <= 76) and (y == 32 or y == 33):
        if (currentMap == 'Mines' or dungeonLevel == 0) and currentMap != 'Town' and currentMap != 'Home' and currentMap != 'Mayor' and currentMap != 'Louis' and currentMap != 'Arianna' and currentMap != 'Maybell':
            choice = returnHomeMenu("Would you like to return home?\n", ['Yes', 'No'], 20)
            if choice == 0:
                currentMap = 'Town'
                dungeonLevel = 0
                makeMap(allMaps[currentMap, dungeonLevel])
            elif choice == 1:
                return
                
    (x, y) = (camera_x + x, camera_y + y)
    
    inInventory = False
    if currentMap == 'Town': 
        if (x == 53 and y == 36) or (x == 53 and y == 35) or (x == 53 and y == 34) or (x == 54 and y == 34) or (x == 55 and y == 34) or (x == 56 and y == 34) or (x == 56 and y == 35) or (x == 56 and y == 36) or (x == 55 and y == 35) or (x == 54 and y == 35) or (x == 54 and y == 36) or (x == 55 and y == 36): 
            if player.y == 37 and (player.x == 53 or player.x == 54 or player.x == 55 or player.x == 56):
                for item in inventory:
                    if item.name == "Purple Gem":
                        inInventory = True
                if inInventory == True:
                    message("You enter the dungeon...", libtcod.green)
                    currentMap = 'Volcano'
                    dungeonLevel = 0
                    makeMap(allMaps[currentMap, dungeonLevel])
                    initializeFOV()
                else:
                    message("You are not ready to enter that dungeon.", libtcod.orange)
            else:
                message("You are not close enough.", libtcod.orange)
        elif x == 9 and y == 12:
            if player.x == 9 and player.y == 13:
                message("You enter the home of the Mayor...", libtcod.green)
                currentMap = 'Mayor'
                dungeonLevel = 0
                makeMap(allMaps[currentMap, dungeonLevel])
                initializeFOV()
            else:
                message("You are not close enough.", libtcod.orange)
        elif x == 14 and y == 53:
            if player.x == 14 and player.y == 54:
                message("You enter the home of Louis...", libtcod.green)
                currentMap = 'Louis'
                dungeonLevel = 0
                makeMap(allMaps[currentMap, dungeonLevel])
                initializeFOV()
            else:
                message("You are not close enough.", libtcod.orange)
        elif x == 88 and y == 15:
            if player.x == 88 and player.y == 16:
                message("You enter the home of the Arianna...", libtcod.green)
                currentMap = 'Arianna'
                dungeonLevel = 0
                makeMap(allMaps[currentMap, dungeonLevel])
                initializeFOV()
            else:
                message("You are not close enough.", libtcod.orange)
        elif x == 39 and y == 9:
            if player.x == 39 and player.y == 10:
                message("You enter the home of the Maybell...", libtcod.green)
                currentMap = 'Maybell'
                dungeonLevel = 0
                makeMap(allMaps[currentMap, dungeonLevel])
                initializeFOV()
            else:
                message("You are not close enough.", libtcod.orange)
        elif x == 88 and y == 48:
            if player.x == 88 and player.y == 49:
                message("You enter your home...", libtcod.green)
                currentMap = 'Home'
                dungeonLevel = 0
                makeMap(allMaps[currentMap, dungeonLevel])
                initializeFOV()
            else:
                message("You are not close enough.", libtcod.orange)
                
    target = None
    for object in objects:
        if object.x == x and object.y == y:
            if (object.fighter is not None and not object == player) or (object.questNPC is not None) or (object.contains is not None):
                target = object
                break
        
    if target is not None:
        if target.fighter is not None:
            if get_equipped_in_slot('weapon') != None:
                if get_equipped_in_slot('weapon').ranged == False:
                    if (target.x == player.x + 1 and target.y == player.y) or (target.x == player.x - 1 and target.y == player.y) or (target.x == player.x and target.y == player.y + 1) or (target.x == player.x and target.y == player.y - 1) or (target.x == player.x + 1 and target.y == player.y + 1) or (target.x == player.x - 1 and target.y == player.y + 1) or (target.x == player.x + 1 and target.y == player.y - 1) or (target.x == player.x - 1 and target.y == player.y - 1):
                        if (timer >= lastTime + 1):
                            cantAttack = False
                            player.fighter.attack(target)
                        else:
                            message("You can't attack yet!", libtcod.orange)
                    else:
                        message("You are not close enough to attack that monster!", libtcod.orange)
                else:
                    if libtcod.map_is_in_fov(fovMap, target.x, target.y):
                        if (timer >= lastTime + 1):
                            cantAttack = False
                            player.fighter.attack(target)
                        else:
                            message("You can't attack yet!", libtcod.orange)
            else:
                if libtcod.map_is_in_fov(fovMap, target.x, target.y):
                    if (timer >= lastTime + 1):
                        cantAttack = False
                        player.fighter.attack(target)
                    else:
                        message("You can't attack yet!", libtcod.orange)
        if target.questNPC is not None:
            if (target.x == player.x + 1 and target.y == player.y) or (target.x == player.x - 1 and target.y == player.y) or (target.x == player.x and target.y == player.y + 1) or (target.x == player.x and target.y == player.y - 1) or (target.x == player.x + 1 and target.y == player.y + 1) or (target.x == player.x - 1 and target.y == player.y + 1) or (target.x == player.x + 1 and target.y == player.y - 1) or (target.x == player.x - 1 and target.y == player.y - 1):
                if target.name == 'Mayor':
                    if mayor1 == False:
                        mayorText(1)
                    elif mayor1 == True and mayor2 == False and hero2 == False:
                        mayorText(2)
                    elif mayor1 == True and mayor2 == False and hero2 == True:
                        mayorText(3)
                    elif mayor2 == True:
                        mayorText(4)
                if target.name == 'Louis':
                    orangeGemInInventory = False
                    for item in inventory:
                        if item.name == "Orange Gem":
                            orangeGemInInventory = True
                    if mayor2 == False:
                        louisText(1)
                    elif louis1 == False and mayor2 == True:
                        louisText(2)
                    elif louis1 == True and orangeGemInInventory == False and louis2 == False:
                        louisText(3)
                    elif louis1 == True and orangeGemInInventory == True and louis2 == False:
                        louisText(4)
                    elif louis1 == True and orangeGemInInventory == True and louis2 == True:
                        louisText(5)
                if target.name == 'Arianna':
                    ariannaText()
                if target.name == 'Maybell':
                    purpleGemInInventory = False
                    for item in inventory:
                        if item.name == "Purple Gem":
                            purpleGemInInventory = True
                    if louis2 == False:
                        maybellText(1)
                    elif maybell1 == False and louis2 == True:
                        maybellText(2)
                    elif maybell1 == True and purpleGemInInventory == False and maybell2 == False:
                        maybellText(3)
                    elif maybell1 == True and purpleGemInInventory == True and maybell2 == False:
                        maybellText(4)
                    elif maybell1 == True and purpleGemInInventory == True and maybell2 == True:
                        maybellText(5)                
                if target.name == 'Ancient Tomb':
                    if (target.y == 12 and (target.x == 46 or target.x == 47)):
                        skullInInventory = False
                        for item in inventory:
                            if item.name == "Skull":
                                skullInInventory = True
                        if hero1 == False:
                            heroText(1)
                        elif hero1 == True and skullInInventory == False and hero2 == False:
                            heroText(2)
                        elif hero1 == True and skullInInventory == True and hero2 == False:
                            heroText(3)
                        elif hero1 == True and skullInInventory == True and hero2 == True:
                            heroText(4)
            else:
                message("You are not close enough to that npc.", libtcod.orange)
                
        if target.contains is not None:
            if target.char is not chestOpenTile:
                if (target.x == player.x + 1 and target.y == player.y) or (target.x == player.x - 1 and target.y == player.y) or (target.x == player.x and target.y == player.y + 1) or (target.x == player.x and target.y == player.y - 1) or (target.x == player.x + 1 and target.y == player.y + 1) or (target.x == player.x - 1 and target.y == player.y + 1) or (target.x == player.x + 1 and target.y == player.y - 1) or (target.x == player.x - 1 and target.y == player.y - 1):
                    for items in target.contains:
                        items.item.pick_up()
                    target.char = chestOpenTile
                else:
                    message("You are not close enough to that chest.", libtcod.orange)

def storyMenu(header, options, width):
    global allStory

    window = libtcod.console_new(40, 40)
    libtcod.console_set_default_background(window, libtcod.brass)
    libtcod.console_rect(window, 0, 0, 40, 40, False, libtcod.BKGND_SCREEN)
    libtcod.console_set_default_foreground(window, libtcod.amber)
    libtcod.console_print_rect_ex(window, 17, 0, 40, 40, libtcod.BKGND_NONE, libtcod.LEFT, header)
    
    y = 2
    for (line, color) in allStory:
        libtcod.console_set_default_foreground(window, color)
        libtcod.console_print_rect_ex(window, 1, y, 40, 40, libtcod.BKGND_NONE, libtcod.LEFT, line)
        y = y + 1
          
    libtcod.console_blit(window, 0, 0, 40, 40, 0, 1, 1, 1.0, 1.0)
    libtcod.console_flush()
    
    key = libtcod.console_wait_for_keypress(True)
    return None

def mainMenuGraphic(header, options, width):
    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = 10
    height = len(options) + header_height
 
    # create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)
 
    # print the header, with auto-wrap
    libtcod.console_set_default_background(window, libtcod.white)
    libtcod.console_rect(window, 0, 0, 20, 20, False, libtcod.BKGND_SET)
    libtcod.console_set_default_foreground(window, libtcod.black)
    libtcod.console_print_rect_ex(window, 0, 4, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
 
    # print all the options
    y = 4
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_set_default_foreground(window, libtcod.black)
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1
 
    x = screenWidth / 2 - width / 2
    y = screenHeight / 2 - height / 2
    libtcod.console_blit(window, 0, 0, width, height, 0, x, 20, 1, 1)
 
    libtcod.console_flush()
    key = libtcod.console_wait_for_keypress(True)
 
    index = key.c - ord('a')
    if index >= 0 and index < len(options): 
        return index
    return None

def questMenu(header, options, width):
    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = libtcod.console_get_height_rect(con, 0, 0, width, screenHeight, header)
    if header == '':
        header_height = 0
    height = 10
 
    # create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)
 
    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
 
    # print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1
 
    x = screenWidth / 2 - width / 2
    y = screenHeight / 2 - height / 2
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 1.0)
 
    libtcod.console_flush()
    key = libtcod.console_wait_for_keypress(True)
 
    index = key.c - ord('a')
    if index >= 0 and index < len(options): 
        return index
    return None

def levelUpMenu(header, options, width):
    if len(options) > 26: 
        raise ValueError('Cannot have a menu with more than 26 options.')
 
    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = libtcod.console_get_height_rect(con, 0, 0, width, screenHeight, header)
    if header == '':
        header_height = 0
    height = len(options) + header_height
 
    # create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)
 
    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
 
    # print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1
 
    x = screenWidth / 2 - width / 2
    y = screenHeight / 2 - height / 2
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 1.0)
 
    libtcod.console_flush()
    key = libtcod.console_wait_for_keypress(True)
 
    index = key.c - ord('a')
    if index >= 0 and index < len(options): 
        return index
    return None

def returnHomeMenu(header, options, width):
    if len(options) > 26: 
        raise ValueError('Cannot have a menu with more than 26 options.')
 
    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = libtcod.console_get_height_rect(con, 0, 0, width, screenHeight, header)
    if header == '':
        header_height = 0
    height = len(options) + header_height
 
    # create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)
 
    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
 
    # print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1
 
    x = screenWidth / 2 - width / 2
    y = screenHeight / 2 - height / 2
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 1.0)
 
    libtcod.console_flush()
    key = libtcod.console_wait_for_keypress(True)
 
    index = key.c - ord('a')
    if index >= 0 and index < len(options): 
        return index
    return None
        
def inventory_menu(header):
    options = [item for item in inventory]
    global key, mouse
    global drop 
    drop = False
    
    if len(options) > 40: raise ValueError('Cannot have a menu with more than 40 options.')
    
    headerHeight = libtcod.console_get_height_rect(con, 0, 0, inventoryWidth, screenHeight, header)
    if header == '':
        headerHeight = 0
    height = 20 + headerHeight
    
    window = libtcod.console_new(inventoryWidth, height)
    libtcod.console_set_default_background(window, libtcod.brass)
    libtcod.console_rect(window, 0, 0, inventoryWidth, height, False, libtcod.BKGND_SCREEN)
    
    libtcod.console_print_rect_ex(window, 0, 0, inventoryWidth, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
    libtcod.console_print_rect_ex(window, 0, 18, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Name: ")
    libtcod.console_print_rect_ex(window, 0, 19, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Info: ")
    
    y = headerHeight
    x = 0
    for option in options:
        libtcod.console_put_char(window, x, y, option.char, libtcod.BKGND_NONE)
        x = x + 2
        if x == 20:
            x = 0
            y = y + 2
        
    libtcod.console_blit(window, 0, 0, inventoryWidth, height, 0, 55, 1, 1.0, 1.0)
    
    while True:
        libtcod.console_flush()
        mousex = mouse.cx - 55
        mousey = mouse.cy - 6
        
        goodY = False
        goodX = False

        # hover
        if (len(options) <= 10 and mousey <= 0) or (len(options) > 10 and len(options) <= 20 and mousey <= 3) or (len(options) > 20 and len(options) <= 30 and mousey <= 5) or (len(options) > 30 and len(options) <= 40 and mousey <= 7):
            goodY = True
                
        if len(options) == 1 and mousex == 0:
            goodX = True
                
        elif len(options) == 2 and mousex <= 2:
            goodX = True
                
        elif len(options) == 3 and mousex <= 4:
            goodX = True
                
        elif len(options) == 4 and mousex <= 6:
            goodX = True
                
        elif len(options) == 5 and mousex <= 8:
            goodX = True
                
        elif len(options) == 6 and mousex <= 10:
            goodX = True
                
        elif len(options) == 7 and mousex <= 12:
            goodX = True
                
        elif len(options) == 8 and mousex <= 14:
            goodX = True
                
        elif len(options) == 9 and mousex <= 16 :
            goodX = True
                
        elif len(options) == 10 and mousex <= 18:
            goodX = True
                
        elif (len(options) == 11 and (mousex == 0 or mousey == 0)) or (len(options) == 21 and (mousex == 0 or mousey <= 1)) or (len(options) == 31 and (mousex == 0 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 12 and (mousex <= 2 or mousey == 0)) or (len(options) == 22 and (mousex <= 2 or mousey <= 1)) or (len(options) == 32 and (mousex <= 2 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 13 and (mousex <= 4 or mousey == 0)) or (len(options) == 23 and (mousex <= 4 or mousey <= 1)) or (len(options) == 33 and (mousex <= 4 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 14 and (mousex <= 6 or mousey == 0)) or (len(options) == 24 and (mousex <= 6 or mousey <= 1)) or (len(options) == 34 and (mousex <= 6 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 15 and (mousex <= 8 or mousey == 0)) or (len(options) == 25 and (mousex <= 8 or mousey <= 1)) or (len(options) == 35 and (mousex <= 8 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 16 and (mousex <= 10 or mousey == 0)) or (len(options) == 26 and (mousex <= 10 or mousey <= 1)) or (len(options) == 36 and (mousex <= 10 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 17 and (mousex <= 12 or mousey == 0)) or (len(options) == 27 and (mousex <= 12 or mousey <= 1)) or (len(options) == 37 and (mousex <= 12 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 18 and (mousex <= 14 or mousey == 0)) or (len(options) == 28 and (mousex <= 14 or mousey <= 1)) or (len(options) == 38 and (mousex <= 14 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 19 and (mousex <= 16 or mousey == 0)) or (len(options) == 29 and (mousex <= 16 or mousey <= 1)) or (len(options) == 39 and (mousex <= 16 or mousey <= 2)):
            goodX = True
                
        elif (len(options) == 20 and (mousex <= 18 or mousey == 0)) or (len(options) == 30 and (mousex <= 18 or mousey <= 1)) or (len(options) == 40 and (mousex <= 18 or mousey <= 2)):
            goodX = True
                
        if mousex < 19 and mousex >= 0 and mousey % 2 == 0 and mousex % 2 == 0 and goodY and mousey >= 0 and goodX:
            if len(inventory) != 0:
                index = mousex - mousex / 2 + 5 * mousey
                name = inventory[index].name + '                  ' 
                description = inventory[index].description + '                                                                             '
        else:
            name = '                '
            description = '                                                                                 '
            
        libtcod.console_print_ex(window, 6, 18, libtcod.BKGND_NONE, libtcod.LEFT, name)
        libtcod.console_print_rect_ex(window, 6, 19, 24, height, libtcod.BKGND_NONE, libtcod.LEFT, description)
        libtcod.console_blit(window, 0, 0, 28, height, 0, 55, 1, 1.0, 1.0)
        
        libtcod.console_flush()
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        goodY = False
        goodX = False
        
        # use
        if (mouse.lbutton_pressed):
            mousex = mouse.cx - 55
            mousey = mouse.cy - 6
            
            if (len(options) <= 10 and mousey <= 0) or (len(options) > 10 and len(options) <= 20 and mousey <= 3) or (len(options) > 20 and len(options) <= 30 and mousey <= 5) or (len(options) > 30 and len(options) <= 40 and mousey <= 7):
                goodY = True
                
            if len(options) == 1 and mousex == 0:
                goodX = True
                
            elif len(options) == 2 and mousex <= 2:
                goodX = True
                
            elif len(options) == 3 and mousex <= 4:
                goodX = True
                
            elif len(options) == 4 and mousex <= 6:
                goodX = True
                
            elif len(options) == 5 and mousex <= 8:
                goodX = True
                
            elif len(options) == 6 and mousex <= 10:
                goodX = True
                
            elif len(options) == 7 and mousex <= 12:
                goodX = True
                
            elif len(options) == 8 and mousex <= 14:
                goodX = True
                
            elif len(options) == 9 and mousex <= 16 :
                goodX = True
                
            elif len(options) == 10 and mousex <= 18:
                goodX = True
                
            elif (len(options) == 11 and (mousex == 0 or mousey == 0)) or (len(options) == 21 and (mousex == 0 or mousey <= 1)) or (len(options) == 31 and (mousex == 0 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 12 and (mousex <= 2 or mousey == 0)) or (len(options) == 22 and (mousex <= 2 or mousey <= 1)) or (len(options) == 32 and (mousex <= 2 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 13 and (mousex <= 4 or mousey == 0)) or (len(options) == 23 and (mousex <= 4 or mousey <= 1)) or (len(options) == 33 and (mousex <= 4 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 14 and (mousex <= 6 or mousey == 0)) or (len(options) == 24 and (mousex <= 6 or mousey <= 1)) or (len(options) == 34 and (mousex <= 6 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 15 and (mousex <= 8 or mousey == 0)) or (len(options) == 25 and (mousex <= 8 or mousey <= 1)) or (len(options) == 35 and (mousex <= 8 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 16 and (mousex <= 10 or mousey == 0)) or (len(options) == 26 and (mousex <= 10 or mousey <= 1)) or (len(options) == 36 and (mousex <= 10 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 17 and (mousex <= 12 or mousey == 0)) or (len(options) == 27 and (mousex <= 12 or mousey <= 1)) or (len(options) == 37 and (mousex <= 12 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 18 and (mousex <= 14 or mousey == 0)) or (len(options) == 28 and (mousex <= 14 or mousey <= 1)) or (len(options) == 38 and (mousex <= 14 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 19 and (mousex <= 16 or mousey == 0)) or (len(options) == 29 and (mousex <= 16 or mousey <= 1)) or (len(options) == 39 and (mousex <= 16 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 20 and (mousex <= 18 or mousey == 0)) or (len(options) == 30 and (mousex <= 18 or mousey <= 1)) or (len(options) == 40 and (mousex <= 18 or mousey <= 2)):
                goodX = True
                
            if mousex < 19 and mousex >= 0 and mousey % 2 == 0 and mousex % 2 == 0 and goodY and mousey >= 0 and goodX:
                if len(inventory) != 0:
                    index = mousex - mousex / 2 + 5 * mousey
                    return inventory[index]
         
        # drop       
        if (mouse.rbutton_pressed):
            mousex = mouse.cx - 55
            mousey = mouse.cy - 6
            
            if (len(options) <= 10 and mousey <= 0) or (len(options) > 10 and len(options) <= 20 and mousey <= 3) or (len(options) > 20 and len(options) <= 30 and mousey <= 5) or (len(options) > 30 and len(options) <= 40 and mousey <= 7):
                goodY = True
                
            if len(options) == 1 and mousex == 0:
                goodX = True
                
            elif len(options) == 2 and mousex <= 2:
                goodX = True
                
            elif len(options) == 3 and mousex <= 4:
                goodX = True
                
            elif len(options) == 4 and mousex <= 6:
                goodX = True
                
            elif len(options) == 5 and mousex <= 8:
                goodX = True
                
            elif len(options) == 6 and mousex <= 10:
                goodX = True
                
            elif len(options) == 7 and mousex <= 12:
                goodX = True
                
            elif len(options) == 8 and mousex <= 14:
                goodX = True
                
            elif len(options) == 9 and mousex <= 16 :
                goodX = True
                
            elif len(options) == 10 and mousex <= 18:
                goodX = True
                
            elif (len(options) == 11 and (mousex == 0 or mousey == 0)) or (len(options) == 21 and (mousex == 0 or mousey <= 1)) or (len(options) == 31 and (mousex == 0 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 12 and (mousex <= 2 or mousey == 0)) or (len(options) == 22 and (mousex <= 2 or mousey <= 1)) or (len(options) == 32 and (mousex <= 2 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 13 and (mousex <= 4 or mousey == 0)) or (len(options) == 23 and (mousex <= 4 or mousey <= 1)) or (len(options) == 33 and (mousex <= 4 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 14 and (mousex <= 6 or mousey == 0)) or (len(options) == 24 and (mousex <= 6 or mousey <= 1)) or (len(options) == 34 and (mousex <= 6 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 15 and (mousex <= 8 or mousey == 0)) or (len(options) == 25 and (mousex <= 8 or mousey <= 1)) or (len(options) == 35 and (mousex <= 8 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 16 and (mousex <= 10 or mousey == 0)) or (len(options) == 26 and (mousex <= 10 or mousey <= 1)) or (len(options) == 36 and (mousex <= 10 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 17 and (mousex <= 12 or mousey == 0)) or (len(options) == 27 and (mousex <= 12 or mousey <= 1)) or (len(options) == 37 and (mousex <= 12 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 18 and (mousex <= 14 or mousey == 0)) or (len(options) == 28 and (mousex <= 14 or mousey <= 1)) or (len(options) == 38 and (mousex <= 14 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 19 and (mousex <= 16 or mousey == 0)) or (len(options) == 29 and (mousex <= 16 or mousey <= 1)) or (len(options) == 39 and (mousex <= 16 or mousey <= 2)):
                goodX = True
                
            elif (len(options) == 20 and (mousex <= 18 or mousey == 0)) or (len(options) == 30 and (mousex <= 18 or mousey <= 1)) or (len(options) == 40 and (mousex <= 18 or mousey <= 2)):
                goodX = True
                
            if mousex < 19 and mousex >= 0 and mousey % 2 == 0 and mousex % 2 == 0 and goodY and mousey >= 0 and goodX:
                if len(inventory) != 0:
                    drop = True
                    index = mousex - mousex / 2 + 5 * mousey
                    return inventory[index]
            
        if key.vk == libtcod.KEY_ENTER:
            return None
    
    return None

def equipment_menu(header):
    global key, mouse
    goodY = False
    global equipped_list
    options = [item for item in equipped_list]
    
    if len(options) > 6: raise ValueError('Cannot have a menu with more than 6 options.')
    
    headerHeight = libtcod.console_get_height_rect(con, 0, 0, equipmentWidth, screenHeight, header)
    if header == '':
        headerHeight = 0
    height = 23 + headerHeight
    
    window = libtcod.console_new(equipmentWidth, height)
    libtcod.console_set_default_background(window, libtcod.brass)
    libtcod.console_rect(window, 0, 0, equipmentWidth, height, False, libtcod.BKGND_SCREEN)
    
    libtcod.console_print_rect_ex(window, 0, 0, equipmentWidth, height, libtcod.BKGND_NONE, libtcod.LEFT, header) 
    line = "HP = " + str(player.fighter.max_hp)
    libtcod.console_print_rect_ex(window, 1, 24, equipmentWidth, height, libtcod.BKGND_NONE, libtcod.LEFT, line)    
    line = "Defense Rating = " + str(player.fighter.defense)
    libtcod.console_print_rect_ex(window, 1, 25, equipmentWidth, height, libtcod.BKGND_NONE, libtcod.LEFT, line)    
    line = "Attack Power = " + str(player.fighter.power)
    libtcod.console_print_rect_ex(window, 1, 26, equipmentWidth, height, libtcod.BKGND_NONE, libtcod.LEFT, line)    

    
    for option in options:
        if option.equipment.slot == 'head':
            libtcod.console_put_char(window, 9, 6, option.char, libtcod.BKGND_NONE)
            
        elif option.equipment.slot == 'chest':
            libtcod.console_put_char(window, 9, 11, option.char, libtcod.BKGND_NONE)
            
        elif option.equipment.slot == 'legs':
            libtcod.console_put_char(window, 9, 16, option.char, libtcod.BKGND_NONE)
            
        elif option.equipment.slot == 'feet':
            libtcod.console_put_char(window, 9, 21, option.char, libtcod.BKGND_NONE)
            
        elif option.equipment.slot == 'hands':
            libtcod.console_put_char(window, 3, 13, option.char, libtcod.BKGND_NONE)
            
        elif option.equipment.slot == 'weapon':
            libtcod.console_put_char(window, 15, 13, option.char, libtcod.BKGND_NONE)

    libtcod.console_set_default_background(window, libtcod.dark_sepia)
        
    # helm coords = (63,6) - (65,8)
    libtcod.console_rect(window, equipmentWidth / 2 - 2, headerHeight, 3, 3, False, libtcod.BKGND_SET)
    
    # chest coords = (63,11) - (65,13)
    libtcod.console_rect(window, equipmentWidth / 2 - 2, headerHeight + 5, 3, 3, False, libtcod.BKGND_SET)
    
    # legs coords = (63,16) - (65,19)
    libtcod.console_rect(window, equipmentWidth / 2 - 2, headerHeight + 10, 3, 3, False, libtcod.BKGND_SET)
    
    # feet coords = (63,21) - (65,24)
    libtcod.console_rect(window, equipmentWidth / 2 - 2, headerHeight + 15, 3, 3, False, libtcod.BKGND_SET)
    
    # hands coords = (57,13) - (59,16)
    libtcod.console_rect(window, equipmentWidth / 3 - 4, headerHeight + 7, 3, 3, False, libtcod.BKGND_SET)
    
    # weapon coords = (69,13) - (71,16)
    libtcod.console_rect(window, equipmentWidth / 3 * 2 + 2, headerHeight + 7, 3, 3, False, libtcod.BKGND_SET)
            
    libtcod.console_blit(window, 0, 0, equipmentWidth, height, 0, 55, 1, 1.0, 1.0)
    
    while True:
        libtcod.console_flush()
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        if (mouse.lbutton_pressed):
            mousex = mouse.cx
            mousey = mouse.cy
            
            # selected head
            if mousex >= 63 and mousex <= 65 and mousey >= 6 and mousey <= 8:
                for option in options:
                    if option.equipment.slot == 'head':
                        if get_equipped_in_slot('head') != None:
                            return option
                            
            # selected chest                  
            elif mousex >= 63 and mousex <= 65 and mousey >= 11 and mousey <= 13:
                for option in options:
                    if option.equipment.slot == 'chest':
                        if get_equipped_in_slot('chest') != None:
                            return option
    
            # selected legs
            elif mousex >= 63 and mousex <= 65 and mousey >= 16 and mousey <= 19:
                for option in options:
                    if option.equipment.slot == 'legs':
                        if get_equipped_in_slot('legs') != None:
                            return option
            
            # selected feet                    
            elif mousex >= 63 and mousex <= 65 and mousey >= 21 and mousey <= 24:
                for option in options:
                    if option.equipment.slot == 'feet':
                        if get_equipped_in_slot('feet') != None:
                            return option
                            
            # selected hands                    
            elif mousex >= 57 and mousex <= 59 and mousey >= 13 and mousey <= 16:
                for option in options:
                    if option.equipment.slot == 'hands':
                        if get_equipped_in_slot('hands') != None:
                            return option
            
            # selected weapon
            elif mousex >= 69 and mousex <= 71 and mousey >= 13 and mousey <= 16:
                for option in options:
                    if option.equipment.slot == 'weapon':
                        if get_equipped_in_slot('weapon') != None:
                            return option
            
        if key.vk == libtcod.KEY_ENTER:
            return None
    
    return None
    
def abilities_menu(header):
    global key, mouse
    global playerSkillPoints
    global allAbilities
    options = [ability for ability in allAbilities]
    
    if len(options) > 45: raise ValueError('Cannot have a menu with more than 40 options.')
    
    headerHeight = libtcod.console_get_height_rect(con, 0, 0, 18, screenHeight, header)
    if header == '':
        headerHeight = 0
    height = 20 + headerHeight
    
    window = libtcod.console_new(28, height)
    libtcod.console_set_default_background(window, libtcod.brass)
    libtcod.console_rect(window, 0, 0, 28, height, False, libtcod.BKGND_SCREEN)
    
    libtcod.console_print_rect_ex(window, 0, 0, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
    libtcod.console_print_rect_ex(window, 1, 5, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Pyromancer")
    libtcod.console_print_rect_ex(window, 1, 7, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Cryomancer")
    libtcod.console_print_rect_ex(window, 1, 9, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Necromancer")
    libtcod.console_print_rect_ex(window, 1, 11, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Psychic")
    libtcod.console_print_rect_ex(window, 1, 13, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Healer")
    libtcod.console_print_rect_ex(window, 0, 15, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Unspent Skill Points = " + str(playerSkillPoints))
    libtcod.console_print_rect_ex(window, 0, 18, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Skill Name: ")
    libtcod.console_print_rect_ex(window, 0, 19, 28, height, libtcod.BKGND_NONE, libtcod.LEFT, "Info: ")

    y = headerHeight
    x = 13
    for option in options:
        libtcod.console_put_char(window, x, y, option.icon, libtcod.BKGND_NONE)
        x = x + 2
        if x >= 22:
            x = 13
            y = y + 2
           
    libtcod.console_blit(window, 0, 0, 28, height, 0, 55, 1, 1.0, 1.0)
    
    while True:
        libtcod.console_flush()
        mousex = mouse.cx - 55
        mousey = mouse.cy - 6
        name = None
    
        if mousex == 13 and mousey == 0:
            name = allAbilities[0].name + '         ' 
            description = allAbilities[0].description
        elif mousex == 15 and mousey == 0:
            name = allAbilities[1].name + '         ' 
            description = allAbilities[1].description
        elif mousex == 17 and mousey == 0:
            name = allAbilities[2].name + '         ' 
            description = allAbilities[2].description
        elif mousex == 19 and mousey == 0:
            name = allAbilities[3].name + '         ' 
            description = allAbilities[3].description      
        elif mousex == 21 and mousey == 0:
            name = allAbilities[4].name + '         ' 
            description = allAbilities[4].description
        elif mousex == 13 and mousey == 2:
            name = allAbilities[5].name + '         ' 
            description = allAbilities[5].description        
        elif mousex == 15 and mousey == 2:
            name = allAbilities[6].name + '         ' 
            description = allAbilities[6].description
        elif mousex == 17 and mousey == 2:
            name = allAbilities[7].name + '         ' 
            description = allAbilities[7].description
        elif mousex == 19 and mousey == 2:
            name = allAbilities[8].name + '         ' 
            description = allAbilities[8].description         
        elif mousex == 21 and mousey == 2:
            name = allAbilities[9].name + '         ' 
            description = allAbilities[9].description
        elif mousex == 13 and mousey == 4:
            name = allAbilities[10].name + '         ' 
            description = allAbilities[10].description 
        elif mousex == 15 and mousey == 4:
            name = allAbilities[11].name + '         ' 
            description = allAbilities[11].description
        elif mousex == 17 and mousey == 4:
            name = allAbilities[12].name + '         ' 
            description = allAbilities[12].description
        elif mousex == 19 and mousey == 4:
            name = allAbilities[13].name + '         ' 
            description = allAbilities[13].description
        elif mousex == 21 and mousey == 4:
            name = allAbilities[14].name + '         ' 
            description = allAbilities[14].description
        elif mousex == 13 and mousey == 6:
            name = allAbilities[15].name + '         ' 
            description = allAbilities[15].description      
        elif mousex == 15 and mousey == 6:
            name = allAbilities[16].name + '         ' 
            description = allAbilities[16].description
        elif mousex == 17 and mousey == 6:
            name = allAbilities[17].name + '         ' 
            description = allAbilities[17].description
        elif mousex == 19 and mousey == 6:
            name = allAbilities[18].name + '         ' 
            description = allAbilities[18].description          
        elif mousex == 21 and mousey == 6:
            name = allAbilities[19].name + '         ' 
            description = allAbilities[19].description
        elif mousex == 13 and mousey == 8:
            name = allAbilities[20].name + '         ' 
            description = allAbilities[20].description          
        elif mousex == 15 and mousey == 8:
            name = allAbilities[21].name + '         ' 
            description = allAbilities[21].description
        elif mousex == 17 and mousey == 8:
            name = allAbilities[22].name + '         ' 
            description = allAbilities[22].description
        elif mousex == 19 and mousey == 8:
            name = allAbilities[23].name + '         ' 
            description = allAbilities[23].description           
        elif mousex == 21 and mousey == 8:
            name = allAbilities[24].name + '         ' 
            description = allAbilities[24].description        
        else:
            name = '                                                                 '
            description = '                                                                                                                                                 '
            
        libtcod.console_print_ex(window, 12, 18, libtcod.BKGND_NONE, libtcod.LEFT, name)
        libtcod.console_print_rect_ex(window, 6, 19, 19, height, libtcod.BKGND_NONE, libtcod.LEFT, description)
        libtcod.console_blit(window, 0, 0, 28, height, 0, 55, 1, 1.0, 1.0)
        
        libtcod.console_flush()

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        if (mouse.lbutton_pressed):
            mousex = mouse.cx - 55
            mousey = mouse.cy - 6
            
            # selected spell in pyromancer
            if mousex == 13 and mousey == 0:
                return allAbilities[0] 
            
            elif mousex == 15 and mousey == 0:
                return allAbilities[1]  

            elif mousex == 17 and mousey == 0:
                return allAbilities[2]  

            elif mousex == 19 and mousey == 0:
                return allAbilities[3]  
      
            elif mousex == 21 and mousey == 0:
                return allAbilities[4]  

            # selected spell in cryomancer   
            elif mousex == 13 and mousey == 2:
                return allAbilities[5]  
        
            elif mousex == 15 and mousey == 2:
                return allAbilities[6] 

            elif mousex == 17 and mousey == 2:
                return allAbilities[7]  

            elif mousex == 19 and mousey == 2:
                return allAbilities[8]  
         
            elif mousex == 21 and mousey == 2:
                return allAbilities[9]  

            # selected spell in necromancer
            elif mousex == 13 and mousey == 4:
                return allAbilities[10]  
 
            elif mousex == 15 and mousey == 4:
                return allAbilities[11]  

            elif mousex == 17 and mousey == 4:
                return allAbilities[12]  

            elif mousex == 19 and mousey == 4:
                return allAbilities[13]  

            elif mousex == 21 and mousey == 4:
                return allAbilities[14] 

            # selected spell in psychic
            elif mousex == 13 and mousey == 6:
                return allAbilities[15]  
      
            elif mousex == 15 and mousey == 6:
                return allAbilities[16]  

            elif mousex == 17 and mousey == 6:
                return allAbilities[17]  

            elif mousex == 19 and mousey == 6:
                return allAbilities[18]  
          
            elif mousex == 21 and mousey == 6:
                return allAbilities[19]  

            # selected spell in healer
            elif mousex == 13 and mousey == 8:
                return allAbilities[20] 
          
            elif mousex == 15 and mousey == 8:
                return allAbilities[21]  

            elif mousex == 17 and mousey == 8:
                return allAbilities[22]  

            elif mousex == 19 and mousey == 8:
                return allAbilities[23]  
           
            elif mousex == 21 and mousey == 8:
                return allAbilities[24] 
            
        if (mouse.rbutton_pressed):
            mousex = mouse.cx - 55
            mousey = mouse.cy - 6
            
            # selected spell in pyromancer
            if mousex == 13 and mousey == 0:
                if allAbilities[0].learned == False:
                    if playerSkillPoints > 0:
                        allAbilities[0].learned = True
                        message('You learned ' + allAbilities[0].name + '.', libtcod.green) 
                        playerSkillPoints = playerSkillPoints - 1
                        return None
                    else:
                        message('You do not have enough skill points to learn ' + allAbilities[0].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[0].name + '.', libtcod.orange)
                    return None  
            
            elif mousex == 15 and mousey == 0:
                if allAbilities[1].learned == False:
                    if allAbilities[0].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[1].learned = True
                            message('You learned ' + allAbilities[1].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[1].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[1].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[1].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 17 and mousey == 0:
                if allAbilities[2].learned == False:
                    if allAbilities[1].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[2].learned = True
                            message('You learned ' + allAbilities[2].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[2].name + '.', libtcod.orange)
                            return None 
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[2].name + '.', libtcod.orange)  
                        return None  
                else:
                    message('You already know ' + allAbilities[2].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 19 and mousey == 0:
                if allAbilities[3].learned == False:
                    if allAbilities[2].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[3].learned = True
                            message('You learned ' + allAbilities[3].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[3].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[3].name + '.', libtcod.orange)
                        return None    
                else:
                    message('You already know ' + allAbilities[3].name + '.', libtcod.orange)
                    return None  
                     
            elif mousex == 21 and mousey == 0:
                if allAbilities[4].learned == False:
                    if allAbilities[3].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[4].learned = True
                            message('You learned ' + allAbilities[4].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[4].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[4].name + '.', libtcod.orange)
                        return None      
                else:
                    message('You already know ' + allAbilities[4].name + '.', libtcod.orange)
                    return None  
                
                
            # selected spell in cryomancer   
            elif mousex == 13 and mousey == 2:
                if allAbilities[5].learned == False:
                    if playerSkillPoints > 0:
                        allAbilities[5].learned = True
                        message('You learned ' + allAbilities[5].name + '.', libtcod.green) 
                        playerSkillPoints = playerSkillPoints - 1
                        return None
                    else:
                        message('You do not have enough skill points to learn ' + allAbilities[5].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[5].name + '.', libtcod.orange)
                    return None  
                        
            elif mousex == 15 and mousey == 2:
                if allAbilities[6].learned == False:
                    if allAbilities[5].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[6].learned = True
                            message('You learned ' + allAbilities[6].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[6].name + '.', libtcod.orange)
                            return None  
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[6].name + '.', libtcod.orange)
                        return None      
                else:
                    message('You already know ' + allAbilities[6].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 17 and mousey == 2:
                if allAbilities[7].learned == False:
                    if allAbilities[6].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[7].learned = True
                            message('You learned ' + allAbilities[7].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[7].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[7].name + '.', libtcod.orange)
                        return None        
                else:
                    message('You already know ' + allAbilities[7].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 19 and mousey == 2:
                if allAbilities[8].learned == False:
                    if allAbilities[7].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[8].learned = True
                            message('You learned ' + allAbilities[8].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[8].name + '.', libtcod.orange)
                            return None 
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[8].name + '.', libtcod.orange)
                        return None         
                else:
                    message('You already know ' + allAbilities[8].name + '.', libtcod.orange)
                    return None  
                         
            elif mousex == 21 and mousey == 2:
                if allAbilities[9].learned == False:
                    if allAbilities[8].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[9].learned = True
                            message('You learned ' + allAbilities[9].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[9].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[9].name + '.', libtcod.orange)
                        return None      
                else:
                    message('You already know ' + allAbilities[9].name + '.', libtcod.orange)
                    return None  
                
                
            # selected spell in necromancer
            elif mousex == 13 and mousey == 4:
                if allAbilities[10].learned == False:
                    if playerSkillPoints > 0:
                        allAbilities[10].learned = True
                        message('You learned ' + allAbilities[10].name + '.', libtcod.green) 
                        playerSkillPoints = playerSkillPoints - 1
                        return None
                    else:
                        message('You do not have enough skill points to learn ' + allAbilities[10].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[10].name + '.', libtcod.orange)
                    return None  
                 
            elif mousex == 15 and mousey == 4:
                if allAbilities[11].learned == False:
                    if allAbilities[10].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[11].learned = True
                            message('You learned ' + allAbilities[11].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[11].name + '.', libtcod.orange)
                            return None 
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[11].name + '.', libtcod.orange)
                        return None 
                else:
                    message('You already know ' + allAbilities[11].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 17 and mousey == 4:
                if allAbilities[12].learned == False:
                    if allAbilities[11].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[12].learned = True
                            message('You learned ' + allAbilities[12].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[12].name + '.', libtcod.orange)
                            return None 
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[12].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[12].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 19 and mousey == 4:
                if allAbilities[13].learned == False:
                    if allAbilities[12].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[13].learned = True
                            message('You learned ' + allAbilities[13].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[13].name + '.', libtcod.orange)
                            return None  
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[13].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[13].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 21 and mousey == 4:
                if allAbilities[14].learned == False:
                    if allAbilities[13].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[14].learned = True
                            message('You learned ' + allAbilities[14].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[14].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[14].name + '.', libtcod.orange)
                        return None    
                else:
                    message('You already know ' + allAbilities[14].name + '.', libtcod.orange)
                    return None  
                
                
            # selected spell in psychic
            elif mousex == 13 and mousey == 6:
                if allAbilities[15].learned == False:
                    if playerSkillPoints > 0:
                        allAbilities[15].learned = True
                        message('You learned ' + allAbilities[15].name + '.', libtcod.green) 
                        playerSkillPoints = playerSkillPoints - 1
                        return None
                    else:
                        message('You do not have enough skill points to learn ' + allAbilities[15].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[15].name + '.', libtcod.orange)
                    return None  
                      
            elif mousex == 15 and mousey == 6:
                if allAbilities[16].learned == False:
                    if allAbilities[15].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[16].learned = True
                            message('You learned ' + allAbilities[16].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[16].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[16].name + '.', libtcod.orange)
                        return None      
                else:
                    message('You already know ' + allAbilities[16].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 17 and mousey == 6:
                if allAbilities[17].learned == False:
                    if allAbilities[16].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[17].learned = True
                            message('You learned ' + allAbilities[17].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[17].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[17].name + '.', libtcod.orange)
                        return None        
                else:
                    message('You already know ' + allAbilities[17].name + '.', libtcod.orange)
                    return None  
                
            elif mousex == 19 and mousey == 6:
                if allAbilities[18].learned == False:
                    if allAbilities[17].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[18].learned = True
                            message('You learned ' + allAbilities[18].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[18].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[18].name + '.', libtcod.orange)
                        return None        
                else:
                    message('You already know ' + allAbilities[18].name + '.', libtcod.orange)
                    return None 
                          
            elif mousex == 21 and mousey == 6:
                if allAbilities[19].learned == False:
                    if allAbilities[18].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[19].learned = True
                            message('You learned ' + allAbilities[19].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[19].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[19].name + '.', libtcod.orange)
                        return None         
                else:
                    message('You already know ' + allAbilities[19].name + '.', libtcod.orange)
                    return None 
                
                
            # selected spell in healer
            elif mousex == 13 and mousey == 8:
                if allAbilities[20].learned == False:
                    if playerSkillPoints > 0:
                        allAbilities[20].learned = True
                        message('You learned ' + allAbilities[20].name + '.', libtcod.green) 
                        playerSkillPoints = playerSkillPoints - 1
                        return None
                    else:
                        message('You do not have enough skill points to learn ' + allAbilities[20].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[20].name + '.', libtcod.orange)
                    return None  
  
                       
            elif mousex == 15 and mousey == 8:
                if allAbilities[21].learned == False:
                    if allAbilities[20].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[21].learned = True
                            message('You learned ' + allAbilities[21].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[21].name + '.', libtcod.orange)
                            return None 
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[21].name + '.', libtcod.orange)
                        return None
                else:
                    message('You already know ' + allAbilities[21].name + '.', libtcod.orange)
                    return None 
                
            elif mousex == 17 and mousey == 8:
                if allAbilities[22].learned == False:
                    if allAbilities[21].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[22].learned = True
                            message('You learned ' + allAbilities[22].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[22].name + '.', libtcod.orange)
                            return None  
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[22].name + '.', libtcod.orange)
                        return None
                else:
                    message('You already know ' + allAbilities[22].name + '.', libtcod.orange)
                    return None 
                
            elif mousex == 19 and mousey == 8:
                if allAbilities[23].learned == False:
                    if allAbilities[22].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[23].learned = True
                            message('You learned ' + allAbilities[23].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[23].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[23].name + '.', libtcod.orange)
                        return None  
                else:
                    message('You already know ' + allAbilities[23].name + '.', libtcod.orange)
                    return None 
                          
            elif mousex == 21 and mousey == 8:
                if allAbilities[24].learned == False:
                    if allAbilities[23].learned == True:
                        if playerSkillPoints > 0:
                            allAbilities[24].learned = True
                            message('You learned ' + allAbilities[24].name + '.', libtcod.green) 
                            playerSkillPoints = playerSkillPoints - 1
                            return None
                        else:
                            message('You do not have enough skill points to learn ' + allAbilities[24].name + '.', libtcod.orange)
                            return None
                    else:
                        message('You do not know a prerequisite spell to ' + allAbilities[24].name + '.', libtcod.orange)
                        return None    
                else:
                    message('You already know ' + allAbilities[24].name + '.', libtcod.orange)
                    return None 
                  
        if key.vk == libtcod.KEY_ENTER:
            return None
    
    return None    
    
def handleKeys():
    global playerx, playery, key, mouse, fovRecompute
    global prevTime
    global cantAttack
    global allAbilities
    global currentMap
    global stairsToCatacombs1, stairsToCatacombs2, stairsToForest1, stairsToForest2, stairsToForest3, stairsToTundra1, stairsToTundra2, stairsToMines1, stairsToMines2
    global mayor1, mayor2
        
    # Add fullscreen support here?
    
    # key handling
    if mouse.lbutton_pressed:
        if game_state == 'playing':
            player_select_or_attack(mouse.cx, mouse.cy, prevTime)
            if cantAttack == False:
                prevTime = time.time()
                cantAttack = True
    
    if key.vk == libtcod.KEY_ESCAPE:  # exit game
        libtcod.console_clear(None)
        return 'exit'

    else:  # other keys
        key_char = chr(key.c)
        if game_state == 'playing':
            if key.vk == libtcod.KEY_UP:
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassAway
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonAway
                elif currentMap == 'Tundra':
                    player.char = charSnowAway
                elif currentMap == 'Mines':
                    player.char = charMineAway
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'House'):
                    player.char = charHouseAway
                player.move(0, -1)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeAway
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathAway
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathAway
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathAway
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathAway
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathAway
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathAway             
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key.vk == libtcod.KEY_DOWN:
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassTowards
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonTowards
                elif currentMap == 'Tundra':
                    player.char = charSnowTowards
                elif currentMap == 'Mines':
                    player.char = charMineTowards
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'Home'):
                    player.char = charHouseTowards
                player.move(0, 1)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeTowards
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathTowards
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathTowards
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathTowards
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathTowards
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathTowards
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathTowards
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key.vk == libtcod.KEY_LEFT:
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassLeft
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonLeft
                elif currentMap == 'Tundra':
                    player.char = charSnowLeft
                elif currentMap == 'Mines':
                    player.char = charMineLeft
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'Home'):
                    player.char = charHouseLeft
                player.move(-1, 0)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeLeft
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathLeft
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathLeft
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathLeft
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathLeft
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathLeft
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathLeft
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key.vk == libtcod.KEY_RIGHT:
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassRight
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonRight
                elif currentMap == 'Tundra':
                    player.char = charSnowRight
                elif currentMap == 'Mines':
                    player.char = charMineRight
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'Home'):
                    player.char = charHouseRight
                player.move(1, 0)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeRight
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathRight
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathRight
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathRight
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathRight
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathRight
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathRight
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key_char == 'w':
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassAway
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonAway
                elif currentMap == 'Tundra':
                    player.char = charSnowAway
                elif currentMap == 'Mines':
                    player.char = charMineAway
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == "Home"):
                    player.char = charHouseAway
                player.move(0, -1)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeAway
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathAway
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathAway
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathAway
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathAway
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathAway
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathAway
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key_char == 's':
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassTowards
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonTowards
                elif currentMap == 'Tundra':
                    player.char = charSnowTowards
                elif currentMap == 'Mines':
                    player.char = charMineTowards
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'Home'):
                    player.char = charHouseTowards
                player.move(0, 1)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeTowards
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathTowards
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathTowards
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathTowards
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathTowards
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathTowards
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathTowards
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key_char == 'a':
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassLeft
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonLeft
                elif currentMap == 'Tundra':
                    player.char = charSnowLeft
                elif currentMap == 'Mines':
                    player.char = charMineLeft
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'Home'):
                    player.char = charHouseLeft
                player.move(-1, 0)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeLeft
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathLeft
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathLeft
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathLeft
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathLeft
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathLeft
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathLeft
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key_char == 'd':
                if currentMap == 'Town' or currentMap == 'Forest':
                    player.char = charGrassRight
                elif currentMap == 'Catacombs' or currentMap == 'Volcano':
                    player.char = charDungeonRight
                elif currentMap == 'Tundra':
                    player.char = charSnowRight
                elif currentMap == 'Mines':
                    player.char = charMineRight
                elif (currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == "Maybell" or currentMap == 'Home'):
                    player.char = charHouseRight
                player.move(1, 0)
                if currentMap == 'Town':
                    if ((player.x >= 79 and player.x < 84) and (player.y == 40 or player.y == 41)) or ((player.x >= 24 and player.x < 30) and (player.y == 25 or player.y == 26)):
                        player.char = charBridgeRight
                    # Left Path Inside
                    if (player.x == 45 and (player.y >= 1 and player.y < 6)) or (player.y == 5 and (player.x <= 44 and player.x > 26)) or (player.x == 27 and (player.y >= 6 and player.y < 10)) or (player.y == 9 and (player.x <= 26 and player.x > 20)) or (player.x == 21 and (player.y >= 10 and player.y < 14)) or (player.y == 13 and (player.x <= 20 and player.x > 15)) or (player.x == 16 and (player.y == 14 or player.y == 15)) or (player.y == 15 and (player.x <= 15 and player.x > 11)) or (player.x == 12 and (player.y >= 16 and player.y < 21)) or (player.y == 20 and (player.x == 11 or player.x == 10)) or (player.x == 10 and (player.y >= 21 and player.y < 29)) or (player.y == 28 and (player.x >= 11 and player.x < 16)) or (player.x == 15 and (player.y == 29 or player.y == 30)) or (player.y == 30 and (player.x >= 16 and player.x < 21)) or (player.x == 20 and (player.y <= 29 and player.y > 24)) or (player.y == 25 and (player.x >= 21 and player.x < 24)):
                        player.char = charPathRight
                    # Left Path Outside
                    if (player.x == 44 and (player.y >= 1 and player.y <= 5)) or (player.y == 4 and (player.x <= 43 and player.x > 25)) or (player.x == 26 and (player.y >= 5 and player.y < 9)) or (player.y == 8 and (player.x <= 25 and player.x > 19)) or (player.x == 20 and (player.y >= 9 and player.y < 13)) or (player.y == 12 and (player.x <= 19 and player.x > 14)) or (player.x == 15 and (player.y == 13 or player.y == 14)) or (player.y == 14 and (player.x <= 14 and player.x > 11)) or (player.x == 11 and (player.y >= 14 and player.y < 20)) or (player.y == 19 and (player.x == 10 or player.x == 9)) or (player.x == 9 and (player.y >= 20 and player.y < 30)) or (player.y == 29 and (player.x >= 10 and player.x < 15)) or (player.x == 14 and (player.y == 30 or player.y == 31)) or (player.y == 31 and (player.x >= 15 and player.x < 22)) or (player.x == 21 and (player.y <= 30 and player.y > 25)) or (player.y == 26 and (player.x == 22 or player.x == 23)):
                        player.char = charPathRight
                    # Right Bottom Path Inside
                    if (player.x == 74 and (player.y <= 60 and player.y > 56)) or (player.y == 57 and (player.x >= 74 and player.x < 83)) or (player.x == 82 and (player.y <= 57 and player.y > 53)) or (player.y == 53 and (player.x >= 82 and player.x < 94)) or (player.x == 93 and (player.y <= 53 and player.y > 48)) or (player.y == 49 and (player.x >= 93 and player.x < 100)) or (player.x == 99 and (player.y <= 49 and player.y > 44)) or (player.y == 45 and (player.x <= 99 and player.x > 95)) or (player.x == 96 and (player.y <= 45 and player.y > 41)):
                        player.char = charPathRight
                    # Right Bottom Path Outside
                    if (player.x == 97 and (player.y >= 42 and player.y < 45)) or (player.y == 44 and (player.x >= 98 and player.x < 101)) or (player.x == 100 and (player.y >= 45 and player.y < 51)) or (player.y == 50 and (player.x <= 99 and player.x > 94)) or (player.x == 94 and (player.y >= 50 and player.y < 54)) or (player.y == 54 and (player.x <= 94 and player.x > 83)) or (player.x == 83 and (player.y >= 54 and player.y < 58)) or (player.y == 58 and (player.x <= 83 and player.x > 75)) or (player.x == 75 and (player.y <= 60 and player.y > 57)):
                        player.char = charPathRight
                    # Right Top Path Inside
                    if (player.y == 40 and (player.x >= 84 and player.x < 97)) or (player.x == 96 and (player.y <= 39 and player.y > 29)) or (player.y == 30 and (player.x >= 97 and player.x < 102)) or (player.x == 101 and (player.y <= 29 and player.y > 19)) or (player.y == 20 and (player.x <= 101 and player.x > 92)) or (player.x == 93 and (player.y <= 19 and player.y > 10)) or (player.y == 11 and (player.x >= 94 and player.x < 105)) or (player.x == 104 and (player.y <= 10 and player.y > 7)) or (player.y == 8 and (player.x >= 105 and player.x < 111)):
                        player.char = charPathRight
                    # Right Top Path Outside
                    if (player.y == 9 and (player.x <= 110 and player.x > 104)) or (player.x == 105 and (player.y >= 10 and player.y < 13)) or (player.y == 12 and (player.x <= 104 and player.x > 93)) or (player.x == 94 and (player.y >= 13 and player.y < 20)) or (player.y == 19 and (player.x >= 95 and player.x < 103)) or (player.x == 102 and (player.y >= 20 and player.y < 32)) or (player.y == 31 and (player.x <= 101 and player.x > 96)) or (player.x == 97 and (player.y >= 32 and player.y < 42)) or (player.y == 41 and (player.x <= 96 and player.x > 83)):
                        player.char = charPathRight
                fovRecompute = True
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            elif key.vk == libtcod.KEY_1:
                if len(hotbarAbilities) <= 0:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[0].cast()
                return
            elif key.vk == libtcod.KEY_2:
                if len(hotbarAbilities) <= 1:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[1].cast()
                return
            elif key.vk == libtcod.KEY_3:
                if len(hotbarAbilities) <= 2:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[2].cast()
                return
            elif key.vk == libtcod.KEY_4:
                if len(hotbarAbilities) <= 3:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[3].cast()
                return
            elif key.vk == libtcod.KEY_5:
                if len(hotbarAbilities) <= 4:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[4].cast()
                return
            elif key.vk == libtcod.KEY_6:
                if len(hotbarAbilities) <= 5:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[5].cast()
                return
            elif key.vk == libtcod.KEY_7:
                if len(hotbarAbilities) <= 6:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[6].cast()
                return
            elif key.vk == libtcod.KEY_8:
                if len(hotbarAbilities) <= 7:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[7].cast()
                return
            elif key.vk == libtcod.KEY_9:
                if len(hotbarAbilities) <= 8:
                    message("No spell loaded.", libtcod.orange)
                else:
                    hotbarAbilities[8].cast()
                return
            elif key.vk == libtcod.KEY_SPACE:
                skullInInventory = False
                orangeInInventory = False
                
                for item in inventory:
                    if item.name == "Skull":
                        skullInInventory = True
                if (currentMap == 'Town'):
                    if ((stairsToCatacombs1.x == player.x and stairsToCatacombs1.y == player.y) or  #and mayor1
                        (stairsToCatacombs2.x == player.x and stairsToCatacombs2.y == player.y) or #and mayor1
                        (stairsToForest1.x == player.x and stairsToForest1.y == player.y) or  #and mayor2
                        (stairsToForest2.x == player.x and stairsToForest2.y == player.y) or  #and mayor2
                        (stairsToForest3.x == player.x and stairsToForest3.y == player.y) or  #and mayor2
                        (stairsToTundra1.x == player.x and stairsToTundra1.y == player.y) or #and orangeInInventory
                        (stairsToTundra2.x == player.x and stairsToTundra2.y == player.y) or #and orangeInInventory
                        (stairsToMines1.x == player.x and stairsToMines1.y == player.y) or
                        (stairsToMines2.x == player.x and stairsToMines2.y == player.y)):
                            next_level()
                    elif ((stairsToCatacombs1.x == player.x and stairsToCatacombs1.y == player.y and mayor1 == False) or
                          (stairsToCatacombs2.x == player.x and stairsToCatacombs2.y == player.y and mayor1 == False)):
                            message("You are not ready to enter that dungeon.", libtcod.orange)
                    elif ((stairsToForest1.x == player.x and stairsToForest1.y == player.y and mayor2 == False) or
                          (stairsToForest2.x == player.x and stairsToForest2.y == player.y and mayor2 == False) or
                          (stairsToForest3.x == player.x and stairsToForest3.y == player.y and mayor2 == False)):
                            message("You are not ready to enter that dungeon.", libtcod.orange)
                    elif ((stairsToTundra1.x == player.x and stairsToTundra1.y == player.y and orangeInInventory == False) or
                           (stairsToTundra2.x == player.x and stairsToTundra2.y == player.y and orangeInInventory == False)):
                            message("You are not ready to enter that dungeon.", libtcod.orange)
                            
                elif (currentMap == 'Home'):
                    if player.x == 33 and player.y == 17:
                        currentMap = 'Town'
                        dungeonLevel = 0
                        makeMap(allMaps[currentMap, dungeonLevel])
                        player.x = 88
                        player.y = 49
                elif (currentMap == 'Mayor'):
                    if player.x == 34 and player.y == 17:
                        currentMap = 'Town'
                        dungeonLevel = 0
                        makeMap(allMaps[currentMap, dungeonLevel]) 
                        player.x = 9
                        player.y = 13             
                elif (currentMap == 'Louis'):
                    if player.x == 31 and player.y == 17:
                        currentMap = 'Town'
                        dungeonLevel = 0
                        makeMap(allMaps[currentMap, dungeonLevel])
                        player.x = 14
                        player.y = 54
                elif (currentMap == 'Arianna'):
                    if player.x == 34 and player.y == 17:
                        currentMap = 'Town'
                        dungeonLevel = 0
                        makeMap(allMaps[currentMap, dungeonLevel]) 
                        player.x = 88
                        player.y = 16              
                elif (currentMap == 'Maybell'):
                    if player.x == 34 and player.y == 20:
                        currentMap = 'Town'
                        dungeonLevel = 0
                        makeMap(allMaps[currentMap, dungeonLevel])
                        player.x = 39
                        player.y = 10
                else:
                    if stairs.x == player.x and stairs.y == player.y:
                        next_level()
       
def target_monster():
    while True:
        libtcod.console_flush()
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        renderAll()
            
        (x, y) = mouse.cx, mouse.cy
        (x, y) = x + camera_x, y + camera_y
            
        if (mouse.lbutton_pressed and libtcod.map_is_in_fov(fovMap, x, y)):
            target = None
            for object in objects:
                if object.x == x and object.y == y:
                    if object.fighter is not None:
                        target = object
                        break
            return target
        
def target_tile(max_range=None):
    global key, mouse
    while True:
        libtcod.console_flush()
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        renderAll()
        
        (x, y) = (mouse.cx, mouse.cy)
        (x, y) = x + camera_x, y + camera_y
        
        if (mouse.lbutton_pressed and libtcod.map_is_in_fov(fovMap, x, y)):
            return (x, y)

def player_death(player):
    global game_state
    message("You died.", libtcod.red)
    game_state = 'dead'
    
def monster_death(monster):
    global playerExperiencePoints
    if (monster.ai.unstable):
        message('The ' + monster.name + ' explodes!', libtcod.green)
        x, y = monster.x, monster.y
        for obj in objects:
            if monster.distance_to_tile(x, y, obj) <= 3 and obj.fighter and obj != player and obj != monster:
                message('The ' + obj.name + ' takes ' + str(5) + ' explosion damage.', libtcod.green)
                obj.fighter.take_damage(5)
    message(monster.name + ' is dead!', libtcod.green)
    playerExperiencePoints = playerExperiencePoints + monster.fighter.experienceWorth
    if (monster.name == "Flaming Skull"):
        item_component = Item()
        item = Object(monster.x, monster.y, skullFloorTile, 'Skull', libtcod.white, 0, 0, 0, item=item_component, description="An old skull.") 
        message("A " + item.name + ' clatters to the floor.', libtcod.green)
        objects.append(item)
    if (monster.name == "Forest Guardian"):
        item_component = Item()
        item = Object(monster.x, monster.y, orangeGemFloorTile, 'Orange Gem', libtcod.white, 0, 0, 0, item=item_component, description="A sparkling orange gem.") 
        message("An " + item.name + ' clatters to the floor.', libtcod.green)
        objects.append(item)
    if (monster.name == "Hybernating Dragon"):
        item_component = Item()
        item = Object(monster.x, monster.y, purpleGemFloorTile, 'Purple Gem', libtcod.white, 0, 0, 0, item=item_component, description="A sparkling purple gem.") 
        message("A " + item.name + ' clatters to the floor.', libtcod.green)
        objects.append(item)
    if (monster.name == 'Lady Azadlonea'):
        win_game()
    objects.remove(monster)
    
def companion_death(companion):
    message(companion.name + ' is dead!', libtcod.red)
    objects.remove(companion)
    
def cast_heal():
    if player.fighter.hp == player.fighter.max_hp:
        message('You are already at full health!', libtcod.orange)
        return 'cancelled'
    message('Your wounds begin to heal.', libtcod.green)
    player.fighter.heal(healAmount)

def win_game():
    global game_state
    
    libtcod.console_clear(None)
    questMenu("Lady Azadlonea falls before you, and all around the mountain begins to calm.", [], 24)
    questMenu("Amongst slowing lava you escape the volcano, returning to town to tell the mayor that everyone is saved.", [], 24)
    questMenu("Sounds of celebration fill the night, but your favorite amongst them...?                                ", [], 24)
    questMenu(""" "THREE CHEERS FOR THE TOWN'S HERO, REINALD!"                                """, [], 24)
    questMenu("        The End", [], 24)
    game_state = 'win'
    libtcod.console_clear(None)

def save_game():
    global currentMap
    file = shelve.open('savegame', 'n')
    file['dungeon'] = dungeon
    file['objects'] = objects
    file['player_index'] = objects.index(player)
    file['inventory'] = inventory
    file['equipped_list'] = equipped_list
    file['playerLevel'] = playerLevel
    file['playerSkillPoints'] = playerSkillPoints
    file['playerExperiencePoints'] = playerExperiencePoints
    file['experienceMax'] = experienceMax 
    file['allMessages'] = allMessages
    file['game_state'] = game_state
    file['hotbarAbilities'] = hotbarAbilities
    file['allAbilities'] = allAbilities
    file['dungeonLevel'] = dungeonLevel
    file['currentMap'] = currentMap
    file['allStory'] = allStory
    file['logUpdate1'] = logUpdate1
    file['logUpdate2'] = logUpdate2
    file['logUpdate3'] = logUpdate3
    file['logUpdate4'] = logUpdate4
    file['logUpdate5'] = logUpdate5
    file['logUpdate6'] = logUpdate6
    file['logUpdate7'] = logUpdate7
    file['logUpdate8'] = logUpdate8
    file['logUpdate9'] = logUpdate9
    file['logUpdate10'] = logUpdate10
    file['logUpdate11'] = logUpdate11
    file['mayor1'] = mayor1
    file['mayor2'] = mayor2
    file['hero1'] = hero1
    file['hero2'] = hero2
    file['louis1'] = louis1
    file['louis2'] = louis2
    file['maybell1'] = maybell1
    file['maybell2'] = maybell2
    file['mapMade'] = mapMade
    file['songPlaying'] = songPlaying
    
    if currentMap == 'Town':
        file['stairsToCatacombs1_index'] = objects.index(stairsToCatacombs1)
        file['stairsToCatacombs2_index'] = objects.index(stairsToCatacombs2)
        file['stairsToForest1_index'] = objects.index(stairsToForest1)
        file['stairsToForest2_index'] = objects.index(stairsToForest2)
        file['stairsToForest3_index'] = objects.index(stairsToForest3)
        file['stairsToTundra1_index'] = objects.index(stairsToTundra1)
        file['stairsToTundra2_index'] = objects.index(stairsToTundra2)
        file['stairsToMines1_index'] = objects.index(stairsToMines1)
        file['stairsToMines2_index'] = objects.index(stairsToMines2)

    elif currentMap != 'Home' and currentMap != 'Mayor' and currentMap != 'Louis' and currentMap != 'Arianna' and currentMap != 'Maybell':
        file['stairs_index'] = objects.index(stairs)

    file.close()
    
def load_game():
    global dungeon, objects, player, inventory, equipped_list, playerLevel, playerSkillPoints, playerExperiencePoints, experienceMax, allMessages, game_state, hotbarAbilities, allAbilities, stairs, dungeonLevel, currentMap, stairsToCatacombs1, stairsToCatacombs2, stairsToForest1, stairsToForest2, stairsToForest3, stairsToTundra1, stairsToTundra2, stairsToMines1, stairsToMines2, allStory, logUpdate1, logUpdate2, logUpdate3, logUpdate4, logUpdate5, logUpdate6, logUpdate7, logUpdate8, logUpdate9, logUpdate10, logUpdate11, mayor1, mayor2, hero1, hero2, louis1, louis2, maybell1, maybell2, mapMade, songPlaying
    file = shelve.open('savegame', 'r')
    dungeon = file['dungeon']
    objects = file['objects']
    player = objects[file['player_index']]
    inventory = file['inventory']
    equipped_list = file['equipped_list']
    playerLevel = file['playerLevel']
    playerSkillPoints = file['playerSkillPoints']
    playerExperiencePoints = file['playerExperiencePoints']
    experienceMax = file['experienceMax']
    allMessages = file['allMessages']
    game_state = file['game_state']
    hotbarAbilities = file['hotbarAbilities']
    allAbilities = file['allAbilities']
    dungeonLevel = file['dungeonLevel']
    currentMap = file['currentMap']
    allStory = file['allStory']
    logUpdate1 = file['logUpdate1']
    logUpdate2 = file['logUpdate2']
    logUpdate3 = file['logUpdate3']
    logUpdate4 = file['logUpdate4']
    logUpdate5 = file['logUpdate5']
    logUpdate6 = file['logUpdate6']
    logUpdate7 = file['logUpdate7']
    logUpdate8 = file['logUpdate8']
    logUpdate9 = file['logUpdate9']
    logUpdate10 = file['logUpdate10']
    logUpdate11 = file['logUpdate11']
    mayor1 = file['mayor1']
    mayor2 = file['mayor2']
    hero1 = file['hero1']
    hero2 = file['hero2']
    louis1 = file['louis1']
    louis2 = file['louis2']
    maybell1 = file['maybell1']
    maybell2 = file['maybell2']
    mapMade = file['mapMade']
    songPlaying = file['songPlaying']
    
    if currentMap == 'Town':
        stairsToCatacombs1 = objects[file['stairsToCatacombs1_index']]
        stairsToCatacombs2 = objects[file['stairsToCatacombs2_index']]
        stairsToForest1 = objects[file['stairsToForest1_index']]
        stairsToForest2 = objects[file['stairsToForest2_index']]
        stairsToForest3 = objects[file['stairsToForest3_index']]
        stairsToTundra1 = objects[file['stairsToTundra1_index']]
        stairsToTundra2 = objects[file['stairsToTundra2_index']]
        stairsToMines1 = objects[file['stairsToMines1_index']]
        stairsToMines2 = objects[file['stairsToMines2_index']]

    elif currentMap != 'Home' and currentMap != 'Mayor' and currentMap != 'Louis' and currentMap != 'Arianna' and currentMap != 'Maybell':
        stairs = objects[file['stairs_index']]
        
    file.close()
    initializeFOV()
    
def new_game():
    global player, inventory, equipped_list, hotbarAbilities, allMessages, game_state, playerLevel, playerExperiencePoints, playerSkillPoints, experienceMax, allAbilities, dungeonLevel, currentMap, allStory, logUpdate1, logUpdate2, logUpdate3, logUpdate4, logUpdate5, logUpdate6, logUpdate7, logUpdate8, logUpdate9, logUpdate10, logUpdate11, mayor1, mayor2, hero1, hero2, louis1, louis2, maybell1, maybell2, mapMade, songPlaying

    libtcod.console_clear(None)
    
    questMenu("                                    ...zzzz...zzzz...zzzz...                     (Press any key to continue)", [], 24)
    questMenu("      ....rumble.....RUMBLE...                                                               ", [], 24)
    questMenu("      ...BOOOOOOOOOOM!", [], 24)
    questMenu("...what on earth was that...?", [], 24)
    questMenu("It sounded like an explosion...maybe the mayor heard it too...?", [], 24)
    questMenu("...I guess I'll get out of bed, then...           ", [], 24)
    questMenu("(Use arrow keys or WASD to move.)           ", [], 24)
    questMenu("(Click to interact with objects or people.)           ", [], 24)
    questMenu("(Press space when standing on stairs or area entrances to progress.)", [], 24)
    questMenu("(Use keys 1-9 to cast spells added to hotbar.)           ", [], 24) 
    questMenu("(If dungeons become too hard at your current level, try the infinite mine south of your house - 100 randomly generated levels that can be entered again and again!)", [], 24)       
    
    fighter_component = Fighter(hp=100, defense=1, power=4, mana=100, death_function=player_death)
    player = Object(0, 0, charTowards, 'Reinald', libtcod.white, 0, 0, 0, False, blocks=True, fighter=fighter_component)
    
    currentMap = 'Home'
    dungeonLevel = 0
    makeMap(allMaps[currentMap, dungeonLevel])
    player.x = 34
    player.y = 11
    player.char = charHouseTowards
    initializeFOV()
    
    game_state = 'playing'

    # initialize messages
    allMessages = []
    message('Welcome!', libtcod.green)
    
    allStory = []
    story("You have woken up to the sound of an explosion outside your home, and have resolved to learn the source of the sound from the town's mayor. The mayor lives on the other side of the volcano, in the leftmost home.", libtcod.light_green)

    # initialize equipment
    inventory = []
    equipped_list = []

    # initialize abilities
    allAbilities = []
    hotbarAbilities = []

    pyromancer1 = Spell('Firebolt', fire1, 'single-target', 10, 20, 7, True, "Deals 7 damage plus caster level to a single enemy.                                                                ")
    pyromancer2 = Spell('Firestorm', fire2, 'multiple-target', 5, 30, 5, True, "Deals 5 damage plus caster level to all enemies within 5 tiles of the target tile.                                ")
    pyromancer3 = Spell('Everburning', fire3, 'burn', 10, 15, 1, True, "Causes the target to take 1 point of damage every time they attack.                                       ")
    pyromancer4 = Spell('Elemental', fire4, 'companion-elemental', 2, 50, 5, True, "Summons a flame elemental to assist you in battle.                                          ")
    pyromancer5 = Spell('Unstable', fire5, 'unstable', 2, 30, 5, True, "Casting on an enemy causes that enemy to explode when killed, dealing damage to other nearby monsters. ")
    allAbilities.append(pyromancer1)
    allAbilities.append(pyromancer2)
    allAbilities.append(pyromancer3)
    allAbilities.append(pyromancer4)
    allAbilities.append(pyromancer5)

    cryomancer1 = Spell('Frostbolt', ice1, 'single-target', 10, 20, 7, True, "Deals 7 damage plus caster level to a single enemy.                                                                 ")
    cryomancer2 = Spell('Freeze', ice2, 'stun', 2, 30, 5, True, "Freezes an enemy in place for 5 seconds, restricting all movement.                                          ")
    cryomancer3 = Spell('Icicles', ice3, 'power-buff', 2, 40, 5, True, "Increases the caster's power by 5 for 30 seconds.                                                     ")
    cryomancer4 = Spell('Shatter', ice4, 'multiple-target', 5, 25, 5, True, "Deals 5 damage plus caster level to all enemies within 5 tiles of the target tile.                                 ")
    cryomancer5 = Spell('Slippery', ice5, 'slip', 2, 30, 5, True, "Any enemy within the field of view at the moment of casting has its speed reduced by half.                  ")
    allAbilities.append(cryomancer1)
    allAbilities.append(cryomancer2)
    allAbilities.append(cryomancer3)
    allAbilities.append(cryomancer4)
    allAbilities.append(cryomancer5)

    necromancer1 = Spell('Decay', necro1, 'single-target', 10, 20, 7, True, "Deals 7 damage plus caster level to a single enemy.                                                              ")
    necromancer2 = Spell('Rot', necro2, 'burn', 10, 15, 1, True, "Causes the target to take 1 point of damage every time they attack.                                     ")
    necromancer3 = Spell('Undeath', necro3, 'companion-undead', 2, 50, 5, True, "Summons a zombie to assist you in battle.                                                     ")
    necromancer4 = Spell('Desecration', necro4, 'multiple-target', 5, 25, 5, True, "Deals 5 damage plus caster level to all enemies within 5 tiles of the target tile.                              ")
    necromancer5 = Spell('Wail', necro5, 'wail', 2, 30, 5, True, "All enemies freeze in fear for 5 seconds.                                                                ")
    allAbilities.append(necromancer1)
    allAbilities.append(necromancer2)
    allAbilities.append(necromancer3)
    allAbilities.append(necromancer4)
    allAbilities.append(necromancer5)

    psychic1 = Spell('Mindfry', psyc1, 'single-target', 10, 20, 7, True, "Deals 7 damage plus caster level to a single enemy.                                                                   ")
    psychic2 = Spell('Slow', psyc2, 'slow', 2, 25, 5, True, "Reduces target's speed by half.                                                                               ")
    psychic3 = Spell('Confusion', psyc3, 'confuse', 2, 30, 5, True, "Confuses a target for 5 seconds.                                                                           ")
    psychic4 = Spell('Polymorph', psyc4, 'polymorph', 2, 40, 5, True, "Transform target monster into a weaker monster.                                                          ")
    psychic5 = Spell('Teleport', psyc5, 'teleport', 2, 50, 5, True, "Teleports the caster to a selected tile within their field of view.                                       ")
    allAbilities.append(psychic1)
    allAbilities.append(psychic2)
    allAbilities.append(psychic3)
    allAbilities.append(psychic4)
    allAbilities.append(psychic5)

    healer1 = Spell('Lightbolt', heal1, 'single-target', 10, 20, 7, True, "Deals 7 damage plus caster level to a single enemy.                                                                    ")
    healer2 = Spell('Heal', heal2, 'heal', 0, 25, 0, True, "Heals 30 hit points.                                                                                           ")
    healer3 = Spell('Shield', heal3, 'defense-buff', 2, 40, 5, True, "Increases the caster's defense by 5 for 30 seconds.                                                     ")
    healer4 = Spell('Blind', heal4, 'confuse', 2, 30, 5, True, "Disorients a target for 5 seconds.                                                                          ")
    healer5 = Spell('Champion', heal5, 'companion-angel', 2, 50, 5, True, "Summons an angel to assist you in battle.                                                           ")
    allAbilities.append(healer1)
    allAbilities.append(healer2)
    allAbilities.append(healer3)
    allAbilities.append(healer4)
    allAbilities.append(healer5)

    # initialize progression info
    playerLevel = 1
    playerSkillPoints = 0
    playerExperiencePoints = 0
    experienceMax = 100 
    
    logUpdate1 = False
    logUpdate2 = False
    logUpdate3 = False
    logUpdate4 = False
    logUpdate5 = False
    logUpdate6 = False
    logUpdate7 = False
    logUpdate8 = False
    logUpdate9 = False
    logUpdate10 = False
    logUpdate11 = False
    mayor1 = False
    mayor2 = False
    hero1 = False
    hero2 = False
    louis1 = False
    louis2 = False
    maybell1 = False
    maybell2 = False
    
    mapMade = False
    songPlaying = False

def next_level():
    global currentMap, dungeonLevel, stairType
    if (currentMap == 'Town'):
        if (player.x == 45 and player.y == 1) or (player.x == 44 and player.y == 1):
            message("You enter the dungeon...", libtcod.green)
            currentMap = "Catacombs"
            dungeonLevel = 0
            makeMap(allMaps[currentMap, dungeonLevel])
        elif (player.x == 17 and player.y == 60) or (player.x == 18 and player.y == 60) or (player.x == 19 and player.y == 60):
            message("You enter the dungeon...", libtcod.green)
            currentMap = "Forest"
            dungeonLevel = 3
            makeMap(allMaps[currentMap, dungeonLevel])
        elif (player.x == 110 and player.y == 8) or (player.x == 110 and player.y == 9):
            message("You enter the dungeon...", libtcod.green)
            currentMap = "Tundra"
            dungeonLevel = 0
            makeMap(allMaps[currentMap, dungeonLevel])
        elif (player.x == 74 and player.y == 60) or (player.x == 75 and player.y == 60):
            message("You enter the dungeon...", libtcod.green)
            currentMap = "Mines"
            dungeonLevel = 1
            makeRandomMap() 
    elif currentMap == 'Mines':
        message('You descend deeper into the dungeon...', libtcod.green)
        makeRandomMap()
        dungeonLevel = dungeonLevel + 1        
    else:
        if stairs.stairType == 'D':
            message('You descend deeper into the dungeon...', libtcod.green)
            dungeonLevel = dungeonLevel + 1
            makeMap(allMaps[currentMap, dungeonLevel])
        elif stairs.stairType == 'U':
            message('You ascend several flights of stairs to return to town...', libtcod.green)
            dungeonWas = currentMap
            currentMap = 'Town'
            dungeonLevel = 0
            makeMap(allMaps[currentMap, dungeonLevel])
            if dungeonWas == 'Catacombs':
                player.x = 44
                player.y = 1
                player.char = charPathTowards
            elif dungeonWas == 'Forest':
                player.x = 17
                player.y = 60
                player.char = charGrassAway
            elif dungeonWas == 'Tundra':
                player.x = 110
                player.y = 8
                player.char = charPathLeft
            elif dungeonWas == 'Volcano':
                player.x = 54
                player.y = 37
                player.char = charGrassTowards

            
    initializeFOV()
    
def initializeFOV():
    global fovRecompute, fovMap, dungeon
    fovRecompute = True   
    fovMap = libtcod.map_new(len(dungeon), len(dungeon[0]))
    for x in range(len(dungeon)):
        for y in range(len(dungeon[0])):
            libtcod.map_set_properties(fovMap, x, y, not dungeon[x][y].block_sight, not dungeon[x][y].blocked)
    libtcod.console_clear(con)

def play_game():
    global camera_x, camera_y, key, mouse, currentMap, playerLevel, hotbarAbilities, prevTime, manaUse, playerExperiencePoints, experienceMax, cantAttack, allAbilities, playerSkillPoints, mapMade, songPlaying

    # initialize mouse and keys
    mouse = libtcod.Mouse()
    key = libtcod.Key()

    # initialize camera
    (camera_x, camera_y) = (0, 0)

    # initialize attack values
    prevTime = time.time()
    manaUse = int(time.time())
    cantAttack = False

    # main loop
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        renderAll()
        updateLog()
        libtcod.console_flush()
    
        for object in objects:
            object.clear()
        
        if handleKeys() == 'exit':  # escape key pressed
            break
    
        monstersExist = False
        for obj in objects:
            if obj.fighter:
                if obj.fighter.death_function == monster_death:
                    if libtcod.map_is_in_fov(fovMap, obj.x, obj.y):
                        monstersExist = True
                        break
        if monstersExist:
            mapMade = False
            if songPlaying == False:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(combatSong)
                pygame.mixer.music.play(-1)                
                songPlaying = True
        else:
            songPlaying = False
            if mapMade == False:
                if currentMap == 'Catacombs':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(catacombsSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Forest':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(forestSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Tundra':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(tundraSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Volcano':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(volcanoSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Mines':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(minesSong)
                    pygame.mixer.music.play(-1)
                mapMade = True
    
        if game_state == 'playing':
            for object in objects:
                if object.ai:
                    if object.wait > 0:
                        object.wait = object.wait - 1
                    else:
                        object.ai.take_turn()
                    
            if player.fighter.mana < player.fighter.max_mana and int(time.time()) >= manaUse + 1:
                player.fighter.mana = player.fighter.mana + 1
                manaUse = int(time.time())
                
            if player.buff:
                if (int(time.time()) > player.buffStart + 30):
                    if player.buff == "defense":
                        message("Your defense buff expires!", libtcod.orange)
                        player.fighter.defense = player.fighter.defense - 5
                        player.buff = None
                        player.buffStart = None
                    if player.buff == "power":
                        message("Your power buff expires!", libtcod.orange)
                        player.fighter.power = player.fighter.power - 5
                        player.buff = None
                        player.buffStart = None             
            
            if playerExperiencePoints >= experienceMax:
                playerLevel = playerLevel + 1
                message("You leveled up! You are now level " + str(playerLevel) + ". You earned 1 skill point.", libtcod.green)
                playerSkillPoints = playerSkillPoints + 1
                playerExperiencePoints = playerExperiencePoints - experienceMax
                experienceMax = experienceMax + (experienceMax*1.25)
                
                choice = None
                while choice == None:
                    choice = levelUpMenu('Level up! Choose a stat to raise:\n', ['+20 HP', '+10 Mana', '+1 Attack', '+1 Defense'], 40)
                    if choice == 0:
                        player.fighter.max_hp += 20
                        player.fighter.hp = player.fighter.max_hp
                        player.fighter.mana = player.fighter.max_mana                       
                    elif choice == 1:
                        player.fighter.max_mana += 10
                        player.fighter.hp = player.fighter.max_hp
                        player.fighter.mana = player.fighter.max_mana
                    elif choice == 2:
                        player.fighter.power += 1
                        player.fighter.hp = player.fighter.max_hp
                        player.fighter.mana = player.fighter.max_mana
                    elif choice == 3:
                        player.fighter.defense += 1
                        player.fighter.hp = player.fighter.max_hp
                        player.fighter.mana = player.fighter.max_mana
        elif game_state == 'win':
            break
            
                        
def main_menu():
    pygame.mixer.music.load(introSong)
    pygame.mixer.music.play(-1)
    img = libtcod.image_load('menu.png')
    while not libtcod.console_is_window_closed():
        libtcod.image_blit_rect(img, 0, 0, 0, -1, -1, libtcod.BKGND_SET) 
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_print_ex(0, 9, 39, libtcod.BKGND_NONE, libtcod.CENTER,'Code By')
        libtcod.console_print_ex(0, 9, 41, libtcod.BKGND_NONE, libtcod.CENTER,'Branaugh Mackay')
        libtcod.console_print_ex(0, 10, 42, libtcod.BKGND_NONE, libtcod.CENTER,'github.com/Rosewired')
        libtcod.console_print_ex(0, 69, 39, libtcod.BKGND_NONE, libtcod.CENTER,'Art and Music By')
        libtcod.console_print_ex(0, 68, 41, libtcod.BKGND_NONE, libtcod.CENTER,'Justin Mackay')
        libtcod.console_print_ex(0, 68, 42, libtcod.BKGND_NONE, libtcod.CENTER,'justinmackay.weebly.com')                    
        choice = mainMenuGraphic('', ['Continue', 'Save Game', 'Load Last Game', 'New Game', 'Quit'], 18)
        if choice == 0:
            try:
                play_game()
            except:
                mainMenuGraphic('\n No data to load. Press any key to return to the main menu. \n', [], 18)
                continue
        elif choice == 1:
            try:
                save_game()
                message("Game saved!", libtcod.green)
            except:
                mainMenuGraphic('\n No data to save. Press any key to return to the main menu. \n', [], 18)
                continue
            play_game()
        elif choice == 2:
            try:
                load_game()
                if currentMap == 'Town':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(townSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Home' or currentMap == 'Mayor' or currentMap == 'Louis' or currentMap == 'Arianna' or currentMap == 'Maybell':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(houseSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Catacombs':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(catacombsSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Forest':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(forestSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Tundra':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(tundraSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Volcano':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(volcanoSong)
                    pygame.mixer.music.play(-1)
                if currentMap == 'Mines':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(minesSong)
                    pygame.mixer.music.play(-1)
            except:
                mainMenuGraphic('\n No saved game to load. Press any key to return to the main menu. \n', [], 18)
                continue
            play_game()
        elif choice == 3:
            new_game()
            play_game()
        elif choice == 4:
            break
    
# load console
libtcod.console_set_custom_font('FinalTiles.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD, 32, 20)
libtcod.console_init_root(screenWidth, screenHeight, 'Nano-ventures: The Adventure\'s Starting', False)
libtcod.sys_set_fps(limitFPS)
con = libtcod.console_new(screenWidth, screenHeight)
panel = libtcod.console_new(screenWidth, panelHeight)
load_customfont()

main_menu()