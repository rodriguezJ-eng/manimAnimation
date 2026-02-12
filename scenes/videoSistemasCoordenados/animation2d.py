from manim import *

class GraficaLineal(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE}
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        graph = axes.plot(lambda x: 2*x + 1, color=RED)
        graph_label = axes.get_graph_label(graph, label="y = 2x + 1")

        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.play(Write(graph_label))
        self.wait()

class GraficaCuadratica(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 16, 2],
            tips=False
        )

        parabola = axes.plot(lambda x: x**2, color=GREEN)
        label = axes.get_graph_label(parabola, "y = x^2")

        dot = Dot(color=YELLOW)
        dot.move_to(axes.c2p(-3, 9))

        self.play(Create(axes))
        self.play(Create(parabola), Write(label))

        self.play(
            MoveAlongPath(dot, parabola),
            run_time=4
        )

        self.wait()


class ComparacionGraficas(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 4], y_range=[-1, 10])

        g1 = axes.plot(lambda x: x**2, color=BLUE)
        g2 = axes.plot(lambda x: x**2 + 2, color=RED)

        l1 = axes.get_graph_label(g1, "y = x^2")
        l2 = axes.get_graph_label(g2, "y = x^2 + 2")

        self.play(Create(axes))
        self.play(Create(g1), Write(l1))
        self.play(Create(g2), Write(l2))
        self.wait()


class ParametroLineal(Scene):
    def construct(self):
        a = ValueTracker(1)

        axes = Axes(x_range=[-4,4], y_range=[-4,4])

        graph = always_redraw(
            lambda: axes.plot(lambda x: a.get_value()*x, color=PURPLE)
        )

        self.play(Create(axes))
        self.play(Create(graph))
        self.play(a.animate.set_value(3), run_time=3)
        self.play(a.animate.set_value(-2), run_time=3)
        self.wait()
