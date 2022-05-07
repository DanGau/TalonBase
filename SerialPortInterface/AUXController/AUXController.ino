// Default baud speed for communication
#define BAUD 9600

void setup()
{
  Serial.begin(BAUD);

  // Pins used for input
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

void loop()
{
  // We send more data than what fits in a single byte, 
  // so we send two bytes and a mask to indicate which one.
  // Since we don't have much data to pack, we use the high order
  // bits to determine which set.

  int state = 0x80;
  // Byte 1 - Mask: 0x80
  state |= (digitalRead(2) == HIGH) ? 0x1 : 0;
  state |= (digitalRead(3) == HIGH) ? 0x2 : 0;
  state |= (digitalRead(4) == HIGH) ? 0x4 : 0;
  state |= (digitalRead(5) == HIGH) ? 0x8 : 0;
  state |= (digitalRead(6) == HIGH) ? 0x10 : 0;
  state |= (digitalRead(7) == HIGH) ? 0x20 : 0;
  
  Serial.write(state);

  state = 0x40;
  // Byte 2 - Mask: 0x40
  state |= (digitalRead(8) == HIGH) ? 0x1 : 0;
  state |= (digitalRead(9) == HIGH) ? 0x2 : 0;
  state |= (digitalRead(10) == HIGH) ? 0x4 : 0;
  state |= (digitalRead(11) == HIGH) ? 0x8 : 0;

  Serial.write(state);
}
