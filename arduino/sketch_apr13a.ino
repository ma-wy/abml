// Rosserial Arduino Library - Version: 0.7.9
//run "$ fuser -k /dev/ttyACM0" if device is busy
#include <ros.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Int32.h>

#define TESTPIN 10
#define PUMP 10
#define MAGNET 11
#define NVAL 13
#define POWER 9

ros::NodeHandle node_handle;

std_msgs::Float64 val_value;
std_msgs::Float64 pump_in;
std_msgs::Int32 magnet_in;
std_msgs::Int32 power_in;

int  Valveout=0;
float val=0.0;
int pump_val_out = 0;
int val_pre = 0;
int  t1=20;  //time  step  during  pressure  changing  to  change  the  activation  speed

void pressureup(int val_pre, int pump_val_out)
{
  for(int i=val_pre; i<pump_val_out;i++)
 {   
 Valveout = val_pre + i;
 Serial.print(Valveout); 
 analogWrite(PUMP,Valveout);
 delay (t1);
  } 
}

void pressuredown(int val_pre, int pump_val_out)
{
  for(int i=pump_val_out; i<val_pre;i++)
 {   
 Valveout = val_pre - i;
 Serial.print(Valveout);
 analogWrite(PUMP,Valveout);
  delay (t1);
  } 
}

// input 0-5V
void subscriberCallbackPump(const std_msgs::Float64& pump_in) {
  pump_val_out = int(pump_in.data /5.0 * 256.0);
  if (pump_val_out < val_pre) pressuredown(val_pre, pump_val_out);
  if (pump_val_out > val_pre) pressureup(val_pre, pump_val_out);
  //analogWrite(PUMP, Valveout); // analogRead values go from 0 to 1023, analogWrite values from 0 to 255
  val_pre = pump_val_out;
}

void subscriberCallbackMagnet(const std_msgs::Int32& magnet_in) {
   if (magnet_in.data  == 1) {
    digitalWrite(MAGNET, HIGH); 
  } else {
    digitalWrite(MAGNET, LOW);
  }
}

void subscriberCallbackPower(const std_msgs::Int32& power_in) {
   if (power_in.data  == 1) {
    digitalWrite(POWER, HIGH); 
  } else {
    digitalWrite(POWER, LOW);
  }
}

ros::Publisher val_publisher("val_value", &val_value);
ros::Subscriber<std_msgs::Float64> pump_subscriber("control_pump", &subscriberCallbackPump);
ros::Subscriber<std_msgs::Int32> magnet_subscriber("control_magnet", &subscriberCallbackMagnet);
ros::Subscriber<std_msgs::Int32> power_subscriber("control_power", &subscriberCallbackPower);

// rostopic pub /control_pump std_msgs/Float64 "data: 3.8"
// rostopic pub /control_magnet std_msgs/Int32 "data: 1"
// rostopic pub /control_power std_msgs/Int32 "data: 1"

void setup()
{
  Serial.begin(57600);
  pinMode(POWER, OUTPUT);
  pinMode(PUMP, OUTPUT);
  pinMode(MAGNET, OUTPUT);
  pinMode(NVAL, OUTPUT);
  node_handle.initNode();
  node_handle.advertise(val_publisher);
  node_handle.subscribe(pump_subscriber);
  node_handle.subscribe(magnet_subscriber);
  node_handle.subscribe(power_subscriber);
}

void loop()
{ 
  val = float(analogRead(TESTPIN))/float(1024)*5.0;//float(analogRead(TESTPIN));//
  val_value.data = val;  // read the input pin
//  Serial.println(val);  
  val_publisher.publish(&val_value);
  node_handle.spinOnce();
  
  delay(100);
}
