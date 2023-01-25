// Íà÷íåì ñ äèðåêòèâ ïðåïðîöåññîðà. ADD_H – ýòî ïðîèçâîëüíîå óíèêàëüíîå èìÿ (îáû÷íî èñïîëüçóåòñÿ èìÿ çàãîëîâî÷íîãî ôàéëà)
#ifndef HELPER_H
#define HELPER_H

#include <vector>
#include <string>
using namespace std;
#pragma once

// â ýòîì ôàéëå îïèñàíû ïðîòîòèïû ôóíêöèé äëÿ ðàáîòû íàøåãî èíòîðïðèòàòîðà

vector<string> split(string str, string sep = " "); // ïðîòîòèï ôóíêöèè split() (íå çàáûâàéòå òî÷êó ñ çàïÿòîé â êîíöå!)

void WriteInFile(string file_for_input, string string_for_input); // ïðîòîòèï ôóíêöèè äîáàâëåíèÿ â ôàèë ñòðîêè
string Read(string file_to_read);// ôóíêöèÿ ÷üòåíèÿ ôàéëà
vector<string> SplitOnFild(string content); // Ïðîòîòèï ôóíêöèè äëÿ ðàçáèâàíèÿ íà ïîëÿ èñõîäíûé òåêñò
void AddInFile(string file_for_input, string string_for_input); // Ôóíêöèÿ ïåðåçàïèñè ôàéëà

string join(std::vector<string> vec);

void log(string log_text);// èíñòðóìåíò çàïèñè ëîãîâ
void printv(vector<string> arr);
string int_to_str(int num);// ôóíêöèÿ äëÿ ïåðåâîäà èø int â str

template<typename T>
string toString(T val); // ïåðåâîä èç ÷èñëà â ñòîðêó
#endif