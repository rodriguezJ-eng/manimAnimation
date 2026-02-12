from manim import *

class SuperficieBase(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=45 * DEGREES
        )

        self.play(Create(axes))
        self.wait()


class Plano3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70*DEGREES, theta=30*DEGREES)

        plane = Surface(
            lambda u, v: axes.c2p(u, v, u + v),
            u_range=[-3, 3],
            v_range=[-3, 3],
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.7
        )

        self.play(Create(axes))
        self.play(Create(plane))
        self.wait()


class Paraboloide(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)

        paraboloid = Surface(
            lambda u, v: axes.c2p(u, v, u**2 + v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[GREEN_D, GREEN_E]
        )

        self.play(Create(axes))
        self.play(Create(paraboloid))
        self.wait()


class ParaboloideHiperbolico(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70*DEGREES, theta=60*DEGREES)

        saddle = Surface(
            lambda u, v: axes.c2p(u, v, u**2 - v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[RED_D, RED_E]
        )

        self.play(Create(axes))
        self.play(Create(saddle))
        self.wait()


class Esfera3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)

        sphere = Surface(
            lambda u, v: axes.c2p(
                2*np.cos(u)*np.sin(v),
                2*np.sin(u)*np.sin(v),
                2*np.cos(v)
            ),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )

        self.play(Create(axes))
        self.play(Create(sphere))
        self.wait()


class Cilindro3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)

        cylinder = Surface(
            lambda u, v: axes.c2p(
                2*np.cos(u),
                2*np.sin(u),
                v
            ),
            u_range=[0, TAU],
            v_range=[-3, 3],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[PURPLE_D, PURPLE_E]
        )

        self.play(Create(axes))
        self.play(Create(cylinder))
        self.wait()


class Elipsoide3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=65*DEGREES, theta=40*DEGREES)

        ellipsoid = Surface(
            lambda u, v: axes.c2p(
                3*np.cos(u)*np.sin(v),
                2*np.sin(u)*np.sin(v),
                1.5*np.cos(v)
            ),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[TEAL_D, TEAL_E]
        )

        self.play(Create(axes))
        self.play(Create(ellipsoid))
        self.wait()


