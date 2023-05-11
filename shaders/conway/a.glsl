#define brushSize 1000.0

#define T(i,j) texture(iChannel0, (uv + vec2(i,j)*vec2(1.0/R) )).r 
#define N(i,j)  + float( T(i,j) > 0.)

float rand(float co) { return fract(sin(co*(91.3458)) * 47453.5453); }
float rand(vec2 co){ return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453); }
float rand(vec3 co){ return rand(co.xy+rand(co.z)); }

//noise see https://www.shadertoy.com/view/ltB3zD
float snoise(in vec2 co){
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

// set value for r key to reset with
const int Key_R = 82;

// process keyboard input
bool ReadKey( int key )//, bool toggle )
{
	bool toggle = false;
	float keyVal = texture( iChannel1, vec2( (float(key)+.5)/256.0, toggle?.75:.25 ) ).x;
	return (keyVal>.5)?true:false;
}


void mainImage( out vec4 O, in vec2 c )
{
	vec2 R = iResolution.xy;
    
    // retrieve the texture coordinate
    vec2 uv = c.xy / R;
    
    // get the current pixel
    float v = texture(iChannel0, uv).r;
    
    // check to seee if we are at the start of the timeline or if the R key is pressed.
    if(iFrame > 4 && !ReadKey(Key_R))
    {
        // draw a circle if the mouse is clicked
        if(distance(iMouse.xy, c) < brushSize && iMouse.z > .0)
        {
            if(rand(c*+iTime/1000.0) < 0.5)
                O = vec4(1.0);
            else
                O = vec4(0.0);
        }
        else
        {
            float n =   N(-1,-1) + N(-1, 0) + N(-1, 1)
                      + N( 0,-1)            + N( 0, 1)
                      + N( 1,-1) + N( 1, 0) + N( 1, 1);


            // resurect if we are not live, and have 3 live neighrbours
            v += (1.0-float(v > 0.0)) * float(n == 3.0);

            // kill if we do not have either 3 or 2 neighbours
            v *= float(n == 2.0) + float(n == 3.0);

            // fade the current pixel as it ages
            v -= float(v > 0.4)*0.05;

            // write out the pixel
            O = vec4(vec3(v), 1.0);
        }
    }
    //Generate some noise to get things going
    else
    {
        O = vec4(snoise(c) > 0.8 ? 1.0 : 0.0);
    }
}