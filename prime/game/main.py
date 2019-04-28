import argparse
import numpy as np
import sys
import time
import moderngl

from importlib import import_module
from pathlib import Path
from typing import List

from prime.engine.renderer.window import Window

class InstancedRendering:

    def __init__(self, ctx, **kwargs):
        self.ctx = ctx
        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330

                in vec2 in_vert;
                in vec4 in_color;

                out vec4 v_color;

                uniform float Rotation;
                uniform vec2 Scale;

                void main() {
                    v_color = in_color;
                    float r = Rotation * (0.5 + gl_InstanceID * 0.05);
                    mat2 rot = mat2(cos(r), sin(r), -sin(r), cos(r));
                    gl_Position = vec4((rot * in_vert) * Scale, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330

                in vec4 v_color;
                out vec4 f_color;

                void main() {
                    f_color = v_color;
                }
            ''',
        )

        self.scale = self.prog['Scale']
        self.rotation = self.prog['Rotation']

        vertices = np.array([
            # x, y, red, green, blue, alpha
            1.0, 0.0, 1.0, 0.0, 0.0, 0.5,
            -0.5, 0.86, 0.0, 1.0, 0.0, 0.5,
            -0.5, -0.86, 0.0, 0.0, 1.0, 0.5,
        ])

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self, time, frame_time):
        width, height = self.wnd.size

        self.ctx.clear(1.0, 1.0, 1.0)
        self.ctx.enable(moderngl.BLEND)
        self.scale.value = (0.5, self.aspect_ratio * 0.5)
        self.rotation.value = time
        self.vao.render(instances=10)


def run(args=None):
    window = Window(title="Prime")

    start_time = time.time()
    current_time = start_time
    prev_time = start_time
    frame_time = 0
    instancer = InstancedRendering(window.ctx)
    instancer.wnd = window
    instancer.aspect_ratio = window.aspect_ratio

    while not window.is_closing:
        current_time, prev_time = time.time(), current_time
        frame_time = max(current_time - prev_time, 1 / 1000)

        window.render(current_time - start_time, frame_time)
        instancer.render(current_time - start_time, frame_time)
        window.swap_buffers()

    duration = time.time() - start_time
    window.destroy()
    print("Duration: {0:.2f}s @ {1:.2f} FPS".format(duration, window.frames / duration))


if __name__ == '__main__':
    run(sys.argv)
