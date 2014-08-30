#include <wiringPi.h>

int main(void){
	//modulu aktifleştir
	wiringPiSetup();
	//4 numarayi out yap
	pinMode(4, OUTPUT);

	//sonsuz döngü
	for(;;){
		digitalWrite(4, HIGH);
		delay(500);
		digitalWrite(4, LOW);
		delay(500);
	}
	return 0;
}

