void mainImage(out vec4 fragColor,in vec2 fragCoord)
{
    vec2 uv=fragCoord/iResolution.xy;
    
    float a=-.5;
    
    //a = (iMouse.x / iResolution.x)*2.0-1.0;
    
    float b=-1.;
    
    //b = (iMouse.y / iResolution.y)*2.0-1.0;
    
    float c=.5;
    
    float dist=a*pow(uv.x,2.)+b*uv.y+c;
    
    if(abs(dist)>.05)
    fragColor=vec4(0,0,0,1.);
}