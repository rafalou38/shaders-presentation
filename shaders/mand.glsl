#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif

#define cx_mul(a,b)mat2(a,-a.y,a.x)*b

void mainImage(out vec4 fragColor,in vec2 fragCoord){
  vec2 uv=fragCoord/iResolution.xy;
  vec2 z=2.*(fragCoord-.5*iResolution.xy)/iResolution.y;
  vec2 c=.36+.02*vec2(sin(.35*iTime),
  cos(.13*iTime));
  for(int i=0;i<100;i++){
    z=cx_mul(z,z)+c;
  }
  
  vec3 col=vec3(length(z));
  fragColor=vec4(col,1.);
}