#include <iostream>
#include <fstream >
#include <string>
#include <sstream>
#include <vector>

using namespace std;



template <typename T>
std::string toString(T val)
{
	std::ostringstream oss;
	oss << val;
	return oss.str();
}

template<typename T>
T fromString(const std::string& s)
{
	std::istringstream iss(s);
	T res;
	iss >> res;
	return res;
}

vector<string> split(string str, string sep = " ") {// Ôóíêöèÿ äëÿ ðàçáèâàíèÿ ñòðîêè íà ñëîâà èëè ïî äðóãîìó îïðåäåëèòåëþ
	int idx = 0, lidx = 0,// îáÿâëåíèå èíäåêñîâ
		sep_len = sep.size();// ïîðëó÷åíèå äëèíû ñòðîêè
	vector<string> ret_list; // îáÿâëåíèå âåêòîðà äëÿ çàïèñè

	while (true) { // áåñêîíå÷üíûé öèêîë
		lidx = str.find(sep, idx);// íàõîæäåíèå èíäåêñà â ñòðîêå

		ret_list.push_back(str.substr(idx, lidx - idx));

		if (lidx == string::npos) // ïðîâåðêà ïîçèöèè
			break;

		idx = lidx + sep.size(); // ïðåñâîåíèå íîâîãî èíäåêñà
	}

	return ret_list;// âåðíóòü ðåçóëüòàò ðàçäåëåíèÿ
}


void AddInFile(string file_for_input, string string_for_input) {// îáÿâëåíèÿ ìåòîäà WriteInFile
	ofstream out(file_for_input, std::ios::app);// ñîçäàíèå ïîòîêà äëÿ çàïèñè
	out << string_for_input;// çàïèñü ðåçóëüòàòà
	out.close();// çàêðûòèå ïîòîêà
}

void WriteInFile(string file_for_input, string string_for_input) {// îáÿâëåíèÿ ìåòîäà WriteInFile
	ofstream out(file_for_input);// ñîçäàíèå ïîòîêà äëÿ çàïèñè
	out << string_for_input;// çàïèñü ðåçóëüòàòà
	out.close();// çàêðûòèå ïîòîêà
}

string join(std::vector<string> vec) {


	std::ostringstream oss;
	if (!vec.empty()) {
		std::copy(vec.begin(), vec.end() - 1, std::ostream_iterator<string>(oss, "\n"));
		oss << vec.back();
	}
	return oss.str();
}

string Read(string file_to_read) {
	std::string line;
	vector<string> return_string;

	std::ifstream in(file_to_read); // îêðûâàåì ôàéë äëÿ ÷òåíèÿ
	if (in.is_open())
	{
		while (getline(in, line))
		{
			return_string.push_back(line);
		}
	}
	else {
		return_string.push_back("");
	}
	in.close();     // çàêðûâàåì ôàéë
	return join(return_string);
}

vector<string> SplitOnFild(string content) {// ôóíêöèÿ ðàçäåëåíèÿ èñõîäíîãî òåêñòà íà ïîëÿ èëè ðàáî÷èè îáëàñòè
	vector<string> Filds = split(content, "<cut>");// ñàìî ðàçäåëåíèå ïî òåãó <cut>

	return Filds;// âîçâðàùÿåì ìàñèâ ñ ïîëÿìè!
}

void log(string log_text) {// ëþáîé ëîã ïðîâåðÿåòñÿ è âûâîäèò èíôîðìàöèþ

	std::string line;

	std::ifstream in("logs.txt"); // îêðûâàåì ôàéë äëÿ ÷òåíèÿ
	if (in.is_open()) {

		if (log_text == "") {
			cout << "Log is empty" << endl;
		}

		else {
			AddInFile("logs.txt", "\n" + log_text);
		}
	}

	else {
		cout << "Logs con't write in file!" << endl;
	}
}

void log_sleep(string log_text) { AddInFile("logs.txt", "\n" + log_text); } // Ëîã ñîõðàíÿåòñÿ áåç âûâîäà è ïðîâåðîê

string int_to_str(int num) {
	std::ostringstream ost;
	ost << num;
	return ost.str();
}


void printv(vector<string> arr) {
	for (int i = 0; i < arr.size(); i++) {
		cout << arr[i];
	}
}


class Vec {


public:
	vector<int> Creat2D(int VecX, int VecY) {
		vector<int> Fin_Vector;
		Fin_Vector.push_back(VecX);
		Fin_Vector.push_back(VecY);
		return Fin_Vector;
	}

public:
	vector<int> Creat3D(int VecX, int VecY) {
		vector<int> Fin_Vector;
		Fin_Vector.push_back(VecX);
		Fin_Vector.push_back(VecY);
		return Fin_Vector;
	}



};