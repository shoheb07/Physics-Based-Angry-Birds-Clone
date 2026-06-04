import pygame
import pymunk

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Physics Angry Birds Clone"
)

clock = pygame.time.Clock()

# Physics Space
space = pymunk.Space()
space.gravity = (0, 900)

# Ground
ground = pymunk.Segment(
    space.static_body,
    (0, HEIGHT - 50),
    (WIDTH, HEIGHT - 50),
    5
)

ground.friction = 1.0

space.add(ground)

# Bird
mass = 1
radius = 20

moment = pymunk.moment_for_circle(
    mass,
    0,
    radius
)

bird_body = pymunk.Body(
    mass,
    moment
)

bird_body.position = (150, 450)

bird_shape = pymunk.Circle(
    bird_body,
    radius
)

bird_shape.elasticity = 0.7

space.add(
    bird_body,
    bird_shape
)

# Target Box
box_body = pymunk.Body(
    5,
    pymunk.moment_for_box(
        5,
        (60, 60)
    )
)

box_body.position = (800, 450)

box_shape = pymunk.Poly.create_box(
    box_body,
    (60, 60)
)

space.add(
    box_body,
    box_shape
)

launched = False

running = True

while running:

    screen.fill((200, 230, 255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if not launched:

                    bird_body.apply_impulse_at_local_point(
                        (12000, -5000)
                    )

                    launched = True

    # Physics Update
    space.step(1/60)

    # Draw Ground
    pygame.draw.line(
        screen,
        (0,0,0),
        (0, HEIGHT - 50),
        (WIDTH, HEIGHT - 50),
        5
    )

    # Draw Bird
    bx, by = bird_body.position

    pygame.draw.circle(
        screen,
        (255,0,0),
        (int(bx), int(by)),
        radius
    )

    # Draw Box
    x, y = box_body.position

    pygame.draw.rect(
        screen,
        (0,255,0),
        (
            int(x-30),
            int(y-30),
            60,
            60
        )
    )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
