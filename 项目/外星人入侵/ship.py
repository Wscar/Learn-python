import  pygame


class Ship():

    def __init__(self, ai_setting, screen):
        """初始化飞船并设置飞船的位置"""
        self.screen = screen
        self.ai_setting = ai_setting
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        # 将每艘新飞创放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            # 更新 center的值
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left:
            self.center -=self.ai_setting.ship_speed_factor

