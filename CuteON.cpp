
#include <iostream>
#include "Helper.h"
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

class Get_ {
public: 
	vector<string> GetLine(string file_read, int Line) {
	string line;
	vector <string> ReturnLine;

	std::ifstream in(file_read); // Запуск стрима чьтения файла
	if (in.is_open())
	{
		while (getline(in, line))
		{
			vector<string> content = split(line, "\n");
			int i = 0;
			string word = content[i];
			vector<string> Word = split(word, "::");
			ReturnLine = Word;
			if (i == Line) {
				return ReturnLine;
			}
			else {
				return Word;
			}
		}
	}
}
public:
	string GetObj(string name, string user_file) {
		
		vector<string> content = split(Read(user_file), "\n");
		for (int i = 0; i < content.size(); i++) {
			vector<string>	content_list = split(content[i], "::");
			if (content[i] == "public::" + name + "::{") {
				if (content_list[1] == name) {

					string splitBlock = "public::" + name + "::{";
					vector<string> Text = split(Read(user_file), splitBlock);

					vector<string> Final_Text = split(Text[1], "}");

					return Final_Text[0];
				}
			}

			else {
				return  "NONE";
			}			
		}
	}

public:
	string GetClass(string name, string user_file) {

		vector<string> content = split(Read(user_file), "\n");
		for (int i = 0; i < content.size(); i++) {
			vector<string>	content_list = split(content[i], "::");
			if (content[i] == "public" + name + "[") {
				if (content_list[1] == name) {
					string splitBlock = "public::" + name + "::[";
					vector<string> Text = split(Read(user_file), splitBlock);

					vector<string> Final_Text = split(Text[1], "]");

					return Final_Text[0];;
				}
			}
			else {
				return  "NONE";
			}
			
		}
	}

public: 
	vector<string> Find(string name, string user_file) {
	vector<string> none_list;
	vector<string> content = split(Read(user_file), "\n");
	for (int i = 0; i < content.size(); i++) {
		vector<string>	content_list = split(content[i], "::");
		if (content_list[0] == "public") {
			if (content_list[1] == name) {
				return content_list;
			}
			else {
				return  none_list;
			}
		}
	}
}
};

class Read_ {

public:
	string Read(string file){
		string line;
		vector<string> return_string;

		std::ifstream in(file); // îêðûâàåì ôàéë äëÿ ÷òåíèÿ
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



};

class Write_{

public:
	void AddLine(string file, string text){
		vector<string> context = split(text, "::");
		if ((context[0] == "public") || (context[0] == "private")) {
			WriteInFile(file, text);
		}
		else {
			WriteInFile(file, "public::" + text);
		}
		
	}


	void AddObj(string file, string name, string Obj) {// Добавляет публичьный обект в фаил
		WriteInFile(file, "\npublic::" + name + "{\n" + Obj + "\n}");
	}

	void AddClass(string file, string name, string Obj) {
		WriteInFile(file, "\npublic::" + name + "[\n" + Obj + "\n]");
	}


};

class Creat_{};

class Print_{};


