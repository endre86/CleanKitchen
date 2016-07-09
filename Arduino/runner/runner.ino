/////////////////////////////////////////////////////////////
// Read analog input from a0 - a4 and print as CSV to Serial
//
// a0 - a3 : Kitchen sink sensors
// a4      : Dishwasher sensor
// 
// Output: "millis, a0, a1, a2, a3, a4"
// (millis: https://www.arduino.cc/en/Reference/Millis)
/////////////////////////////////////////////////////////////

int a0;
int a1;
int a2;
int a3;
int a4;

void setup() {
  Serial.begin(9600);
  analogReference(DEFAULT);
}

void loop() {
  // Read analog
  a0 = analogRead(A0);
  a1 = analogRead(A1);
  a2 = analogRead(A2);
  a3 = analogRead(A3);
  a4 = analogRead(A4);

  // Print so serial of any sink sensors registered data
  if(a0 > 0 || a1 > 0 || a2 > 0 || a3 > 0) {
    Serial.println(String(millis()) + "," + String(a0) + "," + String(a1) + "," + String(a2) + "," + String(a3) + "," + String(a4));
  }

  // Delay next read
  delay(50); 
}
