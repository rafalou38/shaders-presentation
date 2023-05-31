import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import compileShader, compileProgram


def renderFragment(vertex_shader_code):
    # Define the fragment shader code
    fragment_shader_code = """
    void main() {
        gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
    }
    """

    # Create a window and set up OpenGL context
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(512, 512)
    glutCreateWindow("Shader Test")
    glClearColor(0, 0, 0, 1)

    # Compile the shader program
    shader_program = compileProgram(
        compileShader(vertex_shader_code, GL_VERTEX_SHADER),
        compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)
    )

    # Set up a VBO to render a full-screen quad
    quad_vbo = glGenBuffers(1)
    quad_vertices = np.array([
        -1, -1, 0, 0,
        -1, 1, 0, 1,
        1, -1, 1, 0,
        1, 1, 1, 1
    ], dtype=np.float32)
    glBindBuffer(GL_ARRAY_BUFFER, quad_vbo)
    glBufferData(GL_ARRAY_BUFFER, quad_vertices.nbytes,
                 quad_vertices, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)

    # Create a texture to render to
    output_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, output_texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 512, 512,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, None)

    # Set up a framebuffer to render to the texture
    fbo = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, fbo)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
                           GL_TEXTURE_2D, output_texture, 0)

    # Render the full-screen quad using the shader program
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader_program)
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    # Read the output texture data into a NumPy array
    output_data = np.zeros((512, 512, 4), dtype=np.uint8)
    glBindTexture(GL_TEXTURE_2D, output_texture)
    glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA,
                  GL_UNSIGNED_BYTE, output_data.ctypes.data)

    # Clean up resources
    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glDeleteFramebuffers(1, [fbo])
    glDeleteTextures(1, [output_texture])
    glDeleteBuffers(1, [quad_vbo])

    # Print the output data
    return (output_data)


vertex_shader_code = """

void main()
{
    // Compute the distance from the current pixel to the center of the circle
    float distance = length(gl_FragCoord.xy - vec2(200.0, 200.0));

    // Check if the distance is less than the radius of the circle
    if (distance <= 100.0)
    {
        // If the distance is less than the radius, set the pixel color to red
        frag_color = vec4(1.0, 0.0, 0.0, 1.0);
    }
    else
    {
        // If the distance is greater than the radius, set the pixel color to transparent
        frag_color = vec4(0.0, 0.0, 0.0, 0.0);
    }
}
"""

print(renderFragment(vertex_shader_code))
