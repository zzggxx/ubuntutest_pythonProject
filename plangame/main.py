# coding=utf-8
import random

import pygame
import time
from pygame.locals import *  # 键盘检测的


class BasePlane(object):
    def __init__(self, screen, imageName, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        # 加载图片并显示位置
        self.image = pygame.image.load(imageName).convert()
        # 存贮子弹
        self.bulletList = []

    # 更新自己的坐标的时候同时更新子弹的轨迹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            # 删除越界的子弹,不然过一会就会从另一面又跑了出来
            if bullet.judge():
                self.bulletList.remove(bullet)


class HeroPlane(BasePlane):
    def __init__(self, screen):
        imageName = "./feiji/hero.gif"
        # BasePlane.__init__(self, screen, imageName, 230, 500)
        # 注意这里是super()有括号,不用传self
        super().__init__(screen, imageName, 230, 500)

        # 爆炸效果用的如下属性
        self.bomb_list = []  # 用来存储爆炸时需要的图片
        self.__crate_images()  # 调用这个方法向bomb_list中添加图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片

    def __crate_images(self):
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)


class EnemyPlane(BasePlane):

    def __init__(self, screen):
        imageName = "./feiji/enemy-1.gif"
        BasePlane.__init__(self, screen, imageName, 0, 0)
        # super.__init__(self, screen, imageName, 0, 0)
        self.direction = 'right'

    def fire(self):
        rand = random.randint(1, 100)
        if rand == 10 or rand == 70:
            self.bulletList.append(EnemyBullet(self.x, self.y, self.screen))

    def move(self):
        if self.direction == 'right':
            self.x += 5
        elif self.direction == 'left':
            self.x -= 5

        if self.x > 480 - 50:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'


class BaseBullet(object):
    def __init__(self, screen, imageName, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(imageName).convert()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
    def __init__(self, x, y, screen):
        # 注意这里super的写法和别处的不同
        super(Bullet, self).__init__(screen, "./feiji/bullet-3.gif", x + 40, y - 20)

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):

    def __init__(self, x, y, screen):
        super().__init__(screen, "./feiji/bullet-1.gif", x + 30, y + 30)

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 690 - 124:
            return True
        else:
            return False


def main():
    '''
        1. 搭建界面，主要完成窗口和背景图的显示,代码固定,只是画布大小等调整一下即可
    '''
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 690), 0, 32)
    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    # 飞机对象
    heroPlane = HeroPlane(screen)
    enemyPlane = EnemyPlane(screen)

    # 核心:就是画面的快速播放
    while True:
        # 3. 把背景图片放到窗口中显示
        # 设置背景,坐标,坐标和android的一样
        screen.blit(background, (0, 0))

        # 设定需要显示的飞机图片
        heroPlane.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.fire()
        '''
            2. 用来检测事件，比如按键操作
        '''
        # 获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.moveLeft()

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroPlane.moveRight()

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
                    heroPlane.sheBullet()

        # 飞机爆炸,存在的bug
        # for bullet in enemyPlane.bulletList:
        if len(enemyPlane.bulletList) > 0:
            bullet = enemyPlane.bulletList[0]
            # print('--x:%s  y:%s' % (bullet.x, bullet.y))
            if heroPlane.x <= bullet.x <= heroPlane.x + 50 and bullet.y >= heroPlane.y:
                print('boom........................')
                while True:
                    print(heroPlane.image_num)
                    screen.blit(heroPlane.bomb_list[heroPlane.image_num], (heroPlane.x, heroPlane.y))
                    pygame.display.update()
                    time.sleep(0.5)
                    heroPlane.image_num += 1
                    if heroPlane.image_num == 4:
                        exit()  # 调用exit让游戏退出
        # 刷新
        pygame.display.update()
        time.sleep(0.02)


# -------------------------------------------------

if __name__ == "__main__":
    main()
