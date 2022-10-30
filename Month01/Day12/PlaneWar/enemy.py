import pygame
import random
from gameconfig import *


class SmallEnemy(pygame.sprite.Sprite):
    ''' 小型敌机类  '''
    def __init__(self):
        # 调用精灵类的构造方法
        super().__init__()

        # 定义小型飞机的图片对象
        self.image = pygame.image.load('./images/enemy0.png').convert_alpha()
        # 获取小型敌机的尺寸
        self.rect = self.image.get_rect()
        # 设置小型敌机的left --> x轴的值
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        # 设置小型敌机的top --> y轴的值
        self.rect.top = random.randint(-2 * self.image.get_height(), 0)
        # 设置小型敌机的移动速度
        self.speed = 3
        # 定义敌机的存活状态
        self.active = True
        # 定义获取敌机图片的实体
        self.mask = pygame.mask.from_surface(self.image)
        # 定义小型敌机销毁图片
        self.destroy_images = [
            pygame.image.load('./images/enemy0_down1.png').convert_alpha(),
            pygame.image.load('./images/enemy0_down2.png').convert_alpha(),
            pygame.image.load('./images/enemy0_down3.png').convert_alpha(),
            pygame.image.load('./images/enemy0_down4.png').convert_alpha()]

    def move(self):
        '''
            小型敌机移动
        :return: None
        '''
        # 表示小型敌机未超出屏幕之外,则向下移动
        if self.rect.top < SCREEN_HEIGHT:
            self.rect.top += self.speed
        # 判断小型敌机y值超过屏幕高度,则重新设置小型飞机的y值
        else:
            self.reset()

    def reset(self):
        '''
            重置小型敌机
        :return: None
        '''
        self.active = True
        self.rect.top = random.randint(-2 * self.image.get_height(), 0)
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.image.get_width())

    def draw_small_enemy(self, screen):
        '''
            绘制小型敌机
        :return: None
        '''
        screen.blit(self.image, (self.rect.left, self.rect.top))

    @staticmethod
    def add_small_enemy(enemies, small_enemies, count):
        '''
            存储小型敌机对象到精灵组
        :param enemies: 存储所有敌机的精灵组
        :param small_enemies: 存储小型敌机的精灵组
        :param count: int, 数量
        :return: None
        '''
        for i in range(count):  # 循环添加小型敌机对象
            small_enemy = SmallEnemy()  # 小型敌机对象
            enemies.add(small_enemy)  # 添加小型敌机对象到存储所有敌机的精灵组
            small_enemies.add(small_enemy)  # 添加小型敌机对象到存储小型敌机的精灵组

class MiddleEnemy(pygame.sprite.Sprite):
    ''' 中型敌机类  '''
    # 定义中型飞机的生命数
    life = 6

    def __init__(self):
        # 调用精灵类的构造方法
        super().__init__()

        # 定义中型飞机的图片对象
        self.image = pygame.image.load('./images/enemy1.png').convert_alpha()
        # 定义中型飞机被攻击的图片对象
        self.hit_image = pygame.image.load('./images/enemy1_hit.png').convert_alpha()
        # 获取中型敌机的尺寸
        self.rect = self.image.get_rect()
        # 设置中型敌机的left --> x轴的值
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        # 设置中型敌机的top --> y轴的值
        self.rect.top = random.randint(-10 * self.image.get_height(), 0)
        # 设置小型敌机的移动速度
        self.speed = 2
        # 定义敌机的存活状态
        self.active = True
        # 定义获取敌机图片的实体
        self.mask = pygame.mask.from_surface(self.image)
        # 定义中型敌机销毁图片
        self.destroy_images = [
            pygame.image.load('./images/enemy1_down1.png').convert_alpha(),
            pygame.image.load('./images/enemy1_down2.png').convert_alpha(),
            pygame.image.load('./images/enemy1_down3.png').convert_alpha(),
            pygame.image.load('./images/enemy1_down4.png').convert_alpha()]
        # 定义中型敌机的生命值
        self.life = MiddleEnemy.life
        # 定义中型飞机被攻击属性
        self.hit = False

    def move(self):
        '''
            小型敌机移动
        :return: None
        '''
        # 表示小型敌机未超出屏幕之外,则向下移动
        if self.rect.top < SCREEN_HEIGHT:
            self.rect.top += self.speed
        # 判断小型敌机y值超过屏幕高度,则重新设置小型飞机的y值
        else:
            self.reset()

    def reset(self):
        '''
            重置小型敌机
        :return: None
        '''
        self.active = True
        self.life = MiddleEnemy.life   # 重置生命值
        self.rect.top = random.randint(-10 * self.image.get_height(), 0)
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.image.get_width())

    def draw_middle_enemy(self, screen):
        '''
            绘制中型敌机
        :return: None
        '''
        screen.blit(self.image, (self.rect.left, self.rect.top))

    @staticmethod
    def add_middle_enemy(enemies, middle_enemies, count):
        '''
            存储中型敌机对象到精灵组
        :param enemies: 存储所有敌机的精灵组
        :param middle_enemies: 存储中型敌机的精灵组
        :param count: int, 数量
        :return: None
        '''
        for i in range(count):  # 循环添加中型敌机对象
            middle_enemy = MiddleEnemy()  # 中型敌机对象
            enemies.add(middle_enemy)  # 添加中型敌机对象到存储所有敌机的精灵组
            middle_enemies.add(middle_enemy)  # 添加中型敌机对象到存储中型敌机的精灵组

