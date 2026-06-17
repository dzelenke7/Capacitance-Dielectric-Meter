const long R1 = 100000;
const long R2 = 750000;
float e0 = 8.85e-12;
float A = 0.01032;
float d = 0.001;

void setup() 
{
  Serial.begin(9600);
  pinMode(2, INPUT);

}

void loop() 
{
  //Serial.println("--- New Reading ---");
 float highTime = pulseIn(2, HIGH, 100000);
 float lowTime = pulseIn(2, LOW, 100000);

 if(highTime == 0 || lowTime == 0){
  Serial.println(0);
  Serial.println(0);
  Serial.println(0);
  delay(500);
  return;
}
  float period = highTime + lowTime;
  float frequency = 1000000.0/period;
  

  float Capacitance = 1.44/((R1 + 2*R2)*frequency);
  float DielectricC = Capacitance/(e0*(A/d));

  Serial.println(frequency);
  Serial.println(Capacitance, 12);
  Serial.println(DielectricC);
  
  delay(500);
}
