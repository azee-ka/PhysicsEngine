# core/rendering/shaders.py
import OpenGL.GL as gl
import numpy as np

class Shader:
    def __init__(self, vertex_shader_source, fragment_shader_source):
        self.program = gl.glCreateProgram()

        vertex_shader = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        gl.glShaderSource(vertex_shader, vertex_shader_source)
        gl.glCompileShader(vertex_shader)
        gl.glAttachShader(self.program, vertex_shader)

        fragment_shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(fragment_shader, fragment_shader_source)
        gl.glCompileShader(fragment_shader)
        gl.glAttachShader(self.program, fragment_shader)

        gl.glLinkProgram(self.program)

    def use(self):
        """Use the shader program for rendering."""
        gl.glUseProgram(self.program)

    def set_uniform(self, name, value):
        """Set a uniform value in the shader."""
        # Implementation of setting a uniform value
        pass