import pygame

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees - Rainer Tamm")

tootab = True
while tootab:
    for syndmus in pygame.event.get():
        if syndmus.type == pygame.QUIT:
            tootab = False

    aken.fill((0, 0, 0))# Teeme tausta mustaks

    # Joonistame lumemehe 3 ringi (värv: valge, koordinaadid, suurus)
    pygame.draw.circle(aken, (255, 255, 255), (150, 230), 60)
    pygame.draw.circle(aken, (255, 255, 255), (150, 140), 45)
    pygame.draw.circle(aken, (255, 255, 255), (150, 70), 35)

    # Silmad (väikesed mustad ringid)
    pygame.draw.circle(aken, (0, 0, 0), (135, 65), 5)
    pygame.draw.circle(aken, (0, 0, 0), (165, 65), 5)

    # Nina (punane kolmnurk)
    pygame.draw.polygon(aken, (255, 0, 0), [(145, 70), (155, 70), (150, 85)])

    pygame.display.flip()

pygame.quit()