class BigEnemy(pygame.sprite.Sprite):
    ''' 大型敌机类  '''
    # 定义大型飞机的生命数
    life = 12

    def __init__(self):
        # 调用精灵类的构造方法
        super().__init__()
        # 定义大型飞机的图片对象
        self.image = pygame.image.load('./images/enemy2.png').convert_alpha()
        # 定义大型飞机被攻击的图片对象
        self.hit_image = pygame.image.load('./images/enemy2_hit.png').convert_alpha()
        # 获取大型敌机的尺寸
        self.rect = self.image.get_rect()
        # 设置大型敌机的left --> x轴的值
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        # 设置大型敌机的top --> y轴的值
        self.rect.top = random.randint(-15 * self.image.get_height(), 0)
        # 设置大型敌机的移动速度
        self.speed = 1
        # 定义敌机的存活状态
        self.active = True
        # 定义获取敌机图片的实体
        self.mask = pygame.mask.from_surface(self.image)
        # 定义大型敌机销毁图片
        self.destroy_images = [
            pygame.image.load('./images/enemy2_down1.png').convert_alpha(),
            pygame.image.load('./images/enemy2_down2.png').convert_alpha(),
            pygame.image.load('./images/enemy2_down3.png').convert_alpha(),
            pygame.image.load('./images/enemy2_down4.png').convert_alpha(),
            pygame.image.load('./images/enemy2_down5.png').convert_alpha(),
            pygame.image.load('./images/enemy2_down6.png').convert_alpha()]
        # 定义大型敌机的生命值
        self.life = BigEnemy.life
        # 定义大型飞机被攻击属性
        self.hit = False

    def move(self):
        '''
            大型敌机移动
        :return: None
        '''
        # 表示大型敌机未超出屏幕之外,则向下移动
        if self.rect.top < SCREEN_HEIGHT:
            self.rect.top += self.speed
        # 判断大型敌机y值超过屏幕高度,则重新设置大型飞机的y值
        else:
            self.reset()

    def reset(self):
        '''
            重置大型敌机
        :return: None
        '''
        self.active = True
        self.life = BigEnemy.life   # 重置飞机的生命值
        self.rect.top = random.randint(-15 * self.image.get_height(), 0)
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.image.get_width())

    def draw_big_enemy(self, screen):
        '''
            绘制大型敌机
        :return: None
        '''
        screen.blit(self.image, (self.rect.left, self.rect.top))

    @staticmethod
    def add_big_enemy(enemies, big_enemies, count):
        '''
            存储大型敌机对象到精灵组
        :param enemies: 存储所有敌机的精灵组
        :param big_enemies: 存储大型敌机的精灵组
        :param count: int, 数量
        :return: None
        '''
        for i in range(count):  # 循环添加大型敌机对象
            big_enemy = BigEnemy()  # 大型敌机对象
            enemies.add(big_enemy)  # 添加大型敌机对象到存储所有敌机的精灵组
            big_enemies.add(big_enemy)  # 添加大型敌机对象到存储大型敌机的精灵组