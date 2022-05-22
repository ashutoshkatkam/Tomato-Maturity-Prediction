#include "ESP_MICRO.h" //Include the micro library 
String testvariable = "None";
void setup(){
  Serial.begin(9600); // Starting serial port for seeing details
  start("Katkam-2.4G","6302962174");  // EnAIt will connect to your wifi with given details
}
void loop(){
  waitUntilNewReq();  //Waits until a new request from python come
  /* increases index when a new request came*/
  testvariable = "abc 10,30,20";
  returnThisStr(testvariable); //Returns the data to python
}
