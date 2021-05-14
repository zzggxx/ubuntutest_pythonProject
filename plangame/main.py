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
            return True;
        else:
            return False;


class EnemyBullet(BaseBullet):

    def __init__(self, x, y, screen):
        super().__init__(screen, "./feiji/bullet-1.gif", x + 30, y + 30)

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 690:
            return True;
        else:
            return False;


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
        # 刷新
        pygame.display.update()
        time.sleep(0.02)


# -------------------------------------------------


if __name__ == "__main__":
    main()
