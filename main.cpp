#include "CuteON.cpp"

using namespace std;

int main() {
	vector<string> text;
	Get_ get;
	text = get.Find("mark", "test.sws");
	Print_ print;
	Convect_ convect;

	print.PrintVectorInt(convect.ToIntVector(split(text[2], ",")));
	return 0;
}