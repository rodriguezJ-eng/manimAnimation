from manim import *

class DelPlanoAlEspacio(ThreeDScene):
    def construct(self):

        # PARTE 1: SISTEMA 2D (PLANO)

        axes_2d = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )

        labels_2d = axes_2d.get_axis_labels("x", "y")

        punto_2d = Dot(
            axes_2d.c2p(-2, -1),
            color=YELLOW
        )

        coord_2d = MathTex("(x, y)").scale(0.7).next_to(punto_2d, UP)

        self.play(Create(axes_2d), Write(labels_2d))
        self.play(FadeIn(punto_2d), Write(coord_2d))
        self.wait(1)

        # Movimiento suave del punto (refuerza la idea de plano)
        self.play(
            punto_2d.animate.move_to(axes_2d.c2p(2, 1)),
            coord_2d.animate.next_to(punto_2d, UP),
            run_time=3
        )

        self.wait(1)

        # TRANSICIÓN CONCEPTUAL

        self.play(FadeOut(coord_2d), run_time=0.5)
        self.wait(0.5)

        # Inclinamos el plano y cambiamos la cámara
        self.move_camera(
            phi=65 * DEGREES,
            theta=30 * DEGREES,
            run_time=2
        )

        # PARTE 2: SISTEMA 3D (ESPACIO)

        axes_3d = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=4,
        )

        labels_3d = axes_3d.get_axis_labels(
            Tex("x"), Tex("y"), Tex("z")
        )

        self.play(
            Transform(axes_2d, axes_3d),
            Transform(labels_2d, labels_3d),
            run_time=2
        )

        punto_3d = Dot3D(
            axes_3d.c2p(2, 1, 2),
            color=YELLOW
        )

        self.play(Transform(punto_2d, punto_3d))
        self.wait(0.5)

        # Coordenada flotante (siempre de frente)
        coord_3d = always_redraw(
            lambda: MathTex("(x, y, z)")
                .scale(0.7)
                .move_to(punto_3d.get_center() + UP * 0.6)
        )

        self.add(coord_3d)

        # Movimiento del punto en 3D (idea de espacio)
        self.play(
            punto_3d.animate.move_to(axes_3d.c2p(-1, 2, 1)),
            run_time=3
        )

        # Cámara rotando lentamente (sensación espacial)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self.wait(1)
