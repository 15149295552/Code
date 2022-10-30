import pygame
import random
from gameconfig import *

class Bullet_Supply(pygame.sprite.Sprite):
    '''  超级子弹补给包类  '''
    def __init__(self):
        super().__init__()
        # 定义超级子弹图片对象
        self.image = pygame.image.load('./images/bomb-1.gif').convert_alpha()
        # 获取超级子弹图片对象尺寸
        self.rect = self.image.get_rect()
        # 定义超级子弹图片对象的位置
        self.rect.left = random.randint(0, SCREEN_WIDTH-self.rect.width)
        self.rect.top = -100
        # 定义超级子弹图片对象的移动速度
        self.speed = 5
        # 定义超级子弹图片对象存活属性
        self.active = False
        # 定义获取超级子弹图片对象的实体部分
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        ''' 超级子弹移动 '''
        self.rect.top += self.speed

        # 判断超级子弹补给包是否超出屏幕外
        if self.rect.top >= SCREEN_HEIGHT:
            self.active = False

    def reset(self):
        ''' 重置超级子弹  '''
        self.active = True
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.top = -100

class Bomb_Supply(pygame.sprite.Sprite):
    '''  超级炸弹补给包类  '''
    # 定义超级炸弹的数量
    bobm_number = 3

    def __init__(self):
        super().__init__()
        # 定义超级炸弹图片对象
        self.image = pygame.image.load('./images/bomb-2.gif').convert_alpha()
        # 获取超级炸弹图片对象尺寸
        self.rect = self.image.get_rect()
        # 定义超级炸弹图片对象的位置
        self.rect.left = random.randint(0, SCREEN_WIDTH-self.rect.width)
        self.rect.top = -100
        # 定义超级炸弹图片对象的移动速度
        self.speed = 5
        # 定义超级炸弹图片对象存活属性
        self.active = False
        # 定义获取超级炸弹图片对象的实体部分
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        ''' 超级炸弹移动 '''
        self.rect.top += self.speed

        # 判断超级炸弹补给包是否超出屏幕外
        if self.rect.top >= SCREEN_HEIGHT:
            self.active = False

    def reset(self):
        ''' 重置超级炸弹  '''
        self.active = True
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.top = -100

    @classmethod
    def show_bomb_info(cls, images, screen, font_type):
        ''' 显示超级炸弹的图片及数量(窗口左下角) '''
        # 绘制超级炸弹的图片对象
        screen.blit(images, (10, SCREEN_HEIGHT-images.get_height()-5))
        # 绘制超级炸弹的数量
        text = font_type.render(' x %d' % cls.bobm_number, True, WHITE)
        screen.blit(text, (10 + images.get_width(), SCREEN_HEIGHT-50))