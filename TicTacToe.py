import pygame

pygame.init()

screen = pygame.display.set_mode((620, 578))
# pygame.display.set_icon()
imgx = pygame.image.load("images\\img_x.png")
imgo = pygame.image.load("images\\img_o.png")
imgg = pygame.image.load("images\\grid2.png")
imgover = pygame.image.load("images\\game_over1.jpg")
pygame.display.set_caption("TICTACTOE")
win_x = pygame.image.load("images\\win_x.jpg")
win_o = pygame.image.load("images\\win_o.jpg")
win_t = pygame.image.load("images\\win_t.jpg")
Running = True

box1 = pygame.Rect(63,46,155,151)
box2 = pygame.Rect(231,46,155,151)
box3 = pygame.Rect(404,46,155,151)
box4 = pygame.Rect(63,210,155,151)
box5 = pygame.Rect(231,210,155,151)
box6 = pygame.Rect(404,210,155,151)
box7 = pygame.Rect(63,380,155,151)
box8 = pygame.Rect(231,380,155,151)
box9 = pygame.Rect(404,380,155,151)

a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0
x = 2
a_ = False


def wl(a, b, c, d, e, f, g, h, i):
    if a == b == c == 2 or a == b == c == 1:
        return True
    elif d == e == f == 2 or d == e == f == 1:
        return True
    elif g == h == i == 2 or g == h == i == 1:
        return True
    elif a == d == g == 2 or a == d == g == 1:
        return True
    elif b == e == h == 2 or b == e == h == 1:
        return True
    elif c == f == i == 2 or c == f == i == 1:
        return True
    elif a == e == i == 2 or a == e == i == 1:
        return True
    elif c == e == g == 2 or c == e == g == 1:
        return True
    elif x==11:
        return True
    else:
        return False

while Running:

    # screen.fill((255, 0, 0))
    an= wl(a,b,c,d,e,f,g,h,i)
    if not an:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                if box1.collidepoint(pos):
                    if x % 2 == 0 and a == 0:
                        a = 1
                        x += 1
                    if x % 2 != 0 and a == 0:
                        a = 2
                        x += 1

                if box2.collidepoint(pos):
                    if x % 2 == 0 and b == 0:
                        b = 1
                        x += 1

                    if x % 2 != 0 and b == 0:
                        b = 2
                        x += 1

                if box3.collidepoint(pos):
                    if x % 2 == 0 and c == 0:
                        c = 1
                        x += 1

                    if x % 2 != 0 and c == 0:
                        c = 2
                        x += 1
                if box4.collidepoint(pos):
                    if x % 2 == 0 and d == 0:
                        d = 1
                        x += 1

                    if x % 2 != 0 and d == 0:
                        d = 2
                        x += 1

                if box5.collidepoint(pos):
                    if x % 2 == 0 and e == 0:
                        e = 1
                        x += 1

                    if x % 2 != 0 and e == 0:
                        e = 2
                        x += 1

                if box6.collidepoint(pos):
                    if x % 2 == 0 and f == 0:
                        f = 1
                        x += 1

                    if x % 2 != 0 and f == 0:
                        f = 2
                        x += 1

                if box7.collidepoint(pos):
                    if x % 2 == 0 and g == 0:
                        g = 1
                        x += 1

                    if x % 2 != 0 and g == 0:
                        g = 2
                        x += 1

                if box8.collidepoint(pos):
                    if x % 2 == 0 and h == 0:
                        h = 1
                        x += 1

                    if x % 2 != 0 and h == 0:
                        h = 2
                        x += 1

                if box9.collidepoint(pos):
                    if x % 2 == 0 and i == 0:
                        i = 1
                        x += 1

                    if x % 2 != 0 and i == 0:
                        i = 2
                        x += 1

        screen.blit(imgg, (0, 0))
        if a == 1:
            screen.blit(imgx, (63, 46))
        if a == 2:
            screen.blit(imgo, (63, 46))
        if b == 1:
            screen.blit(imgx, (231, 46))
        if b == 2:
            screen.blit(imgo, (231, 46))
        if c == 1:
            screen.blit(imgx, (404, 46))
        if c == 2:
            screen.blit(imgo, (404, 46))
        if d == 1:
            screen.blit(imgx, (63, 210))
        if d == 2:
            screen.blit(imgo, (63, 210))
        if e == 1:
            screen.blit(imgx, (231, 210))
        if e == 2:
            screen.blit(imgo, (231, 210))
        if f == 1:
            screen.blit(imgx, (404, 210))
        if f == 2:
            screen.blit(imgo, (404, 210))
        if g == 1:
            screen.blit(imgx, (63, 380))
        if g == 2:
            screen.blit(imgo, (63, 380))
        if h == 1:
            screen.blit(imgx, (231, 380))
        if h == 2:
            screen.blit(imgo, (231, 380))
        if i == 1:
            screen.blit(imgx, (404, 380))
        if i == 2:
            screen.blit(imgo, (404, 380))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        #pygame.time.delay(100)
        if a == b == c == 2 or d == e == f == 2 or g==h==i==2 or a==d==g== 2 or b==e==h== 2 or c==f==i== 2 or a==e==i==2 or c==e==g==2:
            screen.blit(win_o ,(0,0))
        elif a == b == c == 1 or d == e == f == 1 or g==h==i==1 or a==d==g== 1 or b==e==h== 1 or c==f==i== 1 or a==e==i==1 or c==e==g==1:
            screen.blit(win_x ,(0,0))
        else:
            screen.blit(win_t ,(0,0))
            
    pygame.display.update()
