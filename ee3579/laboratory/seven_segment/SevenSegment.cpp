#include <SevenSegment.hpp>

SevenSegment::SevenSegment(int upper_left, int top, int upper_right, int lower_right, int bottom, int lower_left, int center, int flag) {
	int new_segments[8] = {upper_left, top, upper_right, lower_right, bottom, lower_left, center, flag };
	for (int i = 0; i < 8; i++)  {
		segments[i] = new_segments[i];
	}
}

void SevenSegment::set(int value) {
	if (value < 0)
		digitalWrite(segments[SS_FLAG], HIGH);
	else
		digitalWrite(segments[SS_FLAG], LOW);

	value = abs(value);
	for (int i = 0; i < 7; i++) {
		digitalWrite(segments[i], numbers[value][i]);
	}
}
