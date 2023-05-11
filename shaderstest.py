import OpenGL.GL as gl

# Define the shader source code
shader_source = '''
    #version 330 core
    out vec4 frag_color;
    void main()
    {
        frag_color = vec4(1.0, 0.0, 0.0, 1.0);
    }
'''

# Create a shader program
shader_program = gl.glCreateProgram()

# Create a fragment shader object
fragment_shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)

# Set the shader source code
gl.glShaderSource(fragment_shader, shader_source)

# Compile the shader
gl.glCompileShader(fragment_shader)

# Attach the shader to the program
gl.glAttachShader(shader_program, fragment_shader)

# Link the program
gl.glLinkProgram(shader_program)

# Use the program
gl.glUseProgram(shader_program)
