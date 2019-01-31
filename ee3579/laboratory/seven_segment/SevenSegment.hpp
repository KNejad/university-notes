#ifndef SEVEN_SEGMENT
#define SEVEN_SEGMENT

#include <Arduino.h>

#define SS_UPPER_LEFT  0
#define SS_TOP  1
#define SS_UPPER_RIGHT  2
#define SS_LOWER_RIGHT  3
#define SS_BOTTOM  4
#define SS_LOWER_LEFT  5
#define SS_CENTER  6
#define SS_FLAG  7

class SevenSegment {
	private:
		int segments[8];

		bool numbers[10][7] = {
			{HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW},
			{LOW, LOW, HIGH, HIGH, LOW, LOW, LOW},
			{LOW, HIGH, HIGH, LOW, HIGH, HIGH, HIGH},
			{LOW, HIGH, HIGH, HIGH, HIGH, LOW, HIGH},
			{HIGH, LOW, HIGH, HIGH, LOW, LOW, HIGH},
			{HIGH, HIGH, LOW, HIGH, HIGH, LOW, HIGH},
			{HIGH, HIGH, LOW, HIGH, HIGH, HIGH, HIGH},
			{LOW, HIGH, HIGH, HIGH, LOW, LOW, LOW},
			{HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH},
			{HIGH, HIGH, HIGH, HIGH, LOW, LOW, HIGH},
		};

		void turnOffAll();
	public:
		SevenSegment(int upper_left, int top, int upper_right, int lower_right, int bottom, int lower_left, int center, int flag);
		void set(int value);
};

#endif
