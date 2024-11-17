#include <ros.h>
#include <std_msgs/Int64.h>
#define  Valve1pin 9 //output pin in Arduino,  connected to the white wire of valve

int Valveout=0;
int Base_valve=0;
int t1=20; //time step during pressure changing to change the activation speed
int A;
int global_value;

void messageCb( const std_msgs::Int64 &value_msg)
{
  global_value=value_msg.data;
}

ros::NodeHandle nh;  
ros::Subscriber<std_msgs::Int64> sub("value_topic",&messageCb);

void setup() {
  Serial.begin(57600) ;
  pinMode(Valve1pin, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

  
void pressureup()
{Base_valve =0;
  for(int i=0; i<250;i++)
 {   
 Valveout = Valveout +1;
 Serial.println(Valveout);
 analogWrite(Valve1pin,Valveout);
 delay (t1);
  } 
}
void pressuredown()
{
  for(int i=0; i<250;i++)
 {   
 Valveout = Valveout - 1;
 Serial.println(Valveout);
 analogWrite(Valve1pin,Valveout);
  delay (t1);
  } 
}

void loop() 
{ 
  if (global_value>0)   pressureup();
  if (global_value<0)   pressuredown();
  nh.spinOnce();
}
