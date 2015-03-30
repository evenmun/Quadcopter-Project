
import time;


input = 0
output =0
setpoint = 1
errSum = 0
lastErr = 0;
Kp = 0
Ki = 0
Kd = 0;

lastTime = 0;

def Compute():

    global lastTime,errSum,setpoint,input, output,Kp, Ki, Kd,lastErr;

    #How long since we last calculated
    nowTime = time.time()*1000.0;
    timeChange = (nowTime - lastTime);

    #Compute All the working error variables
    error = (setpoint - input);
    errNewSum =  (error * timeChange);
    #Integral
    errSum += errNewSum;
    #Derivat
    dErr = (error - lastErr) / timeChange;

    #Compute PID Output
    output = Kp*error + Ki*errSum + Kd*dErr;

    #Remember some variables for next time
    lastTime = nowTime;
    lastErr = error;

    return output;

def setTunings(_Kp, _Ki, _Kd):
    global Kp ,Ki, Kd ;
    Kp = _Kp;
    Ki = _Ki;
    Kd = _Kd;



setTunings(1,2,3);

for i in range(20):
    print Compute();
    time.sleep(1);