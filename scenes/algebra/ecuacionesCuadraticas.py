from manim import *

class IntroCuadratica(Scene):
    def construct(self):
        titulo = Title("Ecuaciones Cuadráticas")
        self.play(Write(titulo))

        ecuacion = MathTex(
            "a", "x^2", "+", "b", "x", "+", "c", "=", "0"
        ).scale(1.3)

        ecuacion.set_color_by_tex("a", BLUE)
        ecuacion.set_color_by_tex("b", GREEN)
        ecuacion.set_color_by_tex("c", RED)

        self.play(Write(ecuacion))
        self.wait(2)

        descripcion = Tex(
            "Forma general de una ecuación cuadrática"
        ).next_to(ecuacion, DOWN)

        self.play(FadeIn(descripcion))
        self.wait(2)

class MetodoCompletacion(Scene):
    def construct(self):
        titulo = Title("Completación de Cuadrados")
        self.play(Write(titulo))

        eq = MathTex("x^2 + 6x + 5 = 0")
        self.play(Write(eq))
        self.wait()

        pasos = [
            MathTex("x^2 + 6x = -5"),
            MathTex("x^2 + 6x + 9 = 4"),
            MathTex("(x + 3)^2 = 4"),
            MathTex("x = -1, -5")
        ]

        for paso in pasos:
            self.play(ReplacementTransform(eq, paso))
            eq = paso
            self.wait(1.5)

        self.wait(2)


class MetodoFactorizacion(Scene):
    def construct(self):
        titulo = Title("Factorización")
        self.play(Write(titulo))

        eq = MathTex("x^2 + 5x + 6 = 0")
        self.play(Write(eq))
        self.wait()

        factorizado = MathTex("(x + 2)(x + 3) = 0")
        soluciones = MathTex("x = -2, -3")

        self.play(ReplacementTransform(eq, factorizado))
        self.wait(1.5)

        self.play(ReplacementTransform(factorizado, soluciones))
        self.wait(2)

class FormulaGeneral(Scene):
    def construct(self):
        titulo = Title("Fórmula General")
        self.play(Write(titulo))

        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
        ).scale(1.2)

        self.play(Write(formula))
        self.wait(2)

        ejemplo = MathTex("x^2 + 2x - 8 = 0")
        ejemplo.next_to(formula, DOWN)

        self.play(Write(ejemplo))
        self.wait(2)

        resultado = MathTex(
            r"x = \frac{-2 \pm 6}{2} \Rightarrow x = 2, -4"
        ).next_to(ejemplo, DOWN)

        self.play(Write(resultado))
        self.wait(3)


class GraficaCuadratica(Scene):
    def construct(self):
        titulo = Title("Gráfica de una Función Cuadrática")
        self.play(Write(titulo))

        axes = Axes(
            x_range=[-2, 6, 1],
            y_range=[-5, 10, 1],
            axis_config={"include_numbers": True}
        )

        parabola = axes.plot(
            lambda x: x**2 - 4*x + 3,
            color=BLUE
        )

        self.play(Create(axes))
        self.play(Create(parabola))
        self.wait(3)

class Discriminante(Scene):
    def construct(self):
        titulo = Title("Discriminante Dinámico")
        self.play(Write(titulo))

        a = ValueTracker(1)
        b = ValueTracker(2)
        c = ValueTracker(-3)

        discriminante = always_redraw(
            lambda: MathTex(
                r"\Delta = b^2 - 4ac =",
                f"{b.get_value()**2 - 4*a.get_value()*c.get_value():.1f}"
            ).next_to(titulo, DOWN)
        )

        self.play(Write(discriminante))
        self.wait(2)

        self.play(b.animate.set_value(5), run_time=2)
        self.wait(2)

        self.play(c.animate.set_value(2), run_time=2)
        self.wait(3)
