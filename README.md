# CutestON
 CuteON is a versatile sterilizer for use in a variety of projects. The main priority is to create the most versatile sterilizer that can be used both in regular programs and in special libraries for python. This sterilizer can be used as a data storage and recording system.
 
 This library has the ability to both read and write data to a file. 
 
 They can also be collected into classes as in JsON.
This sterilizer uses a system similar to programming languages. That is, the content of the data can be represented as a collection of data in the form of classes and objects. But CuteON presents an approach of presenting data as a kind of ladder from top to bottom. Where:

> ***A line*** is the lowest unit of data storage. That is, the line stores one variable in itself.
>
> ***An object*** is the second unit, it stores a group of lines, dining with one name of the object.
>
> ***A class*** is the highest unit of data storage and represents a group of objects. Dining in one class

 Special constructs are used to indicate the opening and closing of a class or object. All the necessary structures are written below. A must for familiarization.
 
 | Name  | Sintaxsis |
| ------------- | ------------- |
| Line  | ` Privat/Public::<Name data>::<Data>`  |
| Object  | ` Privat/Public::{ / }::<Name Obj>`  |
| Class  | ` Privat/Public::[ / ]::<Name Class>`  |
 
 
 All constructions have an access modifier that prevents data from being received from an object, class, or line. Or for some objects they show that you need to hide data, the Print class does not show private data, but displays NONE instead. Private data can be used to store bot tokens.
 
## Class Get_
>The Get_ class is made for sterilization. It has methods that allow you to get data from a file by using sterilized >strings, objects, classes. For later use in projects, programs, bots, or for storing any notes there.

 *GetLine* - Needed to get a specific line in a file. In order not to waste time reading the entire file. This method has two arguments fileread, line. Fileread is a file to be read here the file with its full path is specified. Line is the line number that the sterilizer will access, this argument must be an integer, otherwise there will be an error. GetLine - will return an array of values ​​that are in the given line. Or will not return, depending on the string access modifier.

GetObj - This method gets an object from a file. By itself, this method is very similar to Find, but instead of receiving one string, it receives one object at once from serialized for the convenience of working with data in it. There are two mandatory methods: Name, and Fileread. Fileread is a file for reading; here the file with its full path is indicated, you can specify a relative address. Name is the name of the object, that is, the value after the string access modifier.

GetClass - This method gets a serialized class from a file. Similar in use to GetObj, but gets the entire class as an array of non-serialized objects. It has two required methods. name, and fileread. Fileread is a file for reading; here the file with its full path is indicated, you can specify a relative address. Name is the name of the class, i.e. the value after the string access modifier.

Find - to find a line in a file. And then returns the string as an array. Fileread and name, as in GetLine, the same principle is used here as in GetLine. Name is the name of the string, that is, the value after the string access modifier. Fileread is a file to be read here the file with its full path is specified. This method is slower than GetLine, but more versatile.

## class Read_
>The Read_ class is used to read a file. It includes methods of reading, searching, getting. To use this class, refer to >CuteON.Read_ and call the method you need. >All strings have their own “Public” and “Private” access modifier, these >modifiers are used to specify access to the value of the string.

Read - is a method for reading the entire file, regardless of the access modifier or class size. It has one method name - the name of the file to read. Returns the value as a string and is not sterilized for validation.

## class Write

AddLine - is a method for adding only a line to a file. When adding a row, the sterilizer pays attention to whether this row is public or private. This method has only two arguments, they are File and Text. File - contains the path to the file. Text - contains the string itself. The form of the record as in the final file.

