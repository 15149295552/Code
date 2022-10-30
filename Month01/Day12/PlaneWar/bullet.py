import pygame
from gameconfig import *
from enemy import MiddleEnemy, BigEnemy

class Bullet1(pygame.sprite.Sprite):
    '''  单发子弹类  '''
    # 存储子弹对象
    bullet1 = []
    # 子弹索引值
    bullet1_index = 0
    # 子弹数量
    bullet1_number = 15

    def __init__(self, hero):
        # 调用精灵类构造方法
        super().__init__()
        # 设置子弹图片对象
        self.image = pygame.image.load('./images/bullet1.png').convert_alpha()
        # 获取子弹图片对象的尺寸
        self.rect = self.image.get_rect()
        # 定义子弹的左/上的位置
        self.rect.left = hero.rect.midtop[0]-2
        self.rect.top = hero.rect.midtop[1]
        # 定义子弹存活
        self.active = True
        # 定义获取子弹图片的实体
        self.mask = pygame.mask.from_surface(self.image)
        # 定义子弹的移动速度
        self.speed = 5

    def move(self):
        '''
            单发子弹移动
        :return: None
        '''
        # 若子弹未达到窗口的上边缘,则y值减小
        if self.rect.top > 0:
            self.rect.top -= self.speed
        # 否则,重置子弹的存活
        else:
            self.active = False    # 子弹销毁

    def reset(self, hero):
        '''
            重置子弹
        :return: None
        '''
        # 飞机存活绘制到飞机的中心的位置(飞机的x, 飞机的y)
        self.active = True
        self.rect.left = hero.rect.midtop[0]-2
        self.rect.top = hero.rect.midtop[1]

    @classmethod
    def add_bullet1(cls, hero):
        '''
            添加子弹
        :return: None
        '''
        # 循环添加子弹对象到子弹列表中
        for i in range(cls.bullet1_number):
            cls.bullet1.append(Bullet1(hero))

    @classmethod
    def draw_bullet1(cls, hero, screen, delay, enemies, middle_enemies, big_enemies):
        # 设置子弹发射的频率
        if not (delay % 10):
            # 子弹重置
            cls.bullet1[cls.bullet1_index].reset(hero)
            # 获取下一个子弹的索引值
            cls.bullet1_index = (cls.bullet1_index + 1) % cls.bullet1_number

        # 循环绘制子弹对象
        for bullet1 in Bullet1.bullet1:
            # 判断子弹存活
            if bullet1.active:
                # 子弹移动
                bullet1.move()
                # 绘制子弹
                screen.blit(bullet1.image, bullet1.rect)
                # 判断子弹是否与敌机发射碰撞
                enemy_hit = pygame.sprite.spritecollide(bullet1,
                                                        enemies,
                                                        False,
                                                        pygame.sprite.collide_mask)
                # 表示存在有碰撞的敌机对象
                if enemy_hit:
                    bullet1.active = False    # 子弹销毁
                    # 循环遍历被碰撞的敌机对象,设置存活属性为False
                    for e in enemy_hit:
                        # 表示是中型敌机对象或大型敌机对象, 生命值减一,当为0时,则设置存活属性为False
                        if e in middle_enemies or e in big_enemies:
                            e.life -= 1
                            e.hit = True
                            if e.life == 0:
                                e.active = False
                                e.hit = False
                        else:  # 表示小型机中弹,则直接设置存活属性为False
                            e.active = False

class Bullet2(pygame.sprite.Sprite):
    '''  双发子弹类  '''
    # 存储子弹对象
    bullet2 = []
    # 子弹索引值
    bullet2_index = 0
    # 子弹数量
    bullet2_number = 30

    def __init__(self, postion):
        # 调用精灵类构造方法
        super().__init__()
        # 设置子弹图片对象
        self.image = pygame.image.load('./images/bullet2.png').convert_alpha()
        # 获取子弹图片对象的尺寸
        self.rect = self.image.get_rect()
        # 定义子弹的左/上的位置
        self.rect.left = postion[0]
        self.rect.top = postion[1]
        # 定义子弹存活
        self.active = True
        # 定义获取子弹图片的实体
        self.mask = pygame.mask.from_surface(self.image)
        # 定义子弹的移动速度
        self.speed = 5

    def move(self):
        '''
            双发子弹移动
        :return: None
        '''
        # 若子弹未达到窗口的上边缘,则y值减小
        if self.rect.top > 0:
            self.rect.top -= self.speed
        # 否则,重置子弹的存活
        else:
            self.active = False    # 子弹销毁

    def reset(self, postion):
        '''
            重置子弹
        :return: None
        '''
        # 飞机存活绘制到飞机的中心的位置(飞机的x, 飞机的y)
        self.active = True
        self.rect.left = postion[0]
        self.rect.top = postion[1]

    @classmethod
    def add_bullet2(cls, hero):
        '''
            添加子弹
        :return: None
        '''
        # 循环添加子弹对象到子弹列表中
        for i in range(cls.bullet2_number // 2):
            cls.bullet2.append(Bullet2((hero.rect.centerx - 33, hero.rect.centery)))
            cls.bullet2.append(Bullet2((hero.rect.centerx + 30, hero.rect.centery)))

    @classmethod
    def draw_bullet2(cls, hero, screen, delay, enemies, middle_enemies, big_enemies):
        # 设置子弹发射的频率
        if not (delay % 10):
            # 子弹重置
            cls.bullet2[cls.bullet2_index].reset((hero.rect.centerx - 33, hero.rect.centery))
            cls.bullet2[cls.bullet2_index+1].reset((hero.rect.centerx + 30, hero.rect.centery))
            # 获取下一个子弹的索引值
            cls.bullet2_index = (cls.bullet2_index + 2) % cls.bullet2_number

        # 循环绘制子弹对象
        for bullet2 in Bullet2.bullet2:
            # 判断子弹存活
            if bullet2.active:
                # 子弹移动
                bullet2.move()
                # 绘制子弹
                screen.blit(bullet2.image, bullet2.rect)
                # 判断子弹是否与敌机发射碰撞
                enemy_hit = pygame.sprite.spritecollide(bullet2,
                                                        enemies,
                                                        False,
                                                        pygame.sprite.collide_mask)
                # 表示存在有碰撞的敌机对象
                if enemy_hit:
                    bullet2.active = False    # 子弹销毁
                    # 循环遍历被碰撞的敌机对象,设置存活属性为False
                    for e in enemy_hit:
                        # 表示是中型敌机对象或大型敌机对象, 生命值减一,当为0时,则设置存活属性为False
                        if e in middle_enemies or e in big_enemies:
                            e.life -= 1
                            e.hit = True
                            if e.life == 0:
                                e.active = False
                                e.hit = False
                        else:  # 表示小型机中弹,则直接设置存活属性为False
                            e.active = False