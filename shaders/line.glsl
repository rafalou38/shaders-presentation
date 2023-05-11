void mainImage(out vec4 fragColor,in vec2 fragCoord)
{
    vec2 uv=fragCoord/iResolution.xy;
    
    float a=-.5;
    float b=-1.;
    float c=.5;
    
    float dist=a*uv.x+b*uv.y+c;
    
    if(abs(dist)>.05)
    fragColor=vec4(0,0,0,1.);
}