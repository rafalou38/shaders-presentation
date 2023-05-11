void mainImage(out vec4 fragColor,in vec2 fragCoord)
{
    vec2 uv=fragCoord/iResolution.xy;
    
    float dist=pow(uv.x-.5,2.)+pow(uv.y-.5,2.);
    float radius=.25;
    
    if(dist<pow(radius,2.))
    fragColor=vec4(1,1,1,1.);
    else
    fragColor=vec4(0,0,0,1.);
}